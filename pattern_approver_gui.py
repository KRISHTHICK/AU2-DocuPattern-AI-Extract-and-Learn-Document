def launch_review_gui(patterns):
    print("Reviewing Patterns:")
    for pat in patterns:
        print("\n---")
        print(f"Pattern ID: {pat['pattern_id']}")
        print(f"Rows: {pat['rows']}, Columns: {pat['columns']}")
        print(f"Type: {pat['table_type']}")
        print("Approve? (y/n): ", end="")
        user_input = input()
        if user_input.strip().lower() != "y":
            pat["approved"] = False
        else:
            pat["approved"] = True
    
    approved = [p for p in patterns if p["approved"]]
    return approved
