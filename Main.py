import tkinter as tk
import random
from Particles import Particle
from Interface import Interface
from Physics import Physics


root = tk.Tk()
root.title("Particles Renderer")
root.geometry("800x600")

canvas = tk.Canvas(root, width=800, height=600, bg="black")
canvas.pack()

particles = []
physics = Physics()

WIDTH = 800
HEIGHT = 600

speed = 50

# I added a commit Yay!!!!

def draw_particle(particle):
    particle.canvas_id = canvas.create_rectangle(
        particle.x - particle.size,
        particle.y - particle.size,
        particle.x + particle.size,
        particle.y + particle.size,
        fill=particle.color,
        outline="",
        tags="particle"
    )


def add_particle():
    x = random.randint(5, WIDTH - 5)
    y = random.randint(5, HEIGHT - 5)

    color = random.choice(["red", "blue", "green"])

    particle = Particle(x, y, color, 3)
    particles.append(particle)

    draw_particle(particle)


def remove_particle():
    if particles:
        particle = particles.pop()
        canvas.delete(particle.canvas_id)


def reset_simulation():
    particles.clear()
    canvas.delete("particle")


def change_speed(value):
    global speed
    speed = int(value)


def update_simulation():
    speed_multiplier = speed / 50

    for particle in particles:
        physics.update_particle(
            particle,
            WIDTH,
            HEIGHT,
            speed_multiplier
        )

        canvas.coords(
            particle.canvas_id,
            particle.x - particle.size,
            particle.y - particle.size,
            particle.x + particle.size,
            particle.y + particle.size
        )

    root.after(16, update_simulation)


for color in ["red", "blue", "green"]:
    particle = Particle(
        random.randint(5, WIDTH - 5),
        random.randint(5, HEIGHT - 5),
        color,
        3
    )

    particles.append(particle)
    draw_particle(particle)


interface = Interface(
    canvas,
    add_particle,
    remove_particle,
    reset_simulation,
    change_speed
)

update_simulation()

root.mainloop()