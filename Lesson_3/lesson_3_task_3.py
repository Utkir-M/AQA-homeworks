from address import Address
from mailing import Mailing

adr1 = Address(104328, 'Мой город', 'Моя улица', 77, 15)
adr2 = Address(987123, 'Не мой город', 'Не моя улица', 27, 5)

mailing1 = Mailing(adr1, adr2, 1000, '005466')

print(
    'Отправление', 
    mailing1.track, 
    'из', 
    mailing1.from_address.index,',',
    mailing1.from_address.city, ',', 
    mailing1.from_address.street, ',', 
    mailing1.from_address.house, '-', mailing1.from_address.apart, 
    'в', 
    mailing1.to_address.index, ',',
    mailing1.to_address.city, ',', 
    mailing1.to_address.street, ',', 
    mailing1.to_address.house, '-', mailing1.to_address.apart,'.', 
    'Стоимость', mailing1.cost, 'рублей.'
    )