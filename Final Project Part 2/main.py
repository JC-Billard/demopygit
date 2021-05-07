#       Jake Billard        UHID 1582534
#       Final Project       Part 2

import csv
from datetime import datetime

class Complete_Inventory_Output:

    def __init__(self, Item_LIST):
        self.Item_LIST = Item_LIST


#------------------------ FULL INVENTORY ------------------#

    def Full_Inv(self):

        with open('FullInventory.csv', 'w') as FI_newfile:
            Items = self.Item_LIST  #Connects Full_Inv "Items" to __init__
            Item_KEY = sorted(Items.keys(), key=lambda n: Items[n]["Manufacturer_NAME"])     #Sorts Items by Manufacturer.
            for item in Item_KEY:
                ID = item
                Manufacturer_NAME = Items[item]["Manufacturer_NAME"]
                Item_TYPE = Items[item]["Item_TYPE"]
                Item_PRICE = Items[item]["Item_PRICE"]
                ServiceDate = Items[item]["ServiceDate"]
                Item_DAMAGED = Items[item]["Item_DAMAGED"]
                FI_newfile.write('{},{},{},{},{},{}\n'.format(ID, Manufacturer_NAME, Item_TYPE, Item_PRICE, ServiceDate, Item_DAMAGED))

# ------------------------ FULL INVENTORY ------------------#



# ------------------------ TYPE ORGANIZATION ---------------#

    def Type_Org(self):

        Items = self.Item_LIST      #Connects Type_Org "Items" to __init__
        itemtypes = []
        Item_KEY = sorted(Items.keys())
        for item in Items:
            Item_TYPE = Items[item]["Item_TYPE"]
            if Item_TYPE not in itemtypes:
                itemtypes.append(Item_TYPE)     #If Item_TYPE is not in the itemtypes list, it will be appended.
        for type in itemtypes:
            file_name = type.capitalize() + 'Inventory.csv'     #Creates the File with it's respective name.
            with open(file_name, 'w') as TO_newfile:
                for item in Item_KEY:
                    ID = item
                    Manufacturer_NAME = Items[item]["Manufacturer_NAME"]
                    Item_PRICE = Items[item]["Item_PRICE"]
                    ServiceDate = Items[item]["ServiceDate"]
                    Item_DAMAGED = Items[item]["Item_DAMAGED"]
                    Item_TYPE = Items[item]["Item_TYPE"]
                    if type == Item_TYPE:
                        TO_newfile.write('{},{},{},{},{}\n'.format(ID, Manufacturer_NAME, Item_PRICE, ServiceDate, Item_DAMAGED))

# ------------------------ TYPE ORGANIZATION ---------------#



# ------------------------ PAST SERVICE DATE ---------------#

    def Past_Service_Date(self):

        Items = self.Item_LIST      #Connects Past_Service_Date "Items" to __init__
        Item_KEY = sorted(Items.keys(), key=lambda n: datetime.strptime(Items[n]["ServiceDate"], "%m/%d/%Y").date(), reverse=True)  #Dates sorted from Oldest to Newest.
        with open('PastServiceDateInventory.csv', 'w') as PSD_newfile:      #Creates PastServiceDateInventory.csv
            for item in Item_KEY:
                ID = item
                Manufacturer_NAME = Items[item]["Manufacturer_NAME"]
                Item_TYPE = Items[item]["Item_TYPE"]
                Item_PRICE = Items[item]["Item_PRICE"]
                ServiceDate = Items[item]["ServiceDate"]
                Item_DAMAGED = Items[item]["Item_DAMAGED"]
                date_TODAY = datetime.now().date()
                date_EXPIRATION = datetime.strptime(ServiceDate, "%m/%d/%Y").date()
                passed_date = date_EXPIRATION < date_TODAY      #The service date is passed due.
                if passed_date:
                    PSD_newfile.write('{},{},{},{},{},{}\n'.format(ID, Manufacturer_NAME, Item_TYPE, Item_PRICE, ServiceDate, Item_DAMAGED))

# ------------------------ PAST SERVICE DATE ---------------#



