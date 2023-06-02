import json
import yaml
import os
import sys
import xml.etree.ElementTree as ET
from json2xml import json2xml
source_path =  sys.argv[1] # ŚCIEZKA ŹRÓDŁOWA
dest_path = sys.argv[2] #ściezka docelowa

source_ext = os.path.splitext(source_path)[1] # czy źródłowa to json, yaml, xml 
dest_ext = os.path.splitext(dest_path)[1] # czy docelowa to json, yaml, xml


def odczyt_json(source_path):
    try:
        with open(source_path, 'r') as file:
            tekst = json.load(file)
            json_zamiana(tekst,dest_ext, dest_path)
            return tekst
            
    except FileNotFoundError:
        print(f"błąd nie znaleziono pliku")
        return None
    except json.JSONDecodeError:
        print(f"Nie poprawna składnia {source_path} prosze ją poprawić {str(json.JSONDecodeError)}")
        return None

def json_zamiana(tekst,dest_ext, dest_path):
    if dest_ext == ".yaml":
        with open(dest_path, "w") as yaml_f:
            yaml.dump(tekst,yaml_f)

    elif dest_ext == ".xml":
        xml= json2xml.Json2xml(tekst).to_xml()
        with open(dest_path, "w") as xml_f:
            xml_f.write(xml)
    else:
        print("Coś poszło nie tak")


odczyt_json(source_path)