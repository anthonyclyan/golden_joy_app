from pypdf import PdfReader, PdfWriter
from datetime import datetime

def fill_infoSheet (dict_data, contract_number, employer_hkid):
    try:
        reader = PdfReader('blank_PDF/blank_infoSheet.pdf')
        writer = PdfWriter()

        writer.append(reader)

        for i in range(len(reader.pages)):
            writer.update_page_form_field_values(writer.pages[i], dict_data)
        
        with open(employer_hkid + "_" + contract_number + "_infoSheet.pdf", "wb") as output_stream:
            writer.write(output_stream)

        print("infoSheet done")
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