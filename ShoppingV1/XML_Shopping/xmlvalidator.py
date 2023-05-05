
import logging
import xmlschema

def validate(file1,file2):

    # Load the XSD schema file
    xsd_file = file1
    try:
        schema = xmlschema.XMLSchema(xsd_file)
    except Exception as e:
        print(f"Failed to load XSD schema file: {e}")
        raise

    # Load the XML data file
    xml_file = file2
    try:
        with open(xml_file, 'r') as f:
            xml_data = f.read()
    except Exception as e:
        print(f"Failed to load XML data file: {e}")
        raise

    # Validate the XML data against the XSD schema
    is_valid = schema.is_valid(xml_data)

    # Log the validation result
    if is_valid:
        return True
    #    print("The XML data is valid according to the XSD schema.")
    #    print(xml_data)
    else:
        print("The XML data is not valid according to the XSD schema.")
        print(schema.validate(xml_data))
