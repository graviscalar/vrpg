# VRPG

Vehicle Registration Plate Generator (VRPG) is open-source software for Vehicle registration plate generation.


Contents
========

* [Why?](#why)
* [Updates](#Updates)
* [Getting Started](#getting-started)
* [UK plates](#uk-plates)


## Why?

I wanted a tool that allows you to:

+ Improve ANPR dataset
+ Generate all types of UK registration plates

## Updates

[2024-10-06] VRPG v0.0.1 is released.
- United Kingdom Vehicle Registration Plate Generator.

## Getting Started

Supported countries:

| Country   | Font name                | Font link to download                                           | Reference                                                                                                          |
|-----------|--------------------------|-----------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------|
| UK        | Charles Wright           | [Link](https://www.k-type.com/fonts/charles-wright/)            | [Link](https://www.gov.uk/government/publications/vehicle-registration-numbers-and-number-plates)                  |

Please download the font file to create vehicle license plate. 
Upload this file to fonts directory or to any place. 

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
from pg.generator import vrpg


if __name__ == '__main__':
    result = vrpg(country='UK', font='F:/py/vrpg/fonts/CharlesWright-Bold.otf', directory='d:/temp/img/', dpi=150, plate_type='random')
    print(result)
```
## UK plates

Supported plate types

| Country   | Plate type               |
|-----------|--------------------------|
| UK        | 'random', 'Private', 'Motorcycle', 'Trade', 'Trailer', 'Diplomatic', 'Armed forces', 'Armed forces trailer'           |


 Plate type | Images               |
|-----------|--------------------------|
| 'Private'        | ![UK front plate](help/img/UK/UK-Front-2001-KC77MSU-06_Oct_2024-19_37_38.png) ![UK rear plate](help/img/UK/UK-Rear-2001-KC77MSU-06_Oct_2024-19_37_38.png)| 
| 'Motorcycle'        | ![UK front plate](help/img/UK/UK-Front-2001-VO80WFX-06_Oct_2024-19_43_27.png) ![UK rear plate](help/img/UK/UK-Rear-2001-VO80WFX-06_Oct_2024-19_43_27.png)| 
| 'Trade'        | ![UK front plate](help/img/UK/UK-2001-17302-06_Oct_2024-19_45_20.png)| 
| 'Trailer'        | ![UK front plate](help/img/UK/UK-2001-F4054474-06_Oct_2024-19_46_38.png)| 
| 'Diplomatic'        | ![UK front plate](help/img/UK/UK-Front-2001-562D499-06_Oct_2024-19_48_04.png) ![UK front plate](help/img/UK/UK-Rear-2001-562D499-06_Oct_2024-19_48_04.png)| 
| 'Armed forces'        | ![UK front plate](help/img/UK/UK-2001-USAF2818-06_Oct_2024-19_49_41.png)| 
| 'Armed forces trailer' | ![UK front plate](help/img/UK/UK-2001-UKAX5577-06_Oct_2024-19_51_09.png)| 

