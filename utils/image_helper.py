#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Created by Mohammed Jassim at 12/03/25
import base64
import os

import requests
import cv2
from pathlib import Path
from utils.prompt_library import prompts

from dotenv import load_dotenv

load_dotenv()


class OCRImage:
    @staticmethod
    def _preprocess_image(image_path: Path, language: str = "en") -> str:
        """
        Preprocess image before OCR:
        - Convert PDF to image if needed (using pymupdf)
        - Language-specific preprocessing (if applicable)
        - Enhance contrast
        - Reduce noise
        """
        # Read image
        image = cv2.imread(str(image_path))
        if image is None:
            raise ValueError(f"Could not read image at {image_path}")

        # Convert to grayscale
        gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

        # Enhance contrast using CLAHE
        clahe = cv2.createCLAHE(clipLimit=2.0, tileGridSize=(8, 8))
        enhanced = clahe.apply(gray)

        # Denoise
        denoised = cv2.fastNlMeansDenoising(enhanced)

        # Language-specific thresholding
        if language.lower() in ["japanese", "chinese", "zh", "korean"]:
            # For some CJK and similar languages adaptive thresholding may work better
            thresh = cv2.adaptiveThreshold(
                denoised, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C,
                cv2.THRESH_BINARY, 11, 2)
            thresh = cv2.bitwise_not(thresh)

        else:
            # Default: Otsu thresholding
            thresh = cv2.threshold(denoised, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)[1]
            thresh = cv2.bitwise_not(thresh)

        # Save preprocessed image
        preprocessed_path = f"{image_path.stem}_preprocessed.jpg"
        cv2.imwrite(preprocessed_path, thresh)

        return preprocessed_path

    @classmethod
    def get_ocr_image(cls, image_path: Path, selected_model, prompt: str = None):
        if not prompt:
            prompt = prompts.get('text').format(language='English')

        payload = {
            "model": selected_model,
            "stream": False
        }

        if image_path:
            if image_path.suffix == '.png':
                with open(cls._preprocess_image(image_path), "rb") as image_file:
                    content = image_file.read()

                    image_base64 = base64.b64encode(content).decode("utf-8")
                    payload["images"] = [image_base64]

            elif image_path.suffix == '.txt':
                with open(image_path, "r") as image_file:
                    content = image_file.read()

                    prompt = prompt + (f"\n\nPerform the above instructions in following text.\n"
                                       f"Text: {content}")

        payload["prompt"] = prompt
        print(prompt)

        response = requests.post(os.getenv('ollama_url'), json=payload)
        response.raise_for_status()

        result = response.json().get("response", "")
        print(result)

        return result


if __name__ == '__main__':
    OCRImage.get_ocr_image(Path('/Users/jassim/Documents/project/personal/ollama_explorer/data/raw/a.jpeg'))
