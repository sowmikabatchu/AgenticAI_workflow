def rule_based_agent(temp):
    if temp >= 100:
        return "Turn ON cooling system"
    elif temp >= 80:
        return "Reduce temperature"
    elif temp >= 60:
        return "Normal monitoring"
    else:
        return "Temperature is low"


temperatures = [110, 90, 72, 60, 40]

print("PROGRAM STARTED")

for temp in temperatures:
    action = rule_based_agent(temp)

    print(f"Temperature : {temp}")
    print(f"Agent Action: {action}")
    print("-" * 30)