def capitals():
    countries_data = input().split(", ")
    capitals_data = input().split(", ")
    result = dict(zip(countries_data, capitals_data))  # zip(key, value)

    for key, value in result.items():
        print(f"{key} -> {value}")


capitals()
