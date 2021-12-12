from pathlib import Path
import json
from typing import Any, Dict
import requests
import hashlib
import sys

if len(sys.argv) < 2:
    print("Usage: fix-assets.py GLOB_TO_PROCESS")
    sys.exit(1)

def scan_dict_item(item: Dict[Any, Any]):
    for k, v in list(item.items()):
        if isinstance(v, dict):
            scan_dict_item(v)
        if isinstance(v, list):
            for item in v:
                if isinstance(item, dict):
                    scan_dict_item(item)
        if isinstance(k, str):
            if k == "size":
                resp = requests.get(item["url"])
                resp.raise_for_status()
                data = resp.content
                item["size"] = len(data)
                if "sha1" in item:
                    item["sha1"] = hashlib.sha1(data).hexdigest()
                if "sha256" in item:
                    item["sha256"] = hashlib.sha256(data).hexdigest()


for file in Path(".").glob(sys.argv[1]):
    print(file)
    with open(file) as f:
        data = json.load(f)
    scan_dict_item(data)
    with open(file, "w") as f:
        json.dump(data, f, indent=4, sort_keys=True)
