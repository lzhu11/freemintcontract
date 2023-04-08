import json

# Python 的 dict 類型資料
for i in range(0,100):
    myDict = {
    "name": "#"+str(i),
    "image": "ipfs://QmR5aj1mDf5y973SDQYT23MbQQWEVzQGGqhgNQnyhwcSYN/"+str(i)+".png",
    "description": "This NFT collection is created by WINCAN",
    "external_url": "http://wincan.choice-client2252.com/",
    "attributes": [
        {
        "trait_type": "number",
        "value": str(i)
        },
        {
        "trait_type": "creator",
        "value": "WINCAN"
        }
    ]
    }

    # 將 Python 資料轉為 JSON 格式，儲存至 output.json 檔案
    with open(str(i)+".json", "w") as f:
        json.dump(myDict, f, indent = 4)