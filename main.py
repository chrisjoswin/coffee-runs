import decider
import constants
def main():
    turn_index = 0
    coffee_group = []
    menu_dict = {}
    print(constants.INTRO_MESSAGE)
    choice = input("Press y or enter to start program ")

    while choice == "y" or choice == "":
        new_file = decider.open_or_create_excel()
        if len(menu_dict) == 0:
            menu_dict = decider.get_menu_aws()
        if(new_file):
            coffee_group = decider.create_group(menu_dict)
        else:
            coffee_group = decider.get_coffee_group(menu_dict)
            new_group =  input(f"Would you like to use your existing group of {decider.get_names(coffee_group)}?(y/n) ")
            if new_group == "n":
                decider.create_excel_file()
                coffee_group = decider.create_group(menu_dict)
        
        absentee_input = input("List out any absenses from the group today:(press enter if no absences) ")
        absentee_list = []
        if absentee_input:
            absentee_list =  absentee_input.split(', ')
        today_group = decider.today_group_creation(absentee_list, coffee_group)
        turn_index = decider.read_turn(turn_index,coffee_group,today_group)
        choice = input("Would you like to go on another Coffee Run today?(y/n) ")
    print("You have exited Coffee Run Program today. We hope to see you tomorrow!")

if __name__ == "__main__":
    main()
