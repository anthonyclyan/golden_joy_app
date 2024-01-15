from pypdf import PdfReader, PdfWriter
from datetime import datetime
import math
import os

def copy_and_paste_file(source_path, destination_path):
    bash_script_content = f'''
#!/bin/bash

# Declare variable in bash script
source_path="{source_path}"
destination_path="{destination_path}"

# Use variable in bash script
cp -R $source_path $destination_path
'''
    # Write the bash script content to a file
    bash_script_path = 'generate_script.sh'
    with open(bash_script_path, 'w') as bash_script_file: bash_script_file.write(bash_script_content)

    # Make the Bash script executable
    os.system(f'chmod +x {bash_script_path}')

    # Run the Bash script
    os.system(f'./{bash_script_path}')

    # Optionally, you can remove the generated Bash script after execution
    os.remove(bash_script_path)



def fill_infoSheet (dict_data, contract_number, employer_hkid):
    try:
        # Make a copy of original file then append the copied PDF
        blank_infoSheet_source_path = 'blank_PDF/blank_infoSheet.pdf'
        blank_infoSheet_to_fill_path = 'blank_PDF/blank_infoSheet_to_fill.pdf'
        copy_and_paste_file(blank_infoSheet_source_path, blank_infoSheet_to_fill_path)

        reader = PdfReader(blank_infoSheet_to_fill_path)
        writer = PdfWriter()

        writer.append(reader)

        for i in range(len(reader.pages)):
            writer.update_page_form_field_values(writer.pages[i], dict_data)
        
        with open(employer_hkid + "_" + contract_number + "_infoSheet.pdf", "wb") as output_stream:
            writer.write(output_stream)

        # Remove the copied PDF that undergone above steps
        os.remove(blank_infoSheet_to_fill_path)

        print("infoSheet done")
    except Exception as e:
        print(f'Error: {e}')

def fill_transmittalForm (dict_data, contract_number, employer_hkid):
    try:
        # Make a copy of original file then append the copied PDF
        blank_transmittalForm_source_path = 'blank_PDF/blank_transmittalForm.pdf'
        blank_transmittalForm_to_fill_path = 'blank_PDF/blank_transmittalForm_to_fill.pdf'
        copy_and_paste_file(blank_transmittalForm_source_path, blank_transmittalForm_to_fill_path)

        reader = PdfReader(blank_transmittalForm_to_fill_path)
        writer = PdfWriter()
        
        writer.append(reader)

        for i in range(len(reader.pages)):
            writer.update_page_form_field_values(writer.pages[i], dict_data)
        
        with open(employer_hkid + "_" + contract_number + "_transmittalForm.pdf", "wb") as output_stream:
            writer.write(output_stream)

        # Remove the copied PDF that undergone above steps
        os.remove(blank_transmittalForm_to_fill_path)

        print("Transmittal form done")
    except Exception as e:
        print(f'Error: {e}')

def fill_owwa(dict_data, contract_number, employer_hkid):
    try:
        # Make a copy of original file then append the copied PDF
        blank_owwa_source_path = 'blank_PDF/blank_owwa.pdf'
        blank_owwa_to_fill_path = 'blank_PDF/blank_owwa_to_fill.pdf'
        copy_and_paste_file(blank_owwa_source_path, blank_owwa_to_fill_path)

        reader = PdfReader(blank_owwa_to_fill_path)
        writer = PdfWriter()

        writer.append(reader)

        for i in range(len(reader.pages)):
            writer.update_page_form_field_values(writer.pages[i], dict_data)
        
        with open(employer_hkid + "_" + contract_number + "_owwa.pdf", "wb") as output_stream:
            writer.write(output_stream)


        # Remove the copied PDF that undergone above steps
        os.remove(blank_owwa_to_fill_path)

        print("OWWA form done")
    except Exception as e:
        print(f'Error: {e}')

