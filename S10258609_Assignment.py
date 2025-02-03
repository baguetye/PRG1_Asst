#Bryan Lim Aik Sian (S10258609) - P07

#this function read the file,carpark-information.csv and stores it as a list with the elements being dictionaries.

def ReadData():
    #this code is to read the datafile
    with open('carpark-information.csv','r') as datafile:

        cpinfolist=[]

        #this code is to start a loop to convert the data read from the file
        for line in datafile:
            #this code is to convert the string into a list
            line=(line.strip('\n')).split(',',3)
            #this code is to store the listinto cpinfolist
            cpinfolist.append(line)

        #this code is to pop out the header and save it as a list
        header=cpinfolist.pop(0)
        #this code is to convert the elemement into a dictionary with they key being the header
        for i in range(len(cpinfolist)):
            cpinfo={}
            #this code is to pop out the list element to convert it to a dictionary
            convert=cpinfolist.pop(i)
            
            #this code is to start a nested loop to access each element in the list to store it as dictionary values
            for a in range(len(convert)):
                cpinfo[header[a]]=convert[a]

            #this code is to append the dictionary into cpinfolist

            cpinfolist.insert(i,cpinfo)

    #this code is to return the list
    return(cpinfolist)

#this function is to use the list from ReadData() to find out the total number of carparks

#this code is to def a function w parameter if cpinfolist

def option1 (cpinfolist):

    #this code is to print the option string
    
    print('\nOption 1: Display Total Number of Carparks in \'carpark-information.csv\'')

    #this code is to print the string for the total and len(cpinfolist)

    print(('Total Number of carparks in \'carpark-information.csv\': {}.\n').format(len(cpinfolist)))
    return

#this function is to use the list from ReadData() to find all the basement carparks

#This code is to def a function w parameter of cpinfolist

def option2 (cpinfolist):

    total=0

    #this code is to print the option string
    print('\nOption 2: Display All Basement Carparks in \'carpark-information.csv\'')

    #this code is to print the header

    print(('{:<11}{:<19}{}').format('Carpark No','Carpark Type','Address'))
    
    #this code is to print the table as well as count the total for basement carparks
    for i in cpinfolist:
         #This code is to check if the carpark is a basement carpark
         if 'BASEMENT CAR PARK' in i['Carpark Type']:
             print(('{:<11}{:<19}{}').format(i['Carpark Number'],i['Carpark Type'],i['Address']))
             #this code is to increment the total
             total+=1

         else:
            continue
    #this code is to print the total
    print(('Total number: {}\n').format(total))
    return

#this function is to read a file given by the user and store it as a list with its elements being dictionaries. the function also prints out the timestamp

#this code is to define a function with no parameter
def option3 ():
    #this code is to print the option
    print('\nOption 3: Read Carpark Availability Data File')
    #this code is to promt user for input
    filename=input('Enter the file name: ')
    #this code is to open the file
    with open(filename,'r') as CPAfile:

        CPAlist=[]
        #this code is to start a loop to convert the data read from the file
        for line in CPAfile:
            #this code is to convert the string into a list
            line=(line.strip('\n')).split(',')
            #this code is to store the list into cpinfolist
            CPAlist.append(line)
        #this code is to pop out the timestamp
        timestamp=CPAlist.pop(0)
        #this code is to print the timestamp
        print(timestamp[0]+'\n')
        #this code is to pop out the header and save it as a list
        header=CPAlist.pop(0)
        #this code is to convert the elemement into a dictionary with they key being the header
        for i in range(len(CPAlist)):
            CPA={}
            #this code is to pop out the list element to convert it to a dictionary
            convert=CPAlist.pop(i)
        
            #this code is to start a nested loop to access each element in the list to store it as dictionary values
            for a in range(len(convert)):
                CPA[header[a]]=convert[a]

            #this code is to append the dictionary into CPAlist

            CPAlist.insert(i,CPA)

    #this code is to return the list, timestamp and header
    return(CPAlist,timestamp,header)

#this function is used to count the total number of carparks in the list from option3()
        
#this code is to define a function with the parameter of CPAlist
def option4 (CPAlist):
    #this code is to print the option
    print('\nOption 4: Print Total Number of Carparks in the File Read in [3]')

    #this code is to print the total
    print(('Total number of Carparks in the file: {}\n').format(len(CPAlist)))
    return

#this function is used to display the carparks with available lots using the list from option3()
   
#this code is to define a function with the parameters of CPAlist

def option5 (CPAlist):
    total=0
    #this code is to print the option
    print('\nOption 5: Display Carparks without Available Lots')
    #this code is to create a for loop for CPAlist
    for i in CPAlist:
        #this code is to cehck if there are no lots available
        if '0' == i['Lots Available']:
            print(('Carpark Number: {}').format(i['Carpark Number']))
            total+=1
    #this code is to print the total
    print(('Total number: {}\n').format(total))
    return
            
#this function is used to find the number of carparks where the percentage of available slots is higher than the minimum percentage indicated
#by the user

#this code is to define a function with the parameter of CPAlist

