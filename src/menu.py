# src/menu.py

def flatten_menu(node):
    """
    Return a flat list of item names from a nested menu.
    Node has "type": "category" or "item".
    """
    if not node or "type" not in node:
        return []

    if node["type"] == "item":
        # Return name if exists, else empty
        return [node["name"]] if "name" in node else []

    elif node["type"] == "category":
        result = []
        for child in node.get("children", []):
            result.extend(flatten_menu(child))
        return result

    # Unknown type
    return []
