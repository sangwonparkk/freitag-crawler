import json
import requests
import threading
import datetime

from refresh_access import tokens

from selenium import webdriver


def get_new_items():
    driver.refresh()
    try:
        driver.find_element_by_css_selector(
            '#block-freitag-content > article > section:nth-child(2) > div > div > div > div > div > div > div > div > a > div > span').click()
    except:
        pass
    new_items = []
    for item in driver.find_elements_by_css_selector(
            '#block-freitag-content > article > section:nth-child(2) > div > div > div > div > div > div > div > div > div > div.flex.flex-wrap > div:nth-child(n) > div > img'):
        image_src = item.get_attribute('src')
        if image_src not in curr_items:
            new_items.append(image_src)
            curr_items.append(image_src)
    return new_items


def send_api(lists):
    url = "https://kapi.kakao.com/v2/api/talk/memo/default/send"

    # 사용자 토큰
    headers = {
        "Authorization": "Bearer " + tokens['access_token']
    }

    lists = [{"title": '가방',
              "description": '새로운거',
              "image_url": str(elem),
              "image_width": 50, "image_height": 50,
              "link": {
                  "web_url": "www.freitag.ch/en/f11"
              }} for elem in lists]

    template = {
        "object_type": "list",
        "header_title": "Lassie",
        "header_link": {
            "web_url": "www.freitag.ch/en/f11",
            "mobile_web_url": "www.freitag.ch/en/f11"
        },
        "contents": lists,
        "buttons": [
            {
                "title": "웹으로 이동",
                "link": {
                    "web_url": "www.freitag.ch/en/f11",
                    "mobile_web_url": "www.freitag.ch/en/f11"
                }
            }
        ]

    }

    data = {
        "template_object": json.dumps(template)
    }

    response = requests.post(url, data=data, headers=headers)
    if response.json().get('result_code') == 0:
        print('Success!')
        print(datetime.datetime.now().time())
    else:
        print('Failed. Error Message: ' + str(response.json()))
        print(datetime.datetime.now().time())


def call():
    new_items = get_new_items()
    print('called')
    if new_items:
        for i in range(0, len(new_items) // 3 + 1):
            if new_items[i * 3:(i + 1) * 3]:
                send_api(new_items[i * 3:(i + 1) * 3])
    else:
        print('Nothing New')
        print(datetime.datetime.now().time())

    threading.Timer(60, call).start()


if __name__ == "__main__":
    driver = webdriver.Chrome(executable_path=r'C:\Users\Sangwon\Desktop\freitag-crawler\chromedriver.exe')
    url = 'https://www.freitag.ch/en/f11'
    driver.get(url)
    # driver.find_element_by_css_selector('body > div:nth-child(6) > div > div > div:nth-child(3) > a').click()
    curr_items = []
    call()

