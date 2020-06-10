import requests

cookies = {
    'ci_session': 'a12ae902340e957551907d287259e01cc4d2b3c0',
    '_ga': 'GA1.2.1198243042.1591679055',
    '_gid': 'GA1.2.160880471.1591679055',
}

headers = {
    'Host': 'api3.goodchoice.kr',
    'Accept': 'application/json, text/javascript, */*; q=0.01',
    'X-Requested-With': 'XMLHttpRequest',
    'Accept-Language': 'ko-kr',
    'Accept-Encoding': 'gzip, deflate',
    'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
    'Origin': 'https://api3.goodchoice.kr',
    'User-Agent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 13_3_1 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E148',
    'Connection': 'close',
    'Referer': 'https://api3.goodchoice.kr/event3/main/adEventView?aevno=970&version=3.38.11',
    'Content-Length': '151',
}

data = 'aevno=970&uno=8762970&coupon_type=half&coupon_string=B_MKT_EVT_NO970_HOPE_110&coupon_string_type=cpn_code&deviceId=A39822C9-BA8E-4A6B-95C7-5D9826B31E85'

response = requests.post('https://api3.goodchoice.kr/event3/main/issueDeviceCheckingCoupon', headers=headers, cookies=cookies, data=data)
print(response.json()['msg'])
