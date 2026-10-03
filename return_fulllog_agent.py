def agent(action):
    valid_actions = ["observe", "decide", "act"]

    if action not in valid_actions:
        return {
            "status": "error",
            "error": f"Invalid action: {action}"
        }

    return {
        "status": "success",
        "action": action
    }


# Valid action
print(agent("act"))

# Invalid action
print(agent("delete"))
