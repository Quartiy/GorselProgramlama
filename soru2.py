import re


web = input("Siteyi gir: ")
if 'www' and 'com' in web:
    print("bu bir url " + web)
elif 'www' and 'org' in web:
    print("bu bir url " + web)
elif 'www' and 'net' in web:
    print("bu bir url " + web)
elif 'www' and 'gov' in web:
    print("bu bir url " + web)
else:
    print("bu bir url değil " + web)
