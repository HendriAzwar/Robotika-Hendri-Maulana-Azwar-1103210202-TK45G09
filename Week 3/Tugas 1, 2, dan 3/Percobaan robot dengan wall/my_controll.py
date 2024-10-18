from controller import Robot

# Inisialisasi robot
robot = Robot()

# Waktu langkah untuk simulasi (dalam milidetik)
timestep = int(robot.getBasicTimeStep())

# Inisialisasi motor
left_motor = robot.getDevice('left wheel motor')
right_motor = robot.getDevice('right wheel motor')

# Inisialisasi sensor proximity (terdapat 8 sensor di e-puck)
proximity_sensors = []
sensor_names = ['ps0', 'ps1', 'ps2', 'ps3', 'ps4', 'ps5', 'ps6', 'ps7']

for name in sensor_names:
    sensor = robot.getDevice(name)
    sensor.enable(timestep)
    proximity_sensors.append(sensor)

# Set mode motor ke posisi tak terhingga (infinite)
left_motor.setPosition(float('inf'))
right_motor.setPosition(float('inf'))

# Set kecepatan default
forward_speed = 2.0
turn_speed = 1.0

# Loop kontrol utama
while robot.step(timestep) != -1:
    # Cek sensor proximity di depan (ps0 dan ps7 berada di bagian depan)
    front_left = proximity_sensors[0].getValue()
    front_right = proximity_sensors[7].getValue()

    if front_left > 80 or front_right > 80:  # Jika sensor mendeteksi halangan
        # Berbelok kanan jika mendeteksi halangan di depan
        left_motor.setVelocity(turn_speed)
        right_motor.setVelocity(-turn_speed)
    else:
        # Gerakan maju jika tidak ada halangan
        left_motor.setVelocity(forward_speed)
        right_motor.setVelocity(forward_speed)
