import sys
import json
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QVBoxLayout, QScrollArea, QLabel, QLineEdit, QRadioButton, QComboBox, QPushButton, QButtonGroup
from PyQt5.QtGui import QFont
from datetime import datetime
from fill_PDF import *
import math
import traceback

# Create the main window
app = QApplication(sys.argv)
window = QMainWindow()
window.setWindowTitle('User Input Form')
window.setGeometry(100, 100, 600, 400)

# Create the central widget to hold the three panes
main_widget = QWidget()
window.setCentralWidget(main_widget)

# Layout for the main widget
main_layout = QVBoxLayout()
main_widget.setLayout(main_layout)

# Create constant dictionary
constant_dict = {
    "hk_agency_name": "JOJO GOOD WELL EMPLOYMENT AGENCY LIMITED",
    "hk_agency_phone_number": "64656060",
    "philippine_agency_name": "PLACEWELL INTERNATINOAL SERVICE CORPORATION",
    "philippine_agency_phone_number": "63285264838",
    "philippine_agency_code": "MWOHK-2023-170",
    "witness1_name": "CHOW SUK FAN",
    "witness2_name": "KATHERINE CHOW"
}
# Create dictionaries to store user input
employer_pane_dict = {
   # Misc.
    "contract_category": "NEW",     # drop down set default contract_category to NEW
    "contract_number": "",
    "contract_date": "",
    "owwa_recipt_number": "",
    "wage": "4990",     # set default wage = 4990
    "allowance": "1236",    # set default allowance = 1236
    "other_allowance": "",
    "paid_vacation_for_renew_contract": "N/A",     # set default to N/A
    # Employer details
    "employer_sur_name": "",
    "employer_first_name": "",
    "employer_middle_name": "",
    "employer_birthday": "",
    # "employer_age": "",
    "employer_gender": "",
    "employer_nationality": "CHINESE",  # set default nationality to CHINESE
    "employer_hkid": "",
    "employer_passport_number": "",
    "employer_civil_status": "SINGLE",  # set default civil status to SINGLE
    "employer_email": "",
    "employer_hk_phone_number": "",
    "employer_spouse_sur_name": "",
    "employer_spouse_first_name": "",
    "employer_spouse_middle_name": "",
    "employer_spouse_hkid": "",
    "employer_spouse_passport_number": "",
    "employer_address": "",
    "employer_residential_type": "FLAT",    # set default residential type to FLAT
    "employer_residential_size": "",
    "employer_house_type_remarks": "",
    "employer_expected_baby": "",
    "employer_child_0_to_5": "",
    "employer_child_5_to_18": "",
    "employer_adult": "",
    # "employer_people_to_be_served": "",
    "employer_current_worker_number": "",
    "employer_servant_own_room": "YES",    # set default servant room to YES
    "employer_servant_own_room_size": "",
    # "employer_servant_room_shared_with": "",
    "employer_servant_share_room_with_how_many_children": "",
    "employer_servant_share_room_with_children_age": "",
    "employer_servant_room_other_with_remarks": "",
    "employer_provide_light_and_water_supply": "YES",       # set default to YES
    "employer_provide_toilet_and_bathing_facilities": "YES",       # set default to YES
    "employer_provide_bed": "YES",       # set default to YES
    "employer_provide_blankets_or_quilt": "YES",       # set default to YES
    "employer_provide_pillows": "YES",       # set default to YES
    "employer_provide_wardrobe": "YES",       # set default to YES
    "employer_provide_refrigerator": "NO",       # set default to NO
    "employer_provide_desk": "NO",       # set default to NO
    "employer_provide_other_facilities": "",
    "employer_expect_other_duties": ""
    }
helper_pane_dict = {
    "helper_sur_name": "",
    "helper_first_name": "",
    "helper_middle_name": "",
    "helper_birthday": "",
    "helper_place_of_birth": "",
    # "helper_age": "",
    "helper_gender": "",
    "helper_civil_status": "SINGLE",    # set default civil status to SINGLE
    "helper_hkid": "",
    "helper_passport_number": "",
    "helper_passport_issue_place": "",
    "helper_passport_issue_date": "",
    "helper_passport_expire_date": "",
    "helper_visa_expire_date": "",
    "helper_id522_appointment_date": "",
    "helper_hk_phone_number": "",
    "helper_philippine_phone_number": "",
    "helper_address": "",
    "helper_previous_contract_number": "",
    "helper_previous_contract_finish_date": "",
    "helper_philippine_contact_person": "",
    "helper_philippine_contact_person_relationship": "",
    "helper_philippine_contact_person_phone_number": "",
    "helper_philippine_contact_person_birthday": "",
    "helper_philippine_contact_person_address": "",
}

