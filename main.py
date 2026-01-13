import pandas as pd
import matplotlib.pyplot as plt


data = pd.read_csv('score_updated.csv')



def loss_func(m,b,points):# ignore this (Just to understand loss function )
    total_error = 0
    for i in range(len(points)):
        x = points.iloc[i].Hours
        y = points.iloc[i].Scores
        total_error += (y-(m*x+b))** 2
    total_error /float(len(points))

def gradient_decent(m_now,b_now,points,L):
    m_gradient= 0 
    b_gradient = 0 
    n = len(points)
    for i in range(n):
        x = points.iloc[i].Hours
        y = points.iloc[i].Scores

        m_gradient = -(2/n)* x *(y-(m_now * x + b_now))
        b_gradient = -(2/n)*(y-(m_now * x + b_now))

    m = m_now - m_gradient * L
    b = b_now - b_gradient * L

    return m,b

m = 0
b = 0
L = 0.01
epochs = 300

for i in range(epochs):
    m,b =gradient_decent(m,b,data,L)

    if i % 50 == 0:
        print(f"Epochs= {i}")

plt.scatter(data["Hours"],data["Scores"], color = "black")
x_min = data["Hours"].min()
x_max = data["Hours"].max()

plt.plot([x_min, x_max], [m*x_min + b, m*x_max + b], color="red")
plt.show()


