# Cyber-RL: Reinforcement Learning for Intrusion Detection

A prototype Reinforcement Learning (RL) system designed to detect malicious activity using the Proximal Policy Optimization (PPO) algorithm. This project implements a custom Gymnasium environment to simulate an Intrusion Detection System (IDS) task.

## 🚀 Project Overview

The system treats intrusion detection as a sequential decision-making problem:
1. **Environment:** A custom `IdsEnv` that presents network traffic samples.
2. **Agent:** A PPO agent (via Stable Baselines3) that predicts whether traffic is "Safe" (0) or an "Attack" (1).
3. **Reward Logic:** 
   - **Correct Prediction:** +5 reward.
   - **Incorrect Prediction:** -10 penalty.

## 🏗️ Architecture

```text
Data Loader ──▶ Environment (IdsEnv) ──▶ Agent (PPO)
      ▲               │                     │
      └───────────────┴─────────────────────┘
                 (Reward & Feedback)
```

## 📁 Project Structure

- `src/data_loader.py`: Generates synthetic network features with learnable patterns.
- `src/env.py`: Custom Gymnasium environment for IDS.
- `src/train.py`: Script to train the PPO model.
- `src/eval.py`: Evaluation script with Accuracy and Confusion Matrix metrics.
- `models/`: Directory where trained models are saved.

## 🛠️ Installation

1. **Clone the repository:**
   ```bash
   git clone https://github.com/poor0-kaws/Cyber-RL.git
   cd Cyber-RL
   ```

2. **Set up a virtual environment:**
   ```bash
   python -m venv env
   source env/bin/activate  # On macOS/Linux
   ```

3. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

## 🎮 How to Run

### 1. Training
Train the agent on 10,000 timesteps:
```bash
python -m src.train
```

### 2. Evaluation
Evaluate the trained agent on unseen test data and view the confusion matrix:
```bash
python -m src.eval
```

## 📊 Performance Metrics

The system tracks:
- **Accuracy:** Overall percentage of correct classifications.
- **Confusion Matrix:**
  - **True Positives (TP):** Attacks correctly identified and blocked.
  - **True Negatives (TN):** Safe traffic correctly allowed.
  - **False Positives (FP):** Safe traffic incorrectly blocked.
  - **False Negatives (FN):** Attacks missed (Critical security metric).

## 🔮 Future Work
- Integration with real-world datasets (e.g., NSL-KDD, CIC-IDS2017).
- Implementation of more complex reward functions (penalizing FN more than FP).
- Testing with different RL algorithms (A2C, DQN).