# ------------------------ DAMAGED ITEMS -------------------#

    def Damaged_Items(self):

        Items = self.Item_LIST      #Connects Damaged_Items "Items" to __init__
        Item_KEY = sorted(Items.keys(), key=lambda n: Items[n]["Item_PRICE"], reverse=True)
        with open('DamagedInventory.csv', 'w') as DI_newfile:       #Creates DamagedInventory.csvv
            for item in Item_KEY:
                ID = item
                Manufacturer_NAME = Items[item]["Manufacturer_NAME"]
                Item_TYPE = Items[item]["Item_TYPE"]
                Item_PRICE = Items[item]["Item_PRICE"]
                ServiceDate = Items[item]["ServiceDate"]
                Item_DAMAGED = Items[item]["Item_DAMAGED"]
                if Item_DAMAGED:
                    DI_newfile.write('{},{},{},{},{}\n'.format(ID, Manufacturer_NAME, Item_TYPE, Item_PRICE, ServiceDate))

# ------------------------ DAMAGED ITEMS -------------------#



if __name__ == "__main__":
    Items = {}
    files = ['ManufacturerList.csv', 'PriceList.csv', 'ServiceDatesList.csv']
    for file in files:
        with open(file, 'r') as csv_file:
            csv_reader = csv.reader(csv_file, delimiter=',')
            for line in csv_reader:
                Item_ID = line[0]
                if file == files[0]:
                    Items[Item_ID] = {}
                    Manufacturer_NAME = line[1]     #Manufacturer Name is index 1
                    Item_TYPE = line[2]             #Item Type is Index 2
                    Item_DAMAGED = line[3]          #Damaged Item is Index 3
                    Items[Item_ID]["Manufacturer_NAME"] = Manufacturer_NAME.strip()
                    Items[Item_ID]["Item_TYPE"] = Item_TYPE.strip()
                    Items[Item_ID]["Item_DAMAGED"] = Item_DAMAGED
                elif file == files[1]:
                    Item_PRICE = line[1]
                    Items[Item_ID]["Item_PRICE"] = Item_PRICE
                elif file == files[2]:
                    ServiceDate = line[1]
                    Items[Item_ID]["ServiceDate"] = ServiceDate


#------------------ CSV FILE OUTPUT --------------------#
    program = Complete_Inventory_Output(Items)
    program.Full_Inv()
    program.Type_Org()
    program.Past_Service_Date()
    program.Damaged_Items()
#------------------ CSV FILE OUTPUT --------------------#



#=========================================================================================Part 1 ^^^
#=========================================================================================Part 2 vvv



    Manufacturer_LIST = []      #Creates List for each Manufacturer Type
    Item_Type_LIST = []         #Creates List for each Item Type



#--------------------------- MANUFACTURUER/ITEM TYPE LIST APPENDS ---------------#

    for Item_INPUT in Items:
        Manufacturer_add = Items[Item_INPUT]['Manufacturer_NAME']
        Item_TYPE_add = Items[Item_INPUT]['Item_TYPE']
        if Manufacturer_add not in Item_Type_LIST:
            Manufacturer_LIST.append(Manufacturer_add)      #Appends Manufacturer Names into Item_Type_LIST
        if Item_TYPE_add not in Item_Type_LIST:
            Item_Type_LIST.append(Item_TYPE_add)            #Appends Item Type items into Item_Type_LIST

# --------------------------- MANUFACTURUER/ITEM TYPE LIST APPENDS ---------------#



#--------------------------- USER INPUT ------------------------------------------#

    userinput1 = None
    while userinput1 != 'q':    #If The User does NOT enter q, it prompts them for Manufacturer and Item Type
        userinput1 = input("\nEnter Desired Manufacturer & Item Type:\n")
        if userinput1 == 'q':
            exit()              #Exits the program if user enters "q".
        else:
            #Checks the user input for a match between Manufacturer and Item Type
            Manufacturer_userinput = None
            ItemType_userinput = None
            userinput1 = userinput1.split()     #Splits the user input.
            badinput = False
            for name in userinput1:
                if name in Manufacturer_LIST:
                    if Manufacturer_userinput:
                        badinput = True
                    else:
                        Manufacturer_userinput = name       #Confirms only one Manufacturer name in User Input
                elif name in Item_Type_LIST:
                    if ItemType_userinput:
                        badinput = True
                    else:
                        ItemType_userinput = name               #Confirms only one Item Type in User Input

            if not Manufacturer_userinput or not ItemType_userinput or badinput:
                print("No such item in inventory")       #Responds to any user input not present in the CSV files/lists.
            else:
                Item_Price_Org = sorted(Items.keys(), key=lambda x: Items[x]['Item_PRICE'], reverse=True)      #Sorts the items in the list from most expensive to least.
                input_match = []     #Creates a list of matching items based on their input.

