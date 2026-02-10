from __future__ import annotations
from typing import Any, Optional, Dict, List
from pyhtmx.html_tag import HTMLTag
from pyhtmx import Div, Span  # type: ignore
from pyhtmx_gui.kit import Widget, SessionItem, Page


CACHE_DIR = "/cache/ovos-skill-weather.openvoiceos/py-htmx"


HIGH_TEMP_ICON = HTMLTag(
    tag="svg",
    version="1.1",
    _id="high-temp-icon",
    viewBox="0 0 640 640",
    # width="64",
    # height="64",
    _class="fill-blue-800 w-[3.5vw] h-[3.5vw]",
    inner_content=[
        HTMLTag(
            tag="path",
            d=(
                "M128.5 160C128.5 107 171.5 64 224.5 64C277.5 64 320.5 107 320.5 "
                "160L320.5 324.7C350 351.1 368.5 389.4 368.5 432C368.5 511.5 304 "
                "576 224.5 576C145 576 80.5 511.5 80.5 432C80.5 389.4 99 351 128.5 "
                "324.7L128.5 160zM224.5 496C259.8 496 288.5 467.3 288.5 432C288.5 "
                "405.1 272 382.1 248.5 372.7L248.5 160C248.5 146.7 237.8 136 224.5 "
                "136C211.2 136 200.5 146.7 200.5 160L200.5 372.7C177 382.2 160.5 "
                "405.2 160.5 432C160.5 467.3 189.2 496 224.5 496zM503.1 73.4L567.1 "
                "137.4C579.6 149.9 579.6 170.2 567.1 182.7C554.6 195.2 534.3 195.2 "
                "521.8 182.7L512.4 173.3L512.4 352C512.4 369.7 498.1 384 480.4 384C462.7 "
                "384 448.4 369.7 448.4 352L448.4 173.3L439 182.7C426.5 195.2 406.2 195.2 "
                "393.7 182.7C381.2 170.2 381.2 149.9 393.7 137.4L457.7 73.4C463.7 67.4 "
                "471.8 64 480.3 64C488.8 64 496.9 67.4 502.9 73.4z"
            )
        )
    ]
)

LOW_TEMP_ICON = HTMLTag(
    tag="svg",
    version="1.1",
    _id="low-temp-icon",
    viewBox="0 0 640 640",
    # width="64",
    # height="64",
    _class="fill-blue-800 w-[3.5vw] h-[3.5vw]",
    inner_content=[
        HTMLTag(
            tag="path",
            d=(
                "M128.5 160C128.5 107 171.5 64 224.5 64C277.5 64 320.5 107 320.5 "
                "160L320.5 324.7C350 351.1 368.5 389.4 368.5 432C368.5 511.5 304 576 "
                "224.5 576C145 576 80.5 511.5 80.5 432C80.5 389.4 99 351 128.5 324.7L128.5 "
                "160zM224.5 496C259.8 496 288.5 467.3 288.5 432C288.5 405.1 272 382.1 "
                "248.5 372.7L248.5 344C248.5 330.7 237.8 320 224.5 320C211.2 320 200.5 "
                "330.7 200.5 344L200.5 372.7C177 382.2 160.5 405.2 160.5 432C160.5 467.3 "
                "189.2 496 224.5 496zM503.1 374.6C497.1 380.6 489 384 480.5 384C472 384 "
                "463.9 380.6 457.9 374.6L393.9 310.6C381.4 298.1 381.4 277.8 393.9 "
                "265.3C406.4 252.8 426.7 252.8 439.2 265.3L448.6 274.7L448.6 96C448.6 78.3 "
                "462.9 64 480.6 64C498.3 64 512.6 78.3 512.6 96L512.6 274.7L522 265.3C534.5 "
                "252.8 554.8 252.8 567.3 265.3C579.8 277.8 579.8 298.1 567.3 310.6L503.3 "
                "374.6z"
            ),
        )
    ]
)


