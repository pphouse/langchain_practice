import openai
import os


openai.api_key = os.environ["OPENAI_API_KEY"]

res = openai.ChatCompletion.create(
    model="gpt-3.5-turbo",
    temperature=0.1,
    messages=[
        {"role": "system", "content": "pythonコードのみを出力して。日本語などの説明部分は出力しない。"},
        {"role": "user", "content": "bitcoinの日本円に換算した現在価格を取得するpythonコード"},
    ],
)

print(res)
print("-------------------------")
script = res["choices"][0]["message"]["content"]
print(type(script))
print(script)

with open("./log.txt", "w") as f:
    f.write(str(script))
