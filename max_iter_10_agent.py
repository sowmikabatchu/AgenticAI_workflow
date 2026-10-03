def agent():
    max_iters = 10

    for i in range(max_iters):
        print(f"Iteration {i + 1}")

        observation = "observe"
        decision = "decide"
        result = "act"

        if result == "success":
            return "success"

    return "failure"


print(agent())