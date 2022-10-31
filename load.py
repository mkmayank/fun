#!/usr/bin/env python
import yaml
import requests

response = requests.get('https://raw.githubusercontent.com/mkmayank/fun/main/main.yml')
print(yaml.safe_load(response.text))
