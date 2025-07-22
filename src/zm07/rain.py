def get_rain_probability():
    """Yahoo天気から堺市の降水確率を取得"""
    try:
        url = "https://weather.yahoo.co.jp/weather/jp/27/6200/27141.html"
        headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36'}
        
        response = requests.get(url, headers=headers)
        soup = BeautifulSoup(response.content, 'html.parser')
        
        # 降水確率を取得
        max_prob = 0
        
        # 方法1: 降水確率のクラスから取得
        prob_elements = soup.find_all('td', class_='prob')
        for elem in prob_elements:
            text = elem.get_text(strip=True)
            if '%' in text:
                num = re.search(r'\d+', text)
                if num:
                    max_prob = max(max_prob, int(num.group()))
        
  
        
        return max_prob
        
    except:
        return None

