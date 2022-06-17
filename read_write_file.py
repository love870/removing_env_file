#colorama is a library that allows us to print colored text to the console
from colorama import Fore
from colorama import Style

#User can choose any one option like read ya write
option = int(input('''Please select any operation:  
  
1) READ 
  
2) WRITE 
  
Your Choice: '''))

#Taking input from the user
filename=input('enter_file_name=')

#conditions are given to check the option

#if user chooses 1 option then this condition wll be executed
if option==1:
    #Read the text from the file
    with open(filename,'r') as f:
        #loop to read the text from the file
        
        for line in f:
            #Read the text from the file in terminal
            print(line,end='')

# if user chooses 2 option then this condition will be executed           
elif option==2:
    #write the text into the file
    with open(filename,'a') as f:
        #take input from the user
        
        text=input('Enter text here=')
        #\n is used to add new line
        f.write('\n')

        #enter the text into the file
        f.write(text)

        #Message to text added Succesfully
        print(f'{Fore.YELLOW}Text is added successfully{Style.RESET_ALL}')