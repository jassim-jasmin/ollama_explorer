#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Created by Mohammed Jassim at 13/03/25
import os
import tempfile
import streamlit as st

from PIL import Image
from pathlib import Path

from app.components.general_css import markdown_css
from app.components.about_markdown import about_markdown
from utils.image_helper import OCRImage
from utils.model_helper import model_directory


# Page configuration
st.set_page_config(
    page_title="OCR with Ollama",
    page_icon="🔍",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Custom CSS for better UI
st.markdown(markdown_css, unsafe_allow_html=True)


def side_bar_controls():
    # Sidebar controls
    with st.sidebar:
        st.header("🎮 Controls")

        selected_model = st.selectbox(
            "🤖 Select Vision Model",
            model_directory.keys(),
            index=0,
        )

        format_type = st.selectbox(
            "📄 Output Format",
            ["text", "markdown", "json", "structured", "key_value", "table"],
            help="Choose how you want the extracted text to be formatted"
        )

        # Custom prompt input
        custom_prompt_input = st.text_area(
            "📝 Custom Prompt (optional)",
            value="",
            help="Enter a custom prompt to override the default. Leave empty to use the predefined prompt."
        )

        st.markdown("---")

        # # Model info box
        model_options = model_directory.get(selected_model)
        st.info(f"{model_options['name']}: {model_options['info']}")

    return custom_prompt_input, selected_model, format_type


def image_file_upload_bar():
    supported_file_format = ['png', 'jpg', 'jpeg', 'tiff', 'bmp', 'pdf', 'txt']
    # File upload area with multiple file support
    uploaded_files = st.file_uploader(
        "Drop your images here",
        type=supported_file_format,
        accept_multiple_files=True,
        help=f"Supported formats: {','.join(supported_file_format)}"
    )

    return uploaded_files


def save_uploaded_file(uploaded_files, temp_dir):
    image_paths = []

    # Save uploaded files and collect paths
    for uploaded_file in uploaded_files:
        temp_path = os.path.join(temp_dir, uploaded_file.name)
        with open(temp_path, "wb") as f:
            f.write(uploaded_file.getvalue())

        image_paths.append(temp_path)

    return image_paths


def process_button(image_paths, format_type, selected_model, prompt):
    # Process button
    if st.button("🚀 Process File"):
        print(f'{image_paths[0]}, {selected_model}, "{prompt}"')
        with st.spinner("Processing file..."):
            if len(image_paths) == 1:
                result = OCRImage.get_ocr_image(Path(image_paths[0]), selected_model, prompt)
                st.subheader("📝 Extracted Text")
                st.markdown(result)

                # Download button for single result
                st.download_button(
                    "📥 Download Result",
                    result,
                    file_name=f"ocr_result.{format_type}",
                    mime="text/plain"
                )


def file_processing_sub_tab(file_processing_tab, format_type, selected_model, prompt):
    with file_processing_tab:
        if uploaded_files := image_file_upload_bar():
            # Create a temporary directory for uploaded files
            with tempfile.TemporaryDirectory() as temp_dir:
                image_paths = save_uploaded_file(uploaded_files, temp_dir)

                # Display images in a gallery
                st.subheader(f"📸 Input File ({len(uploaded_files)} files)")
                cols = st.columns(min(len(uploaded_files), 4))

                for idx, uploaded_file in enumerate(uploaded_files):
                    with cols[idx % 4]:
                        try:
                            if uploaded_file.name.lower().endswith('.pdf'):
                                # Display a placeholder for PDFs
                                st.image("https://via.placeholder.com/150?text=PDF", caption=uploaded_file.name,
                                         use_container_width=True)
                            elif uploaded_file.name.lower().endswith('.png'):
                                image = Image.open(uploaded_file)
                                st.image(image, caption=uploaded_file.name, use_container_width=True)

                            elif uploaded_file.name.lower().endswith('.txt'):
                                # Display text files
                                text = uploaded_file.read().decode("utf-8")
                                st.text_area("Text File Content", text, height=300)

                        except Exception as e:
                            st.error(f"Error displaying {uploaded_file.name}: {e}")

                process_button(image_paths, format_type, selected_model, prompt)


def about_sub_tab(about_tab):
    with about_tab:
        st.header("About Vision OCR Lab")
        st.markdown(about_markdown)


def main_content(format_type, selected_model, custom_prompt_input):
    # Main content area with tabs
    file_processing_tab, about_tab = st.tabs(["📸 File Processing", "ℹ️ About"])

    file_processing_sub_tab(file_processing_tab, format_type, selected_model, custom_prompt_input)
    about_sub_tab(about_tab)


def main():
    st.title("🔍 OLLAMA Explorer")
    st.markdown("<p style='text-align: center; color: #666;'>Powered by Ollama Vision Models</p>",
                unsafe_allow_html=True)

    custom_prompt_input, selected_model, format_type = side_bar_controls()

    # Determine if a custom prompt should be used (if text area is not empty)
    custom_prompt = custom_prompt_input if custom_prompt_input.strip() != "" else None

    main_content(format_type, selected_model, custom_prompt)
