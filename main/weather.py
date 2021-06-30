import python_weather
import asyncio


async def getweather():
    # declare the client. format defaults to metric system (celcius, km/h, etc.)
    client = python_weather.Client(format=python_weather.METRIC)

    # fetch a weather forecast from a city
    weather = await client.find("New York")

    # returns the current day's forecast temperature (int)
    print("\nToday's average temperature is: ", weather.current.temperature)

    print()
    # get the weather forecast for a few days
    for forecast in weather.forecasts:
        print(str(forecast.date), forecast.sky_text, forecast.temperature)

    # close the wrapper once done
    await client.close()


def run():
    loop = asyncio.get_event_loop()
    loop.run_until_complete(getweather())


# run()
