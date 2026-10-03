def agent():
    state = {
        "steps": 0,
        "log": []
    }

    max_iters = 2

    while state["steps"] < max_iters:
        state["steps"] += 1

        state["log"].append(
            f"Step {state['steps']}: Observe -> Decide -> Act"
        )

    return state


result = agent()

print("Steps:", result["steps"])
print("Log:")

for item in result["log"]:
    print(item)