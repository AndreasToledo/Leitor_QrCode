from core.storage import load_data, save_data

data = load_data()

def process_code(code):
    if not code:
        return 0
    data[code] = data.get(code, 0) + 1
    save_data(data)
    return data[code]