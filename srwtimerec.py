from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from time import sleep
from datetime import datetime
from argparse import ArgumentParser


parser = ArgumentParser()
parser.add_argument('username')
parser.add_argument('password')
parser.add_argument('mode')

if __name__ == "__main__":
    holidays = set([
        "23-08-11",
        "23-08-14",
        "23-08-15"
    ])
    today = datetime.now().strftime("%y-%m-%d")
    assert today not in holidays, 'holiday'
    args = parser.parse_args()
    options = Options()
    options.add_argument("--headless=new")
    options.add_experimental_option("excludeSwitches", ["enable-logging"])
    web = webdriver.Chrome(options=options)

    web.get("https://ut-ppsweb.adm.u-tokyo.ac.jp/cws/srwtimerec")
    sleep(5)
    assert web.title == 'WEB打刻', 'Cannot fetch website'

    uname = web.find_element(By.NAME, 'user_id')
    passw = web.find_element(By.NAME, 'password')
    in_button = web.find_element(By.NAME, 'syussya')
    out_button = web.find_element(By.NAME, 'taisya')

    uname.send_keys(str(args.username))
    passw.send_keys(str(args.password))

    if args.mode == 'in':
        web.execute_script("arguments[0].click();", in_button)
        print(f'logged in {today}')
    else:
        web.execute_script("arguments[0].click();", out_button)
        print(f'logged out {today}')
