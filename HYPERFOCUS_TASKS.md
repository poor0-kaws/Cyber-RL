# RL-Based Intrusion Detection System — Hyper-Focus Task List

## PROJECT OVERVIEW

**Goal:** A trained Reinforcement Learning agent that correctly classifies network traffic (Allow/Block/Investigate) with >95% accuracy, verified by an evaluation script.

---

## PHASE 1: Project Shell (COMPLETED)

**Task List:**

- [x] **Task 1.** Create `src/` and `models/` directories.
- [x] **Task 2.** Create `requirements.txt` with `numpy`, `scikit-learn`, `gymnasium`, `stable-baselines3`.
- [x] **Task 3.** Create `src/run.py` that prints "RL IDS ready".

---

## PHASE 2: Data Generation (COMPLETED)

**Task List:**

- [x] **Task 10.** Create `src/data_loader.py` with `generate_data` returning X, y.
- [x] **Task 16.** Implement `load_and_split` in `src/data_loader.py`.

---

## PHASE 3: Gym Environment

**Goal:** `IdsEnv` class exists; action space has 3 actions; `step` returns correct reward (+5/-10).

**Task List:**

- [x] **Task 21.** Create `src/env.py` with `IdsEnv(gym.Env)` class.
  - *Expected feedback:* Class exists.

- [ ] **Task 22.** In `IdsEnv.__init__`, define `self.n_samples = len(X_train)` and `self.current_idx = 0`.
  - *Expected feedback:* `env.n_samples` returns integer length.
  - *Test Case:* `python -c "from src.env import IdsEnv; import numpy as np; e = IdsEnv(np.zeros((10,2)), np.zeros(10)); print(e.n_samples)"` (Prints 10)

- [ ] **Task 23.** In `IdsEnv.__init__`, define `self.action_space = gym.spaces.Discrete(3)`.
  - *Expected feedback:* `env.action_space` is Discrete(3).
  - *Documentation:* [Gym Spaces](https://gymnasium.farama.org/api/spaces/#discrete)
  - *Test Case:* `python -c "from src.env import IdsEnv; import numpy as np; e = IdsEnv(np.zeros((10,2)), np.zeros(10)); print(e.action_space)"` (Prints Discrete(3))

- [ ] **Task 24.** In `IdsEnv.__init__`, define `self.observation_space = gym.spaces.Box(low=-np.inf, high=np.inf, shape=(self.X.shape[1],), dtype=np.float32)`.
  - *Expected feedback:* `env.observation_space.shape` matches feature count.
  - *Documentation:* [Gym Box Space](https://gymnasium.farama.org/api/spaces/#box)
  - *Test Case:* `python -c "from src.env import IdsEnv; import numpy as np; e = IdsEnv(np.zeros((10,5)), np.zeros(10)); print(e.observation_space.shape)"` (Prints (5,))

- [ ] **Task 25.** Add `reset(self, seed=None, options=None)` method. Call `super().reset(seed=seed)`.
  - *Expected feedback:* Method exists.
  - *Documentation:* [Gym Reset](https://gymnasium.farama.org/api/env/#gymnasium.Env.reset)
  - *Test Case:* `python -c "from src.env import IdsEnv; import numpy as np; e = IdsEnv(np.zeros((10,2)), np.zeros(10)); print(hasattr(e, 'reset'))"` (Prints True)

- [ ] **Task 26.** In `reset`, shuffle data indices: `self.order = np.random.permutation(self.n_samples)` and set `self.current_idx = 0`.
  - *Expected feedback:* `self.order` is shuffled array.
  - *Test Case:* `python -c "from src.env import IdsEnv; import numpy as np; e = IdsEnv(np.zeros((10,2)), np.zeros(10)); e.reset(); print(len(e.order))"` (Prints 10)

- [ ] **Task 27.** In `reset`, return first obs and empty info dict: `return self.X[self.order[0]], {}`.
  - *Expected feedback:* `reset()` returns (array, dict).
  - *Test Case:* `python -c "from src.env import IdsEnv; import numpy as np; e = IdsEnv(np.zeros((10,2)), np.zeros(10)); obs, _ = e.reset(); print(obs.shape)"` (Prints (2,))

- [ ] **Task 28.** Add `step(self, action)` method. Get true label: `true_label = self.y[self.order[self.current_idx]]`.
  - *Expected feedback:* Method exists.
  - *Documentation:* [Gym Step](https://gymnasium.farama.org/api/env/#gymnasium.Env.step)

- [ ] **Task 29.** In `step`, calculate reward (+5 if correct, -10 if missed).
  - *Hint:* `reward = 5 if action == true_label else -10`.
  - *Expected feedback:* Reward calculated.

- [ ] **Task 30.** In `step`, increment `self.current_idx += 1` and check done: `terminated = self.current_idx >= self.n_samples`.
  - *Expected feedback:* Terminated logic works.

- [ ] **Task 31.** In `step`, return full tuple: `(self.X[self.order[self.current_idx]], reward, terminated, False, {"label": true_label})`. Handle index out of bounds (return zeros if done).
  - *Expected feedback:* `step` returns 5-tuple.
  - *Test Case:* `python -c "from src.env import IdsEnv; import numpy as np; e = IdsEnv(np.zeros((2,2)), np.array([0,1])); e.reset(); print(len(e.step(0)))"` (Prints 5)

---

## PHASE 4: Train & Evaluate (PENDING)

(Will populate after Phase 3 is done)

---

## HYPER-FOCUS EXECUTION PROTOCOL

- **Work in 5-minute loops.**
- **Only do one task at a time.**
- **Never think longer than 60 seconds.**
- **Track completed tasks.**
