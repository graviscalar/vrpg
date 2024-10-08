# VRPG

Vehicle Registration Plate Generator (VRPG) is open-source software for Vehicle registration plate generation.


Contents
========

* [Why?](#why)
* [Updates](#Updates)
* [Getting Started](#getting-started)
* [Chile plates](#chile-plates)
* [Guatemala plates](#guatemala-plates)
* [UK plates](#uk-plates)


## Why?

I wanted a tool that allows you to:

+ Improve ANPR dataset
+ Generate all types of Chile registration plates
+ Generate all types of Guatemala registration plates
+ Generate all types of UK registration plates

## Updates

[2024-10-08] VRPG v0.0.3 is released.
- Chile Vehicle Registration Plate Generator.

[2024-10-07] VRPG v0.0.2 is released.
- Guatemala Vehicle Registration Plate Generator.

[2024-10-06] VRPG v0.0.1 is released.
- United Kingdom Vehicle Registration Plate Generator.

## Getting Started

Supported countries:

| Country   | Font name                | Font link to download                                           | Reference                                                                                                          |
|-----------|--------------------------|-----------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------|
| Chile     | FE-Schrift, Arial Narrow | [Link](https://www.andyhoppe.com/design/fonts/euro-plate-font/), [Link](https://online-fonts.com/fonts/arial-narrow/) | [Link](https://es.wikipedia.org/wiki/Matr%C3%ADculas_automovil%C3%ADsticas_de_Chile)                               |
| Guatemala | FE-Schrift, Arial Narrow | [Link](https://www.andyhoppe.com/design/fonts/euro-plate-font/), [Link](https://online-fonts.com/fonts/arial-narrow/) | [Link](https://www.guatecompras.gt/concursos/files/2259/11294345%40ESPECIFICACIONES%20TECNICAS%20PLACAS.pdf)       |
| UK        | Charles Wright           | [Link](https://www.k-type.com/fonts/charles-wright/)            | [Link](https://www.gov.uk/government/publications/vehicle-registration-numbers-and-number-plates)                  |

Please download the font files to create vehicle license plate. Upload thess files to fonts directory or to any place. The font files are not included in the GitHub repository due to potential copyright concerns. 

An example of usage with font name = None (create directory /fonts/ first, font file downloaded to the /fonts/ directory):

``` shell
from pg.generator import *


if __name__ == '__main__':
    result = vrpg(country='UK', font=None, directory='d:/temp/img/', dpi=150, plate_type='random')
    print(result)
```
The UK output images will be:

![UK white plate](help/img/UK/w.png)
![UK yellow plate](help/img/UK/y.png)

An example of usage with font name = absolute path:

``` shell
from pg.generator import *


if __name__ == '__main__':
    result = vrpg(country='UK', font='F:/py/vrpg/fonts/CharlesWright-Bold.otf', directory='d:/temp/img/', dpi=150, plate_type='random')
    print(result)
```

## Chile plates

Supported plate types

| Country   | Plate type               |
|-----------|--------------------------|
| Chile | 'Vehiculo particular', 'Taxi básico', 'Taxi colectivo', 'Radiotaxi vehiculos de turismo', 'Buses de Transantiago', 'Vehículos adquiridos en Zona Franca', 'Remolques de peso bruto mayor a 3860kg', 'Remolques de peso bruto menor a 3860kg', 'Cuerpo diplomático', 'Vehiculos de carabineros', 'Inscripsion provisoria', 'Fuerzas Armadas', 'Bomberos' |

 Plate type | Images               |
|-----------|--------------------------|
| 'Vehiculo particular' | ![Chile Vehiculo particular plate](help/img/Chile/Chile-Vehiculo-particular.png) | 
| 'Taxi básico' | ![Chile Taxi básico plate](help/img/Chile/Chile-Taxi-básico.png) | 
| 'Taxi colectivo' | ![Chile Taxi colectivo plate](help/img/Chile/Chile-Taxi-colectivo.png) | 
| 'Radiotaxi vehiculos de turismo' | ![Chile Radiotaxi vehiculos de turismo plate](help/img/Chile/Chile-Radiotaxi-vehiculos-de-turismo.png) | 
| 'Buses de Transantiago' | ![Chile Buses de Transantiago plate](help/img/Chile/Chile-Buses-de-Transantiago.png) | 
| 'Vehículos adquiridos en Zona Franca' | ![Chile Vehículos adquiridos en Zona Franca plate](help/img/Chile/Chile-Vehículos-adquiridos-en-Zona-Franca.png) | 
| 'Remolques de peso bruto mayor a 3860kg' | ![Chile Remolques de peso bruto mayor a 3860kg plate](help/img/Chile/Chile-Remolques-de-peso-bruto-mayor-a-3860kg.png) | 
| 'Remolques de peso bruto menor a 3860kg' | ![Chile Remolques de peso bruto menor a 3860kg plate](help/img/Chile/Chile-Remolques-de-peso-bruto-menor-a-3860kg.png) | 
| 'Cuerpo diplomático' | ![Chile Cuerpo diplomático plate](help/img/Chile/Chile-Cuerpo-diplomático.png) | 
| 'Vehiculos de carabineros' | ![Chile Vehiculos de carabineros plate](help/img/Chile/Chile-Vehiculos-de-carabineros.png) | 
| 'Inscripsion provisoria' | ![Chile Inscripsion provisoria plate](help/img/Chile/Chile-Inscripsion-provisoria.png) | 
| 'Fuerzas Armadas' | ![Chile Fuerzas Armadas plate](help/img/Chile/Chile-Fuerzas-Armadas.png) | 
| 'Bomberos' | ![Chile Bomberos plate](help/img/Chile/Chile-Bomberos.png) | 


 # Guatemala plates

Supported plate types

| Country   | Plate type               |
|-----------|--------------------------|
| Guatemala | 'Vehículo de alquiler', 'Vehículo Comercial', 'Cuerpo Consular', 'Cuerpo Diplomático', 'Misión Internacional', 'Vehículo Oficial', 'Vehículo Privado', 'Transporte Extraurbano de Personas o Carga', 'Bus urbano'|

 Plate type | Images               |
|-----------|--------------------------|
| 'Vehículo de alquiler' | ![Guatemala Vehículo de alquiler plate](help/img/Guatemala/Guatemala-2021-A525OMN-07_Oct_2024-15_35_28.png) | 
| 'Vehículo Comercial' | ![Guatemala Vehículo Comercial plate](help/img/Guatemala/Guatemala-2021-C372BJQ-07_Oct_2024-15_37_27.png) |
| 'Cuerpo Consular' | ![Guatemala Cuerpo Consular plate](help/img/Guatemala/Guatemala-2021-CC72PVZ-07_Oct_2024-15_39_08.png) |
| 'Cuerpo Diplomático' | ![Guatemala Cuerpo Diplomático plate](help/img/Guatemala/Guatemala-2021-CD61YPY-07_Oct_2024-15_40_23.png) |
| 'Misión Internacional' | ![Guatemala Misión Internacional plate](help/img/Guatemala/Guatemala-2021-MI45FYN-07_Oct_2024-15_42_27.png) |
| 'Vehículo Oficial' | ![Guatemala Vehículo Oficial plate](help/img/Guatemala/Guatemala-2021-O204KDV-07_Oct_2024-15_43_41.png) |
| 'Vehículo Privado' | ![Guatemala Vehículo Privado plate](help/img/Guatemala/Guatemala-2021-P304COJ-07_Oct_2024-15_45_05.png) |
| 'Transporte Extraurbano de Personas o Carga' | ![Guatemala Transporte Extraurbano de Personas o Carga plate](help/img/Guatemala/Guatemala-2021-TE87YYY-07_Oct_2024-15_46_33.png) |
| 'Bus urbano' | ![Guatemala Bus urbano plate](help/img/Guatemala/Guatemala-2021-U277SYU-07_Oct_2024-15_47_36.png) |

## UK plates

Supported plate types

| Country   | Plate type               |
|-----------|--------------------------|
| UK        | 'random', 'Private', 'Motorcycle', 'Trade', 'Trailer', 'Diplomatic', 'Armed forces', 'Armed forces trailer'           |


 Plate type | Images               |
|-----------|--------------------------|
| 'Private'        | ![UK front plate](help/img/UK/UK-Front-2001-KC77MSU-06_Oct_2024-19_37_38.png) ![UK rear plate](help/img/UK/UK-Rear-2001-KC77MSU-06_Oct_2024-19_37_38.png)| 
| 'Motorcycle'        | ![UK front plate](help/img/UK/UK-Front-2001-VO80WFX-06_Oct_2024-19_43_27.png) ![UK rear plate](help/img/UK/UK-Rear-2001-VO80WFX-06_Oct_2024-19_43_27.png)| 
| 'Trade'        | ![UK Trade plate](help/img/UK/UK-2001-17302-06_Oct_2024-19_45_20.png)| 
| 'Trailer'        | ![UK Trailer plate](help/img/UK/UK-2001-F4054474-06_Oct_2024-19_46_38.png)| 
| 'Diplomatic'        | ![UK front plate](help/img/UK/UK-Front-2001-562D499-06_Oct_2024-19_48_04.png) ![UK front plate](help/img/UK/UK-Rear-2001-562D499-06_Oct_2024-19_48_04.png)| 
| 'Armed forces'        | ![UK Armed forces plate](help/img/UK/UK-2001-USAF2818-06_Oct_2024-19_49_41.png)| 
| 'Armed forces trailer' | ![UK Armed forces trailer plate](help/img/UK/UK-2001-UKAX5577-06_Oct_2024-19_51_09.png)| 

