import requests
import pandas as pd

API_URL = "https://api.coincap.io/v2/assets"

def fetch_crypto_data():
    response = requests.get(API_URL)
    
    if response.status_code == 200:
        data = response.json().get('data', [])  # API’den gelen 'data' listesini al
        return data
    else:
        print(f"API Hatası: {response.status_code}")
        return []

def save_to_excel(crypto_data):
    # DataFrame oluştur
    df = pd.DataFrame(crypto_data)
    
    # Excel dosyasına kaydet
    df.to_excel("crypto_data.xlsx", index=False)
    print("Veriler başarıyla 'crypto_data.xlsx' dosyasına kaydedildi.")
    print("aga karisti")
def main():
    crypto_data = fetch_crypto_data()
    #git icin deneme
    # 'search': crypto_symbol şeklinde her bir kripto varlığını listele
    formatted_data = [{"search": asset.get("symbol", ""), "name": asset.get("name", "")} for asset in crypto_data]
    
    save_to_excel(formatted_data)

  
if __name__ == "__main__":
    main()
