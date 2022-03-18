"""
SELECT * FROM product;
Product.object.all()

SELECT id, name FROM product;
Product.objects.only('id', 'name')

SELECT description, price, category_id FROM product;
Product.object.defer('id', 'name')


SELECT * FROM product WHERE price > 50000;
Product.object.filter(price__gt=50000;

SELECT * FROM product WHERE price = 50000;
Product.objects.filter(price=50000)

SELECT * FROM product WHERE price < 50000;
Product.objects.filter(price__lt=50000)

SELECT * FROM product WHERE price != 50000;
Product.objects.exclude(price=50000)
            or
Product.objects.filter(~Q(price=50000))

SELECT * FROM product WHERE price <= 50000;
Product.objects.filter(price__lte=50000)

SELECT * FROM product WHERE price <= 50000;
Product.objects.filter(price__gte=50000)


SELECT * FROM product WHERE price BETWEEN 50000 AND 60000;
Product.objects.filter(price__range=[50000, 60000])

SELECT * FROM product WHERE price >= 50000 AND price <= 60000;
Product.objects.filter(price__gte=50000).filter(price__lte=60000)
                        or
Product.objects.filter(price__gte=50000, price__lte=60000)


SELECT * FROM product WHERE category_id IN ('smartphones', 'accessories');
Product.objects.filter(category_id__in=['smartphones', 'accessories'])

SELECT * FROM product WHERE category_id = 'smartphones' OR category_id = 'accessories'
Product.objects.filter(Q(category_id = 'smartphones') ...................................................








# ORDER BY

SELECT * FROM product OrDER BY price ASC;
Product.objects.order_by('price')

SELECT * FROM product OrDER BY price ASC;
Product.objects.order_by('-price')


# COUNT

SELECT COUNT(*) FROM product;
Product.objects.count()

SELECT COUNT(*) FROM product WHERE category_id = 'smartphones";
Product.objects.filter(category_id='smartphones').count()


# INSERT

INSERT INTO product (...) values (...);
Product.objects.create(...)

product = Product(...)
product.save()

# INSERT INTO product (...) VALUES (...), (...), (...);

Product.objects.bulk_create([
    Product(...),
    Product(...),
    Product(...),
    Product(...)

# UPDATE
"""