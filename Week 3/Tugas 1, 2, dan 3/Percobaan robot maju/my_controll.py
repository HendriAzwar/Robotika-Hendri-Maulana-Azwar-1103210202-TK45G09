from controller import Robot

# Inisialisasi robot
robot = Robot()

# Waktu langkah untuk simulasi (dalam milidetik)
timestep = int(robot.getBasicTimeStep())

# Inisialisasi motor
left_motor = robot.getDevice('left wheel motor')
right_motor = robot.getDevice('right wheel motor')

# Set mode motor ke posisi tak terhingga (infinite)
left_motor.setPosition(float('inf'))
right_motor.setPosition(float('inf'))

# Set kecepatan motor (nilai positif untuk maju)
left_motor.setVelocity(2.0)  # Atur kecepatan motor kiri
right_motor.setVelocity(2.0)  # Atur kecepatan motor kanan

# Loop kontrol untuk menjaga gerakan
while robot.step(timestep) != -1:
    pass  # Tidak ada kontrol tambahan, robot bergerak maju terus menerus
