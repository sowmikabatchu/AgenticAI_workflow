def agent():
    max_iters = 10

    state = {
        "done": False,
        "steps": 0
    }

    while not state["done"] and state["steps"] < max_iters:
        # Observe
        observation = "observe"

        # Decide
        decision = "decide"

        # Act
        result = "success"

        state["steps"] += 1

        if result == "success":
            state["done"] = True

    if state["done"]:
        return "success", state
    else:
        return "failure", state


result, state = agent()

print(result)
print(state)