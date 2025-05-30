# simulator.py
# 2D simulation environment for SAFEGUARD
# Tracks agent motion, obstacles, and environmental conditions like friction

import numpy as np
import matplotlib.pyplot as plt

class Environment2D:
    def __init__(self, width=20, height=10):
        self.width = width
        self.height = height
        self.grid = np.zeros((height, width))  # 0 = empty, 1 = obstacle
        self.friction_map = np.ones((height, width))  # 1.0 = normal, <1.0 = slippery

    def place_obstacle(self, x, y):
        self.grid[y, x] = 1

    def set_friction(self, x, y, value):
        self.friction_map[y, x] = value

class Agent:
    def __init__(self, x=0, y=5, heading=(1, 0)):
        self.x = x
        self.y = y
        self.heading = heading  # (dx, dy)
        self.velocity = 1.0  # units per timestep

    def move(self):
        self.x += self.heading[0] * self.velocity
        self.y += self.heading[1] * self.velocity

    def position(self):
        return int(round(self.x)), int(round(self.y))

def simulate_step(env, agent):
    x, y = agent.position()
    if 0 <= x < env.width and 0 <= y < env.height:
        if env.grid[y, x] == 1:
            print("Collision detected at", (x, y))
        else:
            agent.move()
    else:
        print("Agent out of bounds at", (x, y))

def visualize(env, agent):
    display = env.grid.copy()
    ax, ay = agent.position()
    if 0 <= ay < env.height and 0 <= ax < env.width:
        display[ay, ax] = 0.5  # mark agent
    plt.imshow(display, cmap='gray_r')
    plt.title("Environment View")
    plt.show()

if __name__ == "__main__":
    env = Environment2D()
    env.place_obstacle(10, 5)
    env.set_friction(8, 5, 0.5)

    agent = Agent()

    for _ in range(15):
        simulate_step(env, agent)
        visualize(env, agent)

