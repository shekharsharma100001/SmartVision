def quality_check(classification_result):
    # Define thresholds or conditions for passing quality control
    if classification_result == "Expected Class":
        return "Product Passed"
    else:
        return "Product Failed"
