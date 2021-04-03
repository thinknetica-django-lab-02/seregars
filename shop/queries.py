from main.models import Product, Category

Product.objects.filter(category=Category.objects.get(title='Smartphones'))
Product.objects.filter(category=Category.objects.get(title='Notebooks'))
Product.objects.filter(category=Category.objects.get(title='TV'))
Product.objects.filter(category=Category.objects.get(title='Accessories'))
