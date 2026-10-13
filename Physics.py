class Physics:
    def __init__(self):
        pass

    def update_particle(self, particle, width, height, speed_multiplier=1):
        # Move the particle using the selected speed
        particle.x += particle.vx * speed_multiplier
        particle.y += particle.vy * speed_multiplier

        # Check the left wall
        if particle.x - particle.size <= 0:
            particle.x = particle.size
            particle.vx = -particle.vx

        # Check the right wall
        if particle.x + particle.size >= width:
            particle.x = width - particle.size
            particle.vx = -particle.vx

        # Check the top wall
        if particle.y - particle.size <= 0:
            particle.y = particle.size
            particle.vy = -particle.vy

        # Check the bottom wall
        if particle.y + particle.size >= height:
            particle.y = height - particle.size
            particle.vy = -particle.vy