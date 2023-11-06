from pypdf import PdfReader, PdfWriter
from datetime import datetime
import math

def fill_infoSheet (dict_data, contract_number, employer_hkid):
    try:
        reader = PdfReader('blank_PDF/blank_infoSheet.pdf')
        # reader = PdfReader('blank_PDF/blank_infoSheet_flat_with_fields.pdf')
        writer = PdfWriter()

        writer.append(reader)

        for i in range(len(reader.pages)):
            writer.update_page_form_field_values(writer.pages[i], dict_data)
        
        with open(employer_hkid + "_" + contract_number + "_infoSheet.pdf", "wb") as output_stream:
            writer.write(output_stream)

        print("infoSheet done")
    except Exception as e:
        print(f'Error: {e}')

def fill_transmittalForm (dict_data, contract_number, employer_hkid):
    try:
        reader = PdfReader('blank_PDF/blank_transmittalForm.pdf')
        writer = PdfWriter()
        
        writer.append(reader)

        for i in range(len(reader.pages)):
            writer.update_page_form_field_values(writer.pages[i], dict_data)
        
        with open(employer_hkid + "_" + contract_number + "_transmittalForm.pdf", "wb") as output_stream:
            writer.write(output_stream)

        print("Transmittal form done")
    except Exception as e:
        print(f'Error: {e}')

def fill_owwa(dict_data, contract_number, employer_hkid):
    try:
        reader = PdfReader('blank_PDF/blank_owwa.pdf')
        writer = PdfWriter()

        writer.append(reader)

        for i in range(len(reader.pages)):
            writer.update_page_form_field_values(writer.pages[i], dict_data)
        
        with open(employer_hkid + "_" + contract_number + "_owwa.pdf", "wb") as output_stream:
            writer.write(output_stream)

        print("OWWA form done")
    except Exception as e:
        print(f'Error: {e}')

def fill_id407(dict_data, contract_number, employer_hkid):
    try:
        reader = PdfReader('blank_PDF/blank_id407.pdf')
        writer = PdfWriter()

        writer.append(reader)

        for i in range(len(reader.pages)):
            writer.update_page_form_field_values(writer.pages[i], dict_data)
        
        with open(employer_hkid + "_" + contract_number + "_id407.pdf", "wb") as output_stream:
            writer.write(output_stream)

        print("id407 done")
    except Exception as e:
        print(f'Error: {e}')

