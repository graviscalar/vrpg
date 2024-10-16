from enum import Enum


class BoliviaPlateType(Enum):
    VEHICULO_PARTICULAR = 'Vehiculo particular'
    VEHICULO_MERCOSUR = 'Vehiculo MERCOSUR'
    CUERPO_CONSULAR = 'Cuerpo consular'
    CUERPO_DIPLOMATICO = 'Cuerpo diplomatico'
    MISSION_INTERNACIONAL = 'Mision internacional'
    ORGANIZACION_INTERNACIONAL = 'Organizacion internacional'


class BoliviaPlateColor(Enum):
    TRANSPARENT_BG = (255, 255, 255, 0)
    FLAG_RECT = (0, 0, 0)
    SINE_WAVE = (240, 240, 240)

    VEHICULO_PARTICULAR_BG = (255, 255, 255)
    VEHICULO_PARTICULAR_TEXT = (51, 76, 192)
    VEHICULO_PARTICULAR_RECT = (255, 255, 255)
    VEHICULO_MERCOSUR_BG = (255, 255, 255)
    VEHICULO_MERCOSUR_TEXT = (0, 0, 0)
    VEHICULO_MERCOSUR_RECT = (0, 51, 160)
    CUERPO_CONSULAR_BG = (0, 51, 160)
    CUERPO_CONSULAR_TEXT = (255, 255, 255)
    CUERPO_DIPLOMATICO_BG = (255, 255, 255)
    CUERPO_DIPLOMATICO_TEXT = (255, 0, 0)
    MISSION_INTERNACIONAL_BG = (251, 202, 47)
    MISSION_INTERNACIONAL_TEXT = (0, 0, 0)
    ORGANIZACION_INTERNACIONAL_BG = (96, 152, 57)
    ORGANIZACION_INTERNACIONAL_TEXT = (255, 255, 255)

