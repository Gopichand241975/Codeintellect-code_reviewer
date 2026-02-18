import ast

def analyze_code(code_text):
    result = {}

    try:
        tree = ast.parse(code_text)
    except SyntaxError:
        return {"error": "Invalid Python code."}

    functions = [node for node in ast.walk(tree) if isinstance(node, ast.FunctionDef)]
    loops = [node for node in ast.walk(tree) if isinstance(node, (ast.For, ast.While))]
    conditionals = [node for node in ast.walk(tree) if isinstance(node, ast.If)]

    result["function_count"] = len(functions)
    result["loop_count"] = len(loops)
    result["conditional_count"] = len(conditionals)

    complexity = len(loops) + len(conditionals)
    result["complexity_score"] = complexity

    lines = code_text.split("\n")
    result["line_count"] = len(lines)

    quality_score = 100

    if complexity > 10:
        quality_score -= 20
    if len(lines) > 300:
        quality_score -= 20
    if len(functions) == 0:
        quality_score -= 15

    result["quality_score"] = max(0, quality_score)

    suggestions = []

    if complexity > 10:
        suggestions.append("High complexity detected. Simplify logic.")

    if len(functions) == 0:
        suggestions.append("Use functions to modularize code.")

    if len(lines) > 300:
        suggestions.append("Break large file into modules.")

    if not suggestions:
        suggestions.append("Code structure looks good.")

    result["suggestions"] = suggestions

    return result
