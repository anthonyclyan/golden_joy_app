import sys
import json
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QVBoxLayout, QScrollArea, QLabel, QLineEdit, QRadioButton, QComboBox, QPushButton, QButtonGroup
from PyQt5.QtGui import QFont

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
    "philippine_agnecy_code": "MWOHK-2023-170",
    "witness1_name": "CHOW SUK FUN",
    "witness2_name": "KATHERINE CHOW"
}
# Create dictionaries to store user input
employer_pane_dict = {
    # Misc.
    "category": "NEW",     # drop down set default category to NEW
    "contract_number": "",      
    "contract_date": ""    ,
    "owwa_recipt_number": "",
    "wage": "4870",     # set default wage = 4807
    "allowance": "1236",    # set default allowance = 1236
    "other_allowance": "",
    "paid_vacation_for_renew_contract": "N/A",     # set default to N/A
    # Empolyer detials
    "employer_sur_name": "",
    "employer_first_name": "",
    "employer_middle_name": "",
    "employer_birthday": "",
    "employer_age": "",
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
    "employer_people_to_be_served": "",
    "employer_current_worker_number": "",
    "employer_servant_room": "YES",    # set default servant room to YES
    "employer_servant_room_size": "",
    "employer_servant_room_shared_with": "",
    "employer_servant_room_shared_with_remarks": "",
    "employer_servant_room_shared_with_numbers": "",
    "employer_servant_room_shared_with_people_age": "",
    "employer_provide_light_and_water_supply": "",
    "employer_provide_toilet_and_bathing_facilities": "",
    "employer_provide_bed": "",
    "employer_provide_blankets_or_quilt": "",
    "employer_provide_pillows": "",
    "employer_provide_wardrobe": "",
    "employer_provide_refrigerator": "",
    "employer_provide_desk": "",
    "employer_provide_other_facilities": "",
    "employer_expect_other_duties": ""
    }
helper_pane_dict = {
    "helper_sur_name": "",
    "helper_first_name": "",
    "helper_middle_name": "",
    "helper_birthday": "",
    "helper_place_of_birth": "",
    "helper_age": "",
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
    "helper_philippine_contact_person_address": ""
}

# Employer pane with a vertical scroll
employer_scroll_area = QScrollArea()
employer_widget = QWidget()
employer_layout = QVBoxLayout()

employer_scroll_area.setWidget(employer_widget)
employer_scroll_area.setWidgetResizable(True)
employer_widget.setLayout(employer_layout)

# Init title font size
title_font = QFont()
title_font.setPointSize(16)

# Helper function to match the dictionary key and change the value to user input
def employer_input_changed(text, key):
    employer_pane_dict[key] = text

# Employer Pane Title
employer_title = QLabel("Employer")
employer_title.setFont(title_font)
employer_layout.addWidget(employer_title)

# Go through all the key in employer dictionary and display 
for key, value in employer_pane_dict.items():
    formatted_key_string = " ".join(word.capitalize() for word in key.split('_'))
    label = QLabel(formatted_key_string + ":")
    if key == "category":
        combo_box = QComboBox()
        combo_box.addItems(["NEW", "RENEW", "TRANSFER", "FINISHED", "TERMINATED"])
        combo_box.currentIndexChanged.connect(lambda selection, key=key: employer_input_changed(combo_box.itemText(selection), key))
        employer_layout.addWidget(label)
        employer_layout.addWidget(combo_box)
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
        combo_box = QComboBox()
        combo_box.addItems(["N/A", "YES", "NO"])
        combo_box.currentIndexChanged.connect(lambda selection, key=key: employer_input_changed(combo_box.itemText(selection), key))
        employer_layout.addWidget(label)
        employer_layout.addWidget(combo_box)
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
        combo_box = QComboBox()
        combo_box.addItems(["SINGLE", "MARRIED", "WIDOW", "LEGALLY SEPARATED", "SOLO"])
        combo_box.currentIndexChanged.connect(lambda selection, key=key: employer_input_changed(combo_box.itemText(selection), key))
        employer_layout.addWidget(label)
        employer_layout.addWidget(combo_box)
    elif key == "employer_residential_type":
        combo_box = QComboBox()
        combo_box.addItems(["FLAT", "HOUSE"])
        combo_box.currentIndexChanged.connect(lambda selection, key=key: employer_input_changed(combo_box.itemText(selection), key))
        employer_layout.addWidget(label)
        employer_layout.addWidget(combo_box)
    elif key == "employer_residential_size":
        text_input = QLineEdit()
        text_input.setPlaceholderText("(SQ FEET)")
        text_input.textChanged.connect(lambda text, key=key: employer_input_changed(text, key))
        employer_layout.addWidget(label)
        employer_layout.addWidget(text_input)
    elif key == "employer_servant_room":
        combo_box = QComboBox()
        combo_box.addItems(["YES", "SHARE WITH CHILD/OTHER", "OTHER"])
        combo_box.currentIndexChanged.connect(lambda selection, key=key: employer_input_changed(combo_box.itemText(selection), key))
        employer_layout.addWidget(label)
        employer_layout.addWidget(combo_box)
    elif key == "employer_provide_light_and_water_supply":
        employer_provides_button_group_1 = QButtonGroup()
        radio_button_1 = QRadioButton("YES")
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
helper_layout = QVBoxLayout()

helper_scroll_area.setWidget(helper_widget)
helper_scroll_area.setWidgetResizable(True)
helper_widget.setLayout(helper_layout)

def helper_input_changed(text, key):
    helper_pane_dict[key] = text

# Helper Pane Title
helper_title = QLabel("Helper")
helper_title.setFont(title_font)
helper_layout.addWidget(helper_title)

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
        combo_box = QComboBox()
        combo_box.addItems(["SINGLE", "MARRIED", "WIDOW", "LEGALLY SEPARATED", "SOLO"])
        combo_box.currentIndexChanged.connect(lambda selection, key=key: employer_input_changed(combo_box.itemText(selection), key))
        helper_layout.addWidget(label)
        helper_layout.addWidget(combo_box)
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
    
    # Save the dictionary as a separate Python file
    with open('user_input_data.py', 'w') as f:
        f.write(f'user_input_data = {json.dumps(combined_data, indent=4)}')

submit_button.clicked.connect(on_submit)
submit_layout.addWidget(submit_button)

window.show()

sys.exit(app.exec_())
