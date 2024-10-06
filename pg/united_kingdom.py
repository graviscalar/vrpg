from enum import Enum


class UKPlateType(Enum):
    PRIVATE = 'Private'
    MOTORCYCLE = 'Motorcycle'
    TRADE = 'Trade'
    TRAILER = 'Trailer'
    DIPLOMATIC = 'Diplomatic'
    ARMED_FORCES = 'Armed forces'
    ARMED_FORCES_TRAILER = 'Armed forces trailer'


def uk_exception(name):
    a = {UKPlateType.PRIVATE.value, UKPlateType.DIPLOMATIC.value, UKPlateType.MOTORCYCLE.value}
    return name in a


class UKPlateColor(Enum):
    SERIAL_NUMBER_TEXT = (180, 180, 180)
    TRANSPARENT_BG = (255, 255, 255, 0)
    ARMED_FORCES_BG = (0, 0, 0)
    ARMED_FORCES_TEXT = (255, 255, 255)
    ARMED_FORCES_TRAILER_BG = (0, 0, 0)
    ARMED_FORCES_TRAILER_TEXT = (255, 255, 255)
    TRADE_BG = (255, 255, 255)
    TRADE_TEXT = (255, 0, 0)
    PRIVATE_FRONT_BG = (255, 255, 255)
    PRIVATE_FRONT_TEXT = (0, 0, 0)
    PRIVATE_REAR_BG = (255, 204, 0)
    PRIVATE_REAR_TEXT = (0, 0, 0)
    DIPLOMATIC_FRONT_BG = (255, 255, 255)
    DIPLOMATIC_FRONT_TEXT = (0, 0, 0)
    DIPLOMATIC_REAR_BG = (255, 204, 0)
    DIPLOMATIC_REAR_TEXT = (0, 0, 0)
    MOTORCYCLE_FRONT_BG = (255, 255, 255)
    MOTORCYCLE_FRONT_TEXT = (0, 0, 0)
    MOTORCYCLE_REAR_BG = (255, 204, 0)
    MOTORCYCLE_REAR_TEXT = (0, 0, 0)
    TRAILER_BG = (255, 255, 255)
    TRAILER_TEXT = (0, 0, 0)


