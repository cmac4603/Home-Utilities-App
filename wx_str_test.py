import pyowm

owm = pyowm.OWM('fa7813518ed203b759f116a3bac9bcce')
observation = owm.weather_at_place('London,uk')
w = observation.get_weather()
wtemp = str(w.get_temperature('celsius'))
print(wtemp.strip('{}'))
wtemp_list = list(wtemp)
print(wtemp_list)