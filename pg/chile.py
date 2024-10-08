from enum import Enum

chile_capital = {'Arica', 'Iquique', 'Antofagasta', 'Copiapó', 'La Serena', 'Valparaíso', 'Santiago', 'Rancagua',
                 'Talca', 'Chillán', 'Concepción', 'Temuco', 'Valdivia', 'Puerto Montt', 'Coyhaique', 'Punta Arenas'}


class ChilePlateType(Enum):
    VEHICULO_PARTICULAR = 'Vehiculo particular'
    TAXI_BASICO = 'Taxi básico'
    TAXI_COLECTIVO = 'Taxi colectivo'
    RADIOTAXI = 'Radiotaxi vehiculos de turismo'
    BUSES_DE_TRANSANTIAGO = 'Buses de Transantiago'
    VEHICULOS_ZONA_FRANCA = 'Vehículos adquiridos en Zona Franca'
    REMOLQUES_BRUTO_MAYOR = 'Remolques de peso bruto mayor a 3860kg'
    REMOLQUES_BRUTO_MENOR = 'Remolques de peso bruto menor a 3860kg'
    CUERPO_DIPLOMATICO = 'Cuerpo diplomático'
    VEHICULOS_DE_CARABINEROS = 'Vehiculos de carabineros'
    INSCRIPSION_PROVISORIA = 'Inscripsion provisoria'
    FUERZAS_ARMADAS = 'Fuerzas Armadas'
    BOMBEROS = 'Bomberos'


class ChilePlateColor(Enum):
    SERIAL_NUMBER_TEXT = (180, 180, 180)
    TRANSPARENT_BG = (255, 255, 255, 0)
    VEHICULO_PARTICULAR_BG = (255, 255, 255)
    VEHICULO_PARTICULAR_TEXT = (0, 0, 0)
    TAXI_BASICO_BG = (207, 100, 25)
    TAXI_BASICO_TEXT = (0, 0, 0)
    TAXI_COLECTIVO_BG = (241, 167, 36)
    TAXI_COLECTIVO_TEXT = (0, 0, 0)
    RADIOTAXI_BG = (207, 101, 29)
    RADIOTAXI_TEXT = (255, 255, 255)
    BUSES_DE_TRANSANTIAGO_BG = (255, 255, 255)
    BUSES_DE_TRANSANTIAGO_TEXT = (22, 149, 40)
    VEHICULOS_ZONA_FRANCA_BG = (210, 19, 19)
    VEHICULOS_ZONA_FRANCA_TEXT = (255, 255, 255)
    REMOLQUES_BRUTO_MAYOR_BG = (255, 255, 255)
    REMOLQUES_BRUTO_MAYOR_TEXT = (0, 0, 0)
    REMOLQUES_BRUTO_MENOR_BG = (255, 255, 255)
    REMOLQUES_BRUTO_MENOR_TEXT = (207, 36, 36)
    CUERPO_DIPLOMATICO_BG = (95, 187, 218)
    CUERPO_DIPLOMATICO_TEXT = (255, 255, 255)
    VEHICULOS_DE_CARABINEROS_BG = (0, 0, 0)
    VEHICULOS_DE_CARABINEROS_TEXT = (255, 255, 255)
    INSCRIPSION_PROVISORIA_BG = (207, 100, 25)
    INSCRIPSION_PROVISORIA_TEXT = (0, 0, 0)
    FUERZAS_ARMADAS_BG = (100, 116, 100)
    FUERZAS_ARMADAS_TEXT = (255, 255, 255)
    BOMBEROS_BG = (255, 0, 0)
    BOMBEROS_TEXT = (0, 0, 0)


chile_abreviatura_nacional = {'Arica': 'AP',
                              'Iquique': 'TA',
                              'Antofagasta': 'AN',
                              'Copiapó': 'AT',
                              'La Serena': 'CO',
                              'Valparaíso': 'VA',
                              'Santiago': 'RM',
                              'Rancagua': 'LI',
                              'Talca': 'ML',
                              'Chillán': 'NB',
                              'Concepción': 'BI',
                              'Temuco': 'AR',
                              'Valdivia': 'LR',
                              'Puerto Montt': 'LL',
                              'Coyhaique': 'AI',
                              'Punta Arenas': 'MA'}

chile_capital_selected = None


