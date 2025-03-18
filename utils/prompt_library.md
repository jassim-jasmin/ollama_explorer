# Prompt Library

This script defines a collection of prompts designed to extract text from images with specific formatting and structure. Each prompt is tailored to preserve the original content without adding, modifying, or summarizing any information.

## Prompt Categories

### 1. Markdown Prompt
- Extracts all text content from an image in the specified language, preserving formatting.
- Outputs text in **Markdown** format, maintaining headers, lists, and formatting as seen in the image.
- Does not modify, summarize, or omit any content.

### 2. Text Prompt
- Extracts all visible text from an image without any changes.
- Preserves spacing, punctuation, and formatting exactly as seen.
- Avoids guessing or inferring unclear text.

### 3. JSON Prompt
- Extracts text and formats it as **JSON**, strictly preserving structure.
- Maintains hierarchical sections and subsections as they appear in the image.
- Uses keys that reflect the document’s actual structure.

### 4. Structured Prompt
- Ensures complete structural accuracy in text extraction.
- Identifies tables and list structures and preserves them exactly as shown.
- Maintains section headings, indents, and alignments without alteration.

### 5. Key-Value Prompt
- Extracts all key-value pairs from an image in the specified language.
- Maintains the exact wording, punctuation, and order as shown.
- Formats each pair as 'key: value' only if structured that way in the image.

### 6. Table Prompt
- Extracts all tabular data from an image without modification.
- Preserves table structure, including rows, columns, headers, and merged cells.
- Outputs the table in structured formats such as Markdown, CSV, or JSON.

## Usage Example
You can use these prompts as part of your OCR or text extraction pipeline. Here’s an example of how to use a specific prompt:

```python
from utils.prompt_library import prompts

language = 'English'
prompt = prompts.get('markdown').format(language=language)
print(prompt)
```

## License
This project is licensed under the MIT License.

## Links
- [README.md](../README.md)