import gymnasium as gym 
from stable_baselines3 import PPO 
from src.env import IdsEnv
from src.data_loader import load_and_split


X_train, y_train, X_test, y_test = load_and_split()

env = IdsEnv(X_train, y_train)
model = PPO("MlpPolicy", env, verbose=1)
model.learn(total_timesteps=10000)
model.save("models/ppo_ids")