def fill_id407(dict_data, contract_number, employer_hkid):
    try:
        # Make a copy of original file then append the copied PDF
        blank_id407_source_path = 'blank_PDF/blank_id407.pdf'
        blank_id407_to_fill_path = 'blank_PDF/blank_id407_to_fill.pdf'
        copy_and_paste_file(blank_id407_source_path, blank_id407_to_fill_path)

        reader = PdfReader(blank_id407_to_fill_path)
        writer = PdfWriter()

        writer.append(reader)

        for i in range(len(reader.pages)):
            writer.update_page_form_field_values(writer.pages[i], dict_data)
        
        with open(employer_hkid + "_" + contract_number + "_id407.pdf", "wb") as output_stream:
            writer.write(output_stream)

        # Remove the copied PDF that undergone above steps
        os.remove(blank_id407_to_fill_path)

        print("id407 done")
    except Exception as e:
        print(f'Error: {e}')

def fill_acknowledgement_confirmation_form(dict_data, contract_number, employer_hkid):
    try:
        # Make a copy of original file then append the copied PDF
        blank_golden_joy_acknowledgement_confirmation_source_path = 'blank_PDF/blank_golden_joy_acknowledgement_confirmation.pdf'
        blank_golden_joy_acknowledgement_confirmation_to_fill_path = 'blank_PDF/blank_golden_joy_acknowledgement_confirmation_to_fill.pdf'
        copy_and_paste_file(blank_golden_joy_acknowledgement_confirmation_source_path, blank_golden_joy_acknowledgement_confirmation_to_fill_path)

        reader = PdfReader(blank_golden_joy_acknowledgement_confirmation_to_fill_path)
        writer = PdfWriter()

        writer.append(reader)

        for i in range(len(reader.pages)):
            writer.update_page_form_field_values(writer.pages[i], dict_data)
        
        with open(employer_hkid + "_" + contract_number + "_acknowledgement_confirmation.pdf", "wb") as output_stream:
            writer.write(output_stream)

        # Remove the copied PDF that undergone above steps
        os.remove(blank_golden_joy_acknowledgement_confirmation_to_fill_path)

        print("acknowledgement and confirmation done")
    except Exception as e:
        print(f'Error: {e}')


def split_long_string(input_string, max_lengths):
    # Split the input string into words
    words = input_string.split()
    
    # Initialize a list to store the resulting strings
    result_strings = []

    # Split the words into parts based on the specified maximum lengths
    for max_length in max_lengths:
        if words:
            # Initialize a list to store the words for the current part
            current_part = []

            # While there are words and the current part hasn't reached its maximum length
            while words and len(' '.join(current_part + [words[0]])) <= max_length:
                current_part.append(words.pop(0))

            # Save the current part as a string in the list
            result_strings.append(' '.join(current_part))
        else:
            # If no more words are left but there are remaining lengths
            result_strings.append("")

    return result_strings

def calculate_birthday (birthdate):
    if birthdate != "":
        # Convert the birthdate string to a datetime object
        birth_date = datetime.strptime(birthdate, "%Y-%m-%d")

        # Get the current date
        current_date = datetime.now()

        # Calculate the age
        age = current_date.year - birth_date.year - ((current_date.month, current_date.day) < (birth_date.month, birth_date.day))
        
        return age
    else:
        return ""

