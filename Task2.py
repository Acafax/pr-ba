import json
import yaml
import os
import sys
import xml.etree.ElementTree as ET
"""source_path =  sys.argv[1] # ŚCIEZKA ŹRÓDŁOWA
dest_path = sys.argv[2] #ściezka docelowa

source_ext = os.path.splitext(source_path)[1] # czy źródłowa to json, yaml, xml 
dest_ext = os.path.splitext(dest_path)[1] # czy docelowa to json, yaml, xml

def odczyt_json(source_path):
    try:
        with open(source_path, 'r') as file:
            tekst = json.load(file)
            return tekst
            
    except FileNotFoundError:
        print(f"błąd nie znaleziono pliku")
        return None
    except json.JSONDecodeError:
        print(f"Nie poprawna składnia {source_path} prosze ją poprawić {str(json.JSONDecodeError)}")
        return None
  """  
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

        
   
source_path =  sys.argv[1]
dest_path = sys.argv[2]
konwersja(source_path, dest_path)
