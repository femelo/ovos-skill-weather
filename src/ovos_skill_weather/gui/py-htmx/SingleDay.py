from __future__ import annotations
from typing import Any, Optional, Dict
from pyhtmx import Div, Span  # type: ignore
from pyhtmx_gui.kit import Widget, SessionItem, Page
from pyhtmx.html_tag import HTMLTag


CACHE_DIR = "/cache/ovos-skill-weather.openvoiceos/py-htmx"


FONT_AWESOME_LICENSE = "<!--!{title} {license} {copyright}-->".format(
    title="Font Awesome Free v7.1.0 by @fontawesome - https://fontawesome.com",
    license="License - https://fontawesome.com/license/free",
    copyright="Copyright 2025 Fonticons, Inc.",
)

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

HUMIDITY_ICON = HTMLTag(
    tag="svg",
    version="1.1",
    _id="humidity-icon",
    viewBox="0 0 640 640",
    # width="64",
    # height="64",
    _class="fill-blue-800 w-[3.5vw] h-[3.5vw]",
    inner_content=[
        HTMLTag(
            tag="path",
            d=(
                "M320 576C214 576 128 490 128 384C128 292.8 258.2 109.9 294.6 60.5C300.5 "
                "52.5 309.8 48 319.8 48L320.2 48C330.2 48 339.5 52.5 345.4 60.5C381.8 109.9 "
                "512 292.8 512 384C512 490 426 576 320 576zM240 376C240 362.7 229.3 352 216 "
                "352C202.7 352 192 362.7 192 376C192 451.1 252.9 512 328 512C341.3 512 352 "
                "501.3 352 488C352 474.7 341.3 464 328 464C279.4 464 240 424.6 240 376z"
            ),
        )
    ]
)

WIND_ICON = HTMLTag(
    tag="svg",
    version="1.1",
    _id="wind-icon",
    viewBox="0 0 640 640",
    # width="64",
    # height="64",
    _class="fill-blue-800 w-[3.5vw] h-[3.5vw]",
    inner_content=[
        HTMLTag(
            tag="path",
            d=(
                "M352 96C352 113.7 366.3 128 384 128L424 128C437.3 128 448 138.7 448 152C448 "
                "165.3 437.3 176 424 176L96 176C78.3 176 64 190.3 64 208C64 225.7 78.3 240 96 "
                "240L424 240C472.6 240 512 200.6 512 152C512 103.4 472.6 64 424 64L384 64C366.3 "
                "64 352 78.3 352 96zM416 448C416 465.7 430.3 480 448 480L480 480C533 480 576 437 "
                "576 384C576 331 533 288 480 288L96 288C78.3 288 64 302.3 64 320C64 337.7 78.3 "
                "352 96 352L480 352C497.7 352 512 366.3 512 384C512 401.7 497.7 416 480 416L448 "
                "416C430.3 416 416 430.3 416 448zM192 576L232 576C280.6 576 320 536.6 320 488C320 "
                "439.4 280.6 400 232 400L96 400C78.3 400 64 414.3 64 432C64 449.7 78.3 464 96 "
                "464L232 464C245.3 464 256 474.7 256 488C256 501.3 245.3 512 232 512L192 "
                "512C174.3 512 160 526.3 160 544C160 561.7 174.3 576 192 576z"
            ),
        )
    ]
)

RAIN_ICON = HTMLTag(
    tag="svg",
    version="1.1",
    _id="rain-icon",
    viewBox="0 0 640 640",
    # width="64",
    # height="64",
    _class="fill-blue-800 w-[3.5vw] h-[3.5vw]",
    inner_content=[
        # FONT_AWESOME_LICENSE,
        HTMLTag(
            tag="path",
            d=(
                "M160 384C107 384 64 341 64 288C64 245.5 91.6 209.4 129.9 196.8C128.6 190.1 "
                "128 183.1 128 176C128 114.1 178.1 64 240 64C283.1 64 320.5 88.3 339.2 "
                "124C353.9 106.9 375.7 96 400 96C444.2 96 480 131.8 480 176C480 181.5 479.4 "
                "186.8 478.4 192C478.9 192 479.5 192 480 192C533 192 576 235 576 288C576 341 "
                "533 384 480 384L160 384zM161.6 452.2C162.7 449.7 165.2 448 168 448C170.8 448 "
                "173.3 449.6 174.4 452.2L204.6 520.4C206.8 525.5 208 530.9 208 536.4C208 558.3 "
                "189.9 576 168 576C146.1 576 128 558.3 128 536.4C128 530.9 129.2 525.4 131.4 "
                "520.4L161.6 452.2zM313.6 452.2C314.7 449.7 317.2 448 320 448C322.8 448 325.3 "
                "449.6 326.4 452.2L356.6 520.4C358.8 525.5 360 530.9 360 536.4C360 558.3 341.9 "
                "576 320 576C298.1 576 280 558.3 280 536.4C280 530.9 281.2 525.4 283.4 "
                "520.4L313.6 452.2zM435.4 520.4L465.6 452.2C466.7 449.7 469.2 448 472 "
                "448C474.8 448 477.3 449.6 478.4 452.2L508.6 520.4C510.8 525.5 512 530.9 "
                "512 536.4C512 558.3 493.9 576 472 576C450.1 576 432 558.3 432 536.4C432 "
                "530.9 433.2 525.4 435.4 520.4z"
            ),
        )
    ]
)


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

        item_classes = [
            "inline",
            "bg-blue-100",
            "text-blue-800",
            "text-[1.80vw]",
            "font-medium",
            "me-2",
            "px-[1.0vw]",
            "py-[1.0vh]",
            "rounded-full",
            "dark:bg-gray-700",
            "dark:text-blue-400",
            # "border",
            # "border-blue-400",
            "flex",
            "flex-row",
            "justify-start",
            "gap-[0.5vw]",
            "items-center",
            "min-w-[12vw]",
        ]
        details_items: Dict[str, Div] = {
            "hightTemperature": Div(
                [
                    HIGH_TEMP_ICON,
                    Span(
                        session_data.get('highTemperature', ' --.- '),
                        _id="high-temp",
                    )
                ],
                _class=item_classes,
            ),
            "lowTemperature": Div(
                [
                    LOW_TEMP_ICON,
                    Span(
                        session_data.get('lowTemperature', ' --.- '),
                        _id="low-temp",
                    )
                ],
                _class=item_classes,
            ),
            "humidity": Div(
                [
                    HUMIDITY_ICON,
                    Span(
                        session_data.get('humidity', '--.- '),
                        _id="humidity",
                    )
                ],
                _class=item_classes,
            ),
            "windSpeed": Div(
                [
                    WIND_ICON,
                    Span(
                        session_data.get('windSpeed', '---.- '),
                        _id="wind",
                    )
                ],
                _class=item_classes,
            ),
            "chanceOfPrecipitation": Div(
                [
                    RAIN_ICON,
                    Span(
                        session_data.get('chanceOfPrecipitation', '--.- '),
                        _id="precipitation",
                    )
                ],
                _class=item_classes,
            ),
        }
        self._details: Div = Div(
            inner_content=[item for item in details_items.values()],
            _id="weather-details",
            _class="flex flex-row justify-evenly items-center",
        )
        for key, item in details_items.items():
            self.add_interaction(
                key,
                SessionItem(
                    parameter=item.children[1].attributes.get("id", "none"),
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
                "gap-[2vw]",
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
