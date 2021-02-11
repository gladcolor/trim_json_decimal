import json
import os
import glob
import logging
# logging.basicConfig(level=logging.DEBUG, format="%(levelname)s - %(message)s")
logging.basicConfig(level=logging.INFO, format="%(levelname)s - %(message)s")

def trim_decimal(file_path: str, digits=5):
    '''

    :param file_path:
    :return:
    '''
    saved_path = os.path.join(os.path.dirname(file_path), "trimed")
    if not os.path.exists(saved_path):
        os.makedirs(saved_path)

    digits = int(digits)
    with open(file_path, "rb") as f:
        jdata = json.load(f, encoding='utf8')
        try:
            features = jdata.get("features", None)

            if features:
                # logging.debug("Length of features: %d" , len(features))
                # logging.debug("features[0]: %s" , features[0])
                end = len(features)
                for idx, feature in enumerate(features[:end]):
                    # logging.debug("feature: %s", feature)


                    geometry = feature.get("geometry", None)
                    g_type = geometry.get("type", None)
                    polygons = []
                    polygons = geometry.get("coordinates", None)
                    logging.debug("number of polygon in this feature: %d", len(polygons))
                    if g_type == "Polygon":
                        polygons = [polygons]

                    # logging.debug("geometry: %s", geometry)
                    if polygons:
                        for idx2, polygon in enumerate(polygons):
                            for idx3, ring in enumerate(polygon):
                                # logging.debug("feature # %d, polygon # %d, ring # %d, ring point numbers: %s", idx, idx2, idx3, len(ring))
                                for idx4, (x, y) in enumerate(ring):
                                    # logging.debug("before rounding: x, y: %f, %f", x, y)

                                    x = round(x, digits)
                                    y = round(y, digits)
                                    if g_type == 'Polygon':
                                        jdata['features'][idx]['geometry']['coordinates'][idx3][idx4] = [x, y]
                                        # logging.debug("x, y: %s", jdata['features'][idx]['geometry']['coordinates'][idx3])
                                    if g_type == 'MultiPolygon':
                                        jdata['features'][idx]['geometry']['coordinates'][idx2][idx3][idx4] = [x, y]
                                        # logging.debug("x, y: %s", jdata['features'][idx]['geometry']['coordinates'][idx2][idx3])



        except:
            logging.exception("Json file has no feature key.")


    new_name = os.path.join(saved_path, os.path.basename(file_path))
    with open(new_name, "w") as w:
        jdata['features'] = jdata['features'][0:end]
        json.dump(jdata, w)

def process_decimal_files(json_dir: str):
    '''

    :param json_dir:
    :return:
    '''

    jsons = glob.glob(os.path.join(json_dir, "*.json"))
    print("Number of .json files: ", len(jsons))
    for idx, j in enumerate(jsons):
        print(f"Processing {idx} json file: {j}")
        trim_decimal(j)
    print("Done.")


if __name__ == "__main__":
    json_dir = os.getcwd()
    process_decimal_files(json_dir)