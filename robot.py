from drivetrain import Drivetrain

import wpilib

class MyRobot(wpilib.TimedRobot):
    def robotInit(self):
        self.drivetrain = Drivetrain()
        self.stick = wpilib.Joystick(0)

    def teleopInit(self):
        self.drivetrain.differential_drive.setSafetyEnabled(True)

    def teleopPeriodic(self):
        self.drivetrain.differential_drive.arcadeDrive(
            self.stick.getRawAxis(1),
            self.stick.getRawAxis(0),
            True
        )
    
if __name__ == "__main__":
    wpilib.run(MyRobot)