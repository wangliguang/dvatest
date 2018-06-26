
import os

print os.getcwd()
print os.getcwd()[-7:]

def get_base_path():
    return '../..' if os.getcwd()[-7:] == 'pyTools' else '.'


