# Weather Fetcher

This is a simple Python script that fetches and prints the current weather for a given city using the OpenWeatherMap API. This script was originally created by NateDoesThingz.

## Prerequisites

- Python 3.x
- `requests` library (can be installed via pip: `pip install requests`)
- An API key from OpenWeatherMap

## Usage

1. Clone this repository to your local machine.
2. Replace `api_key` in the script with your actual OpenWeatherMap API key.
3. Run the script in your terminal with the command `python weather.py`.
4. When prompted, enter the name of the city you want to fetch the weather for.

## Integration

To integrate this script into your project:

1. Copy the `weather.py` file into your project directory.
2. Import the `get_weather` function in your code with `from weather import get_weather`.
3. Call `get_weather(city, api_key)` in your code, replacing `city` with the name of the city and `api_key` with your OpenWeatherMap API key.

## License

This project is free to use and modify for any purpose.

## Credits

This script was originally created by NateDoesThingz. Feel free to contribute to this project by submitting pull requests.
