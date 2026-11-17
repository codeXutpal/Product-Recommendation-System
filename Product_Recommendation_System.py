
purchases = {
    "Amit": ["Laptop", "Mouse", "Keyboard"],
    "Bina": ["Laptop", "Mouse", "Headphones"],
    "Chetan": ["Phone", "Charger"],
    "Divya": ["Laptop", "Keyboard", "Monitor", "Webcam"]
}


def jaccard_similarity(products1, products2):
    set1 = set(products1)
    set2 = set(products2)

    union = set1 | set2

    if not union:
        return 0.0

    return len(set1 & set2) / len(union)


def find_popular_product(customers):
    product_counts = {}

    for products in customers.values():
        for product in set(products):
            product_counts[product] = product_counts.get(product, 0) + 1

    if not product_counts:
        return None, 0

    popular_product = max(product_counts, key=product_counts.get)

    return popular_product, product_counts[popular_product]


def recommend_product(customers, customer_name):

    customer_name = customer_name.strip()

    if not customer_name:
        print("Name cannot be empty.")
        return

    customer_lookup = {
        name.lower(): name for name in customers
    }

    actual_name = customer_lookup.get(customer_name.lower())

    if actual_name is None:
        print(f"Customer '{customer_name}' not found.")
        return

    selected_products = set(customers[actual_name])

    similarity_scores = {}

    for name, products in customers.items():

        if name != actual_name:
            similarity_scores[name] = jaccard_similarity(
                selected_products, set(products)
            )

    sorted_scores = sorted(
        similarity_scores.items(),
        key=lambda item: item[1],
        reverse=True
    )

    if not sorted_scores or sorted_scores[0][1] == 0:

        print("No similar customers found.")

        popular_product, count = find_popular_product(customers)

        if popular_product is not None:
            print(
                f"Popular product: {popular_product} "
                f"(bought by {count} customers)"
            )
        else:
            print("No products are available.")

        return

    print("Similarity scores:")

    for name, score in sorted_scores:
        print(f"{name} : {score:.2f}")

    most_similar_customer = sorted_scores[0][0]

    print(f"Most similar customer: {most_similar_customer}")

    recommendations = [
        product
        for product in customers[most_similar_customer]
        if product not in selected_products
    ]

    if recommendations:
        print(f"Recommended: {', '.join(recommendations)}")
    else:
        print("No new products to recommend.")


name = input("Recommend for: ")

recommend_product(purchases, name)



#output:-

# Recommend for: Amit
# Similarity scores:
# Bina : 0.50
# Divya : 0.40
# Chetan : 0.00
# Most similar customer: Bina
# Recommended: Headphones
