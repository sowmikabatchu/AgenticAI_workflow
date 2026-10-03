def agent():
    max_iters = 10

    state = {
        "done": False,
        "steps": 0,
        "status": "running",
        "log": []
    }

    while not state["done"] and state["steps"] < max_iters:

        # Observe
        state["log"].append("observe")

        # Decide
        state["log"].append("decide")

        # Act
        result = "success"
        state["log"].append("act")

        # FIX: increment steps
        state["steps"] += 1

        if result == "success":
            state["done"] = True
            state["status"] = "success"

    if not state["done"]:
        state["status"] = "failure"

    return state


print(agent())