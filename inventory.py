ingredients = [
    {
        "name": "양파",
        "category": "채소",
        "quantity": 10,
        "unit": "kg",
        "minimum_stock": 8,
    },
    {
        "name": "돼지고기",
        "category": "육류",
        "quantity": 5,
        "unit": "kg",
        "minimum_stock": 6,
    },
    {
        "name": "대파",
        "category": "채소",
        "quantity": 3,
        "unit": "단",
        "minimum_stock": 2,
    },
    {
        "name": "간장",
        "category": "공산품",
        "quantity": 4,
        "unit": "병",
        "minimum_stock": 2,
    },
    {
        "name": "두부",
        "category": "냉장식품",
        "quantity": 8,
        "unit": "개",
        "minimum_stock": 10,
    },
]


print("=== 현재 식자재 목록 ===")

for ingredient in ingredients:
    print(
        f"{ingredient['name']} | "
        f"{ingredient['category']} | "
        f"{ingredient['quantity']}{ingredient['unit']}"
    )
    
    if ingredient["quantity"] <= ingredient["minimum_stock"]:
        print("  ⚠ 재고 부족")
    else:
        print("  재고 충분")