for case in range(int(input(''))):
    loss = float(0)
    for recipies in range(int(input(''))):
        price, products, discount = map(float, input('').split(' '))
        inflated_price = price+price*(discount/100.00)
        discounted_price = inflated_price - inflated_price*(discount/100.00)
        loss+=(price-discounted_price)*products
    print(loss)
