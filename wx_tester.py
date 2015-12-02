import pyowm

def wx_forecast():
        owm = pyowm.OWM('fa7813518ed203b759f116a3bac9bcce')
        observation = owm.weather_at_place('London,uk')
        w = observation.get_weather()
        i = w.get_weather_icon_name()
        addr = str("'http://openweathermap.org/img/w/" + i + "'")
        print(w)
        print(i)
        print(addr)

wx_forecast()