#!/usr/bin/python3
"""Module for generating invitation files from a template."""


def generate_invitations(template, attendees):
    """
    Generate personalized invitation files from a template.

    Args:
        template (str): Template string with placeholders
        attendees (list): List of dictionaries containing attendee data

    Returns:
        None
    """
    # Check input types
    if not isinstance(template, str):
        print("Error: Template must be a string")
        return

    if not isinstance(attendees, list):
        print("Error: Attendees must be a list of dictionaries")
        return

    # Check if attendees is a list of dictionaries
    if attendees and not all(isinstance(item, dict) for item in attendees):
        print("Error: Attendees must be a list of dictionaries")
        return

    # Handle empty inputs
    if not template:
        print("Template is empty, no output files generated.")
        return

    if not attendees:
        print("No data provided, no output files generated.")
        return

    # Process each attendee
    for index, attendee in enumerate(attendees, start=1):
        # Create a copy of the template for this attendee
        invitation = template

        # Replace placeholders with actual values or "N/A"
        invitation = invitation.replace("{name}", str(attendee.get("name") or "N/A"))
        invitation = invitation.replace("{event_title}", str(attendee.get("event_title") or "N/A"))
        invitation = invitation.replace("{event_date}", str(attendee.get("event_date") or "N/A"))
        invitation = invitation.replace("{event_location}", str(attendee.get("event_location") or "N/A"))

        # Handle None values explicitly
        invitation = invitation.replace("None", "N/A")

        # Generate output file
        output_filename = f"output_{index}.txt"
        try:
            with open(output_filename, 'w') as output_file:
                output_file.write(invitation)
        except Exception as e:
            print(f"Error writing file {output_filename}: {e}")
