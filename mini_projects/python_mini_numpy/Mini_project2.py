import numpy as np

# For reproducibility (so results are same each run)
np.random.seed(42)

# 1. Generate synthetic house sizes (in sq ft)
#    100 samples, sizes between 500 and 3500
x=np.random.randint(500,3500,size=100)

# 2. True relationship: price = 50 + 0.08 * size + noise
true_intercept=50
true_slope=0.08

noise=np.random.normal(0,20,size=100)

y=true_intercept+true_slope*x+noise


#2. Reshape x to 2D (100,) --> (100,1)
x=x.reshape(-1,1) 

print("x shape after reshaping:",x.shape)
print("y shape:",y.shape)

# 3. Train-test split (80% train, 20% test) using NumPy only
n_samples=x.shape[0]
train_ratio=0.8
n_train=int(n_samples*train_ratio)

# Generate shuffled indices
indices = np.arange(n_samples)
np.random.shuffle(indices)

train_idx = indices[:n_train]
test_idx = indices[n_train:]

X_train = x[train_idx]
y_train = y[train_idx]
X_test = x[test_idx]
y_test = y[test_idx]

print("Train X shape:", X_train.shape)
print("Train y shape:", y_train.shape)
print("Test X shape:", X_test.shape)
print("Test y shape:", y_test.shape)


# 4. Add bias term (column of ones) to X_train and X_test
#    This lets the model learn an intercept term.
X_train_bias = np.hstack([
    np.ones((X_train.shape[0], 1)),  # column of 1s
    X_train                           # original feature
])

X_test_bias = np.hstack([
    np.ones((X_test.shape[0], 1)),
    X_test
])

print("X_train_bias shape:", X_train_bias.shape)  # (80, 2)
print("X_test_bias shape:", X_test_bias.shape)    # (20, 2)

# 5. Compute theta using the Normal Equation:
#    theta = (X^T X)^(-1) X^T y

# Option 1: Direct inverse (okay for this small example)
XtX = X_train_bias.T @ X_train_bias           # X^T X
XtX_inv = np.linalg.inv(XtX)                  # (X^T X)^(-1)
Xt_y = X_train_bias.T @ y_train               # X^T y

theta = XtX_inv @ Xt_y                        # shape (2,)


# Option 2: Safer (handles singular matrices better)
# theta = np.linalg.pinv(X_train_bias) @ y_train

print("Theta (parameters):", theta)
intercept, slope = theta
print("Learned intercept:", intercept)
print("Learned slope:", slope)


# 6. Make predictions on train and test sets
y_train_pred = X_train_bias @ theta
y_test_pred = X_test_bias @ theta

# 7. Define a function to compute Mean Squared Error (MSE)
def mse(y_true, y_pred):
    return np.mean((y_true - y_pred) ** 2)

train_mse = mse(y_train, y_train_pred)
test_mse = mse(y_test, y_test_pred)

print("Train MSE:", train_mse)
print("Test MSE:", test_mse)


def predict_price(size_sqft, theta):
    """
    size_sqft: single number or list/array of numbers (e.g., 1200 or [800, 1200, 2000])
    theta: learned parameters [intercept, slope]
    """
    size_sqft = np.array(size_sqft, dtype=float)

    # If it's a single value, make it 1D
    if size_sqft.ndim == 0:
        size_sqft = size_sqft.reshape(1)

    # Build X with bias: [ [1, size], [1, size], ... ]
    X_input = np.column_stack([
        np.ones(size_sqft.shape[0]),
        size_sqft
    ])

    return X_input @ theta  # returns array of predictions



test_sizes = [800, 1200, 2000]

pred_prices = predict_price(test_sizes, theta)

for size, price in zip(test_sizes, pred_prices):
    print(f"Predicted price for {size} sq ft: {price:.2f} (in thousands)")



def r2_score(y_true, y_pred):
    """
    R² = 1 - SS_res / SS_tot
    SS_res = sum of squared residuals
    SS_tot = total variance in data
    """
    ss_res = np.sum((y_true - y_pred) ** 2)
    ss_tot = np.sum((y_true - np.mean(y_true)) ** 2)
    return 1 - ss_res / ss_tot


train_r2 = r2_score(y_train, y_train_pred)
test_r2 = r2_score(y_test, y_test_pred)

print("Train R²:", train_r2)
print("Test R²:", test_r2)
