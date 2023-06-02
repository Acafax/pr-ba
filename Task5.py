import json
import yaml
import os
import sys
import xml.etree.ElementTree as ET
from json2xml import json2xml
import xmltodict
source_path = sys.argv[1]  # ŚCIEZKA ŹRÓDŁOWA
dest_path = sys.argv[2]  # ściezka docelowa

# czy źródłowa to json, yaml, xml
source_ext = os.path.splitext(source_path)[1]
dest_ext = os.path.splitext(dest_path)[1]  # czy docelowa to json, yaml, xml

# =================================BLOK JSON


def odczyt_json(source_path):
    try:
        with open(source_path, 'r') as file:
            tekst = json.load(file)
            json_zamiana(tekst, dest_ext, dest_path)
            return tekst

    except FileNotFoundError:
        print(f"błąd nie znaleziono pliku")
        return None
    except json.JSONDecodeError:
        print(
            f"Nie poprawna składnia tekstu pliku {source_path} prosze ją poprawić {str(json.JSONDecodeError)}")
        return None


def json_zamiana(tekst, dest_ext, dest_path):
    if dest_ext == ".yaml":
        with open(dest_path, "w") as yaml_f:
            yaml.dump(tekst, yaml_f)

    elif dest_ext == ".xml":
        xml = json2xml.Json2xml(tekst).to_xml()
        with open(dest_path, "w") as xml_f:
            xml_f.write(xml)
    else:
        print("Coś poszło nie tak")

# ======================== BLOK YAML


def odczyt_yaml(source_path, dest_ext, dest_path):
    try:
        with open(source_path, 'r') as file:
            tekst = file.read()
            # zamienia zawartość pliku yaml na coś bardzije zjadliwego
            zmienna_yaml = yaml.safe_load(tekst)
            yaml_zamiana(zmienna_yaml, dest_ext, dest_path,)
    except FileNotFoundError:
        print(f"Nie znaleziono ścieżki do pliku {source_path}")


def yaml_zamiana(zmienna_yaml, dest_ext, dest_path):
    if dest_ext == ".json":
        with open(dest_path, "w") as json_f:
            json.dump(zmienna_yaml, json_f)
    elif dest_ext == ".xml":
        xml = json2xml.Json2xml(zmienna_yaml).to_xml()
        with open(dest_path, "w") as xml_f:
            xml_f.write(xml)
    else:
        return "coś poszło nie tak"
    
if os.path.exists(source_path) == True and os.path.exists(dest_path) == True:

    if source_ext == ".json":
        odczyt_json(source_path)
    elif source_ext == ".yaml":
        odczyt_yaml(source_path, dest_ext, dest_path)
    else:
        print("Coś poszło nie tak")
    

# sprawda czy ściezki są prawdziwe
if os.path.exists(source_path) != True or os.path.exists(dest_path) != True:
    print("poszczególne pliki nie istnieją albo ścieżki nie są poprawne")
    input("Naciśnij enter aby zakończyć")
if source_path == dest_path:
    print(f"BŁĄD ścieżka początkowa {source_path} i ścieżka końcowa {dest_path} są identyczne")
    input("Naciśnij enter aby zakończyć")