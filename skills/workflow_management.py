from .error_handling import log_error

def execute_workflow(steps):
    results = []
    for step in steps:
        try:
            result = step()
            results.append(result)
        except Exception as e:
            log_error(f"Step failed: {str(e)}")
            break
    return results