def plate_uk():
    return {
        "country": "UK",
        "rfy": "2001",  # registration format year
        "font": "CharlesWright-Bold.otf",
        "plates": [
            {
                "name": UKPlateType.ARMED_FORCES.value,
                "width": 520,
                "height": 111,
                "color_bg": UKPlateColor.ARMED_FORCES_BG.value,
                "color_text": UKPlateColor.ARMED_FORCES_TEXT.value,
                "object": [
                    {
                        "type": "rectangle",
                        "fill_color": UKPlateColor.ARMED_FORCES_BG.value,
                        "border_color": None,
                        "border_width": 1,
                        "quantity": 1,
                        "start_x": 0,
                        "start_y": 0,
                        "width": 520,
                        "height": 111,
                        "coord": 0
                    },
                    {
                        "type": "format",
                        "random": 1,
                        "color_bg": UKPlateColor.ARMED_FORCES_BG.value,
                        "color_text": UKPlateColor.ARMED_FORCES_TEXT.value,
                        "start_x": 11,
                        "start_y": 16,
                        "width": 460,
                        "height": 79,
                        "coord": 0,
                        "obj": [
                            [{'type': 2, 'name': 'AB12AB'},
                             {'type': 0, 'r': 1, 'rnd_obj': ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H',
                                                             'J', 'K', 'L', 'M', 'N', 'O', 'P', 'R',
                                                             'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']},
                             {'type': 0, 'r': 1, 'rnd_obj': ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H',
                                                             'J', 'K', 'L', 'M', 'N', 'O', 'P', 'R',
                                                             'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']},
                             {'type': 1, 'r': 1, 'min': 0, 'max': 99, 'zfil': 2},
                             {'type': 0, 'r': 1, 'rnd_obj': ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H',
                                                             'J', 'K', 'L', 'M', 'N', 'O', 'P', 'R',
                                                             'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']},
                             {'type': 0, 'r': 1, 'rnd_obj': ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H',
                                                             'J', 'K', 'L', 'M', 'N', 'O', 'P', 'R',
                                                             'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']},
                             {'type': 3, 'obj': [{'ox': 52, 'oy': 0, 'w': 50, 'h': 79},
                                                 {'ox': 11, 'oy': 0, 'w': 50, 'h': 79},
                                                 {'ox': 30, 'oy': 0, 'w': 50, 'h': 79},
                                                 {'ox': 11, 'oy': 0, 'w': 50, 'h': 79},
                                                 {'ox': 30, 'oy': 0, 'w': 50, 'h': 79},
                                                 {'ox': 11, 'oy': 0, 'w': 50, 'h': 79}]}

                             ],
                            [
                                {'type': 0, 'r': 0, 'text_obj': 'DOT'},
                                {'type': 1, 'r': 1, 'min': 0, 'max': 99999, 'zfil': 5},
                                {'type': 3, 'obj': [{'ox': 0, 'oy': 0, 'w': 50, 'h': 79},
                                                    {'ox': 11, 'oy': 0, 'w': 50, 'h': 79},
                                                    {'ox': 11, 'oy': 0, 'w': 50, 'h': 79},
                                                    {'ox': 30, 'oy': 0, 'w': 50, 'h': 79},
                                                    {'ox': 11, 'oy': 0, 'w': 50, 'h': 79},
                                                    {'ox': 11, 'oy': 0, 'w': 50, 'h': 79},
                                                    {'ox': 11, 'oy': 0, 'w': 50, 'h': 79},
                                                    {'ox': 11, 'oy': 0, 'w': 50, 'h': 79}]}
                            ],
                            [
                                {'type': 0, 'r': 0, 'text_obj': 'RC'},
                                {'type': 1, 'r': 1, 'min': 0, 'max': 99999, 'zfil': 5},
                                {'type': 3, 'obj': [{'ox': 31, 'oy': 0, 'w': 50, 'h': 79},
                                                    {'ox': 11, 'oy': 0, 'w': 50, 'h': 79},
                                                    {'ox': 30, 'oy': 0, 'w': 50, 'h': 79},
                                                    {'ox': 11, 'oy': 0, 'w': 50, 'h': 79},
                                                    {'ox': 11, 'oy': 0, 'w': 50, 'h': 79},
                                                    {'ox': 11, 'oy': 0, 'w': 50, 'h': 79},
                                                    {'ox': 11, 'oy': 0, 'w': 50, 'h': 79}]}
                            ],
                            [
                                {'type': 0, 'r': 0, 'text_obj': 'UKAX'},
                                {'type': 1, 'r': 1, 'min': 0, 'max': 9999, 'zfil': 4},
                                {'type': 3, 'obj': [{'ox': 0, 'oy': 0, 'w': 50, 'h': 79},
                                                    {'ox': 11, 'oy': 0, 'w': 50, 'h': 79},
                                                    {'ox': 11, 'oy': 0, 'w': 50, 'h': 79},
                                                    {'ox': 11, 'oy': 0, 'w': 50, 'h': 79},
                                                    {'ox': 30, 'oy': 0, 'w': 50, 'h': 79},
                                                    {'ox': 11, 'oy': 0, 'w': 50, 'h': 79},
                                                    {'ox': 11, 'oy': 0, 'w': 50, 'h': 79},
                                                    {'ox': 11, 'oy': 0, 'w': 50, 'h': 79}]}
                            ],
                            [
                                {'type': 0, 'r': 0, 'text_obj': 'USAF'},
                                {'type': 1, 'r': 1, 'min': 0, 'max': 9999, 'zfil': 4},
                                {'type': 3, 'obj': [{'ox': 0, 'oy': 0, 'w': 50, 'h': 79},
                                                    {'ox': 11, 'oy': 0, 'w': 50, 'h': 79},
                                                    {'ox': 11, 'oy': 0, 'w': 50, 'h': 79},
                                                    {'ox': 11, 'oy': 0, 'w': 50, 'h': 79},
                                                    {'ox': 30, 'oy': 0, 'w': 50, 'h': 79},
                                                    {'ox': 11, 'oy': 0, 'w': 50, 'h': 79},
                                                    {'ox': 11, 'oy': 0, 'w': 50, 'h': 79},
                                                    {'ox': 11, 'oy': 0, 'w': 50, 'h': 79}]}
                            ],
                            [
                                {'type': 0, 'r': 0, 'text_obj': 'USN'},
                                {'type': 1, 'r': 1, 'min': 0, 'max': 99999, 'zfil': 5},
                                {'type': 3, 'obj': [{'ox': 0, 'oy': 0, 'w': 50, 'h': 79},
                                                    {'ox': 11, 'oy': 0, 'w': 50, 'h': 79},
                                                    {'ox': 11, 'oy': 0, 'w': 50, 'h': 79},
                                                    {'ox': 30, 'oy': 0, 'w': 50, 'h': 79},
                                                    {'ox': 11, 'oy': 0, 'w': 50, 'h': 79},
                                                    {'ox': 11, 'oy': 0, 'w': 50, 'h': 79},
                                                    {'ox': 11, 'oy': 0, 'w': 50, 'h': 79},
                                                    {'ox': 11, 'oy': 0, 'w': 50, 'h': 79}]}
                            ],
                            [
                                {'type': 0, 'r': 0, 'text_obj': 'AFEX'},
                                {'type': 1, 'r': 1, 'min': 0, 'max': 9999, 'zfil': 4},
                                {'type': 3, 'obj': [{'ox': 0, 'oy': 0, 'w': 50, 'h': 79},
                                                    {'ox': 11, 'oy': 0, 'w': 50, 'h': 79},
                                                    {'ox': 11, 'oy': 0, 'w': 50, 'h': 79},
                                                    {'ox': 11, 'oy': 0, 'w': 50, 'h': 79},
                                                    {'ox': 30, 'oy': 0, 'w': 50, 'h': 79},
                                                    {'ox': 11, 'oy': 0, 'w': 50, 'h': 79},
                                                    {'ox': 11, 'oy': 0, 'w': 50, 'h': 79},
                                                    {'ox': 11, 'oy': 0, 'w': 50, 'h': 79}]}
                            ],
                            [
                                {'type': 0, 'r': 0, 'text_obj': 'UKER'},
                                {'type': 1, 'r': 1, 'min': 0, 'max': 9999, 'zfil': 4},
                                {'type': 3, 'obj': [{'ox': 0, 'oy': 0, 'w': 50, 'h': 79},
                                                    {'ox': 11, 'oy': 0, 'w': 50, 'h': 79},
                                                    {'ox': 11, 'oy': 0, 'w': 50, 'h': 79},
                                                    {'ox': 11, 'oy': 0, 'w': 50, 'h': 79},
                                                    {'ox': 30, 'oy': 0, 'w': 50, 'h': 79},
                                                    {'ox': 11, 'oy': 0, 'w': 50, 'h': 79},
                                                    {'ox': 11, 'oy': 0, 'w': 50, 'h': 79},
                                                    {'ox': 11, 'oy': 0, 'w': 50, 'h': 79}]}
                            ]
                        ]

                    },
                ]
            },
            {
                "name": UKPlateType.ARMED_FORCES_TRAILER.value,
                "width": 285,
                "height": 203,
                "color_bg": UKPlateColor.ARMED_FORCES_TRAILER_BG.value,
                "color_text": UKPlateColor.ARMED_FORCES_TRAILER_TEXT.value,
                "object": [
                    {
                        "type": "rectangle",
                        "fill_color": UKPlateColor.ARMED_FORCES_TRAILER_BG.value,
                        "border_color": None,
                        "border_width": 1,
                        "quantity": 1,
                        "start_x": 0,
                        "start_y": 0,
                        "width": 285,
                        "height": 203,
                        "coord": 0
                    },
                    {
                        "type": "format",
                        "random": 1,
                        "color_bg": UKPlateColor.ARMED_FORCES_TRAILER_BG.value,
                        "color_text": UKPlateColor.ARMED_FORCES_TRAILER_TEXT.value,
                        "start_x": 0,
                        "start_y": 16,
                        "width": 460,
                        "height": 79,
                        "coord": 0,
                        "obj": [
                            [{'type': 2, 'name': 'AB12AB'},
                             {'type': 0, 'r': 1, 'rnd_obj': ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H',
                                                             'J', 'K', 'L', 'M', 'N', 'O', 'P', 'R',
                                                             'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']},
                             {'type': 0, 'r': 1, 'rnd_obj': ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H',
                                                             'J', 'K', 'L', 'M', 'N', 'O', 'P', 'R',
                                                             'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']},
                             {'type': 1, 'r': 1, 'min': 0, 'max': 99, 'zfil': 2},
                             {'type': 0, 'r': 1, 'rnd_obj': ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H',
                                                             'J', 'K', 'L', 'M', 'N', 'O', 'P', 'R',
                                                             'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']},
                             {'type': 0, 'r': 1, 'rnd_obj': ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H',
                                                             'J', 'K', 'L', 'M', 'N', 'O', 'P', 'R',
                                                             'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']},
                             {'type': 3, 'obj': [{'ox': 87, 'oy': 0, 'w': 50, 'h': 79},
                                                 {'ox': 11, 'oy': 0, 'w': 50, 'h': 79},
                                                 {'ox': -182, 'oy': 92, 'w': 50, 'h': 79},
                                                 {'ox': 11, 'oy': 0, 'w': 50, 'h': 79},
                                                 {'ox': 30, 'oy': 0, 'w': 50, 'h': 79},
                                                 {'ox': 11, 'oy': 0, 'w': 50, 'h': 79}]}

                             ],
                            [
                                {'type': 0, 'r': 0, 'text_obj': 'DOT'},
                                {'type': 1, 'r': 1, 'min': 0, 'max': 99999, 'zfil': 5},
                                {'type': 3, 'obj': [{'ox': 56, 'oy': 0, 'w': 50, 'h': 79},
                                                    {'ox': 11, 'oy': 0, 'w': 50, 'h': 79},
                                                    {'ox': 11, 'oy': 0, 'w': 50, 'h': 79},
                                                    {'ox': -223, 'oy': 92, 'w': 46, 'h': 79},
                                                    {'ox': 11, 'oy': 0, 'w': 46, 'h': 79},
                                                    {'ox': 11, 'oy': 0, 'w': 46, 'h': 79},
                                                    {'ox': 11, 'oy': 0, 'w': 46, 'h': 79},
                                                    {'ox': 11, 'oy': 0, 'w': 46, 'h': 79}]}
                            ],
                            [
                                {'type': 0, 'r': 0, 'text_obj': 'RC'},
                                {'type': 1, 'r': 1, 'min': 0, 'max': 99999, 'zfil': 5},
                                {'type': 3, 'obj': [{'ox': 87, 'oy': 0, 'w': 50, 'h': 79},
                                                    {'ox': 11, 'oy': 0, 'w': 50, 'h': 79},
                                                    {'ox': -193, 'oy': 92, 'w': 46, 'h': 79},
                                                    {'ox': 11, 'oy': 0, 'w': 46, 'h': 79},
                                                    {'ox': 11, 'oy': 0, 'w': 46, 'h': 79},
                                                    {'ox': 11, 'oy': 0, 'w': 46, 'h': 79},
                                                    {'ox': 11, 'oy': 0, 'w': 46, 'h': 79}]}
                            ],
                            [
                                {'type': 0, 'r': 0, 'text_obj': 'UKAX'},
                                {'type': 1, 'r': 1, 'min': 0, 'max': 9999, 'zfil': 4},
                                {'type': 3, 'obj': [{'ox': 26, 'oy': 0, 'w': 50, 'h': 79},
                                                    {'ox': 11, 'oy': 0, 'w': 50, 'h': 79},
                                                    {'ox': 11, 'oy': 0, 'w': 50, 'h': 79},
                                                    {'ox': 11, 'oy': 0, 'w': 50, 'h': 79},
                                                    {'ox': -225, 'oy': 92, 'w': 46, 'h': 79},
                                                    {'ox': 11, 'oy': 0, 'w': 46, 'h': 79},
                                                    {'ox': 11, 'oy': 0, 'w': 46, 'h': 79},
                                                    {'ox': 11, 'oy': 0, 'w': 46, 'h': 79}]}
                            ],
                            [
                                {'type': 0, 'r': 0, 'text_obj': 'USAF'},
                                {'type': 1, 'r': 1, 'min': 0, 'max': 9999, 'zfil': 4},
                                {'type': 3, 'obj': [{'ox': 26, 'oy': 0, 'w': 50, 'h': 79},
                                                    {'ox': 11, 'oy': 0, 'w': 50, 'h': 79},
                                                    {'ox': 11, 'oy': 0, 'w': 50, 'h': 79},
                                                    {'ox': 11, 'oy': 0, 'w': 50, 'h': 79},
                                                    {'ox': -225, 'oy': 92, 'w': 46, 'h': 79},
                                                    {'ox': 11, 'oy': 0, 'w': 46, 'h': 79},
                                                    {'ox': 11, 'oy': 0, 'w': 46, 'h': 79},
                                                    {'ox': 11, 'oy': 0, 'w': 46, 'h': 79}]}
                            ],
                            [
                                {'type': 0, 'r': 0, 'text_obj': 'USN'},
                                {'type': 1, 'r': 1, 'min': 0, 'max': 99999, 'zfil': 5},
                                {'type': 3, 'obj': [{'ox': 56, 'oy': 0, 'w': 50, 'h': 79},
                                                    {'ox': 11, 'oy': 0, 'w': 50, 'h': 79},
                                                    {'ox': 11, 'oy': 0, 'w': 50, 'h': 79},
                                                    {'ox': -223, 'oy': 92, 'w': 46, 'h': 79},
                                                    {'ox': 11, 'oy': 0, 'w': 46, 'h': 79},
                                                    {'ox': 11, 'oy': 0, 'w': 46, 'h': 79},
                                                    {'ox': 11, 'oy': 0, 'w': 46, 'h': 79},
                                                    {'ox': 11, 'oy': 0, 'w': 46, 'h': 79}]}
                            ],
                            [
                                {'type': 0, 'r': 0, 'text_obj': 'AFEX'},
                                {'type': 1, 'r': 1, 'min': 0, 'max': 9999, 'zfil': 4},
                                {'type': 3, 'obj': [{'ox': 26, 'oy': 0, 'w': 50, 'h': 79},
                                                    {'ox': 11, 'oy': 0, 'w': 50, 'h': 79},
                                                    {'ox': 11, 'oy': 0, 'w': 50, 'h': 79},
                                                    {'ox': 11, 'oy': 0, 'w': 50, 'h': 79},
                                                    {'ox': -225, 'oy': 92, 'w': 46, 'h': 79},
                                                    {'ox': 11, 'oy': 0, 'w': 46, 'h': 79},
                                                    {'ox': 11, 'oy': 0, 'w': 46, 'h': 79},
                                                    {'ox': 11, 'oy': 0, 'w': 46, 'h': 79}]}
                            ],
                            [
                                {'type': 0, 'r': 0, 'text_obj': 'UKER'},
                                {'type': 1, 'r': 1, 'min': 0, 'max': 9999, 'zfil': 4},
                                {'type': 3, 'obj': [{'ox': 26, 'oy': 0, 'w': 50, 'h': 79},
                                                    {'ox': 11, 'oy': 0, 'w': 50, 'h': 79},
                                                    {'ox': 11, 'oy': 0, 'w': 50, 'h': 79},
                                                    {'ox': 11, 'oy': 0, 'w': 50, 'h': 79},
                                                    {'ox': -225, 'oy': 92, 'w': 46, 'h': 79},
                                                    {'ox': 11, 'oy': 0, 'w': 46, 'h': 79},
                                                    {'ox': 11, 'oy': 0, 'w': 46, 'h': 79},
                                                    {'ox': 11, 'oy': 0, 'w': 46, 'h': 79}]}
                            ]
                        ]

                    },
                ]
            },
            {
                "name": UKPlateType.TRADE.value,
                "width": 460,
                "height": 111,
                "color_bg": UKPlateColor.TRADE_BG.value,
                "color_text": UKPlateColor.TRADE_TEXT.value,
                "object": [
                    {
                        "type": "rectangle",
                        "fill_color": UKPlateColor.TRADE_BG.value,
                        "border_color": None,
                        "border_width": 1,
                        "quantity": 1,
                        "start_x": 0,
                        "start_y": 0,
                        "width": 460,
                        "height": 111,
                        "coord": 0
                    },
                    {
                        "type": "image",
                        "image": "img/UK/dvla.png",
                        "random": 0,
                        "letters": None,
                        "quantity": 1,
                        "start_x": 354,
                        "start_y": 32,
                        "width": 78,
                        "height": 50,
                        "coord": 0
                    },
                    {
                        "type": "image",
                        "image": "img/UK/Royal-Cypher-CR-red.png",
                        "random": 0,
                        "letters": None,
                        "quantity": 1,
                        "start_x": 428,
                        "start_y": 4,
                        "width": 26,
                        "height": 26,
                        "coord": 0
                    },
                    {
                        "type": "format",
                        "random": 1,
                        "color_bg": UKPlateColor.TRANSPARENT_BG.value,
                        "color_text": UKPlateColor.TRADE_TEXT.value,
                        "start_x": 26,
                        "start_y": 16,
                        "width": 308,
                        "height": 79,
                        "coord": 0,
                        "obj": [
                            [
                                {'type': 2, 'name': '12345'},
                                {'type': 3, 'obj': [{'ox': 0, 'oy': 0, 'w': 50, 'h': 79},
                                                    {'ox': 11, 'oy': 0, 'w': 50, 'h': 79},
                                                    {'ox': 11, 'oy': 0, 'w': 50, 'h': 79},
                                                    {'ox': 11, 'oy': 0, 'w': 50, 'h': 79},
                                                    {'ox': 11, 'oy': 0, 'w': 50, 'h': 79}]},
                                {'type': 1, 'r': 1, 'min': 0, 'max': 99999, 'zfil': 5}
                            ],
                            [
                                {'type': 2, 'name': 'A1234'},
                                {'type': 3, 'obj': [{'ox': 0, 'oy': 0, 'w': 50, 'h': 79},
                                                    {'ox': 11, 'oy': 0, 'w': 50, 'h': 79},
                                                    {'ox': 11, 'oy': 0, 'w': 50, 'h': 79},
                                                    {'ox': 11, 'oy': 0, 'w': 50, 'h': 79},
                                                    {'ox': 11, 'oy': 0, 'w': 50, 'h': 79}]},
                                {'type': 0, 'r': 1, 'rnd_obj': ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H',
                                                                'J', 'K', 'L', 'M', 'N', 'O', 'P', 'R',
                                                                'S', 'T', 'U', 'V', 'W', 'X', 'Y']},
                                {'type': 1, 'r': 1, 'min': 0, 'max': 9999, 'zfil': 4}
                            ]
                        ]

                    },
                ]
            },
            {
                "name": UKPlateType.DIPLOMATIC.value,
                "width": 520,
                "height": 111,
                "color_bg": UKPlateColor.DIPLOMATIC_FRONT_BG.value,
                "color_bg_rear": UKPlateColor.DIPLOMATIC_REAR_BG.value,
                "color_text": UKPlateColor.DIPLOMATIC_FRONT_TEXT.value,
                "color_text_rear": UKPlateColor.DIPLOMATIC_REAR_TEXT.value,
                "object": [
                    {
                        "type": "rectangle_uk",
                        "fill_color": UKPlateColor.DIPLOMATIC_FRONT_BG.value,
                        "fill_color_rear": UKPlateColor.DIPLOMATIC_REAR_BG.value,
                        "border_color": None,
                        "border_width": 1,
                        "quantity": 1,
                        "start_x": 0,
                        "start_y": 0,
                        "width": 520,
                        "height": 111,
                        "coord": 0
                    },
                    {
                        "type": "format_uk",
                        "random": 1,
                        "color_bg": UKPlateColor.TRANSPARENT_BG.value,
                        "color_bg_rear": UKPlateColor.TRANSPARENT_BG.value,
                        "color_text": UKPlateColor.DIPLOMATIC_FRONT_TEXT.value,
                        "color_text_rear": UKPlateColor.DIPLOMATIC_REAR_TEXT.value,
                        "start_x": 33,
                        "start_y": 16,
                        "width": 308,
                        "height": 79,
                        "coord": 0,
                        "obj": [
                            [
                                {'type': 2, 'name': '101D101'},
                                {'type': 3, 'obj': [{'ox': 0, 'oy': 0, 'w': 50, 'h': 79},
                                                    {'ox': 11, 'oy': 0, 'w': 50, 'h': 79},
                                                    {'ox': 11, 'oy': 0, 'w': 50, 'h': 79},
                                                    {'ox': 30, 'oy': 0, 'w': 50, 'h': 79},
                                                    {'ox': 30, 'oy': 0, 'w': 50, 'h': 79},
                                                    {'ox': 11, 'oy': 0, 'w': 50, 'h': 79},
                                                    {'ox': 11, 'oy': 0, 'w': 50, 'h': 79}]},
                                {'type': 1, 'r': 1, 'min': 101, 'max': 944, 'zfil': 3},
                                {'type': 0, 'r': 0, 'text_obj': 'D'},
                                {'type': 1, 'r': 1, 'min': 101, 'max': 999, 'zfil': 3}
                            ],
                            [
                                {'type': 2, 'name': '101X101'},
                                {'type': 3, 'obj': [{'ox': 0, 'oy': 0, 'w': 50, 'h': 79},
                                                    {'ox': 11, 'oy': 0, 'w': 50, 'h': 79},
                                                    {'ox': 11, 'oy': 0, 'w': 50, 'h': 79},
                                                    {'ox': 30, 'oy': 0, 'w': 50, 'h': 79},
                                                    {'ox': 30, 'oy': 0, 'w': 50, 'h': 79},
                                                    {'ox': 11, 'oy': 0, 'w': 50, 'h': 79},
                                                    {'ox': 11, 'oy': 0, 'w': 50, 'h': 79}]},
                                {'type': 1, 'r': 1, 'min': 101, 'max': 944, 'zfil': 3},
                                {'type': 0, 'r': 0, 'text_obj': 'X'},
                                {'type': 1, 'r': 1, 'min': 101, 'max': 999, 'zfil': 3}
                            ]
                        ]

                    },
                ]
            },
            {
                "name": UKPlateType.PRIVATE.value,
                "width": 520,
                "height": 111,
                "color_bg": UKPlateColor.PRIVATE_FRONT_BG.value,
                "color_bg_rear": UKPlateColor.PRIVATE_REAR_BG.value,
                "color_text": UKPlateColor.PRIVATE_FRONT_TEXT.value,
                "color_text_rear": UKPlateColor.PRIVATE_REAR_TEXT.value,
                "object": [
                    {
                        "type": "rectangle_uk",
                        "fill_color": UKPlateColor.PRIVATE_FRONT_BG.value,
                        "fill_color_rear": UKPlateColor.PRIVATE_REAR_BG.value,
                        "border_color": None,
                        "border_width": 1,
                        "quantity": 1,
                        "start_x": 0,
                        "start_y": 0,
                        "width": 520,
                        "height": 111,
                        "coord": 0
                    },
                    {
                        "type": "format_uk",
                        "random": 1,
                        "color_bg": UKPlateColor.TRANSPARENT_BG.value,
                        "color_bg_rear": UKPlateColor.TRANSPARENT_BG.value,
                        "color_text": UKPlateColor.PRIVATE_FRONT_TEXT.value,
                        "color_text_rear": UKPlateColor.PRIVATE_REAR_TEXT.value,
                        "start_x": 33,
                        "start_y": 16,
                        "width": 308,
                        "height": 79,
                        "coord": 0,
                        "obj": [
                            [
                                {'type': 2, 'name': 'AB12ABC'},
                                {'type': 3, 'obj': [{'ox': 0, 'oy': 0, 'w': 50, 'h': 79},
                                                    {'ox': 11, 'oy': 0, 'w': 50, 'h': 79},
                                                    {'ox': 11, 'oy': 0, 'w': 50, 'h': 79},
                                                    {'ox': 11, 'oy': 0, 'w': 50, 'h': 79},
                                                    {'ox': 30, 'oy': 0, 'w': 50, 'h': 79},
                                                    {'ox': 11, 'oy': 0, 'w': 50, 'h': 79},
                                                    {'ox': 11, 'oy': 0, 'w': 50, 'h': 79}]},
                                {'type': 4, 'obj': plate_uk_dvla()},
                                {'type': 1, 'r': 1, 'min': 0, 'max': 99, 'zfil': 2},
                                {'type': 0, 'r': 1, 'rnd_obj': ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H',
                                                                'J', 'K', 'L', 'M', 'N', 'O', 'P', 'R',
                                                                'S', 'T', 'U', 'V', 'W', 'X', 'Y', ]},
                                {'type': 0, 'r': 1, 'rnd_obj': ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H',
                                                                'J', 'K', 'L', 'M', 'N', 'O', 'P', 'R',
                                                                'S', 'T', 'U', 'V', 'W', 'X', 'Y', ]},
                                {'type': 0, 'r': 1, 'rnd_obj': ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H',
                                                                'J', 'K', 'L', 'M', 'N', 'O', 'P', 'R',
                                                                'S', 'T', 'U', 'V', 'W', 'X', 'Y', ]}

                            ]
                        ]

                    },
                ]
            },
            {
                "name": UKPlateType.MOTORCYCLE.value,
                "width": 231,
                "height": 164,
                "color_bg": UKPlateColor.MOTORCYCLE_FRONT_BG.value,
                "color_bg_rear": UKPlateColor.MOTORCYCLE_REAR_BG.value,
                "color_text": UKPlateColor.MOTORCYCLE_FRONT_TEXT.value,
                "color_text_rear": UKPlateColor.MOTORCYCLE_REAR_TEXT.value,
                "object": [
                    {
                        "type": "rectangle_uk",
                        "fill_color": UKPlateColor.MOTORCYCLE_FRONT_BG.value,
                        "fill_color_rear": UKPlateColor.MOTORCYCLE_REAR_BG.value,
                        "border_color": None,
                        "border_width": 1,
                        "quantity": 1,
                        "start_x": 0,
                        "start_y": 0,
                        "width": 231,
                        "height": 164,
                        "coord": 0
                    },
                    {
                        "type": "format_uk",
                        "random": 1,
                        "color_bg": UKPlateColor.TRANSPARENT_BG.value,
                        "color_bg_rear": UKPlateColor.TRANSPARENT_BG.value,
                        "color_text": UKPlateColor.MOTORCYCLE_FRONT_TEXT.value,
                        "color_text_rear": UKPlateColor.MOTORCYCLE_REAR_TEXT.value,
                        "start_x": 11,
                        "start_y": 11,
                        "width": 308,
                        "height": 79,
                        "coord": 0,
                        "obj": [
                            [
                                {'type': 2, 'name': 'AB12ABC'},
                                {'type': 3, 'obj': [{'ox': 0, 'oy': 0, 'w': 44, 'h': 64},
                                                    {'ox': 10, 'oy': 0, 'w': 44, 'h': 64},
                                                    {'ox': 10, 'oy': 0, 'w': 44, 'h': 64},
                                                    {'ox': 10, 'oy': 0, 'w': 44, 'h': 64},
                                                    {'ox': -178, 'oy': 77, 'w': 44, 'h': 64},
                                                    {'ox': 10, 'oy': 0, 'w': 44, 'h': 64},
                                                    {'ox': 10, 'oy': 0, 'w': 44, 'h': 64}]},
                                {'type': 4, 'obj': plate_uk_dvla()},
                                {'type': 1, 'r': 1, 'min': 0, 'max': 99, 'zfil': 2},
                                {'type': 0, 'r': 1, 'rnd_obj': ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H',
                                                                'J', 'K', 'L', 'M', 'N', 'O', 'P', 'R',
                                                                'S', 'T', 'U', 'V', 'W', 'X', 'Y', ]},
                                {'type': 0, 'r': 1, 'rnd_obj': ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H',
                                                                'J', 'K', 'L', 'M', 'N', 'O', 'P', 'R',
                                                                'S', 'T', 'U', 'V', 'W', 'X', 'Y', ]},
                                {'type': 0, 'r': 1, 'rnd_obj': ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H',
                                                                'J', 'K', 'L', 'M', 'N', 'O', 'P', 'R',
                                                                'S', 'T', 'U', 'V', 'W', 'X', 'Y', ]}

                            ]
                        ]

                    },
                ]
            },
            {
                "name": UKPlateType.TRAILER.value,
                "width": 231,
                "height": 164,
                "color_bg": UKPlateColor.TRAILER_BG.value,
                "color_text": UKPlateColor.TRAILER_TEXT.value,
                "object": [
                    {
                        "type": "rectangle",
                        "fill_color": UKPlateColor.TRAILER_BG.value,
                        "border_color": None,
                        "border_width": 1,
                        "quantity": 1,
                        "start_x": 0,
                        "start_y": 0,
                        "width": 231,
                        "height": 164,
                        "coord": 0
                    },
                    {
                        "type": "format",
                        "random": 1,
                        "color_bg": UKPlateColor.TRANSPARENT_BG.value,
                        "color_text": UKPlateColor.TRAILER_TEXT.value,
                        "start_x": 11,
                        "start_y": 11,
                        "width": 308,
                        "height": 79,
                        "coord": 0,
                        "obj": [
                            [
                                {'type': 2, 'name': 'A1234567'},
                                {'type': 3, 'obj': [{'ox': 0, 'oy': 0, 'w': 44, 'h': 64},
                                                    {'ox': 10, 'oy': 0, 'w': 44, 'h': 64},
                                                    {'ox': 10, 'oy': 0, 'w': 44, 'h': 64},
                                                    {'ox': 10, 'oy': 0, 'w': 44, 'h': 64},
                                                    {'ox': 11, 'oy': 88, 'w': 44, 'h': 64, 'r': False},
                                                    {'ox': 10, 'oy': 0, 'w': 44, 'h': 64},
                                                    {'ox': 10, 'oy': 0, 'w': 44, 'h': 64},
                                                    {'ox': 10, 'oy': 0, 'w': 44, 'h': 64}]},
                                {'type': 0, 'r': 1, 'rnd_obj': ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H',
                                                                'J', 'K', 'L', 'M', 'N', 'O', 'P', 'R',
                                                                'S', 'T', 'U', 'V', 'W', 'X', 'Y', ]},
                                {'type': 1, 'r': 1, 'min': 0, 'max': 9999999, 'zfil': 7},
                            ]
                        ]
                    },
                ]
            },

        ]
    }


