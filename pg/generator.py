from pg.argentina import plate_argentina
from pg.bolivia import plate_bolivia
from pg.chile import plate_chile
from pg.guatemala import plate_guatemala
from pg.ecuador import plate_ecuador
from pg.peru import plate_peru
from pg.united_kingdom import plate_uk
from pg.universal import vrpg_universal
import os
import json
import zipfile
import fnmatch


def vrpg(country: str = None,
         font: str = None,
         directory: str = None,
         dpi: int = 150,
         plate_type: str = 'random') -> dict:
    result = None
    if country == 'Chile':
        result = vrpg_universal(font=font, directory=directory, dpi=dpi, area=plate_chile(), plate_type=plate_type)
    elif country == 'Argentina':
        result = vrpg_universal(font=font, directory=directory, dpi=dpi, area=plate_argentina(), plate_type=plate_type)
    elif country == 'Bolivia':
        result = vrpg_universal(font=font, directory=directory, dpi=dpi, area=plate_bolivia(), plate_type=plate_type)
    elif country == 'Guatemala':
        result = vrpg_universal(font=font, directory=directory, dpi=dpi, area=plate_guatemala(), plate_type=plate_type)
    elif country == 'Ecuador':
        result = vrpg_universal(font=font, directory=directory, dpi=dpi, area=plate_ecuador(), plate_type=plate_type)
    elif country == 'Peru':
        result = vrpg_universal(font=font, directory=directory, dpi=dpi, area=plate_peru(), plate_type=plate_type)
    elif country == 'UK':
        result = vrpg_universal(font=font, directory=directory, dpi=dpi, area=plate_uk(), plate_type=plate_type)
    # elif country == 'US_California':
    #     result = vrpg_universal(font=font, directory=directory, dpi=dpi, area=plate_usa_california_1963(), plate_type=plate_type)

    return result


def ts_directory_zip_and_delete_all_files(directory: str, v_zip_fn: str, pattern: list) -> int:
    print("Compressing and Erasing files in directory ", directory, " procedure started")
    i = 0
    # zip_fn = directory + '/' + v_zip_fn
    zip_fn = v_zip_fn
    dir_len = len(directory)
    zip_f = zipfile.ZipFile(zip_fn, 'w', zipfile.ZIP_DEFLATED)
    for root, dirs, files in os.walk(directory):
        for basename in files:
            for e in pattern:
                if fnmatch.fnmatch(basename, e):
                    file_name = os.path.join(root, basename)
                    # zip_f.write(file_name)
                    zip_f.write(file_name, file_name[dir_len:])
                    os.remove(file_name)
                    i += 1
    print("Compressed and Erased {0} files".format(i))
    print("Compressing and Erasing files in directory ", directory, " procedure complete")
    return i


def vrpg_data_set(country: str = None,
                  font: str = None,
                  directory: str = None,
                  dpi: int = 150,
                  plate_type: str = 'random',
                  quantity: int = 10) -> dict:
    ds = dict()
    i = 0
    while i < quantity:
        r = vrpg(country=country, font=font, directory=directory, dpi=dpi, plate_type=plate_type)
        if r['plate'] not in ds:
            for j in range(len(r['images'])):
                r['images'][j] = os.path.basename(r['images'][j])
            ds[r['plate']] = r
            i += 1
        else:
            for j in range(len(r['images'])):
                os.remove(r['images'][j])
                print('removing ' + r['images'][j])
        print(i)

    json_name = os.path.join(directory, country + '-' + str(quantity) + '-' + 'dataset.json')
    with open(json_name, 'w') as outfile:
        json.dump(ds, outfile, indent=2, ensure_ascii=False)
    zip_name = os.path.join(directory, country + '-' + str(quantity) + '-' + 'dataset.zip')
    ts_directory_zip_and_delete_all_files(directory, zip_name, ['*.png', '*.jpg', '*.json'])

    return ds
