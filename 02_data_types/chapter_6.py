
#String
name="Prapti"
print(f"My name is {name}.")

fruit="Mango is my favourite fruit"
print(f"slicing : {fruit[0:19]}")
print(f"slicing : {fruit[:19]}")
print(f"slicing : {fruit[0:]}")
print(f"slicing : {fruit[2:-3]}")
print(f"slicing : {fruit[::-1]}")

student="Abhijiţ"
encode_student=student.encode("utf-8")
print(f"student before encoding : {student}")
print(f"student after encoding : {encode_student}")

decode_student= encode_student.decode("utf-8")
print(f"After decoding student string : {decode_student}")

label_text = "Chai Spécial"
ecoded_label = label_text.encode("utf-8")
print(f"Non Encoded label: {label_text}")
print(f"Encoded label: {ecoded_label}")
decoded_label = ecoded_label.decode("utf-8")
print(f"Decoded label: {decoded_label}")

