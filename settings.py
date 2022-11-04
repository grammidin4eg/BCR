import configparser

config = configparser.ConfigParser()
config.read('settings.ini')
print(config['DISPLAY']['MODE'] )
# config['DEFAULT']['path'] = '/var/shared/'    # update
# config['DEFAULT']['default_message'] = 'Hey! help me!!'   # create

def saveSettings():
    with open('settings.ini', 'w') as configfile:
        config.write(configfile)

#[DISPLAY]
#MODE=WINDOW / FULLSCREEN

#[SOUND]
#volume=0

#[CONTROLS]
#