# --------------------------- USER INPUT ------------------------------------------#



#----------------------------- SIMILAR/DAMAGED ITEMS ------------------------------#

                Items_SIMILAR_dict = {}     #Creates a Dictionary based on similar items
                for Item in Item_Price_Org:
                    if Items[Item]['Item_TYPE'] == ItemType_userinput:      #Searches for similar item types based on user input.
                        date_TODAY = datetime.now().date()      #Gets the date when the program runs.
                        ServiceDate = Items[Item]['ServiceDate']
                        date_EXPIRATION = datetime.strptime(ServiceDate, "%m/%d/%Y").date()
                        passed_date = date_EXPIRATION < date_TODAY
                        if Items[Item]['Manufacturer_NAME'] == Manufacturer_userinput:
                            if not passed_date and not Items[Item]['Item_DAMAGED']:
                                input_match.append((Item, Items[Item]))         #Passes through User Input if it is not passed service date or damaged
                        else:
                            if not passed_date and not Items[Item]['Item_DAMAGED']:
                                Items_SIMILAR_dict[Item] = Items[Item]          #Passes through Similar items if it is not passed service date or damaged

#----------------------------- SIMILAR/DAMAGED ITEMS ------------------------------#



#----------------------------- OUTPUT MATCHING ITEM -------------------------------#

                if input_match:         #Output user input, if it's matching.
                    Item_INPUT = input_match[0]
                    Item_ID = Item_INPUT[0]
                    Manufacturer_NAME = Item_INPUT[1]['Manufacturer_NAME']
                    Item_TYPE = Item_INPUT[1]['Item_TYPE']
                    Item_PRICE = Item_INPUT[1]['Item_PRICE']
                    print("Your item is: {}, {}, {}, {}\n".format(Item_ID, Manufacturer_NAME, Item_TYPE, Item_PRICE))

# ----------------------------- OUTPUT MATCHING ITEM -------------------------------#



#------------------------------ OUTPUT SIMILAR ITEM WITH CLOSE PRICE ---------------#

                    if Items_SIMILAR_dict:
                        matched_price = Item_PRICE
                        Item_CLOSEST = None
                        Item_CLOSEST_PRICE = None

                        for Item_INPUT in Items_SIMILAR_dict:
                            if Item_CLOSEST_PRICE == None:
                                Item_CLOSEST = Items_SIMILAR_dict[Item_INPUT]
                                Item_CLOSEST_PRICE = abs(int(matched_price) - int(Items_SIMILAR_dict[Item_INPUT]['Item_PRICE']))
                                Item_ID = Item_INPUT
                                Manufacturer_NAME = Items_SIMILAR_dict[Item_INPUT]['Manufacturer_NAME']
                                Item_TYPE = Items_SIMILAR_dict[Item_INPUT]['Item_TYPE']
                                Item_PRICE = Items_SIMILAR_dict[Item_INPUT]['Item_PRICE']
                                continue

                            Difference = abs(int(matched_price) - int(Items_SIMILAR_dict[Item_INPUT]['Item_PRICE']))    #Calculates Matched price to the next best price.
                            if Difference < Item_CLOSEST_PRICE:
                                Item_CLOSEST = Item_INPUT
                                Item_CLOSEST_PRICE = Difference
                                Item_ID = Item_INPUT
                                Manufacturer_NAME = Items_SIMILAR_dict[Item_INPUT]['Manufacturer_NAME']
                                Item_TYPE = Items_SIMILAR_dict[Item_INPUT]['Item_TYPE']
                                Item_PRICE = Items_SIMILAR_dict[Item_INPUT]['Item_PRICE']
                        print("You may, also, consider: {}, {}, {}, {}\n".format(Item_ID, Manufacturer_NAME, Item_TYPE, Item_PRICE))
                else:
                    print("No such item in inventory")

#------------------------------ OUTPUT SIMILAR ITEM WITH CLOSE PRICE ---------------#