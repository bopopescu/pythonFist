
import configparser

config = configparser.ConfigParser()
config['DEFAULT'] = {'ServerAliveInterval': '45', 'Compression': 'yes', 'CompressionLevel': '9'}
# config[]

config.sections()
print(config.read('example.ini'))
print(config.sections())

print('bitbucket.org' in config)
