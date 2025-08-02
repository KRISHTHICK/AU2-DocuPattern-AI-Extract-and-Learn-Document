from utils.doc_parser import parse_document
from pattern_extractor import extract_patterns
from pattern_classifier import learn_and_classify_patterns
from pattern_approver_gui import launch_review_gui

if __name__ == "__main__":
    doc_path = "samples/sample_document.docx"
    parsed_data = parse_document(doc_path)
    detected_patterns = extract_patterns(parsed_data)
    
    classified = learn_and_classify_patterns(detected_patterns)
    
    approved = launch_review_gui(classified)
    
    print("Final approved patterns saved successfully.")
