# AU2-DocuPattern-AI-Extract-and-Learn-Document
Gen AI

DocuPattern AI: Extract and Learn Document Structures & Table Patterns from Complex Word Files
🔍 Objective:
Automatically analyze, detect, and learn structural patterns (like tables, colors, icons, checkboxes, unit-value pairs, nested tables, font sizes, etc.) from unstructured MS Word documents. The AI system will identify repeating table types, conditional styles, background color codes, and annotated units. Then, it lets a human approve or edit the pattern, which is saved for future structured extraction.

🧠 Core AI Goals:
Identify:

Paragraphs, headings, subheadings.

Table types (e.g., plain, with icons, checkboxes, nested tables).

Background colors and formatting logic.

Value-signed boxes (e.g., cells with ± or decimal thresholds).

Store structural rules.

Provide GUI or console review for human approval/edit.

Apply approved rules for extraction in other documents.

🛠️ Tech Stack:
python-docx, docx2python, docx — for Word parsing.

pandas — to manage structured table data.

python-pptx or imagelib — for icons/images inside tables.

PyMuPDF or pytesseract — if documents are image-based.

scikit-learn or rules-based classifier — for table pattern learning.

Optional: Tkinter or Streamlit — for visual review.

