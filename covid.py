#! /usr/bin/env python3
import webbrowser  # python builtin module

"""Interfaces for launching and remotely controlling Web browsers."""
"""
i can scrapp data from websites and i can read it in terminal or save record in text, csv file etc
but webscrapping is ilegal thats why i like to use webbrowser module for redirecting users on site
this is free and opensource script, no copycase matter....
if anybody want to scrapp data from site simply import beautifullsoup and requests
before importing you need to install both libraries  
"""
# pip install request
# pip install bs4
def main_menu():
    """ this function is only for mainmenu """
    print("""
    ------------Main Menu-------------
    [A] : "Cases & Map"    [B] : "Safety"
    
    [C] : "Symptoms"          [D] : "History"
    
                  [H] : "Help"
    """)


main_menu()
my_users = input("Main Menu :")

if my_users in ("a", "A", "cases", "Cases"):
    webbrowser.open_new_tab('https://www.google.com/covid19-map/')
    print(" I am writing this just for a coding exercise, but i hope this script will help you")

elif my_users in ('b', 'B', "Safety", "safety"):
    print("""
    Stay aware of the latest information on the COVID-19 outbreak,
    available on the WHO website and through your national and local public health authority.
    Most people who become infected experience mild illness and recover, but it can be more severe for others.
    Take care of your health and protect others by doing the following:
    
    [Wash your hands frequently]
    
    [Maintain social distancing]
    
    [Avoid touching eyes, nose and mouth]
    
    [Practice respiratory hygiene]
    
    [If you have fever, cough and difficulty breathing, seek medical care early]
    
    [Stay informed and follow advice given by your healthcare provider]
    
    [stay home]
    """)

elif my_users in ('c', 'C', 'signs', 'Signs'):
    print("""
    People may experience:
cough
fever
tiredness
difficulty breathing (severe cases)
flu
    """)

elif my_users in ('d', 'D', 'History', 'history'):
    webbrowser.open_new_tab('https://journals.lww.com/pidj/fulltext/2005/11001/history_and_recent_advances_in_coronavirus.12.aspx')
    print("most of peoples are saying it rised from china, sadly i am not a doctor")
    print("i am just a programmer! thats why i think i should redirect you to link")

elif my_users in ('h', 'H', 'help', 'Help'):
    print("""
    {{{The help/support of this tool, Thanks for using our script}}}
    
    A or a : [ enter "a or A" in main menu to check world wide corrona cases and map ]
    
    B or b : [ "b or B" for safety tips, how to be safe etc ]
    
    C or c : [ "c or C" for signs of corrona virus, infected or not  ]
    
    D or d : [ "d or D" for history of corrona virus how and from where spread ]
    
    H or h : [ "h or H" Help command of this tool how to run ]
    _______________________________________________________________________________________________
    Auther : AnonBaloch| Certified EthicalHacker, FullStack Web-developer and Server-Administrator 
    """)
# if user didn't input anything,,
else:
    print("please enter 'H or h' in menu to read commandline of this tool")