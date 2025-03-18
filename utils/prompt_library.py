#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Created by Mohammed Jassim at 12/03/25


prompts = {
        "markdown": """Extract all text content from this image in {language} **exactly as it appears**, without modification, summarization, or omission.
                                    Format the output in markdown:
                                    - Use headers (#, ##, ###) **only if they appear in the image**
                                    - Preserve original lists (-, *, numbered lists) as they are
                                    - Maintain all text formatting (bold, italics, underlines) exactly as seen
                                    - **Do not add, interpret, or restructure any content**
                                """,
        "text": """Extract all visible text from this image in {language} **without any changes**.
                                    - **Do not summarize, paraphrase, or infer missing text.**
                                    - Retain all spacing, punctuation, and formatting exactly as in the image.
                                    - If text is unclear or partially visible, extract as much as possible without guessing.
                                    - **Include all text, even if it seems irrelevant or repeated.** 
                                    """,

        "json": """Extract all text from this image in {language} and format it as JSON, **strictly preserving** the structure.
                                    - **Do not summarize, add, or modify any text.**
                                    - Maintain hierarchical sections and subsections as they appear.
                                    - Use keys that reflect the document's actual structure (e.g., "title", "body", "footer").
                                    - Include all text, even if fragmented, blurry, or unclear.
                                    """,

        "structured": """Extract all text from this image in {language}, **ensuring complete structural accuracy**:
                                    - Identify and format tables **without altering content**.
                                    - Preserve list structures (bulleted, numbered) **exactly as shown**.
                                    - Maintain all section headings, indents, and alignments.
                                    - **Do not add, infer, or restructure the content in any way.**
                                    """,

        "key_value": """Extract all key-value pairs from this image in {language} **exactly as they appear**:
                                    - Identify and extract labels and their corresponding values without modification.
                                    - Maintain the exact wording, punctuation, and order.
                                    - Format each pair as 'key: value' **only if clearly structured that way in the image**.
                                    - **Do not infer missing values or add any extra text.**
                                    """,

        "table": """Extract all tabular data from this image in {language} **exactly as it appears**, without modification, summarization, or omission.
                                    - **Preserve the table structure** (rows, columns, headers) as closely as possible.
                                    - **Do not add missing values or infer content**—if a cell is empty, leave it empty.
                                    - Maintain all numerical, textual, and special character formatting.
                                    - If the table contains merged cells, indicate them clearly without altering their meaning.
                                    - Output the table in a structured format such as Markdown, CSV, or JSON, based on the intended use.
                                    """,

    }
