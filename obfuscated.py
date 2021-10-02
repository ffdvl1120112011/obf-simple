# -*- coding: UTF-8 -*-

##################################################################
#                             OPEN SOURCE                        #
#                                                                #                                                               
#                                                                #
#    BOLEH DI RECOD TAPI CANTUMKAN NAMA AUTHOR YA KONTOL         #
#                                                                #
#               AUTHOR > Boy Hamzah                              #
#               GITHUB   > https://github.com/BOY-H4MZ4H         #
#               FACEBOOK > https://github.com/Boy.Hamzaah        #
#               TEAM  > XNSCODE                                  #
#                                                                #
#                                                                #
##################################################################

import os
import base64
from sys import argv

OFFSET = 150
VARIABLE_NAME = '__BOY__HAMZAH__' * 350

def obfuscate(content):
    b64_content = base64.b64encode(content.encode()).decode()
    index = 0
    code = f'{VARIABLE_NAME} = ""\n'
    for _ in range(int(len(b64_content) / OFFSET) + 1):
        _str = ''
        for char in b64_content[index:index + OFFSET]:
            byte = str(hex(ord(char)))[2:]
            if len(byte) < 2:
                byte = '0' + byte
            _str += '\\x' + str(byte)
        code += f'{VARIABLE_NAME} += "{_str}"\n'
        index += OFFSET
    code += f'exec(__import__("\\x62\\x61\\x73\\x65\\x36\\x34").b64decode({VARIABLE_NAME}.encode("\\x75\\x74\\x66\\x2d\\x38")).decode("\\x75\\x74\\x66\\x2d\\x38"))'
    return code

def main():
    print('\n\n____ ___  ____ _  _ ____ ____ ____ ___ ____ ___  \n|  | |__] |___ |  | [__  |    |__|  |  |___ |  \ \n|__| |__] |    |__| ___] |___ |  |  |  |___ |__/ ')
    print('\nAU > Boy Hamzah')
    print('GH > https://github.com/BOY-H4MZ4H')
    print('FB > https://github.com/Boy.Hamzaah')
    print('TM > XNSCODE')
    print('')

    try:
        path = argv[1]
        if not os.path.exists(path):
            print('\nFile not found')
            exit()

        if not os.path.isfile(path) or not path.endswith('.py'):
            print('\nInvalid file')
            exit()
        
        with open(path, 'r', encoding='utf-8', errors='ignore') as file:
            file_content = file.read()

        obfuscated_content = obfuscate(file_content)

        with open(f'{path.split(".")[0]}.obfuscated.py', 'w') as file:
            file.write(obfuscated_content)

        print('\nSucceed')
    except:
        print(f'\nUsage > python {argv[0]} file.py')

if __name__ == '__main__':
    main()
