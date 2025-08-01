import os
import glob
import xml.etree.ElementTree as ET
import json

def load_config(config_path: str):
    with open(config_path, 'r', encoding='utf-8') as f:
        return json.load(f)

def remove_xml_tags(input_dir: str, output_dir: str, error_dir: str):
    ns = {"nfe": "http://www.portalfiscal.inf.br/nfe"}
    os.makedirs(output_dir, exist_ok=True)
    os.makedirs(error_dir, exist_ok=True)

    files = glob.glob(os.path.join(input_dir, "*.xml"))

    for path in files:
        try:
            tree = ET.parse(path)
        except ET.ParseError:
            os.rename(path, os.path.join(error_dir, os.path.basename(path)))
            continue

        root = tree.getroot()
        if root.tag.endswith("retArquivoXML"):
            proc = root.find("nfe:proc", ns)
            if proc is None:
                os.rename(path, os.path.join(error_dir, os.path.basename(path)))
                continue

            nfe_proc = proc.find("nfe:nfeProc", ns)
            if nfe_proc is None:
                os.rename(path, os.path.join(error_dir, os.path.basename(path)))
                continue

            for elem in nfe_proc.iter():
                if '}' in elem.tag:
                    elem.tag = elem.tag.split('}', 1)[1]

            output_path = os.path.join(output_dir, os.path.basename(path))
            ET.ElementTree(nfe_proc).write(output_path, encoding="utf-8", xml_declaration=True)
        else:
            os.rename(path, os.path.join(error_dir, os.path.basename(path)))

if __name__ == "__main__":
    config = load_config("config.json")
    remove_xml_tags(config["input_folder"], config["output_folder"], config["error_folder"])
