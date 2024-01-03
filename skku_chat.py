from get_titles import get_titles
import json
import requests

kakao_filename = "C:/Users/admin/OneDrive/바탕 화면/작업/23년도 2학기/proj/kakao_token.json"

def load_tokens(filename):
    with open(filename) as fp:
        tokens = json.load(fp)
    return tokens
tokens = load_tokens(kakao_filename)

titles = get_titles()

cnt = 0
for i in titles:
    if cnt == 0:
        title1 = str(i.text.strip())
        cnt += 1
    elif cnt == 1:
        title2 = str(i.text.strip())
        cnt += 1
    elif cnt == 2:
        title3 = str(i.text.strip())
        cnt += 1
    else:
        break

url = "https://kapi.kakao.com/v2/api/talk/memo/default/send"

headers = {
    "Authorization" : "Bearer " + tokens['access_token']
}

title_text = title1+"\n"+title2+"\n"+title3
data = {
    "template_object" : json.dumps({
        "object_type" : "text",
        "text" : title_text,
        "link" : {
            "web_url" : "https://sco.skku.edu/sco/community/major_info.do"
        }
    })
}

response = requests.post(url, headers = headers, data= data)
print(response.status_code)

if response.status_code != 200:
    print("error!", response.json())
else:
    print("success")