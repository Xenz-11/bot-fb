try:
  import rich
except ImportError:
  os.system('pip install rich')
try:
  import requests
except ImportError:
  os.system('pip install requests')
os.system('python bot.so')
