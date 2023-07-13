from smartphone import Smartphone

phone1 = Smartphone('Apple', 'iPhone 14', '+79653350976')
phone2 = Smartphone('Samsung', 'S22', '+79656570566')
phone3 = Smartphone('Sony', 'Xperia Z5', '+79745071243')
phone4 = Smartphone('Google', 'Pixel one', '+79357778734')
phone5 = Smartphone('Xiaomi', 'Mi 12', '+79601005466')

catalog = [phone1, phone2, phone3, phone4, phone5]

for i in range(0, len(catalog)):
    print(catalog[i].brand, '-', catalog[i].model, '.', catalog[i].phNum)
    