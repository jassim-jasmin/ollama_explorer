# Model Information Box

This Python script defines a dictionary containing information about various language and vision models. It provides metadata such as model names and descriptions to help users understand each model's purpose and capabilities.

## Models Included
The following models are defined in the script:

### 1. Llama 3.2 Vision (11B)
- **Name:** Llama 3.2 Vision
- **Description:** Advanced model with high accuracy for complex text extraction.

### 2. LLaVA 7B
- **Name:** LLaVA 7B
- **Description:** Efficient vision-language model optimized for real-time processing.

### 3. Granite 3.2 Vision
- **Name:** Granite 3.2 Vision
- **Description:** Robust model for detailed document analysis.

### 4. Moondream
- **Name:** Moondream
- **Description:** Lightweight model designed for edge devices.

### 5. Llama 3.3 (70B)
- **Name:** Llama 3.3
- **Description:** The Meta Llama 3.3 multilingual large language model (LLM) is a pretrained and instruction-tuned generative model with 70 billion parameters. It is optimized for multilingual dialogue use cases and outperforms many available open-source and closed chat models on common industry benchmarks.

## Usage
Simply import or access the `model_directory` dictionary to retrieve information about the available models.

### Example
```python
model = model_directory.get("llava:7b")
print(f"Model Name: {model['name']}")
print(f"Model Info: {model['info']}")
```

## License
This project is licensed under the MIT License.

## Links
- [README.md](../README.md)