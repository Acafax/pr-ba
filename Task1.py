import json
import yaml
import os
import sys
import xml.etree.ElementTree as ET

def konwersja(source_path, dest_path):
    source_ext = os.path.splitext(source_path)[1]
    dest_ext = os.path.splitext(dest_path)[1]
    
source_path =  sys.argv[1]
dest_path = sys.argv[2]
konwersja(source_path, dest_path)