def fill_acknowledgement_confirmation_form(dict_data, contract_number, employer_hkid):
    try:
        reader = PdfReader('blank_PDF/blank_golden_joy_acknowledgement_confirmation.pdf')
        writer = PdfWriter()

        writer.append(reader)

        for i in range(len(reader.pages)):
            writer.update_page_form_field_values(writer.pages[i], dict_data)
        
        with open(employer_hkid + "_" + contract_number + "_acknowledgement_confirmation.pdf", "wb") as output_stream:
            writer.write(output_stream)

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
    "witness1_name": "CHOW SUK FUN",
    "witness2_name": "KATHERINE CHOW",
    # Misc.
    # "category": "NEW",     # drop down set default category to NEW
    # "category": "RECONTRACT",     # drop down set default category to NEW
    # "category": "TRANSFER",     # drop down set default category to NEW
    # "category": "FINISHED",     # drop down set default category to NEW
    "category": "TERMINATED",     # drop down set default category to NEW
    "contract_number": "P282923",
    "contract_date": "",
    "owwa_recipt_number": "",
    "wage": "4870",     # set default wage = 4870
    "allowance": "1236",    # set default allowance = 1236
    "other_allowance": "",
    "paid_vacation_for_renew_contract": "N/A",     # set default to N/A
    # Employer details
    "employer_sur_name": "PING",
    "employer_first_name": "FONG",
    "employer_middle_name": "",
    "employer_birthday": "1968-10-10",
    # "employer_age": "",
    "employer_gender": "",
    "employer_nationality": "CHINESE",  # set default nationality to CHINESE
    "employer_hkid": "Y142159(8)",
    "employer_passport_number": "",
    "employer_civil_status": "SINGLE",  # set default civil status to SINGLE
    "employer_email": "",
    "employer_hk_phone_number": "",
    "employer_spouse_sur_name": "",
    "employer_spouse_first_name": "",
    "employer_spouse_middle_name": "",
    "employer_spouse_hkid": "",
    "employer_spouse_passport_number": "",
    "employer_address": "FLAT D 3/F BLK 5 CSD ADDITIONAL DEPT QTRS 8 RAZOR HILL RAZOR HILL NEW TERRITORIES",
    "employer_residential_type": "HOUSE",    # set default residential type to FLAT
    # "employer_residential_type": "FLAT",    # set default residential type to FLAT
    "employer_residential_size": "650",
    "employer_house_type_remarks": "",
    "employer_expected_baby": "",
    "employer_child_0_to_5": "1",
    "employer_child_5_to_18": "",
    "employer_adult": "2",
    "employer_people_to_be_served": "",
    "employer_current_worker_number": "0",
    # "employer_servant_own_room": "YES",    # set default servant room to YES
    "employer_servant_own_room": "NO, OTHER",    # set default servant room to YES
    # "employer_servant_own_room": "NO, SHARE WITH CHILD/OTHER",    # set default servant room to YES
    "employer_servant_own_room_size": "",
    # "employer_servant_room_shared_with": "",
    "employer_servant_share_room_with_how_many_children": "1",
    "employer_servant_share_room_with_children_age": "1 YEAR BOY",
    "employer_servant_room_other_with_remarks": "",
    "employer_provide_light_and_water_supply": "YES",
    "employer_provide_toilet_and_bathing_facilities": "YES",
    "employer_provide_bed": "YES",
    "employer_provide_blankets_or_quilt": "YES",
    "employer_provide_pillows": "YES",
    "employer_provide_wardrobe": "YES",
    "employer_provide_refrigerator": "YES",
    "employer_provide_desk": "YES",
    "employer_provide_other_facilities": "",
    "employer_expect_other_duties": "",
    # Helper
    "helper_sur_name": "PUGAO",
    "helper_first_name": "ANA BELLY",
    "helper_middle_name": "PIRAL",
    "helper_birthday": "1981-07-18",
    "helper_place_of_birth": "",
    # "helper_age": "",
    "helper_gender": "FEMALE",
    "helper_civil_status": "MARRIED",    # set default civil status to SINGLE
    "helper_hkid": "WX517066(2)",
    "helper_passport_number": "P9074638A",
    "helper_passport_issue_place": "",
    "helper_passport_issue_date": "",
    "helper_passport_expire_date": "2028-10-08",
    "helper_visa_expire_date": "2023-12-30",
    "helper_id522_appointment_date": "",
    "helper_hk_phone_number": "93325575",
    "helper_philippine_phone_number": "09504909612",
    "helper_address": "BARANGAY POBLACTION MOLO ILOILO CITY PHILIPPINES 5000",
    "helper_previous_contract_number": "",
    "helper_previous_contract_finish_date": "",
    "helper_philippine_contact_person": "TESSIE P. MAHINAY",
    "helper_philippine_contact_person_relationship": "AUNTIE",
    "helper_philippine_contact_person_phone_number": "09982404767",
    "helper_philippine_contact_person_birthday": "1979-09-02",
    "helper_philippine_contact_person_address": "VILLA CRISTINA SUBDIVISION BLOCK 26 LOT 17 BRGY. CAGBANG OTON ILOILO CITY PHILIPPINES 5020"
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
if combined_data["category"] == "NEW":
    combined_data["category_new"] = "X"
elif combined_data["category"] == "RECONTRACT":
    combined_data["category_recontract"] = "X"
elif combined_data["category"] == "TRANSFER":
    combined_data["category_transfer"] = "X"
elif combined_data["category"] == "FINISHED":
    combined_data["category_finished"] = "X"
elif combined_data["category"] == "TERMINATED":
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
INFOSHEET 
    CONTRACT ADDRESS TOO LONG DOES NOT FIT


id407
    placement still bad
    2 years boy too small


create desktop icon app and run a sh base file
x2 new PDF
'''