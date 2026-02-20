from re import X
from tabnanny import verbose
import gymnasium, stable_baselines3, numpy
from stable_baselines3.ppo import PPO, MlpPolicy, ppo
from src.env import IdsEnv
from src.data_loader import load_and_split


X_train, X_test, y_train, y_test = load_and_split()

env = IdsEnv(X_train, y_train)
model = PPO("MlpPolicy", env, verbose=1)
model.learn(total_timesteps=10000)
model.save("models/ppo_ids")