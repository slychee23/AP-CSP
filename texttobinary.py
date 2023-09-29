"""
 This program encodes user input into binary data!
 Your job is to write the textToBinary function
"""

def text_to_binary(text):
    text_list = list(text)
    # Write this method!
    binary_result = ""
  
    # For every character in the text,
    for i in range(len(text_list)):
        decimal = ord(text_list[i])
        # then convert that decimal value into its equivalent binary encoding
        binary_result += str(decimal_to_binary(decimal))
    return binary_result
            
        # and combine each binary encoding to get the resulting binary string

    
# Converts a given decimal value into an 8 bit binary value
def decimal_to_binary(decimal_value):
    binary_base = 2
    num_bits_desired = 8
    binary_value = str(bin(decimal_value))[2:]
    
    while len(binary_value) < num_bits_desired:
        binary_value = "0" + binary_value
    
    return binary_value

text = input("Input the string you would like to encode: ")
binary = text_to_binary(text)

print(binary)