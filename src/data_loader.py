import numpy as np

def generate_data(n_samples=1000, n_features=10): 
    X = np.random.randn(n_samples, n_features).astype(np.float32)
    y = np.random.randint(0,2, size=n_samples)
    return X, y

def load_and_split(train_ratio=0.8): 

    X, y = generate_data(n_samples=1000, n_features=10)
    
    # Total values 
    n = len(X)
    # 80th percent value to split the data
    idx = int(n * train_ratio)

    # 80% of data for training
    X_train = X[:idx] #clues that the agent will run on
    y_train = y[:idx] # answers to verify the agent's prediction
    
    # 20% of data for validation 
    X_val = X[idx:] # same as above
    y_val = y[idx:] # same as above

    return X_train, y_train, X_val, y_val



    
