import urllib3

http = urllib3.PoolManager()
pagina = http.request('GET', 'http://www.iaexpert.com.br/teste')

# print(pagina.status) <-- Resposta HTTP

print(pagina.data)