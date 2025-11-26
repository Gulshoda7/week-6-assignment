# A single product tuple (id, cat, price, sold)
def calculate_product_revenue(product_tuple):
    revenue = 0
    revenue = product_tuple[-2]*product_tuple[-1]
    return revenue

def find_top_revenue_product(products):
    top_revenue = 0 
    top_product_id = ''
    for j in range(len(products)):
        current_revenue=calculate_product_revenue(products[j])
        if current_revenue > top_revenue:
            top_revenue=current_revenue
            top_product_id=products[j][0]
        elif current_revenue==top_revenue:
            if products[j][0]<top_product_id:
                top_product_id=products[j][0]
    return top_product_id
                
def get_products_in_category(products, category_name):
    same_names = []
    for k in range(len(products)):
        if products[k][1]==category_name:
            same_names.append(products[k][0])
    same_names.sort()
    return same_names

def get_category_sales_summary(products):
    categories = []
    for g in products:
        if g[1] not in categories:
            categories.append(g[1])
    category_sum = []        
    for good_name in categories:
        total_unit=0
        for product in products:
            if product[1]==good_name:
                total_unit+=product[3]
        category_sum.append((good_name, total_unit))
    category_sum.sort()
    return category_sum

def analyze_products(products):
    top_revenue_product_id = find_top_revenue_product(products)
    electronics_product_ids = get_products_in_category(products, 'Electronics')
    category_summary = get_category_sales_summary(products)
    
    return (top_revenue_product_id, electronics_product_ids, category_summary)

products = [
    ('P101', 'Electronics', 799.99, 150),
    ('P205', 'Books', 24.50, 500),
    ('P102', 'Electronics', 499.50, 200),
    ('P301', 'Home Goods', 120.00, 800),
    ('P206', 'Books', 19.99, 650)
]

print(analyze_products(products))
