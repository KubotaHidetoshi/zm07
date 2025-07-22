import requests
import re

def get_rain():
    try:
        url = "https://weather.yahoo.co.jp/weather/jp/27/6200/27141.html"
        headers = {'User-Agent': 'Mozilla/5.0'}
        
        response = requests.get(url, headers=headers)
        html = response.text
        
        # HTMLから降水確率を正規表現で抽出
        patterns = [
            r'降水確率[^>]*>(\d+)%',
            r'prob[^>]*>(\d+)%',
            r'>(\d+)%</td>'
        ]
        
        max_prob = 0
        for pattern in patterns:
            matches = re.findall(pattern, html)
            for match in matches:
                prob = int(match)
                if prob <= 100:  # 有効な確率のみ
                    max_prob = max(max_prob, prob)
        
        return max_prob
        
    except Exception as e:
        return None

if __name__ == "__main__":
    prob = get_rain()
    if prob is not None:
        print(f"{prob}%")
    else:
        print("取得失敗")