combined_data = {

    "hk_agency_name": "JOJO GOOD WELL EMPLOYMENT AGENCY LIMITED",
    "hk_agency_phone_number": "64656060",
    "philippine_agency_name": "PLACEWELL INTERNATINOAL SERVICE CORPORATION",
    "philippine_agency_phone_number": "63285264838",
    "philippine_agency_code": "MWOHK-2023-170",
    "witness1_name": "CHOW SUK FAN",
    "witness2_name": "KATHERINE CHOW",
    "contract_category": "NEW",
    "contract_number": "P856456",
    "contract_date": "2023-12-08",
    "owwa_recipt_number": "",
    "wage": "4870",
    "allowance": "1236",
    "other_allowance": "",
    "paid_vacation_for_renew_contract": "N/A",
    "employer_sur_name": "MAN",
    "employer_first_name": "SIN",
    "employer_middle_name": "NING",
    "employer_birthday": "1987-10-04",
    "employer_gender": "FEMALE",
    "employer_nationality": "CHINESE",
    "employer_hkid": "Z834474(5)",
    "employer_passport_number": "",
    "employer_civil_status": "MARRIED",
    "employer_email": "",
    "employer_hk_phone_number": "63166282",
    "employer_spouse_sur_name": "CHAN",
    "employer_spouse_first_name": "HO",
    "employer_spouse_middle_name": "HEI",
    "employer_spouse_hkid": "Z754094(A)",
    "employer_spouse_passport_number": "",
    "employer_address": "FLAT H 17/F BLK 4 VERY VERY VERY VERY VERY VERY VERY VERY VERY LONG ADDRESS CASCADES 93 CHUNG HAU ST HO MAN TIN KLN",
    "employer_residential_type": "FLAT",
    "employer_residential_size": "500",
    "employer_house_type_remarks": "",
    "employer_expected_baby": "",
    "employer_child_0_to_5": "1",
    "employer_child_5_to_18": "",
    "employer_adult": "2",
    "employer_current_worker_number": "",
    "employer_servant_own_room": "YES",
    "employer_servant_own_room_size": "50",
    "employer_servant_share_room_with_how_many_children": "",
    "employer_servant_share_room_with_children_age": "",
    "employer_servant_room_other_with_remarks": "",
    "employer_provide_light_and_water_supply": "YES",
    "employer_provide_toilet_and_bathing_facilities": "YES",
    "employer_provide_bed": "YES",
    "employer_provide_blankets_or_quilt": "YES",
    "employer_provide_pillows": "YES",
    "employer_provide_wardrobe": "YES",
    "employer_provide_refrigerator": "NO",
    "employer_provide_desk": "NO",
    "employer_provide_other_facilities": "",
    "employer_expect_other_duties": "",
    "helper_sur_name": "RIOLALAS",
    "helper_first_name": "MICHELLE",
    "helper_middle_name": "CANAVERAL",
    "helper_birthday": "1985-02-27",
    "helper_place_of_birth": "COMPOSTELA DAVAO",
    "helper_gender": "FEMALE",
    "helper_civil_status": "SINGLE",
    "helper_hkid": "",
    "helper_passport_number": "P5434873B",
    "helper_passport_issue_place": "PE KUWAIT",
    "helper_passport_issue_date": "2020-08-26",
    "helper_passport_expire_date": "2030-08-25",
    "helper_visa_expire_date": "",
    "helper_id522_appointment_date": "",
    "helper_hk_phone_number": "",
    "helper_philippine_phone_number": "9851485084",
    "helper_address": "ZONE 1 PUROK 15 VERY VERY VERY VERY VERY VERY VERY VERY VERY POBLACION COMPOSTELA DAVAO DE ORO POST CODE 8803 PHILIPPINES",
    "helper_previous_contract_number": "",
    "helper_previous_contract_finish_date": "",
    "helper_philippine_contact_person": "HAROLD RIOLALAS",
    "helper_philippine_contact_person_relationship": "BROTHER",
    "helper_philippine_contact_person_phone_number": "9190658782",
    "helper_philippine_contact_person_birthday": "",
    "helper_philippine_contact_person_address": "ZONE 1 PUROK 15 VERY VERY VERY VERY VERY VERY VERY VERY VERY POBLACION COMPOSTELA DAVAO DE ORO POST CODE 8803 PHILIPPINES",
    "owwa_contract_date": "2023-12-06",
    "employer_name": "MAN SIN NING",
    "employer_birthday_year": "1987",
    "employer_birthday_month": "10",
    "employer_birthday_day": "04",
    "helper_birthday_year": "1985",
    "helper_birthday_month": "02",
    "helper_birthday_day": "27",
    "helper_philippine_contact_person_address_1": "",
    "helper_philippine_contact_person_address_2": "",
    "helper_philippine_contact_person_address_3": "",
    "category_new": "X",
    "employer_age": 36,
    "helper_age": 38,
    "helper_female": "X",
    "helper_single": "X",
    "infoSheet_helper_philippine_contact_person_and_relationship": "HAROLD RIOLALAS / BROTHER",
    "infoSheet_employer_address_1": "FLAT H 17/F BLK 4",
    "infoSheet_employer_address_2": "CASCADES 93 CHUNG HAU",
    "infoSheet_employer_address_3": "ST HO MAN TIN KLN",
    "helper_name": "RIOLALAS MICHELLE CANAVERAL",
    "id407_date": "2023-12-06",
    "id407_helper_address_1": "ZONE 1 PUROK 15 POBLACION",
    "id407_helper_address_2": "COMPOSTELA DAVAO DE ORO POST CODE 8803 PHILIPPINES",
    "id407_helper_address_3": "",
    "id407_employer_address_1": "FLAT H 17/F BLK 4 CASCADES 93 CHUNG",
    "id407_employer_address_2": "HAU ST HO MAN TIN KLN",
    "employer_name_for_signature": "MAN SIN NING",
    "helper_name_for_signature": "RIOLALAS MICHELLE CANAVERAL",
    "employer_residential_erase_house": "XXXXX",
    "employer_servant_own_room_yes": "X",
    "employer_provide_light_and_water_supply_yes": "X",
    "employer_provide_toilet_and_bathing_facilities_yes": "X",
    "employer_provide_bed_yes": "X",
    "employer_provide_blankets_or_quilt_yes": "X",
    "employer_provide_pillows_yes": "X",
    "employer_provide_wardrobe_yes": "X",
    "employer_provide_refrigerator_no": "X",
    "employer_provide_desk_no": "X",
    "employer_provide_other_facilities_1": "",
    "employer_provide_other_facilities_2": "",
    "employer_provide_other_facilities_3": "",
    "employer_expect_other_duties_1": "",
    "employer_expect_other_duties_2": "",
    "employer_expect_other_duties_3": "",
    "employer_expect_other_duties_4": "",
    "employer_sign_id407_date": "2023-12-06",
    "helper_sign_id407_date": "2023-12-06",
    "employer_name_page1": "MAN SIN NING",
    "employer_name_page2": "MAN SIN NING",
    "helper_name_page1": "RIOLALAS MICHELLE CANAVERAL",
    "helper_name_page2": "RIOLALAS MICHELLE CANAVERAL",
    "contract_number_page1_1": "P856456",
    "contract_number_page1_2": "P856456",
    "contract_number_page1_3": "P856456",
    "contract_number_page2_1": "P856456",
    "contract_number_page2_2": "P856456",
    "contract_number_page2_3": "P856456"
}
# OWWA
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