def plate_chile():
    return {
        "country": "Chile",
        "rfy": "2007",  # registration format year
        "font": "EuroPlate.ttf",
        "plates": [
            {
                "name": ChilePlateType.VEHICULO_PARTICULAR.value,
                "width": 360,
                "height": 130,
                "color_bg": ChilePlateColor.VEHICULO_PARTICULAR_BG.value,
                "color_text": ChilePlateColor.VEHICULO_PARTICULAR_TEXT.value,
                "object": [
                    {
                        "type": "rectangle",
                        "fill_color": ChilePlateColor.VEHICULO_PARTICULAR_BG.value,
                        "border_color": None,
                        "border_width": 1,
                        "quantity": 1,
                        "start_x": 0,
                        "start_y": 0,
                        "width": 360,
                        "height": 130,
                        "coord": 0
                    },
                    {
                        "type": "format",
                        "random": 1,
                        "color_bg": ChilePlateColor.TRANSPARENT_BG.value,
                        "color_text": ChilePlateColor.VEHICULO_PARTICULAR_TEXT.value,
                        "start_x": 14,
                        "start_y": 14,
                        "width": 266,
                        "height": 80,
                        "coord": 0,
                        "obj": [
                            [{'type': 2, 'name': 'AB-AB-12'},
                             {'type': 3, 'obj': [{'ox': 0, 'oy': 0, 'w': 44, 'h': 72},
                                                 {'ox': 6, 'oy': 0, 'w': 44, 'h': 72},
                                                 {'ox': 136, 'oy': 14, 'w': 44, 'h': 72, 'r': False},
                                                 {'ox': 6, 'oy': 0, 'w': 44, 'h': 72},
                                                 {'ox': 260, 'oy': 14, 'w': 40, 'h': 72, 'r': False},
                                                 {'ox': 6, 'oy': 0, 'w': 40, 'h': 72}]},
                             {'type': 5, 'sl': {}},
                             {'type': 0, 'r': 1, 'rnd_obj': ['B', 'C', 'D', 'F', 'G', 'H', 'J', 'K', 'L', 'P', 'R',
                                                             'S', 'T', 'V', 'W', 'X', 'Y', 'Z']},
                             {'type': 0, 'r': 1, 'rnd_obj': ['B', 'C', 'D', 'F', 'G', 'H', 'J', 'K', 'L', 'P', 'R',
                                                             'S', 'T', 'V', 'W', 'X', 'Y', 'Z']},
                             {'type': 0, 'r': 1, 'rnd_obj': ['B', 'C', 'D', 'F', 'G', 'H', 'J', 'K', 'L', 'P', 'R',
                                                             'S', 'T', 'V', 'W', 'X', 'Y', 'Z']},
                             {'type': 0, 'r': 1, 'rnd_obj': ['B', 'C', 'D', 'F', 'G', 'H', 'J', 'K', 'L', 'P', 'R',
                                                             'S', 'T', 'V', 'W', 'X', 'Y', 'Z']},
                             {'type': 1, 'r': 1, 'min': 10, 'max': 99, 'zfil': 2}]
                        ]
                    },
                    {
                        "type": "rectangle_rounded",
                        "fill_color": None,
                        "border_color": ChilePlateColor.VEHICULO_PARTICULAR_TEXT.value,
                        "border_width": 4,
                        "border_radius": 10,
                        "quantity": 1,
                        "start_x": 2,
                        "start_y": 2,
                        "width": 356,
                        "height": 126,
                        "coord": 0
                    },
                    {
                        "type": "text",
                        "random": 0,
                        "letters": "C  H  I  L  E",
                        "color_bg": ChilePlateColor.VEHICULO_PARTICULAR_BG.value,
                        "color_text": ChilePlateColor.VEHICULO_PARTICULAR_TEXT.value,
                        "by_letter": 0,
                        "quantity": 0,
                        "start_x": 124,
                        "start_y": 102,
                        "width": 112,
                        "height": 16,
                        "offset_x": 10,
                        "coord": 0,
                        "font": "ARIALN.TTF"
                    },
                    {
                        "type": "image",
                        "image": "img/Chile/chile_black.png",
                        "random": 0,
                        "letters": None,
                        "quantity": 1,
                        "start_x": 234,
                        "start_y": 36,
                        "width": 20,
                        "height": 21,
                        "coord": 0
                    },
                    {
                        "type": "image",
                        "image": "img/Chile/circle_black.png",
                        "random": 0,
                        "letters": None,
                        "quantity": 1,
                        "start_x": 116,
                        "start_y": 42,
                        "width": 9,
                        "height": 9,
                        "coord": 0
                    },

                ]
            },
            {
                "name": ChilePlateType.TAXI_BASICO.value,
                "width": 360,
                "height": 130,
                "color_bg": ChilePlateColor.TAXI_BASICO_BG.value,
                "color_text": ChilePlateColor.TAXI_BASICO_TEXT.value,
                "object": [
                    {
                        "type": "rectangle",
                        "fill_color": ChilePlateColor.TAXI_BASICO_BG.value,
                        "border_color": None,
                        "border_width": 1,
                        "quantity": 1,
                        "start_x": 0,
                        "start_y": 0,
                        "width": 360,
                        "height": 130,
                        "coord": 0
                    },
                    {
                        "type": "format",
                        "random": 1,
                        "color_bg": ChilePlateColor.TRANSPARENT_BG.value,
                        "color_text": ChilePlateColor.TAXI_BASICO_TEXT.value,
                        "start_x": 14,
                        "start_y": 14,
                        "width": 266,
                        "height": 80,
                        "coord": 0,
                        "obj": [
                            [{'type': 2, 'name': 'AB-AB-12'},
                             {'type': 3, 'obj': [{'ox': 0, 'oy': 0, 'w': 44, 'h': 72},
                                                 {'ox': 6, 'oy': 0, 'w': 44, 'h': 72},
                                                 {'ox': 136, 'oy': 14, 'w': 44, 'h': 72, 'r': False},
                                                 {'ox': 6, 'oy': 0, 'w': 44, 'h': 72},
                                                 {'ox': 260, 'oy': 14, 'w': 40, 'h': 72, 'r': False},
                                                 {'ox': 6, 'oy': 0, 'w': 40, 'h': 72}]},
                             {'type': 5, 'sl': {}},
                             {'type': 0, 'r': 1, 'rnd_obj': ['B', 'C', 'D', 'F', 'G', 'H', 'J', 'K', 'L', 'P', 'R',
                                                             'S', 'T', 'V', 'W', 'X', 'Y', 'Z']},
                             {'type': 0, 'r': 1, 'rnd_obj': ['B', 'C', 'D', 'F', 'G', 'H', 'J', 'K', 'L', 'P', 'R',
                                                             'S', 'T', 'V', 'W', 'X', 'Y', 'Z']},
                             {'type': 0, 'r': 1, 'rnd_obj': ['B', 'C', 'D', 'F', 'G', 'H', 'J', 'K', 'L', 'P', 'R',
                                                             'S', 'T', 'V', 'W', 'X', 'Y', 'Z']},
                             {'type': 0, 'r': 1, 'rnd_obj': ['B', 'C', 'D', 'F', 'G', 'H', 'J', 'K', 'L', 'P', 'R',
                                                             'S', 'T', 'V', 'W', 'X', 'Y', 'Z']},
                             {'type': 1, 'r': 1, 'min': 10, 'max': 99, 'zfil': 2}]
                        ]
                    },
                    {
                        "type": "rectangle_rounded",
                        "fill_color": None,
                        "border_color": ChilePlateColor.TAXI_BASICO_TEXT.value,
                        "border_width": 4,
                        "border_radius": 10,
                        "quantity": 1,
                        "start_x": 2,
                        "start_y": 2,
                        "width": 356,
                        "height": 126,
                        "coord": 0
                    },
                    {
                        "type": "text",
                        "random": 0,
                        "letters": "C  H  I  L  E",
                        "color_bg": ChilePlateColor.TAXI_BASICO_BG.value,
                        "color_text": ChilePlateColor.TAXI_BASICO_TEXT.value,
                        "by_letter": 0,
                        "quantity": 0,
                        "start_x": 124,
                        "start_y": 102,
                        "width": 112,
                        "height": 16,
                        "offset_x": 10,
                        "coord": 0,
                        "font": "ARIALN.TTF"
                    },
                    {
                        "type": "image",
                        "image": "img/Chile/chile_black.png",
                        "random": 0,
                        "letters": None,
                        "quantity": 1,
                        "start_x": 234,
                        "start_y": 36,
                        "width": 20,
                        "height": 21,
                        "coord": 0
                    },
                    {
                        "type": "image",
                        "image": "img/Chile/circle_black.png",
                        "random": 0,
                        "letters": None,
                        "quantity": 1,
                        "start_x": 116,
                        "start_y": 42,
                        "width": 9,
                        "height": 9,
                        "coord": 0
                    },

                ]
            },
            {
                "name": ChilePlateType.TAXI_COLECTIVO.value,
                "width": 360,
                "height": 130,
                "color_bg": ChilePlateColor.TAXI_COLECTIVO_BG.value,
                "color_text": ChilePlateColor.TAXI_COLECTIVO_TEXT.value,
                "object": [
                    {
                        "type": "rectangle",
                        "fill_color": ChilePlateColor.TAXI_COLECTIVO_BG.value,
                        "border_color": None,
                        "border_width": 1,
                        "quantity": 1,
                        "start_x": 0,
                        "start_y": 0,
                        "width": 360,
                        "height": 130,
                        "coord": 0
                    },
                    {
                        "type": "format",
                        "random": 1,
                        "color_bg": ChilePlateColor.TRANSPARENT_BG.value,
                        "color_text": ChilePlateColor.TAXI_COLECTIVO_TEXT.value,
                        "start_x": 14,
                        "start_y": 14,
                        "width": 266,
                        "height": 80,
                        "coord": 0,
                        "obj": [
                            [{'type': 2, 'name': 'AB-AB-12'},
                             {'type': 3, 'obj': [{'ox': 0, 'oy': 0, 'w': 44, 'h': 72},
                                                 {'ox': 6, 'oy': 0, 'w': 44, 'h': 72},
                                                 {'ox': 136, 'oy': 14, 'w': 44, 'h': 72, 'r': False},
                                                 {'ox': 6, 'oy': 0, 'w': 44, 'h': 72},
                                                 {'ox': 260, 'oy': 14, 'w': 40, 'h': 72, 'r': False},
                                                 {'ox': 6, 'oy': 0, 'w': 40, 'h': 72}]},
                             {'type': 5, 'sl': {}},
                             {'type': 0, 'r': 1, 'rnd_obj': ['B', 'C', 'D', 'F', 'G', 'H', 'J', 'K', 'L', 'P', 'R',
                                                             'S', 'T', 'V', 'W', 'X', 'Y', 'Z']},
                             {'type': 0, 'r': 1, 'rnd_obj': ['B', 'C', 'D', 'F', 'G', 'H', 'J', 'K', 'L', 'P', 'R',
                                                             'S', 'T', 'V', 'W', 'X', 'Y', 'Z']},
                             {'type': 0, 'r': 1, 'rnd_obj': ['B', 'C', 'D', 'F', 'G', 'H', 'J', 'K', 'L', 'P', 'R',
                                                             'S', 'T', 'V', 'W', 'X', 'Y', 'Z']},
                             {'type': 0, 'r': 1, 'rnd_obj': ['B', 'C', 'D', 'F', 'G', 'H', 'J', 'K', 'L', 'P', 'R',
                                                             'S', 'T', 'V', 'W', 'X', 'Y', 'Z']},
                             {'type': 1, 'r': 1, 'min': 10, 'max': 99, 'zfil': 2}]
                        ]
                    },
                    {
                        "type": "rectangle_rounded",
                        "fill_color": None,
                        "border_color": ChilePlateColor.TAXI_COLECTIVO_TEXT.value,
                        "border_width": 4,
                        "border_radius": 10,
                        "quantity": 1,
                        "start_x": 2,
                        "start_y": 2,
                        "width": 356,
                        "height": 126,
                        "coord": 0
                    },
                    {
                        "type": "text",
                        "random": 0,
                        "letters": "C  H  I  L  E",
                        "color_bg": ChilePlateColor.TAXI_COLECTIVO_BG.value,
                        "color_text": ChilePlateColor.TAXI_COLECTIVO_TEXT.value,
                        "by_letter": 0,
                        "quantity": 0,
                        "start_x": 124,
                        "start_y": 102,
                        "width": 112,
                        "height": 16,
                        "offset_x": 10,
                        "coord": 0,
                        "font": "ARIALN.TTF"
                    },
                    {
                        "type": "image",
                        "image": "img/Chile/chile_black.png",
                        "random": 0,
                        "letters": None,
                        "quantity": 1,
                        "start_x": 234,
                        "start_y": 36,
                        "width": 20,
                        "height": 21,
                        "coord": 0
                    },
                    {
                        "type": "image",
                        "image": "img/Chile/circle_black.png",
                        "random": 0,
                        "letters": None,
                        "quantity": 1,
                        "start_x": 116,
                        "start_y": 42,
                        "width": 9,
                        "height": 9,
                        "coord": 0
                    },

                ]
            },
            {
                "name": ChilePlateType.RADIOTAXI.value,
                "width": 360,
                "height": 130,
                "color_bg": ChilePlateColor.RADIOTAXI_BG.value,
                "color_text": ChilePlateColor.RADIOTAXI_TEXT.value,
                "object": [
                    {
                        "type": "rectangle",
                        "fill_color": ChilePlateColor.RADIOTAXI_BG.value,
                        "border_color": None,
                        "border_width": 1,
                        "quantity": 1,
                        "start_x": 0,
                        "start_y": 0,
                        "width": 360,
                        "height": 130,
                        "coord": 0
                    },
                    {
                        "type": "format",
                        "random": 1,
                        "color_bg": ChilePlateColor.TRANSPARENT_BG.value,
                        "color_text": ChilePlateColor.RADIOTAXI_TEXT.value,
                        "start_x": 14,
                        "start_y": 14,
                        "width": 266,
                        "height": 80,
                        "coord": 0,
                        "obj": [
                            [{'type': 2, 'name': 'AB-AB-12'},
                             {'type': 3, 'obj': [{'ox': 0, 'oy': 0, 'w': 44, 'h': 72},
                                                 {'ox': 6, 'oy': 0, 'w': 44, 'h': 72},
                                                 {'ox': 136, 'oy': 14, 'w': 44, 'h': 72, 'r': False},
                                                 {'ox': 6, 'oy': 0, 'w': 44, 'h': 72},
                                                 {'ox': 260, 'oy': 14, 'w': 40, 'h': 72, 'r': False},
                                                 {'ox': 6, 'oy': 0, 'w': 40, 'h': 72}]},
                             {'type': 5, 'sl': {}},
                             {'type': 0, 'r': 1, 'rnd_obj': ['B', 'C', 'D', 'F', 'G', 'H', 'J', 'K', 'L', 'P', 'R',
                                                             'S', 'T', 'V', 'W', 'X', 'Y', 'Z']},
                             {'type': 0, 'r': 1, 'rnd_obj': ['B', 'C', 'D', 'F', 'G', 'H', 'J', 'K', 'L', 'P', 'R',
                                                             'S', 'T', 'V', 'W', 'X', 'Y', 'Z']},
                             {'type': 0, 'r': 1, 'rnd_obj': ['B', 'C', 'D', 'F', 'G', 'H', 'J', 'K', 'L', 'P', 'R',
                                                             'S', 'T', 'V', 'W', 'X', 'Y', 'Z']},
                             {'type': 0, 'r': 1, 'rnd_obj': ['B', 'C', 'D', 'F', 'G', 'H', 'J', 'K', 'L', 'P', 'R',
                                                             'S', 'T', 'V', 'W', 'X', 'Y', 'Z']},
                             {'type': 1, 'r': 1, 'min': 10, 'max': 99, 'zfil': 2}]
                        ]
                    },
                    {
                        "type": "rectangle_rounded",
                        "fill_color": None,
                        "border_color": ChilePlateColor.RADIOTAXI_TEXT.value,
                        "border_width": 4,
                        "border_radius": 10,
                        "quantity": 1,
                        "start_x": 2,
                        "start_y": 2,
                        "width": 356,
                        "height": 126,
                        "coord": 0
                    },
                    {
                        "type": "text",
                        "random": 0,
                        "letters": "C  H  I  L  E",
                        "color_bg": ChilePlateColor.RADIOTAXI_BG.value,
                        "color_text": ChilePlateColor.RADIOTAXI_TEXT.value,
                        "by_letter": 0,
                        "quantity": 0,
                        "start_x": 124,
                        "start_y": 102,
                        "width": 112,
                        "height": 16,
                        "offset_x": 10,
                        "coord": 0,
                        "font": "ARIALN.TTF"
                    },
                    {
                        "type": "image",
                        "image": "img/Chile/chile_white.png",
                        "random": 0,
                        "letters": None,
                        "quantity": 1,
                        "start_x": 234,
                        "start_y": 36,
                        "width": 20,
                        "height": 21,
                        "coord": 0
                    },
                    {
                        "type": "image",
                        "image": "img/Chile/circle_white.png",
                        "random": 0,
                        "letters": None,
                        "quantity": 1,
                        "start_x": 116,
                        "start_y": 42,
                        "width": 9,
                        "height": 9,
                        "coord": 0
                    },

                ]
            },
            {
                "name": ChilePlateType.BUSES_DE_TRANSANTIAGO.value,
                "width": 360,
                "height": 130,
                "color_bg": ChilePlateColor.BUSES_DE_TRANSANTIAGO_BG.value,
                "color_text": ChilePlateColor.BUSES_DE_TRANSANTIAGO_TEXT.value,
                "object": [
                    {
                        "type": "rectangle",
                        "fill_color": ChilePlateColor.BUSES_DE_TRANSANTIAGO_BG.value,
                        "border_color": None,
                        "border_width": 1,
                        "quantity": 1,
                        "start_x": 0,
                        "start_y": 0,
                        "width": 360,
                        "height": 130,
                        "coord": 0
                    },
                    {
                        "type": "format",
                        "random": 1,
                        "color_bg": ChilePlateColor.BUSES_DE_TRANSANTIAGO_BG.value,
                        "color_text": ChilePlateColor.BUSES_DE_TRANSANTIAGO_TEXT.value,
                        "start_x": 14,
                        "start_y": 14,
                        "width": 266,
                        "height": 80,
                        "coord": 0,
                        "obj": [
                            [{'type': 2, 'name': 'AB-AB-12'},
                             {'type': 3, 'obj': [{'ox': 0, 'oy': 0, 'w': 44, 'h': 72},
                                                 {'ox': 6, 'oy': 0, 'w': 44, 'h': 72},
                                                 {'ox': 136, 'oy': 14, 'w': 44, 'h': 72, 'r': False},
                                                 {'ox': 6, 'oy': 0, 'w': 44, 'h': 72},
                                                 {'ox': 260, 'oy': 14, 'w': 40, 'h': 72, 'r': False},
                                                 {'ox': 6, 'oy': 0, 'w': 40, 'h': 72}]},
                             {'type': 5, 'sl': {}},
                             {'type': 0, 'r': 1, 'rnd_obj': ['B', 'C', 'D', 'F', 'G', 'H', 'J', 'K', 'L', 'P', 'R',
                                                             'S', 'T', 'V', 'W', 'X', 'Y', 'Z']},
                             {'type': 0, 'r': 1, 'rnd_obj': ['B', 'C', 'D', 'F', 'G', 'H', 'J', 'K', 'L', 'P', 'R',
                                                             'S', 'T', 'V', 'W', 'X', 'Y', 'Z']},
                             {'type': 0, 'r': 1, 'rnd_obj': ['B', 'C', 'D', 'F', 'G', 'H', 'J', 'K', 'L', 'P', 'R',
                                                             'S', 'T', 'V', 'W', 'X', 'Y', 'Z']},
                             {'type': 0, 'r': 1, 'rnd_obj': ['B', 'C', 'D', 'F', 'G', 'H', 'J', 'K', 'L', 'P', 'R',
                                                             'S', 'T', 'V', 'W', 'X', 'Y', 'Z']},
                             {'type': 1, 'r': 1, 'min': 10, 'max': 99, 'zfil': 2}]
                        ]
                    },
                    {
                        "type": "rectangle_rounded",
                        "fill_color": None,
                        "border_color": ChilePlateColor.BUSES_DE_TRANSANTIAGO_TEXT.value,
                        "border_width": 4,
                        "border_radius": 10,
                        "quantity": 1,
                        "start_x": 2,
                        "start_y": 2,
                        "width": 356,
                        "height": 126,
                        "coord": 0
                    },
                    {
                        "type": "text",
                        "random": 0,
                        "letters": "T R A N S A N T I A G O",
                        "color_bg": ChilePlateColor.BUSES_DE_TRANSANTIAGO_BG.value,
                        "color_text": ChilePlateColor.BUSES_DE_TRANSANTIAGO_TEXT.value,
                        "by_letter": 0,
                        "quantity": 0,
                        "start_x": 74,
                        "start_y": 102,
                        "width": 212,
                        "height": 16,
                        "offset_x": 10,
                        "coord": 0,
                        "font": "ARIALN.TTF"
                    },
                    {
                        "type": "image",
                        "image": "img/Chile/bus_green.png",
                        "random": 0,
                        "letters": None,
                        "quantity": 1,
                        "start_x": 234,
                        "start_y": 36,
                        "width": 18,
                        "height": 18,
                        "coord": 0
                    },
                    {
                        "type": "image",
                        "image": "img/Chile/circle_green.png",
                        "random": 0,
                        "letters": None,
                        "quantity": 1,
                        "start_x": 116,
                        "start_y": 42,
                        "width": 9,
                        "height": 9,
                        "coord": 0
                    },

                ]
            },
            {
                "name": ChilePlateType.VEHICULOS_ZONA_FRANCA.value,
                "width": 360,
                "height": 130,
                "color_bg": ChilePlateColor.VEHICULOS_ZONA_FRANCA_BG.value,
                "color_text": ChilePlateColor.VEHICULOS_ZONA_FRANCA_TEXT.value,
                "object": [
                    {
                        "type": "rectangle",
                        "fill_color": ChilePlateColor.VEHICULOS_ZONA_FRANCA_BG.value,
                        "border_color": None,
                        "border_width": 1,
                        "quantity": 1,
                        "start_x": 0,
                        "start_y": 0,
                        "width": 360,
                        "height": 130,
                        "coord": 0
                    },
                    {
                        "type": "format",
                        "random": 1,
                        "color_bg": ChilePlateColor.VEHICULOS_ZONA_FRANCA_BG.value,
                        "color_text": ChilePlateColor.VEHICULOS_ZONA_FRANCA_TEXT.value,
                        "start_x": 14,
                        "start_y": 14,
                        "width": 266,
                        "height": 80,
                        "coord": 0,
                        "obj": [
                            [{'type': 2, 'name': 'AB-AB-12'},
                             {'type': 3, 'obj': [{'ox': 0, 'oy': 0, 'w': 44, 'h': 72},
                                                 {'ox': 6, 'oy': 0, 'w': 44, 'h': 72},
                                                 {'ox': 136, 'oy': 14, 'w': 44, 'h': 72, 'r': False},
                                                 {'ox': 6, 'oy': 0, 'w': 44, 'h': 72},
                                                 {'ox': 260, 'oy': 14, 'w': 40, 'h': 72, 'r': False},
                                                 {'ox': 6, 'oy': 0, 'w': 40, 'h': 72}]},
                             {'type': 5, 'sl': {}},
                             {'type': 0, 'r': 1, 'rnd_obj': ['B', 'C', 'D', 'F', 'G', 'H', 'J', 'K', 'L', 'P', 'R',
                                                             'S', 'T', 'V', 'W', 'X', 'Y', 'Z']},
                             {'type': 0, 'r': 1, 'rnd_obj': ['B', 'C', 'D', 'F', 'G', 'H', 'J', 'K', 'L', 'P', 'R',
                                                             'S', 'T', 'V', 'W', 'X', 'Y', 'Z']},
                             {'type': 0, 'r': 1, 'rnd_obj': ['B', 'C', 'D', 'F', 'G', 'H', 'J', 'K', 'L', 'P', 'R',
                                                             'S', 'T', 'V', 'W', 'X', 'Y', 'Z']},
                             {'type': 0, 'r': 1, 'rnd_obj': ['B', 'C', 'D', 'F', 'G', 'H', 'J', 'K', 'L', 'P', 'R',
                                                             'S', 'T', 'V', 'W', 'X', 'Y', 'Z']},
                             {'type': 1, 'r': 1, 'min': 10, 'max': 99, 'zfil': 2}]
                        ]
                    },
                    {
                        "type": "rectangle_rounded",
                        "fill_color": None,
                        "border_color": ChilePlateColor.VEHICULOS_ZONA_FRANCA_TEXT.value,
                        "border_width": 4,
                        "border_radius": 10,
                        "quantity": 1,
                        "start_x": 2,
                        "start_y": 2,
                        "width": 356,
                        "height": 126,
                        "coord": 0
                    },
                    {
                        "type": "text",
                        "random": 0,
                        "letters": "C  H  I  L  E",
                        "color_bg": ChilePlateColor.VEHICULOS_ZONA_FRANCA_BG.value,
                        "color_text": ChilePlateColor.VEHICULOS_ZONA_FRANCA_TEXT.value,
                        "by_letter": 0,
                        "quantity": 0,
                        "start_x": 124,
                        "start_y": 102,
                        "width": 112,
                        "height": 16,
                        "offset_x": 10,
                        "coord": 0,
                        "font": "ARIALN.TTF"
                    },
                    {
                        "type": "image",
                        "image": "img/Chile/chile_white.png",
                        "random": 0,
                        "letters": None,
                        "quantity": 1,
                        "start_x": 234,
                        "start_y": 36,
                        "width": 20,
                        "height": 21,
                        "coord": 0
                    },
                    {
                        "type": "image",
                        "image": "img/Chile/circle_white.png",
                        "random": 0,
                        "letters": None,
                        "quantity": 1,
                        "start_x": 116,
                        "start_y": 42,
                        "width": 9,
                        "height": 9,
                        "coord": 0
                    },

                ]
            },
            {
                "name": ChilePlateType.REMOLQUES_BRUTO_MAYOR.value,
                "width": 360,
                "height": 130,
                "color_bg": ChilePlateColor.REMOLQUES_BRUTO_MAYOR_BG.value,
                "color_text": ChilePlateColor.REMOLQUES_BRUTO_MAYOR_TEXT.value,
                "object": [
                    {
                        "type": "rectangle",
                        "fill_color": ChilePlateColor.REMOLQUES_BRUTO_MAYOR_BG.value,
                        "border_color": None,
                        "border_width": 1,
                        "quantity": 1,
                        "start_x": 0,
                        "start_y": 0,
                        "width": 360,
                        "height": 130,
                        "coord": 0
                    },
                    {
                        "type": "format",
                        "random": 1,
                        "color_bg": ChilePlateColor.REMOLQUES_BRUTO_MAYOR_BG.value,
                        "color_text": ChilePlateColor.REMOLQUES_BRUTO_MAYOR_TEXT.value,
                        "start_x": 14,
                        "start_y": 14,
                        "width": 266,
                        "height": 80,
                        "coord": 0,
                        "obj": [
                            [{'type': 2, 'name': 'AB-AB-12'},
                             {'type': 3, 'obj': [{'ox': 0, 'oy': 0, 'w': 44, 'h': 72},
                                                 {'ox': 6, 'oy': 0, 'w': 44, 'h': 72},
                                                 {'ox': 136, 'oy': 14, 'w': 44, 'h': 72, 'r': False},
                                                 {'ox': 6, 'oy': 0, 'w': 44, 'h': 72},
                                                 {'ox': 260, 'oy': 14, 'w': 40, 'h': 72, 'r': False},
                                                 {'ox': 6, 'oy': 0, 'w': 40, 'h': 72}]},
                             {'type': 5, 'sl': {}},
                             {'type': 0, 'r': 1, 'rnd_obj': ['B', 'C', 'D', 'F', 'G', 'H', 'J', 'K', 'L', 'P', 'R',
                                                             'S', 'T', 'V', 'W', 'X', 'Y', 'Z']},
                             {'type': 0, 'r': 1, 'rnd_obj': ['B', 'C', 'D', 'F', 'G', 'H', 'J', 'K', 'L', 'P', 'R',
                                                             'S', 'T', 'V', 'W', 'X', 'Y', 'Z']},
                             {'type': 1, 'r': 1, 'min': 10, 'max': 99, 'zfil': 2},
                             {'type': 1, 'r': 1, 'min': 10, 'max': 99, 'zfil': 2}]
                        ]
                    },
                    {
                        "type": "rectangle_rounded",
                        "fill_color": None,
                        "border_color": ChilePlateColor.REMOLQUES_BRUTO_MAYOR_TEXT.value,
                        "border_width": 4,
                        "border_radius": 10,
                        "quantity": 1,
                        "start_x": 2,
                        "start_y": 2,
                        "width": 356,
                        "height": 126,
                        "coord": 0
                    },
                    {
                        "type": "text",
                        "random": 0,
                        "letters": "C  H  I  L  E",
                        "color_bg": ChilePlateColor.REMOLQUES_BRUTO_MAYOR_BG.value,
                        "color_text": ChilePlateColor.REMOLQUES_BRUTO_MAYOR_TEXT.value,
                        "by_letter": 0,
                        "quantity": 0,
                        "start_x": 124,
                        "start_y": 102,
                        "width": 112,
                        "height": 16,
                        "offset_x": 10,
                        "coord": 0,
                        "font": "ARIALN.TTF"
                    },
                    {
                        "type": "image",
                        "image": "img/Chile/chile_black.png",
                        "random": 0,
                        "letters": None,
                        "quantity": 1,
                        "start_x": 112,
                        "start_y": 36,
                        "width": 20,
                        "height": 21,
                        "coord": 0
                    },
                    {
                        "type": "image",
                        "image": "img/Chile/circle_black.png",
                        "random": 0,
                        "letters": None,
                        "quantity": 1,
                        "start_x": 240,
                        "start_y": 40,
                        "width": 9,
                        "height": 9,
                        "coord": 0
                    },

                ]
            },
            {
                "name": ChilePlateType.REMOLQUES_BRUTO_MENOR.value,
                "width": 360,
                "height": 130,
                "color_bg": ChilePlateColor.REMOLQUES_BRUTO_MENOR_BG.value,
                "color_text": ChilePlateColor.REMOLQUES_BRUTO_MENOR_TEXT.value,
                "object": [
                    {
                        "type": "rectangle",
                        "fill_color": ChilePlateColor.REMOLQUES_BRUTO_MENOR_BG.value,
                        "border_color": None,
                        "border_width": 1,
                        "quantity": 1,
                        "start_x": 0,
                        "start_y": 0,
                        "width": 360,
                        "height": 130,
                        "coord": 0
                    },
                    {
                        "type": "format",
                        "random": 1,
                        "color_bg": ChilePlateColor.REMOLQUES_BRUTO_MENOR_BG.value,
                        "color_text": ChilePlateColor.REMOLQUES_BRUTO_MENOR_TEXT.value,
                        "start_x": 14,
                        "start_y": 48,
                        "width": 266,
                        "height": 80,
                        "coord": 0,
                        "obj": [
                            [{'type': 2, 'name': 'AB-AB-12'},
                             {'type': 3, 'obj': [{'ox': 0, 'oy': 0, 'w': 44, 'h': 72},
                                                 {'ox': 6, 'oy': 0, 'w': 44, 'h': 72},
                                                 {'ox': 6, 'oy': 0, 'w': 44, 'h': 72},
                                                 {'ox': 204, 'oy': 48, 'w': 40, 'h': 72, 'r': False},
                                                 {'ox': 6, 'oy': 0, 'w': 40, 'h': 72},
                                                 {'ox': 6, 'oy': 0, 'w': 40, 'h': 72}]},
                             {'type': 5, 'sl': {}},
                             {'type': 0, 'r': 1, 'rnd_obj': ['B', 'C', 'D', 'F', 'G', 'H', 'J', 'K', 'L', 'P', 'R',
                                                             'S', 'T', 'V', 'W', 'X', 'Y', 'Z']},
                             {'type': 0, 'r': 1, 'rnd_obj': ['B', 'C', 'D', 'F', 'G', 'H', 'J', 'K', 'L', 'P', 'R',
                                                             'S', 'T', 'V', 'W', 'X', 'Y', 'Z']},
                             {'type': 0, 'r': 1, 'rnd_obj': ['B', 'C', 'D', 'F', 'G', 'H', 'J', 'K', 'L', 'P', 'R',
                                                             'S', 'T', 'V', 'W', 'X', 'Y', 'Z']},
                             {'type': 1, 'r': 1, 'min': 1, 'max': 999, 'zfil': 3}]
                        ]
                    },
                    {
                        "type": "rectangle_rounded",
                        "fill_color": None,
                        "border_color": ChilePlateColor.REMOLQUES_BRUTO_MENOR_TEXT.value,
                        "border_width": 4,
                        "border_radius": 10,
                        "quantity": 1,
                        "start_x": 2,
                        "start_y": 2,
                        "width": 356,
                        "height": 126,
                        "coord": 0
                    },
                    {
                        "type": "image",
                        "image": "img/Chile/letter_sc_red.png",
                        "random": 0,
                        "letters": None,
                        "quantity": 1,
                        "start_x": 174,
                        "start_y": 62,
                        "width": 20,
                        "height": 40,
                        "coord": 0
                    },
                    {
                        "type": "text",
                        "random": 1,
                        "letters": chile_capital,
                        "by_letter": 3,
                        "quantity": 1,
                        "start_x": 78,
                        "start_y": 12,
                        "width": 206,
                        "height": 16,
                        "offset_x": 2,
                        "coord": 0,
                        "font": "ARIALN.TTF"
                    }
                ]
            },
            {
                "name": ChilePlateType.CUERPO_DIPLOMATICO.value,
                "width": 360,
                "height": 130,
                "color_bg": ChilePlateColor.CUERPO_DIPLOMATICO_BG.value,
                "color_text": ChilePlateColor.CUERPO_DIPLOMATICO_TEXT.value,
                "object": [
                    {
                        "type": "rectangle",
                        "fill_color": ChilePlateColor.CUERPO_DIPLOMATICO_BG.value,
                        "border_color": None,
                        "border_width": 1,
                        "quantity": 1,
                        "start_x": 0,
                        "start_y": 0,
                        "width": 360,
                        "height": 130,
                        "coord": 0
                    },
                    {
                        "type": "format",
                        "random": 1,
                        "color_bg": ChilePlateColor.CUERPO_DIPLOMATICO_BG.value,
                        "color_text": ChilePlateColor.CUERPO_DIPLOMATICO_TEXT.value,
                        "start_x": 14,
                        "start_y": 14,
                        "width": 266,
                        "height": 80,
                        "coord": 0,
                        "obj": [
                            [{'type': 2, 'name': 'AB-AB-12'},
                             {'type': 3, 'obj': [{'ox': 0, 'oy': 0, 'w': 44, 'h': 72},
                                                 {'ox': 6, 'oy': 0, 'w': 44, 'h': 72},
                                                 {'ox': 44, 'oy': 0, 'w': 44, 'h': 72},
                                                 {'ox': 6, 'oy': 0, 'w': 40, 'h': 72},
                                                 {'ox': 6, 'oy': 0, 'w': 40, 'h': 72},
                                                 {'ox': 6, 'oy': 0, 'w': 40, 'h': 72}]},
                             {'type': 5, 'sl': {}},
                             {'type': 0, 'r': 1, 'rnd_obj': ['CD', 'CC', 'AT', 'CH', 'OI', 'PAT']},
                             # may be PAT format in my code is not right, there are no examples in internet
                             {'type': 6, 'r': 1, 'min': 1, 'max': 9999, 'zfil': 4, 'sequence_limit': 6}]
                        ]
                    },
                    {
                        "type": "rectangle_rounded",
                        "fill_color": None,
                        "border_color": ChilePlateColor.CUERPO_DIPLOMATICO_TEXT.value,
                        "border_width": 4,
                        "border_radius": 10,
                        "quantity": 1,
                        "start_x": 2,
                        "start_y": 2,
                        "width": 356,
                        "height": 126,
                        "coord": 0
                    },
                    {
                        "type": "text",
                        "random": 0,
                        "letters": "C  H  I  L  E",
                        "color_bg": ChilePlateColor.CUERPO_DIPLOMATICO_BG.value,
                        "color_text": ChilePlateColor.CUERPO_DIPLOMATICO_TEXT.value,
                        "by_letter": 0,
                        "quantity": 0,
                        "start_x": 124,
                        "start_y": 102,
                        "width": 112,
                        "height": 16,
                        "offset_x": 10,
                        "coord": 0,
                        "font": "ARIALN.TTF"
                    },
                    {
                        "type": "image",
                        "image": "img/Chile/star_white.png",
                        "random": 0,
                        "letters": None,
                        "quantity": 1,
                        "start_x": 118,
                        "start_y": 38,
                        "width": 24,
                        "height": 24,
                        "coord": 0
                    },
                ]
            },
            {
                "name": ChilePlateType.VEHICULOS_DE_CARABINEROS.value,
                "width": 360,
                "height": 130,
                "color_bg": ChilePlateColor.VEHICULOS_DE_CARABINEROS_BG.value,
                "color_text": ChilePlateColor.VEHICULOS_DE_CARABINEROS_TEXT.value,
                "object": [
                    {
                        "type": "rectangle",
                        "fill_color": ChilePlateColor.VEHICULOS_DE_CARABINEROS_BG.value,
                        "border_color": None,
                        "border_width": 1,
                        "quantity": 1,
                        "start_x": 0,
                        "start_y": 0,
                        "width": 360,
                        "height": 130,
                        "coord": 0
                    },
                    {
                        "type": "format",
                        "random": 1,
                        "color_bg": ChilePlateColor.VEHICULOS_DE_CARABINEROS_BG.value,
                        "color_text": ChilePlateColor.VEHICULOS_DE_CARABINEROS_TEXT.value,
                        "start_x": 14,
                        "start_y": 44,
                        "width": 266,
                        "height": 80,
                        "coord": 0,
                        "obj": [
                            [{'type': 2, 'name': 'AB-1234'},
                             {'type': 3, 'obj': [{'ox': 0, 'oy': 0, 'w': 44, 'h': 72},
                                                 {'ox': 6, 'oy': 0, 'w': 44, 'h': 72},
                                                 {'ox': 160, 'oy': 44, 'w': 40, 'h': 72, 'r': False},
                                                 {'ox': 6, 'oy': 0, 'w': 40, 'h': 72},
                                                 {'ox': 6, 'oy': 0, 'w': 40, 'h': 72},
                                                 {'ox': 6, 'oy': 0, 'w': 40, 'h': 72}]},
                             {'type': 5, 'sl': {}},
                             {'type': 0, 'r': 1, 'rnd_obj': ['RP', 'AP', 'CB', 'AG', 'LA', 'LC', 'TC', 'CR']},
                             {'type': 1, 'r': 1, 'min': 1, 'max': 9999, 'zfil': 4}],
                            [{'type': 2, 'name': 'A-1234'},
                             {'type': 3, 'obj': [{'ox': 0, 'oy': 0, 'w': 44, 'h': 72},
                                                 {'ox': 160, 'oy': 44, 'w': 40, 'h': 72, 'r': False},
                                                 {'ox': 6, 'oy': 0, 'w': 40, 'h': 72},
                                                 {'ox': 6, 'oy': 0, 'w': 40, 'h': 72},
                                                 {'ox': 6, 'oy': 0, 'w': 40, 'h': 72}]},
                             {'type': 5, 'sl': {}},
                             {'type': 0, 'r': 1, 'rnd_obj': ['A', 'B', 'C', 'F', 'Z', 'J']},
                             {'type': 1, 'r': 1, 'min': 1, 'max': 9999, 'zfil': 4}]
                        ]
                    },
                    {
                        "type": "rectangle_rounded",
                        "fill_color": None,
                        "border_color": ChilePlateColor.VEHICULOS_DE_CARABINEROS_TEXT.value,
                        "border_width": 4,
                        "border_radius": 10,
                        "quantity": 1,
                        "start_x": 2,
                        "start_y": 2,
                        "width": 356,
                        "height": 126,
                        "coord": 0
                    },
                    {
                        "type": "image",
                        "image": "img/Chile/star_white.png",
                        "random": 0,
                        "letters": None,
                        "quantity": 1,
                        "start_x": 118,
                        "start_y": 66,
                        "width": 24,
                        "height": 24,
                        "coord": 0
                    },
                    {
                        "type": "text",
                        "random": 0,
                        "letters": "CARABINEROS DE CHILE",
                        "color_bg": ChilePlateColor.VEHICULOS_DE_CARABINEROS_BG.value,
                        "color_text": ChilePlateColor.VEHICULOS_DE_CARABINEROS_TEXT.value,
                        "by_letter": 0,
                        "quantity": 0,
                        "start_x": 40,
                        "start_y": 12,
                        "width": 280,
                        "height": 20,
                        "offset_x": 10,
                        "coord": 0,
                        "font": "ARIALN.TTF"
                    }
                ]
            },
            {
                "name": ChilePlateType.INSCRIPSION_PROVISORIA.value,
                "width": 360,
                "height": 130,
                "color_bg": ChilePlateColor.INSCRIPSION_PROVISORIA_BG.value,
                "color_text": ChilePlateColor.INSCRIPSION_PROVISORIA_TEXT.value,
                "object": [
                    {
                        "type": "rectangle",
                        "fill_color": ChilePlateColor.INSCRIPSION_PROVISORIA_BG.value,
                        "border_color": None,
                        "border_width": 1,
                        "quantity": 1,
                        "start_x": 0,
                        "start_y": 0,
                        "width": 360,
                        "height": 130,
                        "coord": 0
                    },
                    {
                        "type": "format",
                        "random": 1,
                        "color_bg": ChilePlateColor.INSCRIPSION_PROVISORIA_BG.value,
                        "color_text": ChilePlateColor.INSCRIPSION_PROVISORIA_TEXT.value,
                        "start_x": 14,
                        "start_y": 14,
                        "width": 266,
                        "height": 80,
                        "coord": 0,
                        "obj": [
                            [{'type': 2, 'name': 'PR-1234'},
                             {'type': 3, 'obj': [{'ox': 0, 'oy': 0, 'w': 44, 'h': 72},
                                                 {'ox': 6, 'oy': 0, 'w': 44, 'h': 72},
                                                 {'ox': 164, 'oy': 14, 'w': 40, 'h': 72, 'r': False},
                                                 {'ox': 6, 'oy': 0, 'w': 40, 'h': 72},
                                                 {'ox': 6, 'oy': 0, 'w': 40, 'h': 72},
                                                 {'ox': 6, 'oy': 0, 'w': 40, 'h': 72}]},
                             {'type': 5, 'sl': {}},
                             {'type': 0, 'r': 1, 'rnd_obj': ['PR']},
                             {'type': 1, 'r': 1, 'min': 1, 'max': 9999, 'zfil': 4}]
                        ]
                    },
                    {
                        "type": "rectangle_rounded",
                        "fill_color": None,
                        "border_color": ChilePlateColor.INSCRIPSION_PROVISORIA_TEXT.value,
                        "border_width": 4,
                        "border_radius": 10,
                        "quantity": 1,
                        "start_x": 2,
                        "start_y": 2,
                        "width": 356,
                        "height": 126,
                        "coord": 0
                    },
                    {
                        "type": "image",
                        "image": "img/Chile/star_black.png",
                        "random": 0,
                        "letters": None,
                        "quantity": 1,
                        "start_x": 128,
                        "start_y": 38,
                        "width": 24,
                        "height": 24,
                        "coord": 0
                    },
                    {
                        "type": "text",
                        "random": 0,
                        "letters": "PROVISORIA",
                        "color_bg": ChilePlateColor.INSCRIPSION_PROVISORIA_BG.value,
                        "color_text": ChilePlateColor.INSCRIPSION_PROVISORIA_TEXT.value,
                        "by_letter": 0,
                        "quantity": 1,
                        "start_x": 68,
                        "start_y": 98,
                        "width": 168,
                        "height": 20,
                        "coord": 0,
                        "font": "ARIALN.TTF"
                    },
                    {
                        "type": "number",
                        "random": 1,
                        "letters": None,
                        "color_bg": ChilePlateColor.INSCRIPSION_PROVISORIA_BG.value,
                        "color_text": ChilePlateColor.INSCRIPSION_PROVISORIA_TEXT.value,
                        "by_letter": 0,
                        "number_min": 2007,
                        "number_max": 2030,
                        "number_zfil": 4,
                        "quantity": 1,
                        "start_x": 248,
                        "start_y": 98,
                        "width": 58,
                        "height": 20,
                        "coord": 0
                    }
                ]
            },
            {
                "name": ChilePlateType.FUERZAS_ARMADAS.value,
                "width": 360,
                "height": 130,
                "color_bg": ChilePlateColor.FUERZAS_ARMADAS_BG.value,
                "color_text": ChilePlateColor.FUERZAS_ARMADAS_TEXT.value,
                "object": [
                    {
                        "type": "rectangle",
                        "fill_color": ChilePlateColor.FUERZAS_ARMADAS_BG.value,
                        "border_color": None,
                        "border_width": 1,
                        "quantity": 1,
                        "start_x": 0,
                        "start_y": 0,
                        "width": 360,
                        "height": 130,
                        "coord": 0
                    },
                    {
                        "type": "format",
                        "random": 1,
                        "color_bg": ChilePlateColor.FUERZAS_ARMADAS_BG.value,
                        "color_text": ChilePlateColor.FUERZAS_ARMADAS_TEXT.value,
                        "start_x": 14,
                        "start_y": 32,
                        "width": 266,
                        "height": 80,
                        "coord": 0,
                        "obj": [
                            [{'type': 2, 'name': 'EJTO-1234'},
                             {'type': 3, 'obj': [{'ox': 0, 'oy': 0, 'w': 32, 'h': 72},
                                                 {'ox': 6, 'oy': 0, 'w': 32, 'h': 72},
                                                 {'ox': 6, 'oy': 0, 'w': 32, 'h': 72},
                                                 {'ox': 6, 'oy': 0, 'w': 32, 'h': 72},
                                                 {'ox': 196, 'oy': 32, 'w': 32, 'h': 72, 'r': False},
                                                 {'ox': 6, 'oy': 0, 'w': 32, 'h': 72},
                                                 {'ox': 6, 'oy': 0, 'w': 32, 'h': 72},
                                                 {'ox': 6, 'oy': 0, 'w': 32, 'h': 72}]},
                             {'type': 5, 'sl': {}},
                             {'type': 0, 'r': 1, 'rnd_obj': ['EJTO']},
                             {'type': 1, 'r': 1, 'min': 1, 'max': 9999, 'zfil': 4}]
                        ]
                    },
                    {
                        "type": "rectangle_rounded",
                        "fill_color": None,
                        "border_color": ChilePlateColor.FUERZAS_ARMADAS_TEXT.value,
                        "border_width": 4,
                        "border_radius": 10,
                        "quantity": 1,
                        "start_x": 2,
                        "start_y": 2,
                        "width": 356,
                        "height": 126,
                        "coord": 0
                    },
                    {
                        "type": "image",
                        "image": "img/Chile/Flag_of_the_Chilean_Army.png",
                        "random": 0,
                        "letters": None,
                        "quantity": 1,
                        "start_x": 164,
                        "start_y": 52,
                        "width": 32,
                        "height": 34,
                        "coord": 0
                    }
                ]
            },
            {
                "name": ChilePlateType.BOMBEROS.value,
                "width": 360,
                "height": 130,
                "color_bg": ChilePlateColor.BOMBEROS_BG.value,
                "color_text": ChilePlateColor.BOMBEROS_TEXT.value,
                "object": [
                    {
                        "type": "rectangle",
                        "fill_color": ChilePlateColor.BOMBEROS_BG.value,
                        "border_color": None,
                        "border_width": 1,
                        "quantity": 1,
                        "start_x": 0,
                        "start_y": 0,
                        "width": 360,
                        "height": 130,
                        "coord": 0
                    },
                    {
                        "type": "format",
                        "random": 1,
                        "color_bg": ChilePlateColor.BOMBEROS_BG.value,
                        "color_text": ChilePlateColor.BOMBEROS_TEXT.value,
                        "start_x": 14,
                        "start_y": 44,
                        "width": 266,
                        "height": 80,
                        "coord": 0,
                        "obj": [
                            [{'type': 2, 'name': 'CB-AB-123'},
                             {'type': 3, 'obj': [{'ox': 0, 'oy': 0, 'w': 40, 'h': 72},
                                                 {'ox': 5, 'oy': 0, 'w': 40, 'h': 72},
                                                 {'ox': 5, 'oy': 0, 'w': 40, 'h': 72},
                                                 {'ox': 5, 'oy': 0, 'w': 40, 'h': 72},
                                                 {'ox': 216, 'oy': 44, 'w': 40, 'h': 72, 'r': False},
                                                 {'ox': 5, 'oy': 0, 'w': 40, 'h': 72},
                                                 {'ox': 5, 'oy': 0, 'w': 40, 'h': 72}]},
                             {'type': 5, 'sl': {}},
                             {'type': 0, 'r': 1, 'rnd_obj': ['CB']},
                             {'type': 7, 'r': 1, 'rnd_obj': chile_abreviatura_nacional},
                             {'type': 1, 'r': 1, 'min': 1, 'max': 999, 'zfil': 3}]
                        ]
                    },
                    {
                        "type": "rectangle_rounded",
                        "fill_color": None,
                        "border_color": ChilePlateColor.BOMBEROS_TEXT.value,
                        "border_width": 4,
                        "border_radius": 10,
                        "quantity": 1,
                        "start_x": 2,
                        "start_y": 2,
                        "width": 356,
                        "height": 126,
                        "coord": 0
                    },
                    {
                        "type": "image",
                        "image": "img/Chile/star_black.png",
                        "random": 0,
                        "letters": None,
                        "quantity": 1,
                        "start_x": 191,
                        "start_y": 68,
                        "width": 24,
                        "height": 24,
                        "coord": 0
                    },
                    {
                        "type": "text",
                        "random": 3,
                        "letters": 'CPO.BOMBEROS ',
                        "by_letter": 0,
                        "quantity": 1,
                        "start_x": 14,
                        "start_y": 12,
                        "width": 334,
                        "height": 18,
                        "coord": 0,
                        "font": "ARIALN.TTF"
                    }
                ]
            },
        ]
    }
