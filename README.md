The library consist of  seder.py file with contains the two functions to serialize and deserialize the dictionary file/object

How the serialize function works
the serialize function takes in two parameters: the first is the dict() you want to serialize and the second the name you want to give your file that would be created to save the bytes to disk.

serialize(myDictionary,'myFileName')

You dont have to attach the .bin file extension as that would be added for you when you input the file name.

To use the serialize function you need to import seder into your program

import seder
seder.serialize(myDictionary,'myFileName')

The file would be created in the directory in which you run the program.

How the deserialize function works

The deserialize function takes in only one parameter: that is the filename with the .bin extension you want to deserialize. The file should be in the same directory you run the program from.

deserialize('filename.bin')

To use the deserialize function you need to import seder into your program
import seder
seder.deserialize('filename.bin')

Error Handling

The serialization function only works with dictionaries so should you input any other data type it would give you an error message.

The deserialization function would only work on binary files with the .bin extension if the file extension is not correct an error message would show.