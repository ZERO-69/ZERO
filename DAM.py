#DALVIK UA_GENERATE_CODE

#CODE BY MUHAMMAD HAMMAD
# MUGHAL ZADA
import platform
import random

import os
import random
def clear():
    os.system('clear')
    print(logo)
#sys.stdout.write('\x1b]2; MAFIA M16 \x07')
logo=(f"""\033[1;37m
 \033[1;32m[\033[1;37m+\033[1;32m] \033[1;37m.88b  d88.  .d8b.  d88888b d888888b  .d8b.  
 \033[1;32m[\033[1;37m+\033[1;32m] \033[1;37m88'YbdP`88 d8' `8b 88'       `88'   d8' `8b 
 \033[1;32m[\033[1;37m+\033[1;32m] \033[1;37m88  88  88 88ooo88 88ooo      88    88ooo88 
 \033[1;32m[\033[1;37m+\033[1;32m] \033[1;37m88  88  88 88~~~88 88~~~      88    88~~~88 
 \033[1;32m[\033[1;37m+\033[1;32m] \033[1;37m88  88  88 88   88 88        .88.   88   88 
 \033[1;32m[\033[1;37m+\033[1;32m] \033[1;37mYP  YP  YP YP   YP YP      Y888888P YP   YP 
 \033[1;32m~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
 \033[1;32m[\033[1;37m+\033[1;32m] \033[1;37mAuthor  : YOUSIF
 \033[1;32m[\033[1;37m+\033[1;32m] \033[1;37mGithub  : MAFIAT-2
 \033[1;32m[\033[1;37m+\033[1;32m] \033[1;37mYOUR UA : USERAGENT
 \033[1;32m[\033[1;37m+\033[1;32m] \033[1;37mFacebook : Youcef hafafni
 \033[1;32m~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
 \033[1;32m[\033[1;37m+\033[1;32m] \033[1;37mCloning ids Saved in MAFIA folder
 \033[1;32m~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~""")
def linex():
    print('\033[1;32m ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')
clear()
print(' \033[1;32m[\033[1;37m+\033[1;32m] \033[1;37mYOUR UA \033[97;1m[\033[1;32mUSERAGENT\033[97;1m] \033[1;32mLIST HERE\n\033[1;97m==================================================')
def generate_custom_user_agent():
    android_versions = ["Android 9", "Android 10", "Android 11", "Android 12"]
    selected_android_version = random.choice(android_versions)

    manufacturers = [
        "TECNO", "Samsung", "Xiaomi", 
       
    ]
    selected_manufacturer = random.choice(manufacturers)

    android_models = {
        "TECNO": ["KE5", "Model2", "Model3"],
        "Samsung": ["Galaxy S21", "Galaxy Note 20", "Galaxy A52"],
        "Xiaomi": ["Redmi Note 10", "POCO X3"],
        }

    selected_model = random.choice(android_models.get(selected_manufacturer, []))

    device_names = {
        "TECNO": "TecnoDevice",
        "Samsung": "SamsungDevice",
        "Xiaomi": "XiaomiDevice",
       
    }

    device_name = device_names.get(selected_manufacturer, "DefaultDevice")

    build_number = random.randint(1000, 9999)

    app_packages = ["com.facebook.katana", "com.facebook.ocra", "com.facebook.mlite"]
    selected_app_package = random.choice(app_packages)

    density_version = round(random.uniform(1.0, 3.0), 1)
    height_version = random.randint(500, 2000)
    width_version = random.randint(300, 1500)

    user_agent = (
        f"\033[1;32mDalvik/2.1.0 (Linux; U; {selected_android_version} Build/{build_number}; {selected_manufacturer} {selected_model})"
        f" [FBAN/{random.randint(100, 999)}.{random.randint(1, 9)}.{random.randint(0, 9)}.0;FBBV/{random.randint(100000000, 999999999)};FBRV/{random.randint(0, 9)};"
        f"{selected_app_package};FBLC/en_US;FBMF/{selected_manufacturer};FBBD/{selected_manufacturer};FBDV/{selected_model};"
        f"FBSV/{random.randint(8, 12)};FBCA/armeabi-v7a:armeabi;FBDM/{{density={density_version},width={width_version},height={height_version}}};FB_FW/{random.randint(1, 3)};]"
    )

    return user_agent

# Example usage
custom_user_agent = generate_custom_user_agent()
print(custom_user_agent)