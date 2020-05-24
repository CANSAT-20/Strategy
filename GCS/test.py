class Facade:
    def __init__(self):
        self.sensor = Sensor()
        self.light = Light()
        self.smoke = Smoke()

    def EmergencyOn(self):
        self.sensor.SensorOn()
        self.light.LightOn()
        self.smoke.SmokeOn()
        print("Emergency is On")

    def EmergencyOff(self):
        self.sensor.SensorOff()
        self.smoke.SmokeOff()
        self.light.LightOff()
        print("Emergency is Off")

class Sensor:
    def SensorOn(self):
        print("Sensor is On")

    def SensorOff(self):
        print("Sensor is Off")

class Light:
    def LightOn(self):
        print("Light is On")

    def LightOff(self):
        print("Light is Off")

class Smoke:
    def SmokeOn(self):
        print("Smoke is On")
    def SmokeOff(self):
        print("Smoke is Off")

if __name__ == '__main__':
    print("Enter the sensor Value")
    n=int(input())
    facade = Facade()
    if(n>60):
        facade.EmergencyOn()
    else:
        facade.EmergencyOff()
