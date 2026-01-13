# Linear Regression from Scratch (Gradient Descent) 📈

This project implements **Simple Linear Regression** using **Gradient Descent** from scratch in Python and visualizes the best-fit line using `matplotlib`.

The dataset contains two columns:

- `Hours` → input feature (independent variable)
- `Scores` → target value (dependent variable)

---

## 🚀 Features

- Loads dataset using `pandas`
- Implements gradient descent manually (no sklearn)
- Trains a linear regression model:
  \[
  y = mx + b
  \]
- Plots:
  - Scatter plot of training data
  - Best-fit regression line

---

## 📂 Project Structure

Linear_Regression/
│
├── archive/
│ └── score_updated.csv
│
├── linear_regression.py
└── README.md


---

## 🧠 Gradient Descent Formula

The model is:

\[
y = mx + b
\]

We update parameters using gradient descent:

\[
m = m - L \cdot \frac{\partial}{\partial m}
\]
\[
b = b - L \cdot \frac{\partial}{\partial b}
\]

Where:

- `m` = slope
- `b` = intercept
- `L` = learning rate
- `epochs` = number of iterations

---

## ⚙️ Requirements

Install dependencies:

```bash
pip install pandas matplotlib


▶️ How to Run

Run the Python file:

python linear_regression.py


📌 Notes on Learning Rate

The learning rate controls how fast the model learns.

Example:

L = 0.0001 → very small steps → needs more epochs to converge

L = 0.01 → larger steps → converges faster in fewer epochs

So:

small L + large epochs = slow but stable

large L + small epochs = fast learning (but can diverge if too large)

📊 Output

The program generates a plot showing:

Black dots → dataset points

Red line → regression best-fit line learned using gradient descent
