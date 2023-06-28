

size_process=int(input("Enter size process (Byte) :\n"))
size_main_memory=int(input("Enter size main memory (Byte) :\n"))
page_size=int(input("Enter size page procss:(2 Byte - 4 Byte - 8 Byte - 16 Byte)\n"))
#page_count=int(input("Enter count page procss:"))
frame_size=page_size
page_table=[]

page_count=int(size_process/page_size)
frame_count=int(size_main_memory/page_size)


for i in range(page_count):
    page_table.append(int(input(f"page {i} process to which frame? (frame 0 to {frame_count-1} )\n")))

def status_main_memory():
    empty=[]
    full=[]
    for i in range(frame_count):
        if i not in page_table:
            empty.append(i)
            print(f"frame {i} is empty.")
        else:
            full.append(i)
            print(f"frame {i} is full.")
    quiz=input("Do you want to see a list of empty and full frames ? ")
    if quiz=="yes":
        print(f"Empty : {empty}")
        print(f"Full : {full}")

def show_page_table():
    print("------------")
    for i in range(len(page_table)):
        print(f"  {i}  |  {page_table[i]} |")
        print("------------")

def change_page_table(page,frame):
    for i in range(0,len(page_table)):
        if page_table[i]==frame :
            page_table[i]=page_table[page]

    page_table[page]=frame


def convert_address(address_nesbi):
#address_nesbi=int(input("Enter address nesbi :"))
    #get page
    kamel=address_nesbi//page_size
    #get block in page
    baqi=address_nesbi%page_size
    
    address_fiziki=page_table[kamel]*page_size+baqi
    print(f"it is in frame : {page_table[kamel]} and page : {kamel}")
    return address_fiziki
while(1):
    command=input("Enter command (status/show_page_table/change_page_table/convert_address) :\n")
    if command=="status":
        status_main_memory()
    elif command=="change_page_table":
        page=int(input("page :"))
        frame=int(input("frame :"))
        change_page_table(page,frame)
    elif command=="convert_address":
        address=convert_address(int(input("address nesbi :")))
        print(f"address fiziki : {address}")
    elif command=="show_page_table":
        show_page_table()
    elif command=="Exit" or command=="exit":
        break