# infoSheet
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


# id407
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

# To ensure the employer address string fits in the 2 rows or 1 row if address is too long
id407_employer_address_max_length_row_1 = 35
id407_employer_address_max_length_row_2 = 106
# id407_employer_address_max_row = 1
# if len(combined_data["employer_address"]) > (id407_employer_address_max_length_row_1 + id407_employer_address_max_length_row_2):
#     combined_data["id407_employer_address_1"] = ""
#     combined_data["id407_employer_address_2"] = combined_data["employer_address"]
# else:
#     combined_data["id407_employer_address_1"], combined_data["id407_employer_address_2"] = split_long_string(combined_data["employer_address"], [id407_employer_address_max_length_row_1, id407_employer_address_max_length_row_2])
combined_data["id407_employer_address_1"], combined_data["id407_employer_address_2"] = split_long_string(combined_data["employer_address"], [id407_employer_address_max_length_row_1, id407_employer_address_max_length_row_2])


# Page 2
combined_data["employer_name_for_signature"] = combined_data["employer_name"]
combined_data["helper_name_for_signature"] = combined_data["helper_name"]

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


# acknowledgement and confirmation form
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


# Call functions to write to PDF
fill_owwa(combined_data, combined_data["contract_number"], combined_data["employer_hkid"])
fill_infoSheet(combined_data, combined_data["contract_number"], combined_data["employer_hkid"])
fill_id407(combined_data, combined_data["contract_number"], combined_data["employer_hkid"])
fill_acknowledgement_confirmation_form(combined_data, combined_data["contract_number"], combined_data["employer_hkid"])

'''
DONE:
- INFOSHEET 
    - CONTRACT ADDRESS TOO LONG DOES NOT FIT
- id988a
    - CANNOT DO, HK GOV LOCKED PDF WITH PASSWORD
- id988b
    - CANNOT DO, HK GOV LOCKED PDF WITH PASSWORD

id407
    placement still bad
    2 years boy too small

owwa
    use new form




create desktop icon app and run a sh base file
x2 new PDF
'''