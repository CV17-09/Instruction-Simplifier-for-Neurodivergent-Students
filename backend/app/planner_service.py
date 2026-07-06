def estimate_workload(text: str) -> str:
    word_count = len(text.split())

    if word_count < 300:
        return "Small assignment: about 1–2 hours"
    elif word_count < 1000:
        return "Medium assignment: about 3–5 hours"
    else:
        return "Large assignment: about 5+ hours"

def create_basic_timeline():
    return [
        "Day 1: Read instructions and list requirements",
        "Day 2: Gather materials or research",
        "Day 3: Create outline or first draft",
        "Day 4: Revise and check rubric",
        "Day 5: Submit assignment"
    ]