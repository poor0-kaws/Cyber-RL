from stable_baselines3 import PPO 
from src.env import IdsEnv
from src.data_loader import load_and_split

# 1. Load Data (We only need the test data for evaluation)
# Recall the order: X_train, y_train, X_test, y_test
_, _, X_test, y_test = load_and_split()

# 2. Recreate the environment using the TEST data
# This ensures we are testing on data the agent hasn't seen before
env = IdsEnv(X_test, y_test)

# 3. Load the trained model
model = PPO.load("models/ppo_ids")

# 4. Run the evaluation loop
obs, _ = env.reset()
done = False
total_reward = 0

# Metrics Counters
correct_predictions = 0
tp = 0 # True Positive
tn = 0 # True Negative
fp = 0 # False Positive
fn = 0 # False Negative

print("Starting evaluation...")

while not done:
    # Ask the model what to do (predict action)
    action, _ = model.predict(obs)
    
    # Take that action in the environment
    obs, reward, done, truncated, info = env.step(action)
    
    # Track the reward
    total_reward += reward
    
    # --- Metrics Calculation ---
    # y_test is the ground truth label array
    # The environment processes samples in order from 0 to 199
    # We can get the true label from info['label'] which we added to env.py
    true_label = info['label']
    
    if action == true_label:
        correct_predictions += 1
    
    if action == 1 and true_label == 1:
        tp += 1
    elif action == 0 and true_label == 0:
        tn += 1
    elif action == 1 and true_label == 0:
        fp += 1
    elif action == 0 and true_label == 1:
        fn += 1

print(f"--------------------------------")
print(f"Total Reward: {total_reward}")
print(f"--------------------------------")

accuracy = (correct_predictions / 200) * 100
print(f"Accuracy: {accuracy:.2f}%")
print(f"--------------------------------")
print(f"Confusion Matrix:")
print(f"True Positives (Attack Blocked): {tp}")
print(f"True Negatives (Safe Allowed):   {tn}")
print(f"False Positives (Safe Blocked):  {fp}")
print(f"False Negatives (Attack Missed): {fn}")
print(f"--------------------------------")
