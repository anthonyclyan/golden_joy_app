from pypdf import PdfReader, PdfWriter
from datetime import datetime
import os

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
        blank_acknowledgement_confirmation_source_path = 'blank_PDF/blank_good_well_acknowledgement_confirmation.pdf'
        blank_acknowledgement_confirmation_to_fill_path = 'blank_PDF/blank_good_well_acknowledgement_confirmation_to_fill.pdf'
        copy_and_paste_file(blank_acknowledgement_confirmation_source_path, blank_acknowledgement_confirmation_to_fill_path)

        reader = PdfReader(blank_acknowledgement_confirmation_to_fill_path)
        writer = PdfWriter()

        writer.append(reader)

        for i in range(len(reader.pages)):
            writer.update_page_form_field_values(writer.pages[i], dict_data)
        
        with open(employer_hkid + "_" + contract_number + "_acknowledgement_confirmation.pdf", "wb") as output_stream:
            writer.write(output_stream)

        # Remove the copied PDF that undergone above steps
        os.remove(blank_acknowledgement_confirmation_to_fill_path)

        print("acknowledgement and confirmation done")
    except Exception as e:
        print(f'Error: {e}')

def fill_service_agreement(dict_data, contract_number, employer_hkid):
    try:
        # Make a copy of original file then append the copied PDF
        blank_service_agreement_source_path = 'blank_PDF/blank_good_well_service_agreement.pdf'
        blank_service_agreement_to_fill_path = 'blank_PDF/blank_good_well_service_agreement_to_fill.pdf'
        copy_and_paste_file(blank_service_agreement_source_path, blank_service_agreement_to_fill_path)

        reader = PdfReader(blank_service_agreement_to_fill_path)
        writer = PdfWriter()

        writer.append(reader)

        for i in range(len(reader.pages)):
            writer.update_page_form_field_values(writer.pages[i], dict_data)
        
        with open(employer_hkid + "_" + contract_number + "_service_agreement.pdf", "wb") as output_stream:
            writer.write(output_stream)

        # Remove the copied PDF that undergone above steps
        os.remove(blank_service_agreement_to_fill_path)

        print("service agreement done")
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
    
    return None

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