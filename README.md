# VRPG

Vehicle Registration Plate Generator (VRPG) is open-source software for Vehicle registration plate generation.


Contents
========

* [Why?](#why)
* [Updates](#Updates)
* [Getting Started](#getting-started)
* [Argentina plates](#argentina-plates)
* [Bolivia plates](#bolivia-plates)
* [Chile plates](#chile-plates)
* [Guatemala plates](#guatemala-plates)
* [Ecuador plates](#ecuador-plates)
* [UK plates](#uk-plates)


## Why?

I wanted a tool that allows you to:

+ Improve ANPR dataset
+ Generate all types of Argentina registration plates
+ Generate all types of Bolivia registration plates
+ Generate all types of Chile registration plates
+ Generate all types of Guatemala registration plates
+ Generate all types of Ecuador registration plates
+ Generate all types of UK registration plates

## Updates

[2024-10-16] VRPG v0.0.4 is released.
- Bolivia, Argentina, Ecuador Vehicle Registration Plate Generator.

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
| Argentina | FE-Schrift, Arial Narrow, Arimo-SemiBold, NotoSerif-Medium | [Link](https://www.andyhoppe.com/design/fonts/euro-plate-font/), [Link](https://online-fonts.com/fonts/arial-narrow/), [Link](https://fonts.google.com/specimen/Arimo/), [Link](https://fonts.google.com/noto/specimen/Noto+Serif/)  | [Link](https://www.guatecompras.gt/concursos/files/2259/11294345%40ESPECIFICACIONES%20TECNICAS%20PLACAS.pdf)       |
| Bolivia   | Roadgeek 2005 Series 1B, Traffic 02, Arial Narrow | [Link](https://fonts2u.com/roadgeek-2005-series-1b.font/), [Link](https://fonts2u.com/traffic-02.font/), [Link](https://online-fonts.com/fonts/arial-narrow/) | [Link](https://es.wikipedia.org/wiki/Matr%C3%ADculas_automovil%C3%ADsticas_de_Bolivia)                               |
| Chile     | FE-Schrift, Arial Narrow | [Link](https://www.andyhoppe.com/design/fonts/euro-plate-font/), [Link](https://online-fonts.com/fonts/arial-narrow/) | [Link](https://es.wikipedia.org/wiki/Matr%C3%ADculas_automovil%C3%ADsticas_de_Chile)                               |
| Guatemala | FE-Schrift, Arial Narrow | [Link](https://www.andyhoppe.com/design/fonts/euro-plate-font/), [Link](https://online-fonts.com/fonts/arial-narrow/) | [Link](https://www.guatecompras.gt/concursos/files/2259/11294345%40ESPECIFICACIONES%20TECNICAS%20PLACAS.pdf)       |
| Ecuador   | FE-Fschrift, Arial Narrow| [Link](https://www.andyhoppe.com/design/fonts/euro-plate-font/), [Link](https://online-fonts.com/fonts/arial-narrow/) | [Link](https://en.wikipedia.org/wiki/Vehicle_registration_plates_of_Ecuador)|
| UK        | Charles Wright           | [Link](https://www.k-type.com/fonts/charles-wright/)            | [Link](https://www.gov.uk/government/publications/vehicle-registration-numbers-and-number-plates)                  |

Please download the font files to create vehicle license plate. Upload these files to fonts directory. The font files are not included in the GitHub repository due to potential copyright concerns. 

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
## Argentina plates

Supported plate types

| Country   | Plate type               |
|-----------|--------------------------|
| Argentina | 'Vehículo privado', 'Cuerpo diplomático', 'Cuerpo consular', 'Organismos internacionales', 'Misiones especiales', 'Personal administrativo', 'Remolque', 'Vehiculos restricted', 'Trailer', 'RNPA', 'Motocicleta particular', 'Motocicleta restricted' |

| Plate type | Images               |
|-----------|--------------------------|
| 'Vehiculo privado' | ![Argentina Vehículo privado plate](help/img/Argentina/Argentina-2014-CK111HQ-16_Nov_2023-18_09_05.png) | 
| 'Cuerpo diplomático' | ![Argentina Cuerpo diplomático plate](help/img/Argentina/Argentina-2014-D507QBC-15_Oct_2024-11_09_58.png) | 
| 'Cuerpo consular' | ![Argentina Cuerpo consular plate](help/img/Argentina/Argentina-2014-C309UJD-15_Oct_2024-11_12_43.png) | 
| 'Organismos internacionales' | ![Argentina Organismos internacionales plate](help/img/Argentina/Argentina-2014-I199OAU-15_Oct_2024-11_14_12.png) | 
| 'Misiones especiales' | ![Argentina Misiones especiales plate](help/img/Argentina/Argentina-2014-M061CLJ-15_Oct_2024-11_17_09.png) | 
| 'Personal administrativo' | ![Argentina Personal administrativo plate](help/img/Argentina/Argentina-2014-A079RMM-16_Nov_2023-18_09_23.png) | 
| 'Remolque' | ![Argentina Remolque plate](help/img/Argentina/Argentina-2014-077TGF261-16_Nov_2023-18_09_06.png) | 
| 'Vehiculos restricted' | ![Argentina Vehiculos restricted plate](help/img/Argentina/Argentina-2014-BP731MI-16_Nov_2023-18_09_20.png) | 
| 'Trailer' | ![Argentina Trailer plate](help/img/Argentina/Argentina-2014-AQ425VE-16_Nov_2023-18_09_14.png) | 
| 'RNPA' | ![Argentina RNPA plate](help/img/Argentina/Argentina-2014-HUA99-15_Oct_2024-11_26_24.png) | 
| 'Motocicleta particular' | ![Argentina Motocicleta particular plate](help/img/Argentina/Argentina-2014-BP854SP-16_Nov_2023-18_09_13.png) | 
| 'Motocicleta restricted' | ![Argentina Motocicleta restricted plate](help/img/Argentina/Argentina-2014-AA053NL-16_Nov_2023-18_09_07.png) | 




## Bolivia plates

Supported plate types

| Country   | Plate type               |
|-----------|--------------------------|
| Bolivia |'Vehiculo particular', 'Vehiculo MERCOSUR', 'Cuerpo consular', 'Cuerpo diplomatico', 'Mision internacional', 'Organizacion internacional'  |

| Plate type | Images               |
|-----------|--------------------------|
| 'Vehiculo particular' | ![Bolivia Vehiculo particular plate](help/img/Bolivia/Bolivia-1999-2794EOX-23_Nov_2023-13_21_05.png) | 
| 'Vehiculo MERCOSUR' | ![Bolivia Vehiculo MERCOSUR plate](help/img/Bolivia/Bolivia-1999-LP84321-23_Nov_2023-13_21_10.png) | 
| 'Cuerpo consular' | ![Bolivia Cuerpo consular plate](help/img/Bolivia/Bolivia-1999-07-CC-83-23_Nov_2023-13_21_05.png) | 
| 'Cuerpo diplomatico' | ![Bolivia Cuerpo diplomatico plate](help/img/Bolivia/Bolivia-1999-04-CD-04-23_Nov_2023-13_21_14.png) | 
| 'Mision internacional' | ![Bolivia Mision internacional plate](help/img/Bolivia/Bolivia-1999-01-MI-42-23_Nov_2023-13_21_06.png) | 


## Chile plates

Supported plate types

| Country   | Plate type               |
|-----------|--------------------------|
| Chile | 'Vehiculo particular', 'Taxi básico', 'Taxi colectivo', 'Radiotaxi vehiculos de turismo', 'Buses de Transantiago', 'Vehículos adquiridos en Zona Franca', 'Remolques de peso bruto mayor a 3860kg', 'Remolques de peso bruto menor a 3860kg', 'Cuerpo diplomático', 'Vehiculos de carabineros', 'Inscripsion provisoria', 'Fuerzas Armadas', 'Bomberos' |

| Plate type | Images               |
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

 # Ecuador plates

Supported plate types

| Country   | Plate type               |
|-----------|--------------------------|
| Ecuador | 'Vehículos comerciales', 'Vehículos gubernamentales', 'Vehículos de uso oficial', 'Vehículos de los gobiernos autónomos descentralizados', 'Vehículo privado', 'Vehículo privado duplicata', 'Vehículos de servicio diplomático', 'Matrícula temporal', 'Vehículos de internación temporal', 'Policía Nacional del Ecuador'|

 Plate type | Images               |
|-----------|--------------------------|
| 'Vehículos comerciales' | ![Ecuador Vehículos comerciales plate](help/img/Ecuador/Ecuador-2012-GAU-7723-15_Nov_2023-11_42_58.png) | 
| 'Vehículos gubernamentales' | ![Ecuador Vehículos gubernamentales plate](help/img/Ecuador/Ecuador-2012-MER-5320-15_Oct_2024-17_33_11.png) | 
| 'Vehículos de uso oficial' | ![Ecuador Vehículos de uso oficial plate](help/img/Ecuador/Ecuador-2012-BXZ-8960-15_Nov_2023-11_42_57.png) | 
| 'Vehículos de los gobiernos autónomos descentralizados' | ![Ecuador Vehículos de los gobiernos autónomos descentralizados plate](help/img/Ecuador/Ecuador-2012-BSC-9330-15_Nov_2023-11_43_07.png) | 
| 'Vehículo privado' | ![Ecuador Vehículo privado plate](help/img/Ecuador/Ecuador-2012-ADE-3644-15_Nov_2023-11_43_01.png) | 
| 'Vehículo privado duplicata' | ![Ecuador Vehículo privado duplicata plate](help/img/Ecuador/Ecuador-2012-OVN-6745-15_Oct_2024-17_36_10.png) | 
| 'Vehículos de servicio diplomático' | ![Ecuador Vehículos de servicio diplomático plate](help/img/Ecuador/Ecuador-2012-AT-2011-15_Nov_2023-11_43_00.png) | 
| 'Matrícula temporal' | ![Ecuador Matrícula temporal plate](help/img/Ecuador/Ecuador-2012-BCB-521-15_Nov_2023-11_43_08.png) | 
| 'Vehículos de internación temporal' | ![Ecuador Vehículos de internación temporal plate](help/img/Ecuador/Ecuador-2012-IT-2228-15_Nov_2023-11_43_10.png) | 
| 'Policía Nacional del Ecuador' | ![Ecuador Policía Nacional del Ecuador plate](help/img/Ecuador/Ecuador-2012-AWP-8632-16_Oct_2024-09_56_41.png) | 






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

