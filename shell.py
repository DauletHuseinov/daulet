from shop.models import Item, Purchase

item_1 = Item.objects.create(name='Korea', price=10000)
item_2 = Item.objects.create(name='New York', price=20000)
item_3 = Item.objects.create(name='Japan', price=30000)
item_4 = Item.objects.create(name='Russia', price=40000)
item_5 = Item.objects.create(name='Africa', price=50000)
item_6 = Item.objects.create(name='Kazakstan', price=60000)
item_7 = Item.objects.create(name='Uzbekistan', price=70000)
item_8 = Item.objects.create(name='Tadjikistan', price=80000)
item_9 = Item.objects.create(name='Kyrgyzstan', price=90000)
item_10 = Item.objects.create(name='America', price=100000)


item_10.purchase.create(name='Daulet', age=16)
item_4.purchase.create(name='Buster', age=24)
item_5.purchase.create(name='SpiderMan', age=20)
item_5.purchase.create(name='Marvel', age=34)
item_3.purchase.create(name='Isa', age=23)
item_8.purchase.create(name='Iron Man', age=25)
item_8.purchase.create(name='SAb', age=25)
item_8.purchase.create(name='Wera', age=23)
item_8.purchase.create(name='Sasha', age=25)
item_8.purchase.create(name='Ira', age=25)
item_10.purchase.create(name='Ali', age=16)
item_4.purchase.create(name='Gena', age=24)
item_5.purchase.create(name='Max', age=20)
item_5.purchase.create(name='Korj', age=34)
item_3.purchase.create(name='Muha', age=23)
item_8.purchase.create(name='Qwerty', age=25)
item_8.purchase.create(name='Galileo', age=25)
item_8.purchase.create(name='Panda', age=25)
item_8.purchase.create(name='Kastiel', age=25)
item_8.purchase.create(name='Ha1sse', age=25)


q.choices.all()