# Employer pane with a vertical scroll
employer_scroll_area = QScrollArea()
employer_widget = QWidget()
employer_widget.setStyleSheet("font-size: 20px;")
employer_layout = QVBoxLayout()

employer_scroll_area.setWidget(employer_widget)
employer_scroll_area.setWidgetResizable(True)
employer_widget.setLayout(employer_layout)

# Helper function to match the dictionary key and change the value to user input
def employer_input_changed(text, key):
    employer_pane_dict[key] = text

# Go through all the key in employer dictionary and display 
for key, value in employer_pane_dict.items():
    formatted_key_string = " ".join(word.capitalize() for word in key.split('_'))
    label = QLabel(formatted_key_string + ":")
    if key == "contract_category":
        contract_category_combo_box = QComboBox()
        contract_category_combo_box.addItems(["NEW", "RECONTRACT", "TRANSFER", "FINISHED", "TERMINATED"])
        contract_category_combo_box.currentIndexChanged.connect(lambda selection, key=key: employer_input_changed(contract_category_combo_box.itemText(selection), key))
        employer_layout.addWidget(label)
        employer_layout.addWidget(contract_category_combo_box)
    elif key == "contract_date":
        text_input = QLineEdit()
        text_input.setPlaceholderText("YYYY-MM-DD")
        text_input.textChanged.connect(lambda text, key=key: employer_input_changed(text, key))
        employer_layout.addWidget(label)
        employer_layout.addWidget(text_input)
    elif key == "wage":
        text_input = QLineEdit()
        text_input.setText("4870")
        text_input.textChanged.connect(lambda text, key=key: employer_input_changed(text, key))
        employer_layout.addWidget(label)
        employer_layout.addWidget(text_input)
    elif key == "allowance":
        text_input = QLineEdit()
        text_input.setText("1236")
        text_input.textChanged.connect(lambda text, key=key: employer_input_changed(text, key))
        employer_layout.addWidget(label)
        employer_layout.addWidget(text_input)
    elif key == "paid_vacation_for_renew_contract":
        paid_vacation_for_new_contract_combo_box = QComboBox()
        paid_vacation_for_new_contract_combo_box.addItems(["N/A", "YES", "NO"])
        paid_vacation_for_new_contract_combo_box.currentIndexChanged.connect(lambda selection, key=key: employer_input_changed(paid_vacation_for_new_contract_combo_box.itemText(selection), key))
        employer_layout.addWidget(label)
        employer_layout.addWidget(paid_vacation_for_new_contract_combo_box)
    elif key == "employer_birthday":
        text_input = QLineEdit()
        text_input.setPlaceholderText("YYYY-MM-DD")
        text_input.textChanged.connect(lambda text, key=key: employer_input_changed(text, key))
        employer_layout.addWidget(label)
        employer_layout.addWidget(text_input)
    elif key == "employer_gender":
        employer_gender_radio_buttons_group = QButtonGroup()
        employer_gender_radio_button_1 = QRadioButton("MALE")
        employer_gender_radio_button_2 = QRadioButton("FEMALE")
        employer_gender_radio_buttons_group.addButton(employer_gender_radio_button_1)
        employer_gender_radio_buttons_group.addButton(employer_gender_radio_button_2)
        employer_gender_radio_button_1.toggled.connect(lambda text, key=key: employer_input_changed("MALE", key))
        employer_gender_radio_button_2.toggled.connect(lambda text, key=key: employer_input_changed("FEMALE", key))
        employer_layout.addWidget(label)
        employer_layout.addWidget(employer_gender_radio_button_1)
        employer_layout.addWidget(employer_gender_radio_button_2)
    elif key == "employer_nationality":
        text_input = QLineEdit()
        text_input.setText("CHINESE")
        text_input.textChanged.connect(lambda text, key=key: employer_input_changed(text, key))
        employer_layout.addWidget(label)
        employer_layout.addWidget(text_input)
    elif key == "employer_civil_status":
        employer_civil_status_combo_box = QComboBox()
        employer_civil_status_combo_box.addItems(["SINGLE", "MARRIED", "WIDOW", "LEGALLY SEPARATED", "SOLO"])
        employer_civil_status_combo_box.currentIndexChanged.connect(lambda selection, key=key: employer_input_changed(employer_civil_status_combo_box.itemText(selection), key))
        employer_layout.addWidget(label)
        employer_layout.addWidget(employer_civil_status_combo_box)
    elif key == "employer_residential_type":
        employer_residential_type_combo_box = QComboBox()
        employer_residential_type_combo_box.addItems(["FLAT", "HOUSE"])
        employer_residential_type_combo_box.currentIndexChanged.connect(lambda selection, key=key: employer_input_changed(employer_residential_type_combo_box.itemText(selection), key))
        employer_layout.addWidget(label)
        employer_layout.addWidget(employer_residential_type_combo_box)
    elif key == "employer_residential_size":
        text_input = QLineEdit()
        text_input.setPlaceholderText("(SQ FEET)")
        text_input.textChanged.connect(lambda text, key=key: employer_input_changed(text, key))
        employer_layout.addWidget(label)
        employer_layout.addWidget(text_input)
    elif key == "employer_servant_own_room":
        employer_servant_own_room_combo_box = QComboBox()
        employer_servant_own_room_combo_box.addItems(["YES", "NO, SHARE WITH CHILD", "NO, OTHER"])
        employer_servant_own_room_combo_box.currentIndexChanged.connect(lambda selection, key=key: employer_input_changed(employer_servant_own_room_combo_box.itemText(selection), key))
        employer_layout.addWidget(label)
        employer_layout.addWidget(employer_servant_own_room_combo_box)
    elif key == "employer_servant_own_room_size":
        text_input = QLineEdit()
        text_input.setPlaceholderText("(SQ FEET)")
        text_input.textChanged.connect(lambda text, key=key: employer_input_changed(text, key))
        employer_layout.addWidget(label)
        employer_layout.addWidget(text_input)
    elif key == "employer_provide_light_and_water_supply":
        employer_provides_button_group_1 = QButtonGroup()
        radio_button_1 = QRadioButton("YES")
        # Set the default radio button to "YES"
        radio_button_1.setChecked(True)     
        radio_button_2 = QRadioButton("NO")
        employer_provides_button_group_1.addButton(radio_button_1)
        employer_provides_button_group_1.addButton(radio_button_2)
        radio_button_1.toggled.connect(lambda text, key=key: employer_input_changed("YES", key))
        radio_button_2.toggled.connect(lambda text, key=key: employer_input_changed("NO", key))
        employer_layout.addWidget(label)
        employer_layout.addWidget(radio_button_1)
        employer_layout.addWidget(radio_button_2)
    elif key == "employer_provide_toilet_and_bathing_facilities":
        employer_provides_button_group_2 = QButtonGroup()
        radio_button_1 = QRadioButton("YES")
        # Set the default radio button to "YES"
        radio_button_1.setChecked(True)    
        radio_button_2 = QRadioButton("NO")
        employer_provides_button_group_2.addButton(radio_button_1)
        employer_provides_button_group_2.addButton(radio_button_2)
        radio_button_1.toggled.connect(lambda text, key=key: employer_input_changed("YES", key))
        radio_button_2.toggled.connect(lambda text, key=key: employer_input_changed("NO", key))
        employer_layout.addWidget(label)
        employer_layout.addWidget(radio_button_1)
        employer_layout.addWidget(radio_button_2)
    elif key == "employer_provide_bed":
        employer_provides_button_group_3 = QButtonGroup()
        radio_button_1 = QRadioButton("YES")
        # Set the default radio button to "YES"
        radio_button_1.setChecked(True)    
        radio_button_2 = QRadioButton("NO")
        employer_provides_button_group_3.addButton(radio_button_1)
        employer_provides_button_group_3.addButton(radio_button_2)
        radio_button_1.toggled.connect(lambda text, key=key: employer_input_changed("YES", key))
        radio_button_2.toggled.connect(lambda text, key=key: employer_input_changed("NO", key))
        employer_layout.addWidget(label)
        employer_layout.addWidget(radio_button_1)
        employer_layout.addWidget(radio_button_2)
    elif key == "employer_provide_blankets_or_quilt":
        employer_provides_button_group_4 = QButtonGroup()
        radio_button_1 = QRadioButton("YES")
        # Set the default radio button to "YES"
        radio_button_1.setChecked(True)    
        radio_button_2 = QRadioButton("NO")
        employer_provides_button_group_4.addButton(radio_button_1)
        employer_provides_button_group_4.addButton(radio_button_2)
        radio_button_1.toggled.connect(lambda text, key=key: employer_input_changed("YES", key))
        radio_button_2.toggled.connect(lambda text, key=key: employer_input_changed("NO", key))
        employer_layout.addWidget(label)
        employer_layout.addWidget(radio_button_1)
        employer_layout.addWidget(radio_button_2)
    elif key == "employer_provide_pillows":
        employer_provides_button_group_5 = QButtonGroup()
        radio_button_1 = QRadioButton("YES")
        # Set the default radio button to "YES"
        radio_button_1.setChecked(True)    
        radio_button_2 = QRadioButton("NO")
        employer_provides_button_group_5.addButton(radio_button_1)
        employer_provides_button_group_5.addButton(radio_button_2)
        radio_button_1.toggled.connect(lambda text, key=key: employer_input_changed("YES", key))
        radio_button_2.toggled.connect(lambda text, key=key: employer_input_changed("NO", key))
        employer_layout.addWidget(label)
        employer_layout.addWidget(radio_button_1)
        employer_layout.addWidget(radio_button_2)
    elif key == "employer_provide_wardrobe":
        employer_provides_button_group_6 = QButtonGroup()
        radio_button_1 = QRadioButton("YES")
        # Set the default radio button to "YES"
        radio_button_1.setChecked(True)    
        radio_button_2 = QRadioButton("NO")
        employer_provides_button_group_6.addButton(radio_button_1)
        employer_provides_button_group_6.addButton(radio_button_2)
        radio_button_1.toggled.connect(lambda text, key=key: employer_input_changed("YES", key))
        radio_button_2.toggled.connect(lambda text, key=key: employer_input_changed("NO", key))
        employer_layout.addWidget(label)
        employer_layout.addWidget(radio_button_1)
        employer_layout.addWidget(radio_button_2)
    elif key == "employer_provide_refrigerator":
        employer_provides_button_group_7 = QButtonGroup()
        radio_button_1 = QRadioButton("YES")
        radio_button_2 = QRadioButton("NO")
        # Set the default radio button to "NO"
        radio_button_2.setChecked(True)    
        employer_provides_button_group_7.addButton(radio_button_1)
        employer_provides_button_group_7.addButton(radio_button_2)
        radio_button_1.toggled.connect(lambda text, key=key: employer_input_changed("YES", key))
        radio_button_2.toggled.connect(lambda text, key=key: employer_input_changed("NO", key))
        employer_layout.addWidget(label)
        employer_layout.addWidget(radio_button_1)
        employer_layout.addWidget(radio_button_2)
    elif key == "employer_provide_desk":
        employer_provides_button_group_8 = QButtonGroup()
        radio_button_1 = QRadioButton("YES")
        radio_button_2 = QRadioButton("NO")
        # Set the default radio button to "NO"
        radio_button_2.setChecked(True)
        employer_provides_button_group_8.addButton(radio_button_1)
        employer_provides_button_group_8.addButton(radio_button_2)
        radio_button_1.toggled.connect(lambda text, key=key: employer_input_changed("YES", key))
        radio_button_2.toggled.connect(lambda text, key=key: employer_input_changed("NO", key))
        employer_layout.addWidget(label)
        employer_layout.addWidget(radio_button_1)
        employer_layout.addWidget(radio_button_2)
    else:
        text_input = QLineEdit()
        text_input.textChanged.connect(lambda text, key=key: employer_input_changed(text, key))
        employer_layout.addWidget(label)
        employer_layout.addWidget(text_input)

