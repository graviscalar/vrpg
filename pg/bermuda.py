from enum import Enum


class BermudaPlateType(Enum):
    PRIVATE = 'Private'
    CLASSIC = 'Classic'
    LIGHT_TRUCK = 'Light truck'
    INTERMEDIATE_TRUCK = 'Intermediate truck'
    HEAVY_TRUCK = 'Heavy truck'
    LIGHT_PRIVATE = 'Light private'
    TAXI = 'Taxi'
    CONSTRUCTION = 'Construction'
    ELECTRIC_FOR_TOURIST = 'Electric for tourist'
    US_FORCES = 'US forces'
    AUXILIARY_CYCLE = 'Auxiliary cycle'
    MOTORCYCLE = 'Motorcycle'


class BermudaPlateColor(Enum):
    TRANSPARENT_BG = (255, 255, 255, 0)

    PRIVATE_BG = (255, 255, 255)
    PRIVATE_TEXT = (0, 0, 0)
    CLASSIC_BG = (255, 255, 255)
    CLASSIC_TEXT = (0, 0, 0)
    LIGHT_TRUCK_BG = (255, 255, 255)
    LIGHT_TRUCK_TEXT = (0, 0, 0)
    INTERMEDIATE_TRUCK_BG = (255, 255, 255)
    INTERMEDIATE_TRUCK_TEXT = (0, 0, 0)
    HEAVY_TRUCK_BG = (255, 255, 255)
    HEAVY_TRUCK_TEXT = (0, 0, 0)
    LIGHT_PRIVATE_BG = (255, 255, 255)
    LIGHT_PRIVATE_TEXT = (0, 0, 0)
    TAXI_BG = (255, 255, 255)
    TAXI_TEXT = (0, 0, 0)
    CONSTRUCTION_BG = (255, 255, 255)
    CONSTRUCTION_TEXT = (0, 0, 0)
    ELECTRIC_FOR_TOURIST_BG = (255, 255, 255)
    ELECTRIC_FOR_TOURIST_TEXT = (255, 0, 0)
    US_FORCES_BG = (0, 0, 0)
    US_FORCES_TEXT = (255, 255, 255)
    AUXILIARY_CYCLE_BG = (255, 255, 255)
    AUXILIARY_CYCLE_TEXT = (0, 0, 0)
    MOTORCYCLE_BG = (255, 255, 255)
    MOTORCYCLE_TEXT = (0, 0, 0)


