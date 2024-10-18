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

# Atur kecepatan motor untuk gerakan melingkar
# Kecepatan motor kiri lebih lambat daripada motor kanan
left_motor.setVelocity(1.2)  # Kecepatan lebih lambat
right_motor.setVelocity(2.0)  # Kecepatan lebih cepat

# Loop kontrol untuk menjaga gerakan
while robot.step(timestep) != -1:
    pass  # Robot terus bergerak dalam lingkaran
