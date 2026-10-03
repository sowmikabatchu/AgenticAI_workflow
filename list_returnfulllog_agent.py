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
        observation = "observe"
        state["log"].append({
            "step": state["steps"] + 1,
            "action": "observe",
            "result": observation
        })

        # Decide
        decision = "decide"
        state["log"].append({
            "step": state["steps"] + 1,
            "action": "decide",
            "result": decision
        })

        # Act
        result = "success"
        state["log"].append({
            "step": state["steps"] + 1,
            "action": "act",
            "result": result
        })

        state["steps"] += 1

        if result == "success":
            state["done"] = True
            state["status"] = "success"
            return state

    # Maximum iterations exceeded
    state["status"] = "failure"
    state["log"].append({
        "step": state["steps"],
        "action": "system",
        "result": "max iterations exceeded"
    })

    return state


state = agent()

print("Status:", state["status"])
print("Steps:", state["steps"])
print("Full Log:")

for entry in state["log"]:
    print(entry)