main_layout.addWidget(employer_scroll_area)

# Helper pane with a vertical scroll
helper_scroll_area = QScrollArea()
helper_widget = QWidget()
helper_widget.setStyleSheet("font-size: 20px;")
helper_layout = QVBoxLayout()

helper_scroll_area.setWidget(helper_widget)
helper_scroll_area.setWidgetResizable(True)
helper_widget.setLayout(helper_layout)

def helper_input_changed(text, key):
    helper_pane_dict[key] = text

for key, value in helper_pane_dict.items():
    formatted_key_string = " ".join(word.capitalize() for word in key.split('_'))
    label = QLabel(formatted_key_string + ":")
    if key == "helper_birthday":
        text_input = QLineEdit()
        text_input.setPlaceholderText("YYYY-MM-DD")
        text_input.textChanged.connect(lambda text, key=key: helper_input_changed(text, key))
        helper_layout.addWidget(label)
        helper_layout.addWidget(text_input)
    elif key == "helper_gender":
        helper_gender_radio_buttons_group = QButtonGroup()
        helper_gender_radio_button_1 = QRadioButton("MALE")
        helper_gender_radio_button_2 = QRadioButton("FEMALE")
        helper_gender_radio_buttons_group.addButton(helper_gender_radio_button_1)
        helper_gender_radio_buttons_group.addButton(helper_gender_radio_button_2)
        helper_gender_radio_button_1.toggled.connect(lambda text, key=key: helper_input_changed("MALE", key))
        helper_gender_radio_button_2.toggled.connect(lambda text, key=key: helper_input_changed("FEMALE", key))
        helper_layout.addWidget(label)
        helper_layout.addWidget(helper_gender_radio_button_1)
        helper_layout.addWidget(helper_gender_radio_button_2)
    elif key == "helper_civil_status":
        helper_civil_status_combo_box = QComboBox()
        helper_civil_status_combo_box.addItems(["SINGLE", "MARRIED", "WIDOW", "LEGALLY SEPARATED", "SOLO"])
        helper_civil_status_combo_box.currentIndexChanged.connect(lambda selection, key=key: helper_input_changed(helper_civil_status_combo_box.itemText(selection), key))
        helper_layout.addWidget(label)
        helper_layout.addWidget(helper_civil_status_combo_box)
    elif key == "helper_passport_issue_date":
        text_input = QLineEdit()
        text_input.setPlaceholderText("YYYY-MM-DD")
        text_input.textChanged.connect(lambda text, key=key: helper_input_changed(text, key))
        helper_layout.addWidget(label)
        helper_layout.addWidget(text_input)
    elif key == "helper_passport_expire_date":
        text_input = QLineEdit()
        text_input.setPlaceholderText("YYYY-MM-DD")
        text_input.textChanged.connect(lambda text, key=key: helper_input_changed(text, key))
        helper_layout.addWidget(label)
        helper_layout.addWidget(text_input)
    elif key == "helper_visa_expire_date":
        text_input = QLineEdit()
        text_input.setPlaceholderText("YYYY-MM-DD")
        text_input.textChanged.connect(lambda text, key=key: helper_input_changed(text, key))
        helper_layout.addWidget(label)
        helper_layout.addWidget(text_input)
    elif key == "helper_id522_appointment_date":
        text_input = QLineEdit()
        text_input.setPlaceholderText("YYYY-MM-DD")
        text_input.textChanged.connect(lambda text, key=key: helper_input_changed(text, key))
        helper_layout.addWidget(label)
        helper_layout.addWidget(text_input)
    elif key == "helper_previous_contract_finish_date":
        text_input = QLineEdit()
        text_input.setPlaceholderText("YYYY-MM-DD")
        text_input.textChanged.connect(lambda text, key=key: helper_input_changed(text, key))
        helper_layout.addWidget(label)
        helper_layout.addWidget(text_input)
    elif key == "helper_philippine_contact_person_birthday":
        text_input = QLineEdit()
        text_input.setPlaceholderText("YYYY-MM-DD")
        text_input.textChanged.connect(lambda text, key=key: helper_input_changed(text, key))
        helper_layout.addWidget(label)
        helper_layout.addWidget(text_input)
    elif key == "helper_philippine_contact_person_birthday":
        text_input = QLineEdit()
        text_input.setPlaceholderText("YYYY-MM-DD")
        text_input.textChanged.connect(lambda text, key=key: helper_input_changed(text, key))
        helper_layout.addWidget(label)
        helper_layout.addWidget(text_input)
    else:
        text_input = QLineEdit()
        text_input.textChanged.connect(lambda text, key=key: helper_input_changed(text, key))
        helper_layout.addWidget(label)
        helper_layout.addWidget(text_input)

