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
    "witness1_name": "CHOW SUK FAN",
    "witness2_name": "KATHERINE CHOW",
    "contract_category": "NEW",
    "contract_number": "P856451",
    "contract_date": "2023-10-30",
    "owwa_recipt_number": "",
    "wage": "4870",
    "allowance": "1236",
    "other_allowance": "",
    "paid_vacation_for_renew_contract": "N/A",
    "employer_sur_name": "MA",
    "employer_first_name": "CHING",
    "employer_middle_name": "YUK",
    "employer_birthday": "1948-10-01",
    "employer_gender": "MALE",
    "employer_nationality": "CHINESE",
    "employer_hkid": "A953426(4)",
    "employer_passport_number": "",
    "employer_civil_status": "MARRIED",
    "employer_email": "",
    "employer_hk_phone_number": "91303778",
    "employer_spouse_sur_name": "",
    "employer_spouse_first_name": "",
    "employer_spouse_middle_name": "",
    "employer_spouse_hkid": "",
    "employer_spouse_passport_number": "",
    "employer_address": "15 YUK SAU ST HAPPY VALLEY HK",
    "employer_residential_type": "HOUSE",
    "employer_residential_size": "7000",
    "employer_house_type_remarks": "GARDEN 1000 SQ FT",
    "employer_expected_baby": "",
    "employer_child_0_to_5": "1",
    "employer_child_5_to_18": "1",
    "employer_adult": "3",
    "employer_current_worker_number": "2",
    "employer_servant_own_room": "YES",
    "employer_servant_own_room_size": "60",
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
    "helper_sur_name": "LAGHAY",
    "helper_first_name": "ANNIE ROSE",
    "helper_middle_name": "GAID",
    "helper_birthday": "1991-05-29",
    "helper_place_of_birth": "LAGUINDINGAN M O",
    "helper_gender": "FEMALE",
    "helper_civil_status": "SINGLE",
    "helper_hkid": "",
    "helper_passport_number": "P0081168B",
    "helper_passport_issue_place": "PE RIYADH",
    "helper_passport_issue_date": "2019-01-03",
    "helper_passport_expire_date": "",
    "helper_visa_expire_date": "2029-01-02",
    "helper_id522_appointment_date": "",
    "helper_hk_phone_number": "",
    "helper_philippine_phone_number": "9754000704",
    "helper_address": "ZONE 2 MAUSWAGON LAGUINDINGAN MISAMIS ORIENTAL PHILIPPINES POST CODE 9019",
    "helper_previous_contract_number": "",
    "helper_previous_contract_finish_date": "",
    "helper_philippine_contact_person": "BRENDA G LAGHAY",
    "helper_philippine_contact_person_relationship": "MOTHER",
    "helper_philippine_contact_person_phone_number": "9754000740",
    "helper_philippine_contact_person_birthday": "",
    "helper_philippine_contact_person_address": "",
    "owwa_contract_date": "2023-11-22",
    "employer_name": "MA CHING YUK",
    "employer_birthday_year": "1948",
    "employer_birthday_month": "10",
    "employer_birthday_day": "01",
    "helper_birthday_year": "1991",
    "helper_birthday_month": "05",
    "helper_birthday_day": "29",
    "helper_philippine_contact_person_address_1": "",
    "helper_philippine_contact_person_address_2": "",
    "helper_philippine_contact_person_address_3": "",
    "category_new": "X",
    "employer_age": 75,
    "helper_age": 32,
    "helper_female": "X",
    "helper_single": "X",
    "infoSheet_helper_philippine_contact_person_and_relationship": "BRENDA G LAGHAY / MOTHER",
    "infoSheet_employer_address_1": "15 YUK SAU ST HAPPY",
    "infoSheet_employer_address_2": "VALLEY HK",
    "infoSheet_employer_address_3": "",
    "helper_name": "LAGHAY ANNIE ROSE GAID",
    "id407_date": "2023-11-22",
    "id407_helper_address_1": "ZONE 2 MAUSWAGON LAGUINDINGAN",
    "id407_helper_address_2": "MISAMIS ORIENTAL PHILIPPINES POST CODE 9019",
    "id407_helper_address_3": "",
    "id407_employer_address_1": "15 YUK SAU ST HAPPY VALLEY HK",
    "id407_employer_address_2": "",
    "employer_name_for_signature": "MA CHING YUK",
    "helper_name_for_signature": "LAGHAY ANNIE ROSE GAID",
    "employer_residential_erase_flat": "XXX",
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
    "employer_sign_id407_date": "2023-11-22",
    "helper_sign_id407_date": "2023-11-22",
    "employer_name_page1": "MA CHING YUK",
    "employer_name_page2": "MA CHING YUK",
    "helper_name_page1": "LAGHAY ANNIE ROSE GAID",
    "helper_name_page2": "LAGHAY ANNIE ROSE GAID",
    "contract_number_page1_1": "P856451",
    "contract_number_page1_2": "P856451",
    "contract_number_page1_3": "P856451",
    "contract_number_page2_1": "P856451",
    "contract_number_page2_2": "P856451",
    "contract_number_page2_3": "P856451"
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
INFOSHEET 
    CONTRACT ADDRESS TOO LONG DOES NOT FIT


id407
    placement still bad
    2 years boy too small


create desktop icon app and run a sh base file
x2 new PDF
'''