def plate_uk_dvla():
    return [
        {
            "letter_1": "A",
            "mnemonic": "Anglia",
            "DVLA_office": [
                {
                    "name": "Peterborough",
                    "letter_2": "ABCDEFGJKMN"
                },
                {
                    "name": "Norwich",
                    "letter_2": "OPRSTU"
                },
                {
                    "name": "Ipswich",
                    "letter_2": "VWXY"
                }
            ]
        },
        {
            "letter_1": "B",
            "mnemonic": "Birmingham",
            "DVLA_office": [
                {
                    "name": "Birmingham",
                    "letter_2": "ABCDEFGHJKLMNOPRSTUVWX"
                }
            ]
        },
        {
            "letter_1": "C",
            "mnemonic": "Cymru (Wales)",
            "DVLA_office": [
                {
                    "name": "Cardiff",
                    "letter_2": "ABCDEFGHJKLMNO"
                },
                {
                    "name": "Swansea",
                    "letter_2": "PRSTUV"
                },
                {
                    "name": "Bangor",
                    "letter_2": "WXY"
                }
            ]
        },
        {
            "letter_1": "D",
            "mnemonic": "Deeside",
            "DVLA_office": [
                {
                    "name": "Chester",
                    "letter_2": "ABCDEFGHJK"
                },
                {
                    "name": "Shrewsbury",
                    "letter_2": "LMNOPSTUVWXY"
                }
            ]
        },
        {
            "letter_1": "E",
            "mnemonic": "Essex",
            "DVLA_office": [
                {
                    "name": "Chelmsford",
                    "letter_2": "ABCEFGJKLMNOPRSTUVWXY"
                }
            ]
        },
        {
            "letter_1": "F",
            "mnemonic": "Forest and Fens",
            "DVLA_office": [
                {
                    "name": "Nottingham",
                    "letter_2": "ABCDEFGHJKLMNP"
                },
                {
                    "name": "Lincoln",
                    "letter_2": "RSTVWXY"
                }
            ]
        },
        {
            "letter_1": "G",
            "mnemonic": "Garden of England",
            "DVLA_office": [
                {
                    "name": "Maidstone",
                    "letter_2": "ABCDEFGHJKLMN"
                },
                {
                    "name": "Brighton",
                    "letter_2": "PRSTUVWXY"
                }
            ]
        },
        {
            "letter_1": "H",
            "mnemonic": "Hampshire and Dorset",
            "DVLA_office": [
                {
                    "name": "Bournemouth",
                    "letter_2": "ABCDEFGHJ"
                },
                {
                    "name": "Portsmouth",
                    "letter_2": "KLMNPRSTUVXY"
                },
                {
                    "name": "Isle of Wight",
                    "letter_2": "W"
                }
            ]
        },
        {
            "letter_1": "K",
            "mnemonic": "No official mnemonic",
            "DVLA_office": [
                {
                    "name": "Borehamwood (formerly Luton)",
                    "letter_2": "ABCDEFGHJKL"
                },
                {
                    "name": "Northampton",
                    "letter_2": "MNOPRSTUVWXY"
                }
            ]
        },
        {
            "letter_1": "L",
            "mnemonic": "London",
            "DVLA_office": [
                {
                    "name": "Wimbledon",
                    "letter_2": "ABCDEFGHJ"
                },
                {
                    "name": "Borehamwood (formerly Stanmore)",
                    "letter_2": "KLMNOPRST"
                },
                {
                    "name": "Sidcup",
                    "letter_2": "UVWXY"
                }
            ]
        },
        {
            "letter_1": "M",
            "mnemonic": "Manchester and Merseyside",
            "DVLA_office": [
                {
                    "name": "Manchester",
                    "letter_2": "ABCDEFGHJKLMPTUVWX"
                },
                {
                    "name": "Isle of Man",
                    "letter_2": "N"
                }
            ]
        },
        {
            "letter_1": "N",
            "mnemonic": "Newcastle",
            "DVLA_office": [
                {
                    "name": "Newcastle",
                    "letter_2": "ABCDEFGHJKLMNO"
                },
                {
                    "name": "Stockton",
                    "letter_2": "PRSTUVWXY"
                }
            ]
        },
        {
            "letter_1": "O",
            "mnemonic": "Oxford",
            "DVLA_office": [
                {
                    "name": "Oxford",
                    "letter_2": "ABCDEFGHJLMOPTUVWXY"
                }
            ]
        },
        {
            "letter_1": "P",
            "mnemonic": "Preston",
            "DVLA_office": [
                {
                    "name": "Preston",
                    "letter_2": "ABCDEFGHJKLMNOPRST"
                },
                {
                    "name": "Carlisle",
                    "letter_2": "UVWXY"
                }
            ]
        },
        {
            "letter_1": "R",
            "mnemonic": "Reading",
            "DVLA_office": [
                {
                    "name": "Reading",
                    "letter_2": "ABCDEFGHJKLMNOPRSTVWXY"
                }
            ]
        },
        {
            "letter_1": "S",
            "mnemonic": "Scotland",
            "DVLA_office": [
                {
                    "name": "Glasgow",
                    "letter_2": "ABCDEFGHJ"
                },
                {
                    "name": "Edinburgh",
                    "letter_2": "KLMNO"
                },
                {
                    "name": "Dundee",
                    "letter_2": "PRST"
                },
                {
                    "name": "Aberdeen",
                    "letter_2": "VW"
                },
                {
                    "name": "Inverness",
                    "letter_2": "XY"
                }
            ]
        },
        {
            "letter_1": "V",
            "mnemonic": "Severn Valley",
            "DVLA_office": [
                {
                    "name": "Worcester",
                    "letter_2": "ABCEFGHJKLMNOPRSTUVXY"
                }
            ]
        },
        {
            "letter_1": "W",
            "mnemonic": "West of England",
            "DVLA_office": [
                {
                    "name": "Exeter",
                    "letter_2": "ABDEFGHJ"
                },
                {
                    "name": "Truro",
                    "letter_2": "KL"
                },
                {
                    "name": "Bristol",
                    "letter_2": "MNOPRSTUVWXY"
                }
            ]
        },
        {
            "letter_1": "X",
            "mnemonic": "Personal export",
            "DVLA_office": [
                {
                    "name": "Beverley, Birmingham, Bristol, Chelmsford, Glasgow, Leeds, Lincoln, Maidstone, Manchester, Northampton, Norwich, Oxford, Stockton, Wimbledon",
                    "letter_2": "ABCDEF"
                }
            ]
        },
        {
            "letter_1": "Y",
            "mnemonic": "Yorkshire",
            "DVLA_office": [
                {
                    "name": "Leeds",
                    "letter_2": "ABCDEFGHJKL"
                },
                {
                    "name": "Sheffield",
                    "letter_2": "MNOPRSTUV"
                },
                {
                    "name": "Beverley",
                    "letter_2": "WXY"
                }
            ]
        }
    ]
