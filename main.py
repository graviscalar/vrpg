from pg.generator import *


if __name__ == '__main__':
    # An example of usage for Guatemala random plate generation
    r = vrpg(country='Guatemala', font=None, directory='d:/temp/img/', dpi=150, plate_type='random')
    print(r)
    # An example of usage for UK random plate generation
    r = vrpg(country='UK', font=None, directory='d:/temp/img/', dpi=150, plate_type='random')
    print(r)

