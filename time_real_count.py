import time
""""burada bilgisayar satimizi kullanarak oradaki dk bilgisine 15 dk ekleyecek ve şimiki
zamanı bir b değerine atarak bir işlemin 15dk boyunca yapılmasını sağladım.
"""
print(time.strftime('%H:%M:%S'))#saat dakika saniye şeklinde verilmiş
a=int(time.strftime('%M'))#suan ki zamandaki  dakikayı a değerine atadım
a=a+3
b = int(time.strftime('%M'))
while b<=a:
    b = int(time.strftime('%M'))
    print("b =",b)



