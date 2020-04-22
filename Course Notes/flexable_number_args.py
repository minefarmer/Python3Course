def print_people(*people):  # tle colon creates the indent (differient block)
    for person in people:  # people is a list ** array
        print("This person is", person)

print_people("Sandra", "Roger", "Carl", "Rich", "Beth")  # This person is Sandra
                                                        # This person is Roger
                                                        # This person is Carl
                                                        # This person is Rich
                                                        # This person is Beth
