import pandas # type: ignore
import random
from datetime import datetime

def select_todays_zodiac(excel_file_path):
    """
    エクセルファイルから12星座を読み込み、今日のおすすめ星座をランダムで選択する
    
    Args:
        excel_file_path (str): 星座一覧が入ったエクセルファイルのパス
    
    Returns:
        str: 選択された星座名
    """
    try:
        # エクセルファイルを読み込み
        df = pd.read_excel(excel_file_path)
        
        # 星座一覧を取得（最初の列を使用）
        zodiac_list = df.iloc[:, 0].tolist()
        
        # 今日の日付を取得
        today = datetime.now().strftime('%Y-%m-%d')
        
        # 今日の日付をシードとしてランダムを初期化（同じ日なら同じ結果）
        random.seed(today)
        
        # ランダムで星座を選択
        selected_zodiac = random.choice(zodiac_list)
        
        return selected_zodiac
        
    except FileNotFoundError:
        print(f"エラー: ファイル '{excel_file_path}' が見つかりません。")
        return None
    except Exception as e:
        print(f"エラーが発生しました: {e}")
        return None

def create_sample_excel(file_path="zodiac_list.xlsx"):
    """
    サンプル用の12星座エクセルファイルを作成する
    
    Args:
        file_path (str): 作成するエクセルファイルのパス
    """
    zodiac_signs = [
        "牡羊座", "牡牛座", "双子座", "蟹座", "獅子座", "乙女座",
        "天秤座", "蠍座", "射手座", "山羊座", "水瓶座", "魚座"
    ]
    
    df = pd.DataFrame({"星座名": zodiac_signs})
    df.to_excel(file_path, index=False)
    print(f"サンプルファイル '{file_path}' を作成しました。")

def main():
    # サンプルファイルを作成
    sample_file = "zodiac_list.xlsx"
    create_sample_excel(sample_file)
    
    # 今日のおすすめ星座を選択
    todays_zodiac = select_todays_zodiac(sample_file)
    
    if todays_zodiac:
        today_date = datetime.now().strftime('%Y年%m月%d日')
        print(f"\n{today_date}の今日のおすすめ星座は...")
        print(f"🌟 {todays_zodiac} 🌟")
        print("素敵な一日をお過ごしください！")

# メイン実行
if __name__ == "__main__":
    main()