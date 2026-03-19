import requests
import re
import time
import csv




PRINTER_IP = input("Вставить ip адрес принтера Canon:")
count = int(input("Введите начальный номер")) # начало записи адресной книги
session = requests.Session()
i0014 = input("Username:")
i0016 = input("Password:")
login_payload = {
    "i0012": '1',
    "i0014": i0014, 
    "i0016": i0016 
}

def extract_token(reqtoken):
    match = re.search(r'name\s*=\s*"?iToken"?\s+value\s*=\s*"?(\d+)"?', reqtoken.text)
    if not match:
        print("Token not found at:", reqtoken.url)
        print(reqtoken.text[:500])
        return None
    return match.group(1)


req = session.post(f"{PRINTER_IP}/checkLogin.cgi", data=login_payload)

print("Login status:", req.status_code)
print("Cookies after login:", session.cookies.get_dict())


reqtoken = session.get(f"{PRINTER_IP}/a_addresslist.html")
token = extract_token(reqtoken)

with open("printer_import.csv", encoding="utf-8") as f:

    reader = csv.reader(f, delimiter=";")
    for row in reader:
        lastname, email = row

        addresslist = {
        "iToken": token,
        "i2200": count
        }
        req = session.post(f"{PRINTER_IP}/cgi/m_addresslist.cgi", data=addresslist)


        reqtoken = session.get(f"{PRINTER_IP}/a_new.html?no={count}")
        token = extract_token(reqtoken)

        
        a_new = {
        "no": count,
        "iToken": token,
        "i2011": "2", 
        "i2020": count 
        }

        req = session.post(f"{PRINTER_IP}/cgi/a_new.cgi", data=a_new)



        reqtoken = session.get(f"{PRINTER_IP}/a_email_regist.html?no={count}")
        token = extract_token(reqtoken)

        payload = {
            "no": count,
            "iToken": token,
            "i2012": count,
            "i2021": lastname,
            "i2032": email
        }

        req = session.post(f"{PRINTER_IP}/cgi/a_email_regist.cgi", data=payload)
        count += 1
        print(f"Added: {lastname}")
        print(f"Status: {req.status_code}")
        print(f"Response length: {len(req.text)}")
        time.sleep(0.2)
