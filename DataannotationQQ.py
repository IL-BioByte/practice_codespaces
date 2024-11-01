import requests
import pandas as pd

def get_google_doc(url):
    raw_url = url.replace('/edit', '/export?format=html')
    response = requests.get(raw_url)
    return pd.read_html(response.text)

def print_msg(url):
    tables = get_google_doc(url)

    character_data = tables[0]
    grid_dict = {}

    for _, row in character_data.iterrows():
        if row[0] == 'x-coordinate':
            continue
        x = int(row[0]) 
        char = row[1]  
        y = int(row[2])    

        grid_dict[(x, y)] = char 

    max_x = max(x for x, _ in grid_dict.keys())
    max_y = max(y for _, y in grid_dict.keys())

    grid = [[' ' for _ in range(max_x + 1)] for _ in range(max_y + 1)]

    for (x, y), char in grid_dict.items():
        grid[y][x] = char

    for row in grid:
        print(''.join(row))


doc_url = 'URL'
print_msg(doc_url)

BOECMXH