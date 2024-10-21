from pg.generator import *


if __name__ == '__main__':
    # An example of usage for Argentina random plate generation
    r = vrpg(country='Argentina', font=None, directory='d:/temp/img/', dpi=72, plate_type='Cuerpo consular')
    print(r)
    # An example of usage for Bolivia random plate generation
    r = vrpg(country='Bolivia', font=None, directory='d:/temp/img/', dpi=72, plate_type='Organizacion internacional')
    print(r)
    # An example of usage for Chile random plate generation
    r = vrpg(country='Chile', font=None, directory='d:/temp/img/', dpi=72, plate_type='Vehiculo particular')
    print(r)
    # An example of usage for Guatemala random plate generation
    r = vrpg(country='Guatemala', font=None, directory='d:/temp/img/', dpi=72, plate_type='Bus urbano')
    print(r)
    # An example of usage for Ecuador random plate generation
    r = vrpg(country='Ecuador', font=None, directory='d:/temp/img/', dpi=150, plate_type='Policía Nacional del Ecuador')
    print(r)
    # An example of usage for Peru random plate generation
    r = vrpg(country='Peru', font=None, directory='d:/temp/img/', dpi=150, plate_type='Automóvil')
    print(r)
    # An example of usage for UK random plate generation
    r = vrpg(country='UK', font=None, directory='d:/temp/img/', dpi=150, plate_type='random')
    print(r)

