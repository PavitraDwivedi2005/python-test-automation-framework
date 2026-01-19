def find_virtual_service(vs_list, target_name):
    for vs in vs_list.get("results", []):
        if vs.get("name") == target_name:
            return vs
    return None

def validate_enabled_state(vs, expected_state):
    actual = vs.get("enabled")
    if actual != expected_state:
        raise Exception(
            f"Validation failed: expected enabled={expected_state}, got {actual}"
        )
