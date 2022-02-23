"""
Final Implementation of WeatherData.  Complete all the TODOs
"""


class Subject:
    # Both of the following two methods take an
    # observer as an argument; that is, the observer
    # to be registered ore removed.
    def registerObserver(observer):
        pass
    def removeObserver(observer):
        pass

    # This method is called to notify all observers
    # when the Subject's state (measuremetns) has changed.
    def notifyObservers():
        pass

# The observer class is implemented by all observers,
# so they all have to implemented the update() method. Here
# we're following Mary and Sue's lead and
# passing the measurements to the observers.
class Observer:
    def update(self, temp, humidity, pressure):
        pass

# WeatherData now implements the subject interface.
class WeatherData(Subject):

    def __init__(self):
        self.observers = []
        self.temperature = 0
        self.humidity = 0
        self.pressure = 0


    def registerObserver(self, observer):
        # When an observer registers, we just
        # add it to the end of the list.
        self.observers.append(observer)

    def removeObserver(self, observer):
        # When an observer wants to un-register,
        # we just take it off the list.
        self.observers.remove(observer)

    def notifyObservers(self):
        # We notify the observers when we get updated measurements
        # from the Weather Station.
        for ob in self.observers:
            ob.update(self.temperature, self.humidity, self.pressure)

    def measurementsChanged(self):
        self.notifyObservers()

    def setMeasurements(self, temperature, humidity, pressure):
        self.temperature = temperature
        self.humidity = humidity
        self.pressure = pressure

        self.measurementsChanged()

    # other WeatherData methods here.

class CurrentConditionsDisplay(Observer):

    def __init__(self, weatherData):
        self.temerature = 0
        self.humidity = 0
        self.pressure = 0

        self.weatherData = weatherData # save the ref in an attribute.
        weatherData.registerObserver(self) # register the observer
                                           # so it gets data updates.
    def update(self, temperature, humidity, pressure):
        self.temerature = temperature
        self.humidity = humidity
        self.pressure = pressure
        self.display()

    def display(self):
        print("Current conditions:", self.temerature,
              "F degrees and", self.humidity, "[%] humidity",
              "and pressure", self.pressure,
              "\n ----------------------------------------------------")

# Implement StatisticsDisplay class and ForecastDisplay class.

# The StatisticsDisplay class should keep track of the min/average/max
# measurements and display them.
class StatsiticsDisplay(Observer):

    def __init__(self, weatherData):
        self.temp_list = []
        self.humidity_list = []
        self.pressure_list = []

        self.weatherData = weatherData # save the ref in an attribute.
        weatherData.registerObserver(self) # register the observer
                                           # so it gets data updates.
    def update(self, temperature, humidity, pressure):
        self.temp_list.append(temperature)
        self.humidity_list.append(humidity)
        self.pressure_list.append(pressure)
        self.stats_display()

    def calculate_stats(self, measurements_list):
        min = average = max = total = 0
        if measurements_list:
            min = max = measurements_list[0]
            for measurement in measurements_list:
                if measurement < min:
                    min = measurement
                elif measurement > max:
                    max = measurement
                total += measurement

            average = total / len(measurements_list)
            
        return min, average, max

    def stats_display(self):
        print("Current weather stats (min/average/max):", 
              self.calculate_stats(self.temp_list), "F degrees",
              "and", self.calculate_stats(self.humidity_list), "[%] humidity",
              "and pressure", self.calculate_stats(self.pressure_list),
              "\n ----------------------------------------------------")


# The ForecastDisplay class shows the weather forcast based on the current
# temperature, humidity and pressure. Use the following formuals :
# forcast_temp = temperature + 0.11 * humidity + 0.2 * pressure
# forcast_humadity = humidity - 0.9 * humidity
# forcast_pressure = pressure + 0.1 * temperature - 0.21 * pressure
class ForecastDisplay(Observer):

    def __init__(self, weatherData):
        self.forcast_temerature = 0
        self.forcast_humidity = 0
        self.forcast_pressure = 0

        self.weatherData = weatherData # save the ref in an attribute.
        weatherData.registerObserver(self) # register the observer
                                           # so it gets data updates.
    def update(self, temperature, humidity, pressure):
        self.forcast_temperature = temperature + (0.11 * humidity) + (0.2 * pressure)
        self.forcast_humidity = humidity - (0.9 * humidity)
        self.forcast_pressure = pressure + (0.1 * temperature) - (0.21 * pressure)
        self.forecast_display()

    def forecast_display(self):
        print("Current weather forcast:", self.forcast_temerature,
              "F degrees and", self.forcast_humidity, "[%] humidity",
              "and pressure", self.forcast_pressure,
              "\n ----------------------------------------------------")


class WeatherStation:
    def main(self):
        
        ### Subject ###
        weather_data = WeatherData()

        ### Observers ###
        current_display = CurrentConditionsDisplay(weather_data)
        # Create two objects from StatisticsDisplay class and
        # ForecastDisplay class. Also register them to the concerete instance
        # of the Subject class so the they get the measurements' updates.
        statistics_display = StatsiticsDisplay(weather_data)
        forecast_display = ForecastDisplay(weather_data)

        ### Weather Updates ###
        print("----------------------------------------------------")
        weather_data.setMeasurements(80, 65, 30.4)
        print()
        weather_data.setMeasurements(82, 70, 29.2)
        print()
        weather_data.setMeasurements(78, 90, 29.2)
        print()

        # un-register the observers
        weather_data.removeObserver(current_display)
        weather_data.removeObserver(statistics_display)
        weather_data.removeObserver(forecast_display)

        weather_data.setMeasurements(120, 100, 1000)



if __name__ == "__main__":
    w = WeatherStation()
    w.main()
