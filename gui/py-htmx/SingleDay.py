from __future__ import annotations
from typing import Any, Optional, Dict
from pyhtmx import Div, Ul, Li  # type: ignore
from pyhtmx_gui.kit import Widget, SessionItem, Page
from pyhtmx.html_tag import HTMLTag

CACHE_DIR = "/cache/ovos-skill-weather.openvoiceos/py-htmx"


class SingleDayWeatherWidget(Widget):
    _parameters = (
        "weatherCode",
        "weatherDate",
        "weatherCondition",
        "weatherLocation",
        "highTemperature",
        "lowTemperature",
        "chanceOfPrecipitation",
        "windSpeed",
        "humidity",
    )

    def __init__(self, session_data: Optional[Dict[str, Any]] = None):
        super().__init__(name="single-day-weather-widget", session_data=session_data)

        session_data = session_data or {}
        weather_code = session_data.get("weatherCode", 0)
        animation_src = SingleDayWeatherWidget.get_weather_animation(weather_code)

        self._icon: HTMLTag = HTMLTag(
            tag="lottie-player",
            _id="weather-animation",
            src=animation_src,
            background="transparent",
            loop="",
            autoplay="",
            style={
                "width": "10vw",
                "height": "10vw",
            },
        )
        self.add_interaction(
            "weatherCondition",
            SessionItem(
                parameter="weatherCondition",
                attribute="src",
                component=self._icon,
            ),
        )

        self._date: Div = Div(
            inner_content=session_data.get("weatherDate", "Unknown Date"),
            _id="weather-date",
            _class="text-[2vw] font-semibold text-gray-800",
        )
        self.add_interaction(
            "weatherDate",
            SessionItem(
                parameter="weatherDate",
                attribute="inner_content",
                component=self._date,
            ),
        )

        self._location: Div = Div(
            inner_content=session_data.get("weatherLocation", "Unknown Location"),
            _id="weather-location",
            _class="text-[2vw] font-semibold text-gray-800",
        )
        self.add_interaction(
            "weatherLocation",
            SessionItem(
                parameter="weatherLocation",
                attribute="inner_content",
                component=self._location,
            ),
        )

        details_items: Dict[str, Li] = {
            "hightTemperature": Li(
                f"High: {session_data.get('highTemperature', '--')}°C",
                _id="high-temp",
                _class="inline",
            ),
            "lowTemperature": Li(
                f"Low: {session_data.get('lowTemperature', '--')}°C",
                _id="low-temp",
                _class="inline",
            ),
            "humidity": Li(
                f"Humidity: {session_data.get('humidity', '--')}%",
                _id="humidity",
                _class="inline",
            ),
            "windSpeed": Li(
                f"Wind: {session_data.get('windSpeed', '--')} km/h",
                _id="wind",
                _class="inline",
            ),
            "chanceOfPrecipitation": Li(
                f"Precipitation: {session_data.get('chanceOfPrecipitation', '--')}%",
                _id="precipitation",
                _class="inline",
            ),
        }
        self._details: Div = Div(
            Ul(
                [item for item in details_items.values()],
                style={"list-style-type": "none"},
            ),
            _id="weather-details",
            _class="text-[1.5vw] text-gray-800",
        )
        for key, item in details_items.items():
            self.add_interaction(
                key,
                SessionItem(
                    parameter=item._id,
                    attribute="inner_content",
                    component=item,
                ),
            )

        self._widget: Div = Div(
            [
                self._icon,
                self._date,
                self._location,
                self._details,
            ],
            _id="single-day-weather-widget",
            _class=[
                "p-[2vw]",
                "flex",
                "flex-col",
                "justify-center",
                "items-center",
                "rounded-2xl",
                "shadow-xl",
                "bg-blue-100",  # Effen achtergrondkleur
            ],
            style={
                "width": "80vw",
                "height": "80vh",
                # geen achtergrond gradient hier!
            },
        )

    @staticmethod
    def get_weather_animation(weather_code: int) -> str:
        animations = {
            0: f"{CACHE_DIR}/animations/sun.json",
            1: f"{CACHE_DIR}/animations/night.json",
            2: f"{CACHE_DIR}/animations/partial_clouds.json",
            3: f"{CACHE_DIR}/animations/partial_clouds.json",
            4: f"{CACHE_DIR}/animations/clouds.json",
            5: f"{CACHE_DIR}/animations/clouds.json",
            6: f"{CACHE_DIR}/animations/partial_clouds.json",
            7: f"{CACHE_DIR}/animations/partial_clouds.json",
            8: f"{CACHE_DIR}/animations/rain.json",
            9: f"{CACHE_DIR}/animations/rain.json",
            10: f"{CACHE_DIR}/animations/rain.json",
            11: f"{CACHE_DIR}/animations/rain.json",
            12: f"{CACHE_DIR}/animations/storm.json",
            13: f"{CACHE_DIR}/animations/storm.json",
            14: f"{CACHE_DIR}/animations/snow.json",
            15: f"{CACHE_DIR}/animations/snow.json",
            16: f"{CACHE_DIR}/animations/fog.json",
            17: f"{CACHE_DIR}/animations/fog.json",
        }
        return animations.get(weather_code, f"{CACHE_DIR}/animations/default_weather.json")


class SingleDayWeatherPage(Page):
    def __init__(self, session_data: Optional[Dict[str, Any]] = None):
        super().__init__(name="single-day-weather-page", session_data=session_data)

        weather_widget = SingleDayWeatherWidget(session_data=session_data)

        background_container = Div(
            [weather_widget._widget],
            _id="weather-bg",
            _class=[
                "h-full",
                "w-full",
                "flex",
                "flex-col",
                "items-center",
                "justify-center",
            ],
            style={
                "background": "linear-gradient(to right, rgb(59, 130, 246), rgb(255, 182, 193))",
                "transition": "background 0.5s ease",
            },
        )

        self._page: Div = Div(
            [background_container],
            _id="single-day-weather-page",
            _class="flex flex-col fade-in",
            style={"width": "100vw", "height": "100vh"},
        )
