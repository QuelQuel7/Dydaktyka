import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import random

num_electrons = 50  # Number of electrons
num_frames = 100  # Number of frames in the animation
delta_t = 0.05  # Time interval between frames
velocity = 1
positions = [0]*50
positions_y = [0]*50
positions_yprime = [-5] * 50
positionsprime = [-5]*50
numbers = [0,1]
for i in range(50):
    positions[i] = i/100. - 0.47
def update_positions(frames):
    
    delta_s = velocity * delta_t

    for i in range(50):
        if(positions[i] >= 0.35 and positions_y[i-1] <=0):
            positions[i] = 0.39
            if(positions_y[i] >= 0.47):
                positions_y[i] -= delta_s
            else:
                positions_y[i] += delta_s
            positionsprime[i] = 0.61
            positions_yprime[i] = positions_y[i]
        elif(positions[i] >= 0.35):
            positions[i] = 0.39
            if(positions_y[i] ==0):
                 positions_y[i] -=delta_s
            if(positions_y[i] <= -0.47):
                 positions_y[i] += delta_s
            else:
                 positions_y[i] -= delta_s
            positionsprime[i] = 0.61
            positions_yprime[i] = positions_y[i]
        else:  
            positions[i] += delta_s
    
    plt.clf()
    plt.plot([0.4, 0.4], [-0.5, 0.5], color='black')
    plt.plot([0.6, 0.6], [-0.5, 0.5], color='black') 
    plt.plot([0.,0.4],[0,0],color='black')
    plt.plot([0.6,1],[0,0],color='black')
    plt.scatter(positions,positions_y, color='blue')
    plt.scatter(positionsprime,positions_yprime, color = 'red')
    plt.xlim(0, 1)
    plt.ylim(-1, 1)

fig, ax = plt.subplots()

ani = animation.FuncAnimation(fig, update_positions, frames=num_frames)

# Display the animation
plt.show()
