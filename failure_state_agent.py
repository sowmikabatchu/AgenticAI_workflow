def agent():
    max_iters = 10

    state = {
        "done": False,
        "steps": 0,
        "status": "running"
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
            state["status"] = "success"
            return state

    # Maximum iterations exceeded
    state["status"] = "failure"
    return state


state = agent()

print(state)
{
    "done": True,
    "steps": 1,
    "status": "success"
}
{
    "done": False,
    "steps": 10,
    "status": "failure"
}