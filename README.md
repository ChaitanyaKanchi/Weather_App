# Weather Forecast Dashboard

This Streamlit application provides a weather forecast for the next few days, allowing users to select a location and view detailed information about temperature, pressure, and sky conditions. The app also offers suggestions based on the current temperature and pressure.

## Features

- **Location-based Forecast**: Input a location to receive weather data for the next 1 to 7 days.
- **Temperature Data**: View temperature forecasts with interactive line charts.
- **Pressure Data**: Check atmospheric pressure trends over the selected days.
- **Sky Conditions**: See visual representations of weather conditions (clear, cloudy, rain, snow) over time.
- **Real-time Suggestions**: Get weather-related suggestions based on the nearest forecasted temperature or pressure.
- **Time Zone Conversion**: Automatically converts the forecast time from UTC to IST (Indian Standard Time).

## Installation

### Prerequisites

- **Python 3.7+**: Ensure Python is installed on your machine. You can download it from [python.org](https://www.python.org/downloads/).
- **Pip**: Pip is typically installed with Python. Verify it by running `pip --version` in your terminal.

### Clone the Repository

1. Open a terminal or command prompt.
2. Clone the repository:
   ```bash
   git clone https://github.com/your-username/weather-forecast-dashboard.git
   cd weather-forecast-dashboard
## Setup API Key

To use this application, you need an API key from OpenWeatherMap.

1. **Obtain an API Key**:
   - Sign up for a free account on [OpenWeatherMap](https://home.openweathermap.org/users/sign_up).
   - After logging in, navigate to the API keys section in your profile.
   - Create a new API key or use the default one provided.

2. **Configure the API Key in the Project**:
   - In the root directory of your project, create a directory named `.streamlit`:
     ```bash
     mkdir .streamlit
     ```
   - Inside the `.streamlit` directory, create a file named `secrets.toml`:
     ```bash
     touch .streamlit/secrets.toml
     ```
   - Open the `secrets.toml` file and add your API key like this:
     ```toml
     [secrets]
     api_key = "YOUR_API_KEY"
     ```
   - Replace `"YOUR_API_KEY"` with the actual API key you obtained from OpenWeatherMap.

3. **Keep Your API Key Secure**:
   - The `.streamlit/secrets.toml` file should not be included in version control. It is automatically ignored by Git when using a `.gitignore` file.
   - Never share your API key publicly.
## Usage

1. **Input a Place**: Enter the name of the location you want the weather forecast for in the text input field.

2. **Select Forecast Days**: Use the slider in the sidebar to choose the number of forecast days (1 to 7).

3. **Choose Data to View**:
   - **Temperature**: Displays a line chart of the temperature for the selected days.
   - **Pressure**: Shows a line chart of the atmospheric pressure.
   - **Sky**: Provides visual icons for different weather conditions (e.g., Clear, Clouds, Rain, Snow).

4. **View Suggestions**: After selecting "Temperature" or "Pressure," click the "Suggestion" button to get weather-related advice based on the nearest forecast data.

5. **Interpretation**:
   - **Temperature**: The line chart displays the temperature over the selected number of days. The nearest forecasted temperature to the current time is highlighted with suggestions.
   - **Pressure**: The pressure line chart shows atmospheric pressure trends. A suggestion based on the nearest forecasted pressure is also provided.
   - **Sky Conditions**: Sky conditions are visually represented with images, allowing you to quickly understand the weather for the coming days.
## Dependencies

- **Streamlit**: Interactive web application framework for Python. Required to build and run the dashboard.
- **Plotly**: Library used to create interactive line charts for visualizing temperature and pressure data.
- **Requests**: For making HTTP requests to the OpenWeatherMap API to fetch weather data.
- **Pytz**: For handling time zone conversions, particularly converting UTC time to IST (Indian Standard Time).

To install the dependencies, make sure you're in the root directory of your project and run:

```bash
pip install -r requirements.txt