main_layout.addWidget(helper_scroll_area)

# Submit pane with a submit button
submit_widget = QWidget()
submit_layout = QVBoxLayout()
main_layout.addWidget(submit_widget)
submit_widget.setLayout(submit_layout)

submit_button = QPushButton("Submit")

def on_submit():
    # Combine different dict data into one dictionary
    combined_data = {**constant_dict, **employer_pane_dict, **helper_pane_dict}
    
    # Create some new key for specific PDF
    # OWWA
    try:
        combined_data["owwa_contract_date"] = datetime.now().strftime('%Y-%m-%d')
        combined_data["employer_name"] = combined_data["employer_sur_name"] + " " + combined_data["employer_first_name"] + " " + combined_data["employer_middle_name"]
        combined_data["employer_birthday_year"], combined_data["employer_birthday_month"], combined_data["employer_birthday_day"] = combined_data["employer_birthday"].split('-')
        combined_data["helper_birthday_year"], combined_data["helper_birthday_month"], combined_data["helper_birthday_day"] = combined_data["helper_birthday"].split('-')
        # Contact person address
        helper_philippine_contact_person_address_max_length_per_row = 19
        helper_philippine_contact_person_address_max_row = 3
        # If the address is longer than 66 characters then evenly split the max_length per row so the font size are similar
        if len(combined_data["helper_philippine_contact_person_address"]) > (helper_philippine_contact_person_address_max_length_per_row*helper_philippine_contact_person_address_max_row):
            really_long_string_max_length_per_row = math.ceil(len(combined_data["helper_philippine_contact_person_address"]) / helper_philippine_contact_person_address_max_row)  # divide and round up
            max_length = []
            for i in range (helper_philippine_contact_person_address_max_row):
                max_length.append(really_long_string_max_length_per_row) 
            combined_data["helper_philippine_contact_person_address_1"], combined_data["helper_philippine_contact_person_address_2"], combined_data["helper_philippine_contact_person_address_3"] = split_long_string(combined_data["helper_philippine_contact_person_address"], max_length)
        else:
            max_length = []
            for i in range (helper_philippine_contact_person_address_max_row):
                max_length.append(helper_philippine_contact_person_address_max_length_per_row)
            combined_data["helper_philippine_contact_person_address_1"], combined_data["helper_philippine_contact_person_address_2"], combined_data["helper_philippine_contact_person_address_3"] = split_long_string(combined_data["helper_philippine_contact_person_address"], max_length)
    except Exception as e:
        print(f'Error: {e}')
        traceback.print_exc()
    
    # infoSheet
    try:
        # Contract contract_category check box
        if combined_data["contract_category"] == "NEW":
            combined_data["category_new"] = "X"
        elif combined_data["contract_category"] == "RECONTRACT":
            combined_data["category_recontract"] = "X"
        elif combined_data["contract_category"] == "TRANSFER":
            combined_data["category_transfer"] = "X"
        elif combined_data["contract_category"] == "FINISHED":
            combined_data["category_finished"] = "X"
        elif combined_data["contract_category"] == "TERMINATED":
            combined_data["category_terminated"] = "X"

        # Calculate age in case we need it
        combined_data["employer_age"] = calculate_birthday(combined_data["employer_birthday"])
        combined_data["helper_age"] = calculate_birthday(combined_data["helper_birthday"])

        # Helper gender check box
        if combined_data["helper_gender"] == "MALE":
            combined_data["helper_male"] = "X"
        elif combined_data["helper_gender"] == "FEMALE":
            combined_data["helper_female"] = "X"

        # Helper civi status check box
        if combined_data["helper_civil_status"] == "MARRIED":
            combined_data["helper_married"] = "X"
        else:
            combined_data["helper_single"] = "X"
        combined_data["infoSheet_helper_philippine_contact_person_and_relationship"] = combined_data["helper_philippine_contact_person"] + " / " + combined_data["helper_philippine_contact_person_relationship"]

        # infoSheet contract address 
        info_sheet_employer_address_max_length_per_row = 22
        info_sheet_employer_address_max_row = 3
        # If the address is longer than 66 characters then evenly split the max_length per row so the font size are similar
        if len(combined_data["employer_address"]) > (info_sheet_employer_address_max_length_per_row*info_sheet_employer_address_max_row):
            really_long_string_max_length_per_row = math.ceil(len(combined_data["employer_address"]) / info_sheet_employer_address_max_row)  # divide and round up
            max_length = []
            for i in range (info_sheet_employer_address_max_row):
                max_length.append(really_long_string_max_length_per_row) 
            combined_data["infoSheet_employer_address_1"], combined_data["infoSheet_employer_address_2"], combined_data["infoSheet_employer_address_3"] = split_long_string(combined_data["employer_address"], max_length)
        else:
            max_length = []
            for i in range (info_sheet_employer_address_max_row):
                max_length.append(info_sheet_employer_address_max_length_per_row)
            combined_data["infoSheet_employer_address_1"], combined_data["infoSheet_employer_address_2"], combined_data["infoSheet_employer_address_3"] = split_long_string(combined_data["employer_address"], max_length)
    except Exception as e:
        print(f'Error: {e}')
        traceback.print_exc()

    # id407
    try:
        # Page 1
        # combined_data["employer_name"] = combined_data["employer_sur_name"] + " " + combined_data["employer_first_name"] + " " + combined_data["employer_middle_name"]    # already exist above for OWWA
        combined_data["helper_name"] = combined_data["helper_sur_name"] + " " + combined_data["helper_first_name"] + " " + combined_data["helper_middle_name"]
        combined_data["id407_date"] = datetime.now().strftime('%Y-%m-%d')

        # To ensure the helper address string fits in the 3 rows or 2 rows if address is too long
        id407_helper_address_max_length_row_1 = 35
        id407_helper_address_max_length_row_2 = 106
        id407_helper_address_max_length_row_3 = 106
        id407_helper_address_max_row = 2        # if string is too long, will just populate in the bottom two long line
        if len(combined_data["helper_address"]) > (id407_helper_address_max_length_row_1 + id407_helper_address_max_length_row_2 + id407_helper_address_max_length_row_3):
            really_long_string_max_length_per_row = math.ceil(len(combined_data["helper_address"]) / info_sheet_employer_address_max_row)  # divide and round up
            max_length = []
            for i in range (id407_helper_address_max_row):
                max_length.append(really_long_string_max_length_per_row)
            combined_data["id407_helper_address_1"] = ""
            combined_data["id407_helper_address_2"], combined_data["id407_helper_address_3"] = split_long_string(combined_data["helper_address"], max_length)
        else:
            max_length = [id407_helper_address_max_length_row_1, id407_helper_address_max_length_row_2, id407_helper_address_max_length_row_3]
            combined_data["id407_helper_address_1"], combined_data["id407_helper_address_2"], combined_data["id407_helper_address_3"] = split_long_string(combined_data["helper_address"], [id407_helper_address_max_length_row_1, id407_helper_address_max_length_row_2, id407_helper_address_max_length_row_3])

        combined_data["commencing_on"] = combined_data["helper_previous_contract_finish_date"]
        combined_data["dh_contract_number"] = combined_data["helper_previous_contract_number"]
    
        # To ensure the employer address string fits in the 2 rows or 1 row if address is too long
        id407_employer_address_max_length_row_1 = 35
        id407_employer_address_max_length_row_2 = 106
        combined_data["id407_employer_address_1"], combined_data["id407_employer_address_2"] = split_long_string(combined_data["employer_address"], [id407_employer_address_max_length_row_1, id407_employer_address_max_length_row_2])

        # Page 2
        combined_data["employer_name_for_signature"] = combined_data["employer_name"]
        combined_data["helper_name_for_signature"] = combined_data["helper_name"]
        combined_data["witness2_name"] = combined_data["witness2_name"]

        # Page 3
        # Cross out FLAT/HOUSE on id407 when the residential type is HOUSE/FLAT
        if combined_data["employer_residential_type"] == "FLAT":
            combined_data["employer_residential_erase_house"] = "XXXXX"
        elif combined_data["employer_residential_type"] == "HOUSE":
            combined_data["employer_residential_erase_flat"] = "XXX"

        # Helper get own room or not
        if combined_data["employer_servant_own_room"] == "YES":
            combined_data["employer_servant_own_room_yes"] = "X"
        else:
            combined_data["employer_servant_own_room_no"] = "X"
            if combined_data["employer_servant_own_room"] == "NO, SHARE WITH CHILD/OTHER":
                # combined_data["employer_servant_own_share_room"] = "X"
                combined_data["employer_servant_share_room"] = "X"
            elif combined_data["employer_servant_own_room"] == "NO, OTHER":
                combined_data["employer_servant_room_other"] = "X"
                # To ensure the other sleeping arrangment are captured evenly on the 2.5 rows
                max_length = [32, 58, 58]
                combined_data["employer_servant_room_other_with_remarks_1"], combined_data["employer_servant_room_other_with_remarks_2"], combined_data["employer_servant_room_other_with_remarks_3"] = split_long_string(combined_data["employer_servant_room_other_with_remarks"], max_length)


        if combined_data["employer_provide_light_and_water_supply"] == "YES":
            combined_data["employer_provide_light_and_water_supply_yes"] = "X"
        else:
            combined_data["employer_provide_light_and_water_supply_no"] = "X"

        if combined_data["employer_provide_toilet_and_bathing_facilities"] == "YES":
            combined_data["employer_provide_toilet_and_bathing_facilities_yes"] = "X"
        else:
            combined_data["employer_provide_toilet_and_bathing_facilities_no"] = "X"

        if combined_data["employer_provide_bed"] == "YES":
            combined_data["employer_provide_bed_yes"] = "X"
        else:
            combined_data["employer_provide_bed_no"] = "X"

        if combined_data["employer_provide_blankets_or_quilt"] == "YES":
            combined_data["employer_provide_blankets_or_quilt_yes"] = "X"
        else:
            combined_data["employer_provide_blankets_or_quilt_no"] = "X"

        if combined_data["employer_provide_pillows"] == "YES":
            combined_data["employer_provide_pillows_yes"] = "X"
        else:
            combined_data["employer_provide_pillows_no"] = "X"

        if combined_data["employer_provide_wardrobe"] == "YES":
            combined_data["employer_provide_wardrobe_yes"] = "X"
        else:
            combined_data["employer_provide_wardrobe_no"] = "X"

        if combined_data["employer_provide_refrigerator"] == "YES":
            combined_data["employer_provide_refrigerator_yes"] = "X"
        else:
            combined_data["employer_provide_refrigerator_no"] = "X"

        if combined_data["employer_provide_desk"] == "YES":
            combined_data["employer_provide_desk_yes"] = "X"
        else:
            combined_data["employer_provide_desk_no"] = "X"

        # To ensure employer provide other facilites are evenly captured in 3 rows
        if len(combined_data["employer_provide_other_facilities"]) > (3*41):
            really_long_string_max_length_per_row = math.ceil(len(combined_data["employer_provide_other_facilities"]) / info_sheet_employer_address_max_row)  # divide and round up
            max_length = []
            for i in range (3):
                max_length.append(really_long_string_max_length_per_row)
            combined_data["employer_provide_other_facilities_1"], combined_data["employer_provide_other_facilities_2"], combined_data["employer_provide_other_facilities_3"] = split_long_string(combined_data["employer_provide_other_facilities"], max_length)
        else:
            max_length = [41, 41, 41]
            combined_data["employer_provide_other_facilities_1"], combined_data["employer_provide_other_facilities_2"], combined_data["employer_provide_other_facilities_3"] = split_long_string(combined_data["employer_provide_other_facilities"], max_length)

        # Page 4
        # To ensure the other duties string fits in the 4 rows
        max_length = [61, 61, 61, 61]
        combined_data["employer_expect_other_duties_1"], combined_data["employer_expect_other_duties_2"], combined_data["employer_expect_other_duties_3"], combined_data["employer_expect_other_duties_4"] = split_long_string(combined_data["employer_expect_other_duties"],max_length)
        combined_data["employer_sign_id407_date"] = datetime.now().strftime('%Y-%m-%d')
        combined_data["helper_sign_id407_date"] = datetime.now().strftime('%Y-%m-%d')
    except Exception as e:
        print(f'Error: {e}')
        traceback.print_exc()

    # acknowledgement and confirmation form
    try:
        combined_data["employer_name_page1"] = combined_data["employer_name"]
        combined_data["employer_name_page2"] = combined_data["employer_name"]
        combined_data["helper_name_page1"] = combined_data["helper_name"]
        combined_data["helper_name_page2"] = combined_data["helper_name"]
        combined_data["contract_number_page1_1"] = combined_data["contract_number"]
        combined_data["contract_number_page1_2"] = combined_data["contract_number"]
        combined_data["contract_number_page1_3"] = combined_data["contract_number"]
        combined_data["contract_number_page2_1"] = combined_data["contract_number"]
        combined_data["contract_number_page2_2"] = combined_data["contract_number"]
        combined_data["contract_number_page2_3"] = combined_data["contract_number"]
    except Exception as e:
        print(f'Error: {e}')
        traceback.print_exc()
    
    # service agreement
    try:
        # Service Agreement
        combined_data["service_agreement_contract_date"] = datetime.now().strftime('%Y-%m-%d')
        combined_data["helper_name_consent"] = combined_data["helper_sur_name"] + " " + combined_data["helper_first_name"] + " " + combined_data["helper_middle_name"]
        combined_data["service_agreement_hk_agency_signature_date"] = datetime.now().strftime('%Y-%m-%d')
    except Exception as e:
        print(f'Error: {e}')
        traceback.print_exc()


    # Save the dictionary as a separate Python file with <CONTRACT_NUMBER>.py for future references
    with open(combined_data["employer_hkid"] + "_" + combined_data["contract_number"] + '_metadata.py', 'w') as f:
        f.write(f'input_data = {json.dumps(combined_data, indent=4)}')
    
    # Create x3 PDF
    fill_infoSheet(combined_data, employer_pane_dict["contract_number"], employer_pane_dict["employer_hkid"])
    fill_owwa(combined_data, employer_pane_dict["contract_number"], employer_pane_dict["employer_hkid"])
    fill_id407(combined_data, combined_data["contract_number"], combined_data["employer_hkid"])
    fill_acknowledgement_confirmation_form(combined_data, combined_data["contract_number"], combined_data["employer_hkid"])
    fill_service_agreement(combined_data, combined_data["contract_number"], combined_data["employer_hkid"])


submit_button.clicked.connect(on_submit)
submit_layout.addWidget(submit_button)

window.show()

sys.exit(app.exec_())