class DailyForecastWidget(Widget):
    _parameters = ("forecast",)

    def __init__(self, session_data: Optional[Dict[str, Any]] = None):
        super().__init__(name="daily-forecast-widget", session_data=session_data)

        session_data = session_data or {}
        forecast: List[Dict[str, Any]] = session_data.get("forecast", {}).get("all", [])

        forecast_items: List[Div] = []
        for day in forecast:
            date = day.get("date", "Unknown")
            high_temp = day.get("highTemperature", " --.- ")
            low_temp = day.get("lowTemperature", " --.- ")
            condition_code = day.get("weatherCondition", 0)

            animation_src = self.get_weather_animation(condition_code)

            subitem_classes = [
                "inline",
                # "bg-blue-100",
                "text-blue-800",
                "text-[1.50vw]",
                "font-medium",
                "me-2",
                "px-[1.0vw]",
                "py-[1.0vh]",
                # "rounded-full",
                # "dark:bg-gray-700",
                # "dark:text-blue-400",
                # "border",
                # "border-blue-400",
                "flex",
                "flex-row",
                "justify-start",
                "gap-[0.5vw]",
                "items-center",
                "min-w-[10vw]",
            ]
            day_item = Div(
                [
                    Div(inner_content=date, _class="text-[2vw] font-bold mb-[0.5vw] text-gray-800"),
                    HTMLTag(
                        tag="lottie-player",
                        src=animation_src,
                        background="transparent",
                        loop="",
                        autoplay="",
                        style={"width": "8vw", "height": "8vw"},
                    ),
                    Div(
                        inner_content=[
                            Div(
                                [HIGH_TEMP_ICON, Span(inner_content=high_temp, _class="ml-[0.5vw]")],
                                _class=subitem_classes,
                            ),
                            Div(
                                [LOW_TEMP_ICON, Span(inner_content=low_temp, _class="ml-[0.5vw]")],
                                _class=subitem_classes,
                            ),
                        ],
                        _class="text-[1.5vw] font-semibold mt-[0.5vw] text-gray-800",
                    ),
                ],
                _class=(
                    "min-w-[15vw] p-[1vw] border border-gray-300 rounded-lg "
                    "flex flex-col items-center bg-white shadow-md"
                ),
            )
            forecast_items.append(day_item)

        self._forecast_list = Div(
            forecast_items,
            _id="daily-forecast-list",
            _class="flex flex-row w-full overflow-x-auto gap-[1vw] pb-[1vw] justify-center",
            style={"scrollbar-width": "none"},
        )

        self.add_interaction(
            "forecast",
            SessionItem(
                parameter="forecast",
                attribute="inner_content",
                component=self._forecast_list,
            ),
        )

        self._title = Div(
            inner_content="Daily Forecast",
            _id="daily-forecast-title",
            _class="text-[3vw] font-bold mb-[1vw] text-gray-800",
        )

        self._widget = Div(
            [
                self._title,
                self._forecast_list,
            ],
            _id="daily-forecast-widget",
            _class=[
                "p-[2vw]",
                "flex",
                "flex-col",
                "justify-center",
                "items-center",
                "rounded-2xl",
                "shadow-xl",
                "bg-blue-100",
            ],
            style={
                "width": "80vw",
                "height": "80vh",
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


class DailyForecastPage(Page):
    def __init__(self, session_data: Optional[Dict[str, Any]] = None):
        super().__init__(name="daily-forecast-page", session_data=session_data)

        daily_forecast_widget = DailyForecastWidget(session_data=session_data)
        self.add_component(daily_forecast_widget)

        background_container = Div(
            [daily_forecast_widget._widget],
            _id="daily-forecast-bg",
            _class=[
                "flex",
                "flex-col",
                "items-center",
                "justify-center",
            ],
            style={
                "width": "100vw",
                "height": "100vh",
                "background": "linear-gradient(to right, rgb(59, 130, 246), rgb(255, 182, 193))",
                "transition": "background 0.5s ease",
            },
        )

        self._page = Div(
            [background_container],
            _id="daily-forecast-page",
            _class="flex flex-col fade-in",
            style={"width": "100vw", "height": "100vh"},
        )
