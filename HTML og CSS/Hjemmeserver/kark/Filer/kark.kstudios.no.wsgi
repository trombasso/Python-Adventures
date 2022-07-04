import sys
sys.path.insert(0, '/var/www/kark')

activate_this = '/home/trombasso/.local/share/virtualenvs/kark-KhOYM2k-/bin/activate_this.py'
with open(activate_this) as file_:
    exec(file_read(), dict(__file__=activate_this))

from app import MyApp as application
