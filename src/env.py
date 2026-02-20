from random import seed
from turtle import Terminator, reset
import gymnasium as gym
from gymnasium.spaces.utils import T
import numpy as np 

class IdsEnv(gym.Env): 
    
    def __init__(self, X_train, y_train): 
        self.X = X_train
        self.y = y_train

        self.n_samples = len(self.X)
        self.current_idx = 0
        
        self.action_space = gym.spaces.Discrete(3)

        self.observation_space = gym.spaces.Box(low=-np.inf, high=np.inf,shape=(self.X.shape[1],),dtype=np.float32)
        
    def reset(self,seed=None, options=None): 
        super().reset(seed=seed)
        self.order = np.random.permutation(self.n_samples)
        self.current_idx = 0
        first_obs = self.X[self.order[0]]
        
        return first_obs, {}

    def step(self, action: int): 
        
        idx = self.order[self.current_idx] # getting 
        
        y = self.y[idx] # getting the true answer for the true

        reward = None

        if action == y: # comparing action (agent guess) with the true answer
            reward += 5
            self.current_idx += 1 
        else: 
            reward -= 10
            self.current_idx += 1 
        
        terminated = self.current_idx >= self.n_samples

        if not terminated:
            obs = self.X[self.order[self.current_idx]]
        else: 
            obs = np.zeros(self.observation_space.shape, dtype=np.float32)

        return obs, reward, terminated, False, {"label": y}


        
            