def plate_bolivia():
    return {
        "country": "Bolivia",
        "rfy": "1999",  # registration format year
        "font": "roadgeek 2005 series 1b.ttf",
        "plates": [
            {
                "name": BoliviaPlateType.VEHICULO_PARTICULAR.value,
                "width": 305,
                "height": 152,
                "color_bg": BoliviaPlateColor.VEHICULO_PARTICULAR_BG.value,
                "color_text": BoliviaPlateColor.VEHICULO_PARTICULAR_TEXT.value,
                "object": [
                    {
                        "type": "rectangle",
                        "fill_color": BoliviaPlateColor.VEHICULO_PARTICULAR_BG.value,
                        "border_color": None,
                        "border_width": 1,
                        "quantity": 1,
                        "start_x": 0,
                        "start_y": 0,
                        "width": 305,
                        "height": 152,
                        "coord": 0
                    },
                    {
                        "type": "rectangle",
                        "fill_color": BoliviaPlateColor.VEHICULO_PARTICULAR_RECT.value,
                        "border_color": None,
                        "border_width": 1,
                        "quantity": 1,
                        "start_x": 4,
                        "start_y": 4,
                        "width": 397,
                        "height": 33,
                        "coord": 0
                    },
                    {
                        "type": "format",
                        "random": 1,
                        "color_bg": BoliviaPlateColor.TRANSPARENT_BG.value,
                        "color_text": BoliviaPlateColor.VEHICULO_PARTICULAR_TEXT.value,
                        "start_x": 24,
                        "start_y": 57,
                        "width": 266,
                        "height": 80,
                        "coord": 0,
                        "font": "TRAFFIC2_0.ttf",
                        "obj": [
                            [{'type': 2, 'name': '1234ABC'},
                             {'type': 3, 'obj': [{'ox': 0, 'oy': 0, 'w': 32, 'h': 74},
                                                 {'ox': 5, 'oy': 0, 'w': 32, 'h': 74},
                                                 {'ox': 5, 'oy': 0, 'w': 32, 'h': 74},
                                                 {'ox': 5, 'oy': 0, 'w': 32, 'h': 74},
                                                 {'ox': 5, 'oy': 0, 'w': 32, 'h': 74},
                                                 {'ox': 5, 'oy': 0, 'w': 32, 'h': 74},
                                                 {'ox': 5, 'oy': 0, 'w': 32, 'h': 74}]},
                             {'type': 5, 'sl': {'I', '1'}},
                             {'type': 1, 'r': 1, 'min': 0, 'max': 9999, 'zfil': 4},
                             {'type': 0, 'r': 1, 'rnd_obj': ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H',
                                                             'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P',
                                                             'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']},
                             {'type': 0, 'r': 1, 'rnd_obj': ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H',
                                                             'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P',
                                                             'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']},
                             {'type': 0, 'r': 1, 'rnd_obj': ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H',
                                                             'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P',
                                                             'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']},
                             ]
                        ]
                    },
                    {
                        "type": "rectangle_rounded",
                        "fill_color": None,
                        "border_color": BoliviaPlateColor.VEHICULO_PARTICULAR_TEXT.value,
                        "border_width": 4,
                        "border_radius": 10,
                        "quantity": 1,
                        "start_x": 0,
                        "start_y": 0,
                        "width": 305,
                        "height": 152,
                        "coord": 0
                    },
                    {
                        "type": "image",
                        "image": "img/Bolivia/Bandera_de_Bolivia.png",
                        "random": 0,
                        "letters": None,
                        "quantity": 1,
                        "start_x": 15,
                        "start_y": 21,
                        "width": 40,
                        "height": 25,
                        "coord": 0
                    },
                    {
                        "type": "rectangle",
                        "fill_color": None,
                        "border_color": BoliviaPlateColor.FLAG_RECT.value,
                        "border_width": 1,
                        "quantity": 1,
                        "start_x": 15,
                        "start_y": 21,
                        "width": 40,
                        "height": 25,
                        "coord": 0
                    },
                    {
                        "type": "text",
                        "random": 0,
                        "letters": u"B O L I V I A",
                        "color_bg": BoliviaPlateColor.TRANSPARENT_BG.value,
                        "color_text": BoliviaPlateColor.VEHICULO_PARTICULAR_TEXT.value,
                        "by_letter": 0,
                        "quantity": 0,
                        "start_x": 81,
                        "start_y": 22,
                        "width": 142,
                        "height": 20,
                        "offset_x": 10,
                        "coord": 0,
                        "font": "ARIALN.TTF"
                    },
                    {
                        "type": "text",
                        "random": 1,
                        "letters": ['C', 'H', 'B', 'L', 'O', 'N', 'P', 'S', 'T'],
                        "by_letter": 0,
                        "quantity": 1,
                        "start_x": 260,
                        "start_y": 22,
                        "width": 22,
                        "height": 18,
                        "offset_x": 2,
                        "coord": 0,
                        "font": "ARIALN.TTF"
                    }
                ]
            },
            {
                "name": BoliviaPlateType.VEHICULO_MERCOSUR.value,
                "width": 400,
                "height": 130,
                "color_bg": BoliviaPlateColor.VEHICULO_MERCOSUR_BG.value,
                "color_text": BoliviaPlateColor.VEHICULO_MERCOSUR_TEXT.value,
                "object": [
                    {
                        "type": "rectangle",
                        "fill_color": BoliviaPlateColor.VEHICULO_MERCOSUR_BG.value,
                        "border_color": None,
                        "border_width": 1,
                        "quantity": 1,
                        "start_x": 0,
                        "start_y": 0,
                        "width": 404,
                        "height": 154,
                        "coord": 0
                    },
                    {
                        "type": "sine_wave",
                        "fill_color": BoliviaPlateColor.SINE_WAVE.value,
                        "wave_width": 2,
                        "wave_period": 54,
                        "wave_amplitude": 7,
                        "wave_phase": 0,
                        "start_x": 5,
                        "start_y": 85,
                        "end_x": 400,
                        "end_y": 85,
                    },
                    {
                        "type": "sine_wave",
                        "fill_color": BoliviaPlateColor.SINE_WAVE.value,
                        "wave_width": 2,
                        "wave_period": 54,
                        "wave_amplitude": 7,
                        "wave_phase": 12,
                        "start_x": 5,
                        "start_y": 86,
                        "end_x": 400,
                        "end_y": 86,
                    },
                    {
                        "type": "rectangle",
                        "fill_color": BoliviaPlateColor.VEHICULO_MERCOSUR_RECT.value,
                        "border_color": None,
                        "border_width": 1,
                        "quantity": 1,
                        "start_x": 4,
                        "start_y": 4,
                        "width": 397,
                        "height": 33,
                        "coord": 0
                    },
                    {
                        "type": "format",
                        "random": 1,
                        "color_bg": BoliviaPlateColor.TRANSPARENT_BG.value,
                        "color_text": BoliviaPlateColor.VEHICULO_MERCOSUR_TEXT.value,
                        "start_x": 24,
                        "start_y": 46,
                        "width": 266,
                        "height": 80,
                        "coord": 0,
                        "font": "EuroPlate.ttf",
                        "obj": [
                            [{'type': 2, 'name': 'AB123CD'},
                             {'type': 3, 'obj': [{'ox': 0, 'oy': 0, 'w': 35, 'h': 64},
                                                 {'ox': 11, 'oy': 0, 'w': 35, 'h': 64},
                                                 {'ox': 40, 'oy': 0, 'w': 35, 'h': 64},
                                                 {'ox': 11, 'oy': 0, 'w': 35, 'h': 64},
                                                 {'ox': 11, 'oy': 0, 'w': 35, 'h': 64},
                                                 {'ox': 11, 'oy': 0, 'w': 35, 'h': 64},
                                                 {'ox': 11, 'oy': 0, 'w': 35, 'h': 64}]},
                             {'type': 5, 'sl': {}},
                             {'type': 0, 'r': 1, 'rnd_obj': ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H',
                                                             'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P',
                                                             'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']},
                             {'type': 0, 'r': 1, 'rnd_obj': ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H',
                                                             'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P',
                                                             'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']},
                             {'type': 1, 'r': 1, 'min': 0, 'max': 99999, 'zfil': 5},
                             ]
                        ]
                    },
                    {
                        "type": "rectangle_rounded",
                        "fill_color": None,
                        "border_color": BoliviaPlateColor.VEHICULO_MERCOSUR_TEXT.value,
                        "border_width": 4,
                        "border_radius": 10,
                        "quantity": 1,
                        "start_x": 0,
                        "start_y": 0,
                        "width": 400,
                        "height": 130,
                        "coord": 0
                    },
                    {
                        "type": "image",
                        "image": "img/Argentina/Flag_of_Mercosur.png",
                        "random": 0,
                        "letters": None,
                        "quantity": 1,
                        "start_x": 18,
                        "start_y": 8,
                        "width": 34,
                        "height": 26,
                        "coord": 0
                    },
                    {
                        "type": "image",
                        "image": "img/Bolivia/Bandera_de_Bolivia.png",
                        "random": 0,
                        "letters": None,
                        "quantity": 1,
                        "start_x": 353,
                        "start_y": 12,
                        "width": 28,
                        "height": 20,
                        "coord": 0
                    },
                    {
                        "type": "text",
                        "random": 0,
                        "letters": u"BOLIVIA",
                        "color_bg": BoliviaPlateColor.TRANSPARENT_BG.value,
                        "color_text": BoliviaPlateColor.VEHICULO_MERCOSUR_BG.value,
                        "by_letter": 0,
                        "quantity": 0,
                        "start_x": 144,
                        "start_y": 10,
                        "width": 110,
                        "height": 20,
                        "offset_x": 10,
                        "coord": 0,
                        "font": "ARIALN.TTF"
                    },
                ]
            },
            {
                "name": BoliviaPlateType.CUERPO_CONSULAR.value,
                "width": 305,
                "height": 152,
                "color_bg": BoliviaPlateColor.CUERPO_CONSULAR_BG.value,
                "color_text": BoliviaPlateColor.CUERPO_CONSULAR_TEXT.value,
                "object": [
                    {
                        "type": "rectangle",
                        "fill_color": BoliviaPlateColor.CUERPO_CONSULAR_BG.value,
                        "border_color": None,
                        "border_width": 1,
                        "quantity": 1,
                        "start_x": 0,
                        "start_y": 0,
                        "width": 305,
                        "height": 152,
                        "coord": 0
                    },
                    # {
                    #     "type": "rectangle",
                    #     "fill_color": BoliviaPlateColor.CUERPO_CONSULAR_RECT.value,
                    #     "border_color": None,
                    #     "border_width": 1,
                    #     "quantity": 1,
                    #     "start_x": 4,
                    #     "start_y": 4,
                    #     "width": 397,
                    #     "height": 33,
                    #     "coord": 0
                    # },
                    {
                        "type": "format",
                        "random": 1,
                        "color_bg": BoliviaPlateColor.TRANSPARENT_BG.value,
                        "color_text": BoliviaPlateColor.CUERPO_CONSULAR_TEXT.value,
                        "start_x": 24,
                        "start_y": 56,
                        "width": 266,
                        "height": 80,
                        "coord": 0,
                        "font": "TRAFFIC2_0.ttf",
                        "obj": [
                            [{'type': 2, 'name': '12-CC-34'},
                             {'type': 3, 'obj': [{'ox': 0, 'oy': 0, 'w': 32, 'h': 74},
                                                 {'ox': 7, 'oy': 0, 'w': 32, 'h': 74},
                                                 {'ox': 100, 'oy': 94, 'w': 12, 'h': 6, 'r': False},
                                                 {'ox': 116, 'oy': 56, 'w': 32, 'h': 74, 'r': False},
                                                 {'ox': 7, 'oy': 0, 'w': 32, 'h': 74},
                                                 {'ox': 192, 'oy': 94, 'w': 12, 'h': 6, 'r': False},
                                                 {'ox': 208, 'oy': 56, 'w': 32, 'h': 74, 'r': False},
                                                 {'ox': 7, 'oy': 0, 'w': 32, 'h': 74}]},
                             {'type': 5, 'sl': {'I', '1'}},
                             {'type': 1, 'r': 1, 'min': 0, 'max': 99, 'zfil': 2},
                             {'type': 0, 'r': 0, 'text_obj': '-'},
                             {'type': 0, 'r': 1, 'rnd_obj': ['CC']},
                             {'type': 0, 'r': 0, 'text_obj': '-'},
                             {'type': 1, 'r': 1, 'min': 0, 'max': 99, 'zfil': 2},
                             ]
                        ]
                    },
                    {
                        "type": "rectangle_rounded",
                        "fill_color": None,
                        "border_color": BoliviaPlateColor.CUERPO_CONSULAR_TEXT.value,
                        "border_width": 4,
                        "border_radius": 10,
                        "quantity": 1,
                        "start_x": 0,
                        "start_y": 0,
                        "width": 305,
                        "height": 152,
                        "coord": 0
                    },
                    {
                        "type": "image",
                        "image": "img/Bolivia/Bandera_de_Bolivia.png",
                        "random": 0,
                        "letters": None,
                        "quantity": 1,
                        "start_x": 15,
                        "start_y": 21,
                        "width": 40,
                        "height": 25,
                        "coord": 0
                    },
                    {
                        "type": "rectangle",
                        "fill_color": None,
                        "border_color": BoliviaPlateColor.FLAG_RECT.value,
                        "border_width": 1,
                        "quantity": 1,
                        "start_x": 15,
                        "start_y": 21,
                        "width": 40,
                        "height": 25,
                        "coord": 0
                    },
                    {
                        "type": "text",
                        "random": 0,
                        "letters": u"B O L I V I A",
                        "color_bg": BoliviaPlateColor.TRANSPARENT_BG.value,
                        "color_text": BoliviaPlateColor.CUERPO_CONSULAR_TEXT.value,
                        "by_letter": 0,
                        "quantity": 0,
                        "start_x": 81,
                        "start_y": 22,
                        "width": 142,
                        "height": 20,
                        "offset_x": 10,
                        "coord": 0,
                        "font": "ARIALN.TTF"
                    },
                ]
            },
            {
                "name": BoliviaPlateType.CUERPO_DIPLOMATICO.value,
                "width": 305,
                "height": 152,
                "color_bg": BoliviaPlateColor.CUERPO_DIPLOMATICO_BG.value,
                "color_text": BoliviaPlateColor.CUERPO_DIPLOMATICO_TEXT.value,
                "object": [
                    {
                        "type": "rectangle",
                        "fill_color": BoliviaPlateColor.CUERPO_DIPLOMATICO_BG.value,
                        "border_color": None,
                        "border_width": 1,
                        "quantity": 1,
                        "start_x": 0,
                        "start_y": 0,
                        "width": 305,
                        "height": 152,
                        "coord": 0
                    },
                    # {
                    #     "type": "rectangle",
                    #     "fill_color": BoliviaPlateColor.CUERPO_CONSULAR_RECT.value,
                    #     "border_color": None,
                    #     "border_width": 1,
                    #     "quantity": 1,
                    #     "start_x": 4,
                    #     "start_y": 4,
                    #     "width": 397,
                    #     "height": 33,
                    #     "coord": 0
                    # },
                    {
                        "type": "format",
                        "random": 1,
                        "color_bg": BoliviaPlateColor.TRANSPARENT_BG.value,
                        "color_text": BoliviaPlateColor.CUERPO_DIPLOMATICO_TEXT.value,
                        "start_x": 24,
                        "start_y": 56,
                        "width": 266,
                        "height": 80,
                        "coord": 0,
                        "font": "TRAFFIC2_0.ttf",
                        "obj": [
                            [{'type': 2, 'name': '12-CC-34'},
                             {'type': 3, 'obj': [{'ox': 0, 'oy': 0, 'w': 32, 'h': 74},
                                                 {'ox': 7, 'oy': 0, 'w': 32, 'h': 74},
                                                 {'ox': 100, 'oy': 94, 'w': 12, 'h': 6, 'r': False},
                                                 {'ox': 116, 'oy': 56, 'w': 32, 'h': 74, 'r': False},
                                                 {'ox': 7, 'oy': 0, 'w': 32, 'h': 74},
                                                 {'ox': 192, 'oy': 94, 'w': 12, 'h': 6, 'r': False},
                                                 {'ox': 208, 'oy': 56, 'w': 32, 'h': 74, 'r': False},
                                                 {'ox': 7, 'oy': 0, 'w': 32, 'h': 74}]},
                             {'type': 5, 'sl': {'I', '1'}},
                             {'type': 1, 'r': 1, 'min': 0, 'max': 99, 'zfil': 2},
                             {'type': 0, 'r': 0, 'text_obj': '-'},
                             {'type': 0, 'r': 1, 'rnd_obj': ['CD']},
                             {'type': 0, 'r': 0, 'text_obj': '-'},
                             {'type': 1, 'r': 1, 'min': 0, 'max': 99, 'zfil': 2},
                             ]
                        ]
                    },
                    {
                        "type": "rectangle_rounded",
                        "fill_color": None,
                        "border_color": BoliviaPlateColor.CUERPO_DIPLOMATICO_TEXT.value,
                        "border_width": 4,
                        "border_radius": 10,
                        "quantity": 1,
                        "start_x": 0,
                        "start_y": 0,
                        "width": 305,
                        "height": 152,
                        "coord": 0
                    },
                    {
                        "type": "image",
                        "image": "img/Bolivia/Bandera_de_Bolivia.png",
                        "random": 0,
                        "letters": None,
                        "quantity": 1,
                        "start_x": 15,
                        "start_y": 21,
                        "width": 40,
                        "height": 25,
                        "coord": 0
                    },
                    {
                        "type": "rectangle",
                        "fill_color": None,
                        "border_color": BoliviaPlateColor.FLAG_RECT.value,
                        "border_width": 1,
                        "quantity": 1,
                        "start_x": 15,
                        "start_y": 21,
                        "width": 40,
                        "height": 25,
                        "coord": 0
                    },
                    {
                        "type": "text",
                        "random": 0,
                        "letters": u"B O L I V I A",
                        "color_bg": BoliviaPlateColor.TRANSPARENT_BG.value,
                        "color_text": BoliviaPlateColor.CUERPO_DIPLOMATICO_TEXT.value,
                        "by_letter": 0,
                        "quantity": 0,
                        "start_x": 81,
                        "start_y": 22,
                        "width": 142,
                        "height": 20,
                        "offset_x": 10,
                        "coord": 0,
                        "font": "ARIALN.TTF"
                    },
                ]
            },
            {
                "name": BoliviaPlateType.MISSION_INTERNACIONAL.value,
                "width": 305,
                "height": 152,
                "color_bg": BoliviaPlateColor.MISSION_INTERNACIONAL_BG.value,
                "color_text": BoliviaPlateColor.MISSION_INTERNACIONAL_TEXT.value,
                "object": [
                    {
                        "type": "rectangle",
                        "fill_color": BoliviaPlateColor.MISSION_INTERNACIONAL_BG.value,
                        "border_color": None,
                        "border_width": 1,
                        "quantity": 1,
                        "start_x": 0,
                        "start_y": 0,
                        "width": 305,
                        "height": 152,
                        "coord": 0
                    },
                    # {
                    #     "type": "rectangle",
                    #     "fill_color": BoliviaPlateColor.CUERPO_CONSULAR_RECT.value,
                    #     "border_color": None,
                    #     "border_width": 1,
                    #     "quantity": 1,
                    #     "start_x": 4,
                    #     "start_y": 4,
                    #     "width": 397,
                    #     "height": 33,
                    #     "coord": 0
                    # },
                    {
                        "type": "format",
                        "random": 1,
                        "color_bg": BoliviaPlateColor.TRANSPARENT_BG.value,
                        "color_text": BoliviaPlateColor.MISSION_INTERNACIONAL_TEXT.value,
                        "start_x": 24,
                        "start_y": 56,
                        "width": 266,
                        "height": 80,
                        "coord": 0,
                        "font": "TRAFFIC2_0.ttf",
                        "obj": [
                            [{'type': 2, 'name': '12-CC-34'},
                             {'type': 3, 'obj': [{'ox': 0, 'oy': 0, 'w': 32, 'h': 74},
                                                 {'ox': 7, 'oy': 0, 'w': 32, 'h': 74},
                                                 {'ox': 100, 'oy': 94, 'w': 12, 'h': 6, 'r': False},
                                                 {'ox': 116, 'oy': 56, 'w': 32, 'h': 74, 'r': False},
                                                 {'ox': 7, 'oy': 0, 'w': 32, 'h': 74},
                                                 {'ox': 192, 'oy': 94, 'w': 12, 'h': 6, 'r': False},
                                                 {'ox': 208, 'oy': 56, 'w': 32, 'h': 74, 'r': False},
                                                 {'ox': 7, 'oy': 0, 'w': 32, 'h': 74}]},
                             {'type': 5, 'sl': {'I', '1'}},
                             {'type': 1, 'r': 1, 'min': 0, 'max': 99, 'zfil': 2},
                             {'type': 0, 'r': 0, 'text_obj': '-'},
                             {'type': 0, 'r': 1, 'rnd_obj': ['MI']},
                             {'type': 0, 'r': 0, 'text_obj': '-'},
                             {'type': 1, 'r': 1, 'min': 0, 'max': 99, 'zfil': 2},
                             ]
                        ]
                    },
                    {
                        "type": "rectangle_rounded",
                        "fill_color": None,
                        "border_color": BoliviaPlateColor.MISSION_INTERNACIONAL_TEXT.value,
                        "border_width": 4,
                        "border_radius": 10,
                        "quantity": 1,
                        "start_x": 0,
                        "start_y": 0,
                        "width": 305,
                        "height": 152,
                        "coord": 0
                    },
                    {
                        "type": "image",
                        "image": "img/Bolivia/Bandera_de_Bolivia.png",
                        "random": 0,
                        "letters": None,
                        "quantity": 1,
                        "start_x": 15,
                        "start_y": 21,
                        "width": 40,
                        "height": 25,
                        "coord": 0
                    },
                    {
                        "type": "rectangle",
                        "fill_color": None,
                        "border_color": BoliviaPlateColor.FLAG_RECT.value,
                        "border_width": 1,
                        "quantity": 1,
                        "start_x": 15,
                        "start_y": 21,
                        "width": 40,
                        "height": 25,
                        "coord": 0
                    },
                    {
                        "type": "text",
                        "random": 0,
                        "letters": u"B O L I V I A",
                        "color_bg": BoliviaPlateColor.TRANSPARENT_BG.value,
                        "color_text": BoliviaPlateColor.MISSION_INTERNACIONAL_TEXT.value,
                        "by_letter": 0,
                        "quantity": 0,
                        "start_x": 81,
                        "start_y": 22,
                        "width": 142,
                        "height": 20,
                        "offset_x": 10,
                        "coord": 0,
                        "font": "ARIALN.TTF"
                    },
                ]
            },
            {
                "name": BoliviaPlateType.ORGANIZACION_INTERNACIONAL.value,
                "width": 305,
                "height": 152,
                "color_bg": BoliviaPlateColor.ORGANIZACION_INTERNACIONAL_BG.value,
                "color_text": BoliviaPlateColor.ORGANIZACION_INTERNACIONAL_TEXT.value,
                "object": [
                    {
                        "type": "rectangle",
                        "fill_color": BoliviaPlateColor.ORGANIZACION_INTERNACIONAL_BG.value,
                        "border_color": None,
                        "border_width": 1,
                        "quantity": 1,
                        "start_x": 0,
                        "start_y": 0,
                        "width": 305,
                        "height": 152,
                        "coord": 0
                    },
                    # {
                    #     "type": "rectangle",
                    #     "fill_color": BoliviaPlateColor.CUERPO_CONSULAR_RECT.value,
                    #     "border_color": None,
                    #     "border_width": 1,
                    #     "quantity": 1,
                    #     "start_x": 4,
                    #     "start_y": 4,
                    #     "width": 397,
                    #     "height": 33,
                    #     "coord": 0
                    # },
                    {
                        "type": "format",
                        "random": 1,
                        "color_bg": BoliviaPlateColor.TRANSPARENT_BG.value,
                        "color_text": BoliviaPlateColor.ORGANIZACION_INTERNACIONAL_TEXT.value,
                        "start_x": 24,
                        "start_y": 56,
                        "width": 266,
                        "height": 80,
                        "coord": 0,
                        "font": "TRAFFIC2_0.ttf",
                        "obj": [
                            [{'type': 2, 'name': '12-CC-34'},
                             {'type': 3, 'obj': [{'ox': 0, 'oy': 0, 'w': 32, 'h': 74},
                                                 {'ox': 7, 'oy': 0, 'w': 32, 'h': 74},
                                                 {'ox': 100, 'oy': 94, 'w': 12, 'h': 6, 'r': False},
                                                 {'ox': 116, 'oy': 56, 'w': 32, 'h': 74, 'r': False},
                                                 {'ox': 7, 'oy': 0, 'w': 32, 'h': 74},
                                                 {'ox': 192, 'oy': 94, 'w': 12, 'h': 6, 'r': False},
                                                 {'ox': 208, 'oy': 56, 'w': 32, 'h': 74, 'r': False},
                                                 {'ox': 7, 'oy': 0, 'w': 32, 'h': 74}]},
                             {'type': 5, 'sl': {'I', '1'}},
                             {'type': 1, 'r': 1, 'min': 0, 'max': 99, 'zfil': 2},
                             {'type': 0, 'r': 0, 'text_obj': '-'},
                             {'type': 0, 'r': 1, 'rnd_obj': ['OI']},
                             {'type': 0, 'r': 0, 'text_obj': '-'},
                             {'type': 1, 'r': 1, 'min': 0, 'max': 99, 'zfil': 2},
                             ]
                        ]
                    },
                    {
                        "type": "rectangle_rounded",
                        "fill_color": None,
                        "border_color": BoliviaPlateColor.ORGANIZACION_INTERNACIONAL_TEXT.value,
                        "border_width": 4,
                        "border_radius": 10,
                        "quantity": 1,
                        "start_x": 0,
                        "start_y": 0,
                        "width": 305,
                        "height": 152,
                        "coord": 0
                    },
                    {
                        "type": "image",
                        "image": "img/Bolivia/Bandera_de_Bolivia.png",
                        "random": 0,
                        "letters": None,
                        "quantity": 1,
                        "start_x": 15,
                        "start_y": 21,
                        "width": 40,
                        "height": 25,
                        "coord": 0
                    },
                    {
                        "type": "rectangle",
                        "fill_color": None,
                        "border_color": BoliviaPlateColor.FLAG_RECT.value,
                        "border_width": 1,
                        "quantity": 1,
                        "start_x": 15,
                        "start_y": 21,
                        "width": 40,
                        "height": 25,
                        "coord": 0
                    },
                    {
                        "type": "text",
                        "random": 0,
                        "letters": u"B O L I V I A",
                        "color_bg": BoliviaPlateColor.TRANSPARENT_BG.value,
                        "color_text": BoliviaPlateColor.ORGANIZACION_INTERNACIONAL_TEXT.value,
                        "by_letter": 0,
                        "quantity": 0,
                        "start_x": 81,
                        "start_y": 22,
                        "width": 142,
                        "height": 20,
                        "offset_x": 10,
                        "coord": 0,
                        "font": "ARIALN.TTF"
                    },
                ]
            },
        ]
    }