def option6 (CPAlist):
    total=0
    #this code is to print the option
    print('\nOption 6: Displays Carparks With At Least x% Available Lots')
    #this code prompts the user for an input
    minimum=float(input('Enter the percentage required: '))
    assert 0<=minimum<=100
    #this code is to print the header
    print(('{:<10}  {:>10}  {:>14}  {:>10}').format('Carpark No','Total lots','Lots Available','Percentage'))    

    #this code is to start a loop for CPAlist

    for i in CPAlist:
        #this code is to check that the total lots is not 0
        if i['Total Lots'] !='0' and i['Total Lots'] !=0 :
            #this code is to calculate the percentage available for the lot
            percentage=(int(i['Lots Available'])/int(i['Total Lots']))*100
        #this code is to check if the percentage is higher than the minimum
        if percentage>=minimum:
            print(('{:<10}  {:>10}  {:>14}  {:>10.1f}').format(i['Carpark Number'],i['Total Lots'],i['Lots Available'],percentage))
            #this code is to increment the total
            total+=1
    #this code is to print the total
    print(('Total Number: {}\n').format(total))
    return

#this function is used to find the number of carparks where the percentage of available slots is higher than the minimum percentage indicated
#by the user and display the address as well

#this code is to define a function with the parameter of CPAlist and CPinfolist

def option7 (CPAlist,CPinfolist):
    total=0
    #this code is to print the option
    print('\nOption 7: Display Addresses of Carparks With At Least x% Available Lots')
    #this code prompts the user for an input
    minimum=float(input('Enter the percentage required: '))
    assert 0<=minimum<=100
    #this code is to print the header
    print(('{:<10}  {:>10}  {:>14}  {:>10}  {}').format('Carpark No','Total lots','Lots Available','Percentage','Address'))

    #this code is to start a loop for CPinfolist
    for i in CPAlist:
        #this code is to check that the total lots is not 0
        if i['Total Lots'] !='0' and i['Total Lots'] !=0 :
            #this code is to calculate the percentage available for the lot
            percentage=(int(i['Lots Available'])/int(i['Total Lots']))*100
        #this code is to check if the percentage is higher than the minimum
        if percentage>=minimum:
            #this code is to increment the total count
            total+=1
            #this code is to find the address of the carpark
            for a in CPinfolist:
                if i['Carpark Number']==a['Carpark Number']:
                    address=a['Address']
                    #this code is to print the table
                    print(('{:<10}  {:>10}  {:>14}  {:>10.1f}  {}').format(i['Carpark Number'],i['Total Lots'],i['Lots Available'],percentage,a['Address'].strip('"')))
                    #this code is to print the total
    print(('Total Number: {}\n').format(total))
    return


#this function is used to display the menu for the programme as well as get the input from the user
        
#this code is to define a function with no parameters for the menu

def MainMenu ():
        #this code is to print the header
        print('MENU\n====')
        #this code is to print the options
        print('[1] Display Total Number of Carparks in \'carpark-information.csv\'')
        print('[2] Display All Basement Carparks in \'carpark-information.csv\'')
        print('[3] Read Carpark Availability Data File')
        print('[4] Print Total Number of Carparks in the File Read in [3]')
        print('[5] Display Carparks Without Available Lots')
        print('[6] Display Carparks With At Least x% Available Lots')
        print('[7] Display Addresses of Carparks With At Least x% Available Lots')
        print('[8] Display All Carparks at x Location')
        print('[9] Display Carpark With The Most Parking Lots')
        print('[10] Create an Output File with Carpark Availability')
        print('[0] Exit')

        #this code is to prompt user for input
        choice=int(input('Enter your option: '))

        return(choice)
    
#This fuction is to display the carparks at a given location by the user


#this code is def a function with the parameter of CPAlist and CPinfolist
def option8 (CPAlist,CPinfolist):
    total=0
    #this code is to display the option
    print('\nOption 8:Display All Carparks at x Location')
    #this code is to prompt user for input
    location=input('Please enter the location to search for: ')
    #this code is to determine whether or not to print the header
    for i in CPinfolist:
        if location.upper() in i['Address']:
            print(i)
            print(('{:<10}  {:>10}  {:>14}  {:>10}  {}').format('Carpark No','Total lots','Lots Available','Percentage','Address'))
            break
    #this code is to find the location
    for i in CPinfolist:
        #this code is to check if the carpark is at the location
        if location.upper() in i['Address']:
            #this code is to get the lots available for the location
            for a in CPAlist:
                if i['Carpark Number'] == a['Carpark Number']:
                    #this code is to calculate the percentage
                    percentage=(int(a['Lots Available'])/int(a['Total Lots']))*100
                    #this code is to print the values
                    print(('{:<10}  {:>10}  {:>14}  {:>10.1f}  {}').format(a['Carpark Number'],a['Total Lots'],a['Lots Available'],percentage,i['Address'].strip('"')))
                    #this code is to increment the total
                    total+=1
            #this code is to print the total
    if total>0:
        print(('Total Number: {}\n').format(total))
    else:
        print(('No Carparks Found at Location: {}.\n').format(location))

