import requests
import re


PRINTER = input("Вставить ip адрес принтера Canon:")
count = 15 # начало записи адресной книги
session = requests.Session()
i0014 = input("Username:")
i0016 = input("Password:")
login_payload = {
    "i0012": 1,
    "i0014": i0014, 
    "i0016": i0016 
}

def extract_token(rt):
    match = re.search(r'name\s*=\s*"?iToken"?\s+value\s*=\s*"?(\d+)"?', rt.text)
    if not match:
        print("Token not found at:", rt.url)
        print(rt.text[:500])
        return None
    return match.group(1)


r = session.post(f"{PRINTER}/checkLogin.cgi", data=login_payload)

print("Login status:", r.status_code)
print("Cookies after login:", session.cookies.get_dict())


rt = session.get(f"{PRINTER}/a_addresslist.html")
token = extract_token(rt)
print("URL:", rt.url)
print("Status:", rt.status_code)
print("Contains iToken:", "iToken" in rt.text)



with open("printer_import.csv", encoding="utf-8") as f:

    for line in f:
        lastname, email = line.strip().split(",")
        

        addresslist = {
        "iToken": token,
        "i2200": count
        }
        r = session.post(f"{PRINTER}/cgi/m_addresslist.cgi", data=addresslist)


        rt = session.get(f"{PRINTER}/a_new.html?no={count}")
        token = extract_token(rt)

        
        a_new = {
        "no": count,
        "iToken": token,
        "i2011": 2,   # str or int? - str worked
        "i2020": count 
        }

        r = session.post(f"{PRINTER}/cgi/a_new.cgi", data=a_new)



        rt = session.get(f"{PRINTER}/a_email_regist.html?no={count}")
        token = extract_token(rt)

        payload = {
            "no": count,
            "iToken": token,
            "i2012": count,
            "i2021": lastname,
            "i2032": email
        }

        r = session.post(f"{PRINTER}/cgi/a_email_regist.cgi", data=payload)
        count += 1
        print("Added:", lastname)
        print("Status:", r.status_code)
        print("Response length:", len(r.text))
         