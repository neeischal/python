def capitalize_name(name):
    name_parts = name.split()
    if len(name_parts) > 1:
        first_name = name_parts[0].capitalize()
        last_name = name_parts[-1].capitalize()
        middle_name = name_parts[1:-1]
        middle_name = [i.capitalize() for i in middle_name]
        name_parts = [first_name] + middle_name + [last_name]
        return " ".join(name_parts)
    else:
        return name.capitalize()

print(capitalize_name("nischal ram kharel"))
