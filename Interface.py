import tkinter as tk


class Interface:
    def __init__(self, canvas, add_particle, remove_particle, reset_simulation, change_speed):
        self.canvas = canvas

        self.add_particle_button = tk.Button(
            canvas,
            text="Add Particle",
            command=add_particle
        )
        self.add_particle_button.place(relx=0.99, y=10, anchor="ne")

        self.remove_particle_button = tk.Button(
            canvas,
            text="Remove Particle",
            command=remove_particle
        )
        self.remove_particle_button.place(relx=0.99, y=45, anchor="ne")

        self.reset_button = tk.Button(
            canvas,
            text="Reset Simulation",
            command=reset_simulation
        )
        self.reset_button.place(relx=0.99, y=80, anchor="ne")

        self.speed_slider = tk.Scale(
            canvas,
            from_=1,
            to=1000,
            orient="horizontal",
            command=change_speed,
            length=150,
            bg="black",
            fg="white",
            highlightthickness=0
        )
        self.speed_slider.set(50)
        self.speed_slider.place(relx=0.99, y=115, anchor="ne")