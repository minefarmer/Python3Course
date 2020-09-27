# Infinate arguments
def print_people(*people):
    for person in people:
        print('This Person is', person)

print_people('Nick', 'Dan', 'Jack', 'King', 'Smiley')  # This Person is Nick
                                                        # This Person is Dan
                                                        # This Person is Jack
                                                        # This Person is King
                                                        # This Person is Smiley
