def extract_patterns(parsed_data):
    table_patterns = []
    for table in parsed_data["tables"]:
        row_lengths = [len(row) for row in table]
        max_cols = max(row_lengths)
        has_units = any(any("mg" in cell or "kg" in cell for cell in row) for row in table)
        has_checkboxes = any("[ ]" in cell or "[x]" in cell for row in table for cell in row)
        
        table_patterns.append({
            "rows": len(table),
            "columns": max_cols,
            "contains_units": has_units,
            "contains_checkboxes": has_checkboxes,
            "table_type": "unit_value_table" if has_units else "checkbox_table" if has_checkboxes else "plain_text_table"
        })
    
    return table_patterns
