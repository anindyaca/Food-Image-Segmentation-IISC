# using wget package to import data from link
# other methods of importing is using package -- urllib3




import requests


url = 'http://www.ivl.disco.unimib.it/download/http://www.ivl.disco.unimib.it/minisites/UNIMIB2016/UNIMIB2016-images.zip'
df_food = requests.get(url, allow_redirects = True)