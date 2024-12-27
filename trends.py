from pytrends.request import TrendReq
import pandas as pd
import time

# 初始化 pytrend
pytrend = TrendReq(hl='en-US', tz=360)

# 關鍵字清單
keywords = [
    'shiba-inu', 'pepe', 'bonk', 'floki', 'mog-coin', 'spx6900', 'baby-doge-coin', 'turbo',
    'neiro-3', 'memecoin-2', 'pepecoin-2', 'corgiai', 'andy-the-wisguy', 'constitutiondao',
    'apu-s-club', 'non-playable-coin', 'degen-base', 'landwolf-0x67', 'shiro-neko-2',
    'harrypotterobamasonic10in', 'department-of-government-efficiency', 'osaka-protocol',
    'milady-cult-coin', 'game-stop', 'bone-shibaswap', 'dogelon-mars', 'puff-the-dragon',
    'rekt-4', 'pepe-unchained', 'milady-meme-coin', 'maga', 'wojak', 'bobo-coin', 'patriot',
    'the-doge-nft', 'moo-deng-2', 'ninja-squad', 'hoppy-meme', 'peipeicoin-vip', 'pikaboss',
    'neiro-on-eth', 'kishu-inu', 'grok-2', 'gameswift', 'amaterasu-omikami', 'kendu-inu',
    'illuminaticoin', 'lmeow-2', 'zero-tech', 'leash', 'feg-token-2', 'shrub', 'pepefork',
    'squidgrow-2', 'spunkysdx', 'maga-hat', 'joe-coin', 'terminus-2', 'catslap',
    'volt-inu-2', 'kiboshib', 'bitbonk', 'musmecoin', 'mystery-2', 'phil',
    'strategic-bitcoin-reserve', 'katana-inu', 'max-on-eth', 'mstr2100', 'bob-token',
    'zyncoin-2', 'dogecast', 'dogecast', 'jesus-coin', 'trog', 'catecoin', 'pepe-2-0',
    'the-balkan-dwarf', 'brett-memecoin', 'ryujin', 'catcoin-cash', 'troll', 'bad-idea-ai',
    'wrapped-ayeayecoin', 'frogevip', 'hoge-finance', 'nya', 'marvin-inu-2', 'kizuna',
    'astropepex', 'og-roaring-kitty', 'feisty-doge-nft', 'luffy-inu', 'tomo-cat', 'bobacat',
    'bird-dog', 'fleabone', 'byte', 'i-love-puppies', 'drip'
]

important_keywords = ['SHIB', 'PEPE', 'BONK', 'FLOKI', 'MOG']

# 將關鍵字分組，每組最多 5 個
#groups = [keywords[i:i + 5] for i in range(0, len(keywords), 5)]

# 時間範圍
timeframe = '2024-01-01 2024-12-21'

# 儲存所有分組查詢的結果
all_data = []

#print(groups[0])
pytrend.build_payload(kw_list=important_keywords, timeframe=timeframe, geo='')
data = pytrend.interest_over_time()

# 確保數據不是空的
if not data.empty:
    # 去掉 'isPartial' 欄位
    data = data.drop(columns=['isPartial'])

    # 顯示數據
    print(data)

    # 儲存結果為 CSV 文件
    data.to_csv('google_trends_data.csv', index=True)
    print("結果已保存為 'google_trends_data.csv'")
else:
    print("沒有找到符合條件的資料")

'''
# 查詢每組關鍵字
for group in groups:
    pytrend.build_payload(kw_list=group, timeframe=timeframe, geo='')
    data = pytrend.interest_over_time()
    if not data.empty:
        data = data.drop(columns=['isPartial'])  # 去掉 isPartial 欄位
        all_data.append(data)
    time.sleep(20)  # 避免請求過快導致封鎖

# 合併所有查詢結果
final_data = pd.concat(all_data, axis=1)

# 去掉重複的日期欄位
final_data = final_data.loc[:, ~final_data.columns.duplicated()]

# 儲存結果到 CSV
output_file = "google_trends_data.csv"
final_data.to_csv(output_file, index=True)
print(f"結果已保存為 CSV 文件：{output_file}")

# 將數據轉為 Python 格式（如字典）
final_result = final_data.reset_index().to_dict(orient='records')
print(final_result)'''    
