#Serialization Function
def serialize(dictionary,filename):
        bin_file_create = filename+'.bin'
        try:
                if isinstance(dictionary,dict):
                        convert_to_string=str(dictionary)
                else:
                        print("Sorry can only serialize dictionaries")
                convert_to_binary =' '.join(format(i,'02x')for i in bytearray(formater(convert_to_string), encoding ='utf-8'))
                print(formater(convert_to_string))
                with open(bin_file_create,'w')as binary_file:
                        binary_file.write(convert_to_binary)
                print("File Converted successfully")
        except:
                print("Sorry Error Occured Conversion Was Not Successful")
                

#Deserialization Function

import ast

def deserialize(filename):
    file_extension = filename.split(".")
    file_content=''
    convert_to_dictionary =''
    if file_extension[-1] !='bin':
        print("Sorry .bin file extensions only")
    else:
        try:
            with open(filename) as binary_file:
                file_content = binary_file.read()
            convert_to_string = bytes.fromhex(file_content).decode('utf-8')
            convert_to_dictionary = ast.literal_eval(deformater(convert_to_string))
        except:
            print("Error Deserialization Was Not Completed")
    return convert_to_dictionary



def formater(str_dicti):
    char_to_replace = {'{':'!','}':'#','\'':'\"',',':'$',':':' ','[':'%',']':'&'}#replacing the characters that take more byte space
    hold= str_dicti.translate(str.maketrans(char_to_replace))
    return hold

def deformater(str_dicti):
    char_to_replace = {'!':'{','#':'}','$':',','%':'[','&':']'}
    hold= str_dicti.translate(str.maketrans(char_to_replace))
    return hold