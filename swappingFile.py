
# creating a function 
def swappingFileData():
    # taking the user file input 
    file_input1 = input('File 1 :- ');
    file_input2 = input('File 2 :- ');

    with open(file_input1, 'r') as a:
        data_a = a.read();

    with open(file_input2, 'r') as b:
        data_b = b.read();

    with open(file_input1, 'w') as a:
        a.write(data_b);

    with open(file_input2, 'w') as b:
        b.write(data_a);

swappingFileData();

