import re    # This is an imported library


# string = "'I AM NOT YELLING', she said. Though we knew it not to be true."
# new = re.sub('[A-Z]', '', string)
# print(new)  # '   ', she said. hough we knew it not to be true.


# string = "'I AM NOT YELLING', she said. Though we knew it not to be true."
# new = re.sub('[a-z]', '', string)
# print(new)  # 'I AM NOT YELLING',  . T       .


# string = "'I AM NOT YELLING', she said. Though we knew it not to be true."
# new = re.sub('[.,\']', '', string)
# print(new)  # I AM NOT YELLING she said Though we knew it not to be true


# string = "'I AM NOT YELLING', she said. Though we knew it not to be true."
# new = re.sub('[.,\'a-x]', '', string)
# print(new)  # I AM NOT YELLING she said   T


# string = "'I AM NOT YELLING', she said. Though we knew it not to be true."
# new = re.sub('[.,\'a-xA-Z]', '', string)
# print(new)  #             **** blank = nothing printed


# string = "'I AM NOT YELLING', she said. Though we knew it not to be true."
# new = re.sub('[.,\'a-z]', '', string)
# print(new)  # I AM NOT YELLING   T 


# string = "'I AM NOT YELLING', she said. Though we knew it not to be true."
# new = re.sub('[.,\'A-Z]', '', string)
# print(new)  #     she said hough we knew it not to be true 


# string = "'I AM NOT YELLING', she said. Though we knew it not to be true."
# new = re.sub('[.,\'A-Z+" "]', '', string)
# print(new)  # shesaidhoughweknewitnottobetrue


string = "'I AM NOT YELLING', she said. Though we knew it not to be true."
string = string + "6 298 - 345"
print(string)  # 'I AM NOT YELLING', she said. Though we knew it not to be true.6 298 - 345
new = re.sub('[^0-9]', '', string)
print(new)  # 6298345

