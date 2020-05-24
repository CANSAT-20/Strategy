class Sensor(object):
	def __init__(self):
		pass
	def sensorOn(self):
		print("Sensor ON")
	def sensorOff(self):
		print("Sensor off")


class Light(object):
	def __init__(self):
		pass
	def lightOn(self):
		print("Light on")
	def lightOff(self):
		print("Light off")


class Smoke(object):
	def __init__(self):
		pass
	def smokeOn(self):
		print("Smoke on")
	def smokeOff(self):
		print("Smoke off")


class Meta(type):
	""" SingleTon """
	_instance = {}

	def __call__(cls, *args, **kwargs):
		if cls not in cls._instance:
			cls._instance[cls] = super(Meta, cls).__call__(*args, **kwargs)
			return cls._instance[cls]

class Facade(metaclass = Meta):
	def __init__(self):
		self._sensor = Sensor()
		self._light = Light()
		self._smoke = Smoke()

	def Emergency(self):
		self._sensor.sensorOn()
		self._light.lightOn()
		self._smoke.smokeOn()

	def NoEmergency(self):
		self._sensor.sensorOff()
		self._light.lightOff()
		self._smoke.smokeOff()




if __name__ == "__main__":
	facade = Facade()
	print(facade)
	facade1 = Facade()
	print(facade1)
	sensor = int(input("Enter the sensor value: "))

	if(sensor > 30):
		facade.Emergency()
	else:
		facade.NoEmergency()
