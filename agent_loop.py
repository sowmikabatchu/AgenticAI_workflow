def observe():
    print("👀 OBSERVE: Collecting current information...")
    return "User needs help with a task"


def decide(observation):
    print(f"🧠 DECIDE: Analyzing -> {observation}")
    return "Perform the required action"


def act(decision):
    print(f"⚡ ACT: {decision}")


# Observe → Decide → Act loop
for iteration in range(1, 4):
    print(f"\n========== ITERATION {iteration} ==========")

    observation = observe()
    decision = decide(observation)
    act(decision)

print("\n✅ 3 iterations completed.")