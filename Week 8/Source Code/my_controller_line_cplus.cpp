#include <webots/Robot.hpp>
#include <webots/Motor.hpp>
#include <webots/DistanceSensor.hpp>
#include <iostream>

#define TIME_STEP 32  // Langkah waktu simulasi (32 ms)

using namespace webots;

int main() {
  Robot robot;

  // Motor
  Motor *left_motor = robot.getMotor("left wheel motor");
  Motor *right_motor = robot.getMotor("right wheel motor");
  left_motor->setPosition(INFINITY);
  right_motor->setPosition(INFINITY);
  left_motor->setVelocity(0.0);
  right_motor->setVelocity(0.0);

  // Sensor
  DistanceSensor *ir0 = robot.getDistanceSensor("ir0");
  DistanceSensor *ir1 = robot.getDistanceSensor("ir1");
  ir0->enable(TIME_STEP);
  ir1->enable(TIME_STEP);

  const double THRESHOLD = 100.0;  // Ambang batas baru

  while (robot.step(TIME_STEP) != -1) {
    double ir0_value = ir0->getValue();
    double ir1_value = ir1->getValue();

    // Debugging
    std::cout << "IR Left: " << ir0_value << ", IR Right: " << ir1_value << std::endl;

    // Logika kontrol
    double left_speed = 0.0;
    double right_speed = 0.0;

    if (ir0_value > THRESHOLD && ir1_value > THRESHOLD) {
      left_speed = 3.0;
      right_speed = 3.0;
    } else if (ir0_value > THRESHOLD) {
      left_speed = 3.0;
      right_speed = 1.0;
    } else if (ir1_value > THRESHOLD) {
      left_speed = 1.0;
      right_speed = 3.0;
    } else {
      left_speed = 0.0;
      right_speed = 0.0;
    }

    left_motor->setVelocity(left_speed);
    right_motor->setVelocity(right_speed);
  }

  return 0;
}
