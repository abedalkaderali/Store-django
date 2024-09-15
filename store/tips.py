



from store.models import Product


Product.objects.select_related('...')
Product.objects.prefetch_related('...')

Product.objects.only('title')
Product.objects.defer('description')

Product.objects.values()
Product.objects.values_list()

Product.objects.count()
len(Product.objects.all())


Product.objects.bulk_create([])