def plate_bermuda():
    return {
        "country": "Bermuda",
        "rfy": "1975",  # registration format year
        "font": "CharlesWright-Bold.otf",
        "plates": [
            {
                "name": BermudaPlateType.PRIVATE.value,
                "width": 520,
                "height": 110,
                "color_bg": BermudaPlateColor.PRIVATE_BG.value,
                "color_text": BermudaPlateColor.PRIVATE_TEXT.value,
                "object": [
                    {
                        "type": "rectangle",
                        "fill_color": BermudaPlateColor.PRIVATE_BG.value,
                        "border_color": None,
                        "border_width": 1,
                        "quantity": 1,
                        "start_x": 0,
                        "start_y": 0,
                        "width": 520,
                        "height": 110,
                        "coord": 0
                    },
                    {
                        "type": "format",
                        "random": 1,
                        "color_bg": BermudaPlateColor.TRANSPARENT_BG.value,
                        "color_text": BermudaPlateColor.PRIVATE_TEXT.value,
                        "start_x": 118,
                        "start_y": 16,
                        "width": 266,
                        "height": 80,
                        "coord": 0,
                        "obj": [
                            [{'type': 2, 'name': '11111'},
                             {'type': 3, 'obj': [{'ox': 0, 'oy': 0, 'w': 50, 'h': 79},
                                                 {'ox': 11, 'oy': 0, 'w': 50, 'h': 79},
                                                 {'ox': 11, 'oy': 0, 'w': 50, 'h': 79},
                                                 {'ox': 11, 'oy': 0, 'w': 50, 'h': 79},
                                                 {'ox': 11, 'oy': 0, 'w': 50, 'h': 79}]},
                             {'type': 1, 'r': 1, 'min': 0, 'max': 99999, 'zfil': 5},
                             ]
                        ]
                    }
                ]
            },
            {
                "name": BermudaPlateType.CLASSIC.value,
                "width": 520,
                "height": 110,
                "color_bg": BermudaPlateColor.CLASSIC_BG.value,
                "color_text": BermudaPlateColor.CLASSIC_TEXT.value,
                "object": [
                    {
                        "type": "rectangle",
                        "fill_color": BermudaPlateColor.CLASSIC_BG.value,
                        "border_color": None,
                        "border_width": 1,
                        "quantity": 1,
                        "start_x": 0,
                        "start_y": 0,
                        "width": 520,
                        "height": 110,
                        "coord": 0
                    },
                    {
                        "type": "format",
                        "random": 1,
                        "color_bg": BermudaPlateColor.TRANSPARENT_BG.value,
                        "color_text": BermudaPlateColor.CLASSIC_TEXT.value,
                        "start_x": 118,
                        "start_y": 16,
                        "width": 266,
                        "height": 80,
                        "coord": 0,
                        "obj": [
                            [{'type': 2, 'name': 'CL111'},
                             {'type': 0, 'r': 0, 'text_obj': 'CL'},
                             {'type': 3, 'obj': [{'ox': 0, 'oy': 0, 'w': 50, 'h': 79},
                                                 {'ox': 11, 'oy': 0, 'w': 50, 'h': 79},
                                                 {'ox': 30, 'oy': 0, 'w': 50, 'h': 79},
                                                 {'ox': 11, 'oy': 0, 'w': 50, 'h': 79},
                                                 {'ox': 11, 'oy': 0, 'w': 50, 'h': 79}]},
                             {'type': 1, 'r': 1, 'min': 0, 'max': 999, 'zfil': 3},
                             ]
                        ]
                    }
                ]
            },
            {
                "name": BermudaPlateType.LIGHT_TRUCK.value,
                "width": 520,
                "height": 110,
                "color_bg": BermudaPlateColor.LIGHT_TRUCK_BG.value,
                "color_text": BermudaPlateColor.LIGHT_TRUCK_TEXT.value,
                "object": [
                    {
                        "type": "rectangle",
                        "fill_color": BermudaPlateColor.LIGHT_TRUCK_BG.value,
                        "border_color": None,
                        "border_width": 1,
                        "quantity": 1,
                        "start_x": 0,
                        "start_y": 0,
                        "width": 520,
                        "height": 110,
                        "coord": 0
                    },
                    {
                        "type": "format",
                        "random": 1,
                        "color_bg": BermudaPlateColor.TRANSPARENT_BG.value,
                        "color_text": BermudaPlateColor.LIGHT_TRUCK_TEXT.value,
                        "start_x": 118,
                        "start_y": 16,
                        "width": 266,
                        "height": 80,
                        "coord": 0,
                        "obj": [
                            [{'type': 2, 'name': 'CL111'},
                             {'type': 0, 'r': 0, 'text_obj': 'L'},
                             {'type': 3, 'obj': [{'ox': 0, 'oy': 0, 'w': 50, 'h': 79},
                                                 {'ox': 30, 'oy': 0, 'w': 50, 'h': 79},
                                                 {'ox': 11, 'oy': 0, 'w': 50, 'h': 79},
                                                 {'ox': 11, 'oy': 0, 'w': 50, 'h': 79},
                                                 {'ox': 11, 'oy': 0, 'w': 50, 'h': 79}]},
                             {'type': 1, 'r': 1, 'min': 0, 'max': 9999, 'zfil': 4},
                             ]
                        ]
                    }
                ]
            },
            {
                "name": BermudaPlateType.INTERMEDIATE_TRUCK.value,
                "width": 520,
                "height": 110,
                "color_bg": BermudaPlateColor.INTERMEDIATE_TRUCK_BG.value,
                "color_text": BermudaPlateColor.INTERMEDIATE_TRUCK_TEXT.value,
                "object": [
                    {
                        "type": "rectangle",
                        "fill_color": BermudaPlateColor.INTERMEDIATE_TRUCK_BG.value,
                        "border_color": None,
                        "border_width": 1,
                        "quantity": 1,
                        "start_x": 0,
                        "start_y": 0,
                        "width": 520,
                        "height": 110,
                        "coord": 0
                    },
                    {
                        "type": "format",
                        "random": 1,
                        "color_bg": BermudaPlateColor.TRANSPARENT_BG.value,
                        "color_text": BermudaPlateColor.INTERMEDIATE_TRUCK_TEXT.value,
                        "start_x": 90,
                        "start_y": 16,
                        "width": 266,
                        "height": 80,
                        "coord": 0,
                        "obj": [
                            [{'type': 2, 'name': 'IN1111'},
                             {'type': 0, 'r': 0, 'text_obj': 'IN'},
                             {'type': 3, 'obj': [{'ox': 0, 'oy': 0, 'w': 50, 'h': 79},
                                                 {'ox': 11, 'oy': 0, 'w': 50, 'h': 79},
                                                 {'ox': 30, 'oy': 0, 'w': 50, 'h': 79},
                                                 {'ox': 11, 'oy': 0, 'w': 50, 'h': 79},
                                                 {'ox': 11, 'oy': 0, 'w': 50, 'h': 79},
                                                 {'ox': 11, 'oy': 0, 'w': 50, 'h': 79}]},
                             {'type': 1, 'r': 1, 'min': 0, 'max': 9999, 'zfil': 4},
                             ]
                        ]
                    }
                ]
            },
            {
                "name": BermudaPlateType.HEAVY_TRUCK.value,
                "width": 520,
                "height": 110,
                "color_bg": BermudaPlateColor.HEAVY_TRUCK_BG.value,
                "color_text": BermudaPlateColor.HEAVY_TRUCK_TEXT.value,
                "object": [
                    {
                        "type": "rectangle",
                        "fill_color": BermudaPlateColor.HEAVY_TRUCK_BG.value,
                        "border_color": None,
                        "border_width": 1,
                        "quantity": 1,
                        "start_x": 0,
                        "start_y": 0,
                        "width": 520,
                        "height": 110,
                        "coord": 0
                    },
                    {
                        "type": "format",
                        "random": 1,
                        "color_bg": BermudaPlateColor.TRANSPARENT_BG.value,
                        "color_text": BermudaPlateColor.HEAVY_TRUCK_TEXT.value,
                        "start_x": 110,
                        "start_y": 16,
                        "width": 266,
                        "height": 80,
                        "coord": 0,
                        "obj": [
                            [{'type': 2, 'name': 'HA111'},
                             {'type': 0, 'r': 0, 'text_obj': 'HA'},
                             {'type': 3, 'obj': [{'ox': 0, 'oy': 0, 'w': 50, 'h': 79},
                                                 {'ox': 11, 'oy': 0, 'w': 50, 'h': 79},
                                                 {'ox': 30, 'oy': 0, 'w': 50, 'h': 79},
                                                 {'ox': 11, 'oy': 0, 'w': 50, 'h': 79},
                                                 {'ox': 11, 'oy': 0, 'w': 50, 'h': 79}]},
                             {'type': 1, 'r': 1, 'min': 0, 'max': 999, 'zfil': 3},
                             ]
                        ]
                    }
                ]
            },
            {
                "name": BermudaPlateType.LIGHT_PRIVATE.value,
                "width": 520,
                "height": 110,
                "color_bg": BermudaPlateColor.LIGHT_PRIVATE_BG.value,
                "color_text": BermudaPlateColor.LIGHT_PRIVATE_TEXT.value,
                "object": [
                    {
                        "type": "rectangle",
                        "fill_color": BermudaPlateColor.LIGHT_PRIVATE_BG.value,
                        "border_color": None,
                        "border_width": 1,
                        "quantity": 1,
                        "start_x": 0,
                        "start_y": 0,
                        "width": 520,
                        "height": 110,
                        "coord": 0
                    },
                    {
                        "type": "format",
                        "random": 1,
                        "color_bg": BermudaPlateColor.TRANSPARENT_BG.value,
                        "color_text": BermudaPlateColor.LIGHT_PRIVATE_TEXT.value,
                        "start_x": 80,
                        "start_y": 16,
                        "width": 266,
                        "height": 80,
                        "coord": 0,
                        "obj": [
                            [{'type': 2, 'name': 'LP1111'},
                             {'type': 0, 'r': 0, 'text_obj': 'LP'},
                             {'type': 3, 'obj': [{'ox': 0, 'oy': 0, 'w': 50, 'h': 79},
                                                 {'ox': 11, 'oy': 0, 'w': 50, 'h': 79},
                                                 {'ox': 30, 'oy': 0, 'w': 50, 'h': 79},
                                                 {'ox': 11, 'oy': 0, 'w': 50, 'h': 79},
                                                 {'ox': 11, 'oy': 0, 'w': 50, 'h': 79},
                                                 {'ox': 11, 'oy': 0, 'w': 50, 'h': 79}]},
                             {'type': 1, 'r': 1, 'min': 0, 'max': 9999, 'zfil': 4},
                             ]
                        ]
                    }
                ]
            },
            {
                "name": BermudaPlateType.TAXI.value,
                "width": 520,
                "height": 110,
                "color_bg": BermudaPlateColor.TAXI_BG.value,
                "color_text": BermudaPlateColor.TAXI_TEXT.value,
                "object": [
                    {
                        "type": "rectangle",
                        "fill_color": BermudaPlateColor.TAXI_BG.value,
                        "border_color": None,
                        "border_width": 1,
                        "quantity": 1,
                        "start_x": 0,
                        "start_y": 0,
                        "width": 520,
                        "height": 110,
                        "coord": 0
                    },
                    {
                        "type": "format",
                        "random": 1,
                        "color_bg": BermudaPlateColor.TRANSPARENT_BG.value,
                        "color_text": BermudaPlateColor.TAXI_TEXT.value,
                        "start_x": 110,
                        "start_y": 16,
                        "width": 266,
                        "height": 80,
                        "coord": 0,
                        "obj": [
                            [{'type': 2, 'name': 'T1111'},
                             {'type': 0, 'r': 0, 'text_obj': 'T'},
                             {'type': 3, 'obj': [{'ox': 0, 'oy': 0, 'w': 50, 'h': 79},
                                                 {'ox': 30, 'oy': 0, 'w': 50, 'h': 79},
                                                 {'ox': 11, 'oy': 0, 'w': 50, 'h': 79},
                                                 {'ox': 11, 'oy': 0, 'w': 50, 'h': 79},
                                                 {'ox': 11, 'oy': 0, 'w': 50, 'h': 79}]},
                             {'type': 1, 'r': 1, 'min': 0, 'max': 9999, 'zfil': 4},
                             ]
                        ]
                    }
                ]
            },
            {
                "name": BermudaPlateType.CONSTRUCTION.value,
                "width": 520,
                "height": 110,
                "color_bg": BermudaPlateColor.CONSTRUCTION_BG.value,
                "color_text": BermudaPlateColor.CONSTRUCTION_TEXT.value,
                "object": [
                    {
                        "type": "rectangle",
                        "fill_color": BermudaPlateColor.CONSTRUCTION_BG.value,
                        "border_color": None,
                        "border_width": 1,
                        "quantity": 1,
                        "start_x": 0,
                        "start_y": 0,
                        "width": 520,
                        "height": 110,
                        "coord": 0
                    },
                    {
                        "type": "format",
                        "random": 1,
                        "color_bg": BermudaPlateColor.TRANSPARENT_BG.value,
                        "color_text": BermudaPlateColor.CONSTRUCTION_TEXT.value,
                        "start_x": 110,
                        "start_y": 16,
                        "width": 266,
                        "height": 80,
                        "coord": 0,
                        "obj": [
                            [{'type': 2, 'name': 'CM111'},
                             {'type': 0, 'r': 0, 'text_obj': 'CM'},
                             {'type': 3, 'obj': [{'ox': 0, 'oy': 0, 'w': 50, 'h': 79},
                                                 {'ox': 11, 'oy': 0, 'w': 50, 'h': 79},
                                                 {'ox': 30, 'oy': 0, 'w': 50, 'h': 79},
                                                 {'ox': 11, 'oy': 0, 'w': 50, 'h': 79},
                                                 {'ox': 11, 'oy': 0, 'w': 50, 'h': 79}]},
                             {'type': 1, 'r': 1, 'min': 0, 'max': 999, 'zfil': 3},
                             ]
                        ]
                    }
                ]
            },
            {
                "name": BermudaPlateType.ELECTRIC_FOR_TOURIST.value,
                "width": 520,
                "height": 110,
                "color_bg": BermudaPlateColor.ELECTRIC_FOR_TOURIST_BG.value,
                "color_text": BermudaPlateColor.ELECTRIC_FOR_TOURIST_TEXT.value,
                "object": [
                    {
                        "type": "rectangle",
                        "fill_color": BermudaPlateColor.ELECTRIC_FOR_TOURIST_BG.value,
                        "border_color": None,
                        "border_width": 1,
                        "quantity": 1,
                        "start_x": 0,
                        "start_y": 0,
                        "width": 520,
                        "height": 110,
                        "coord": 0
                    },
                    {
                        "type": "format",
                        "random": 1,
                        "color_bg": BermudaPlateColor.TRANSPARENT_BG.value,
                        "color_text": BermudaPlateColor.ELECTRIC_FOR_TOURIST_TEXT.value,
                        "start_x": 75,
                        "start_y": 16,
                        "width": 266,
                        "height": 80,
                        "coord": 0,
                        "obj": [
                            [{'type': 2, 'name': 'RMC111'},
                             {'type': 0, 'r': 0, 'text_obj': 'RMC'},
                             {'type': 3, 'obj': [{'ox': 0, 'oy': 0, 'w': 50, 'h': 79},
                                                 {'ox': 11, 'oy': 0, 'w': 50, 'h': 79},
                                                 {'ox': 11, 'oy': 0, 'w': 50, 'h': 79},
                                                 {'ox': 30, 'oy': 0, 'w': 50, 'h': 79},
                                                 {'ox': 11, 'oy': 0, 'w': 50, 'h': 79},
                                                 {'ox': 11, 'oy': 0, 'w': 50, 'h': 79}]},
                             {'type': 1, 'r': 1, 'min': 0, 'max': 999, 'zfil': 3},
                             ]
                        ]
                    }
                ]
            },
            {
                "name": BermudaPlateType.US_FORCES.value,
                "width": 520,
                "height": 110,
                "color_bg": BermudaPlateColor.US_FORCES_BG.value,
                "color_text": BermudaPlateColor.US_FORCES_TEXT.value,
                "object": [
                    {
                        "type": "rectangle",
                        "fill_color": BermudaPlateColor.US_FORCES_BG.value,
                        "border_color": None,
                        "border_width": 1,
                        "quantity": 1,
                        "start_x": 0,
                        "start_y": 0,
                        "width": 520,
                        "height": 110,
                        "coord": 0
                    },
                    {
                        "type": "format",
                        "random": 1,
                        "color_bg": BermudaPlateColor.TRANSPARENT_BG.value,
                        "color_text": BermudaPlateColor.US_FORCES_TEXT.value,
                        "start_x": 110,
                        "start_y": 16,
                        "width": 266,
                        "height": 80,
                        "coord": 0,
                        "obj": [
                            [{'type': 2, 'name': 'RMC111'},
                             {'type': 0, 'r': 1, 'rnd_obj': ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H',
                                                             'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P',
                                                             'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']},
                             {'type': 3, 'obj': [{'ox': 0, 'oy': 0, 'w': 50, 'h': 79},
                                                 {'ox': 30, 'oy': 0, 'w': 50, 'h': 79},
                                                 {'ox': 11, 'oy': 0, 'w': 50, 'h': 79},
                                                 {'ox': 11, 'oy': 0, 'w': 50, 'h': 79},
                                                 {'ox': 11, 'oy': 0, 'w': 50, 'h': 79}]},
                             {'type': 1, 'r': 1, 'min': 0, 'max': 9999, 'zfil': 4},
                             ]
                        ]
                    }
                ]
            },
            {
                "name": BermudaPlateType.AUXILIARY_CYCLE.value,
                "width": 231,
                "height": 164,
                "color_bg": BermudaPlateColor.AUXILIARY_CYCLE_BG.value,
                "color_text": BermudaPlateColor.AUXILIARY_CYCLE_TEXT.value,
                "object": [
                    {
                        "type": "rectangle",
                        "fill_color": BermudaPlateColor.AUXILIARY_CYCLE_BG.value,
                        "border_color": None,
                        "border_width": 1,
                        "quantity": 1,
                        "start_x": 0,
                        "start_y": 0,
                        "width": 520,
                        "height": 110,
                        "coord": 0
                    },
                    {
                        "type": "format",
                        "random": 1,
                        "color_bg": BermudaPlateColor.TRANSPARENT_BG.value,
                        "color_text": BermudaPlateColor.AUXILIARY_CYCLE_TEXT.value,
                        "start_x": 11,
                        "start_y": 52,
                        "width": 266,
                        "height": 80,
                        "coord": 0,
                        "obj": [
                            [{'type': 2, 'name': '111A'},
                             {'type': 3, 'obj': [{'ox': 0, 'oy': 0, 'w': 42, 'h': 64},
                                                 {'ox': 10, 'oy': 0, 'w': 42, 'h': 64},
                                                 {'ox': 10, 'oy': 0, 'w': 42, 'h': 64},
                                                 {'ox': 10, 'oy': 0, 'w': 42, 'h': 64}]},
                             {'type': 1, 'r': 1, 'min': 0, 'max': 999, 'zfil': 3},
                             {'type': 0, 'r': 1, 'rnd_obj': ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H',
                                                             'J', 'K', 'L', 'M', 'N', 'P',
                                                             'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']},
                             ]
                        ]
                    }
                ]
            },
            {
                "name": BermudaPlateType.MOTORCYCLE.value,
                "width": 231,
                "height": 164,
                "color_bg": BermudaPlateColor.MOTORCYCLE_BG.value,
                "color_text": BermudaPlateColor.MOTORCYCLE_TEXT.value,
                "object": [
                    {
                        "type": "rectangle",
                        "fill_color": BermudaPlateColor.MOTORCYCLE_BG.value,
                        "border_color": None,
                        "border_width": 1,
                        "quantity": 1,
                        "start_x": 0,
                        "start_y": 0,
                        "width": 520,
                        "height": 110,
                        "coord": 0
                    },
                    {
                        "type": "format",
                        "random": 1,
                        "color_bg": BermudaPlateColor.TRANSPARENT_BG.value,
                        "color_text": BermudaPlateColor.MOTORCYCLE_TEXT.value,
                        "start_x": 8,
                        "start_y": 52,
                        "width": 266,
                        "height": 80,
                        "coord": 0,
                        "obj": [
                            [{'type': 2, 'name': 'AA111'},
                             {'type': 0, 'r': 1, 'rnd_obj': ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H',
                                                             'J', 'K', 'L', 'M', 'N', 'P',
                                                             'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']},
                             {'type': 0, 'r': 1, 'rnd_obj': ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H',
                                                             'J', 'K', 'L', 'M', 'N', 'P',
                                                             'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']},
                             {'type': 1, 'r': 1, 'min': 0, 'max': 999, 'zfil': 3},
                             {'type': 3, 'obj': [{'ox': 0, 'oy': 0, 'w': 38, 'h': 64},
                                                 {'ox': 6, 'oy': 0, 'w': 38, 'h': 64},
                                                 {'ox': 6, 'oy': 0, 'w': 38, 'h': 64},
                                                 {'ox': 6, 'oy': 0, 'w': 38, 'h': 64},
                                                 {'ox': 6, 'oy': 0, 'w': 38, 'h': 64}]},
                             ]
                        ]
                    }
                ]
            },

        ]
    }
