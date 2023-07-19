import requests
from pprint import pprint


API_key = 'Sua API_key'

cidade = str(input('Digite o nome da sua cidade: '))

base_url = "url do fornecedor da API_key"+API_key+'&q='+cidade

wheater_data = requests.get(base_url).json()

pprint(wheater_data)