#this function is to Display the carparks with the most parking lots in the file given in option3()

#this code is to def a function w the parameter of CPAlist and CPinfolist
def option9 (CPAlist,CPinfolist):
    highest=CPAlist[0]
    #this code is to idsplay the option
    print('\nOption 9: Display Carpark With The Most Parking Lots')
    #this code is to start a loop to find out which carpark has the most parking lots
    for i in CPAlist:
        if int(i['Lots Available'])>int(highest['Lots Available']):
            highest=i
    #this code is to find the carpark information in CPinfolist
    for i in CPinfolist:
        if highest['Carpark Number'] == i['Carpark Number']:
            highest.update(i)
    #this code is to display the carpark details
    print(('Carpark Number: {}\nCarpark Type: {}\nType of Parking System: {}\nTotal Lots: {}\nLots Available: {}\nPercentage: {:.1f}%\nAddress: {}\n')\
          .format(highest['Carpark Number'],highest['Carpark Type'],highest['Type of Parking System'],highest['Total Lots'],highest['Lots Available'],\
                  (int(highest['Lots Available'])/int(highest['Total Lots']))*100,highest['Address'].strip('"')))

#this function is used to create an output file with carpark availability                 

#this code is to def a function with the parameter of CPAlist,tiemstamp,header,CPinfolist

def option10 (CPAlist,CPAtiemstamp,CPAheader,CPinfolist):
    #this code is to print the option
    print('\nOption 10: Create an Output with Carpark Availability')
    #this code is to add an address to the header
    CPAheader.append('Address')
    CPAlots=[]
    #this code is to create a list with lots available and sort it
    for i in CPAlist:
        if not(int(i['Lots Available']) in CPAlots):
            CPAlots.append(int(i['Lots Available']))
        CPAlots.sort()

    

    #this code is to open a file to write to
    with open('carpark-availability-with-addresses.csv','w') as datafile:
        #this code is to write the timestamp into the file
        datafile.write(CPAtimestamp[0]+'\n')
        #this code is to write the header into the file
        for i in CPAheader:
            datafile.write(str(i)+',')
        datafile.write('\n')
        #this code is to count the number of lines written to the file
        count=2
        #this code is to write the values into the file
        for lot in CPAlots:
            for number in CPAlist:
                #this code is to find the carpark number
                if str(lot) ==number['Lots Available']:
                    #this code is to get the address
                    for element in CPinfolist:
                        if element['Carpark Number'] == number['Carpark Number']:
                            address=element['Address']
                    #this code is to write the info to the datafile
                    for key in number:
                        datafile.write(number[key]+',')
                    datafile.write(address+'\n')
                    count+=1
    #this code is to print the total number of lines written to the file
    print(('Number of lines written into the file: {}').format(count))
    #this code is to display the file name
    print('Filename: carpark-availability-with-addresses.csv\n')
                            
       



#this code is to start the program execution

CPinfolist=ReadData()
while True:
    #This code is to call upon the main menu function and store the return variable as choice
    try:
        choice=MainMenu()
    except ValueError:
            print('\nPlease enter a number value\n')
            continue
    #this code is to determine the option the user has chosen and execute the correct function
    if choice == 1:
        option1(CPinfolist)
    elif choice== 2:
        option2(CPinfolist)
    elif choice== 3:
        while True:
            try:
                CPAinfolist,CPAtimestamp,CPAheader=option3()
            except FileNotFoundError:
                print('\nPlease enter a valid file name')
                continue
            break
    elif choice== 4:
        try:
            option4(CPAinfolist)
        except NameError:
            print('\nPlease choose option 3 first\n')
                
    elif choice== 5:
        try:
            option5(CPAinfolist)
        except NameError:
            print('\nPlease choose option 3 first\n')
            
    elif choice==6:
        
        while True:
            try:
                option6(CPAinfolist)
            except NameError:
                print('\nPlease choose option 3 first\n')
                break
            except ValueError:
                print('\nPlease enter a number value')
                continue
            except AssertionError:
                print('\nPlease enter a percentage value that is between 0 and 100')
                continue
            break
       
    elif choice==7:
        while True:
            try:
                option7(CPAinfolist,CPinfolist)
            except NameError:
                print('\nPlease choose option 3 first\n')
                break
            except ValueError:
                print('\nPlease enter a number value')
                continue
            except AssertionError:
                print('\nPlease enter a percentage value that is between 0 and 100')
                continue
            break
    elif choice==8:
        try:
            option8(CPAinfolist,CPinfolist)
        except NameError:
            print('\nPlease choose option 3 first\n')
            
    elif choice==9:
        try:
            option9(CPAinfolist,CPinfolist)
        except NameError:
            print('\nPlease choose option 3 first\n')
    elif choice==10:
        try:
            option10(CPAinfolist,CPAtimestamp,CPAheader,CPinfolist)
        except NameError:
            print('\nPlease choose option 3 first\n')
            
    elif choice==0:
        break
    else:
        print('\nPlease enter a valid choice\n')
