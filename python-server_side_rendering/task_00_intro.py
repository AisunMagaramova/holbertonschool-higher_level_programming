# task_00_intro.py
def generate_invitations(template, attendees):
    # Input tipini yoxla
    if not isinstance(template, str):
        print(f"Error: Invalid template type. Expected str, got {type(template).__name__}")
        return
    if not isinstance(attendees, list) or not all(isinstance(a, dict) for a in attendees):
        print(f"Error: Invalid attendees type. Expected list of dicts, got {type(attendees).__name__}")
        return

    # Boş template yoxlaması
    if template.strip() == "":
        print("Template is empty, no output files generated.")
        return

    # Boş attendee siyahısı yoxlaması
    if not attendees:
        print("No data provided, no output files generated.")
        return

    # Hər bir attendee üçün template doldur
    for index, attendee in enumerate(attendees, start=1):
        personalized_content = template
        for placeholder in ["name", "event_title", "event_date", "event_location"]:
            value = attendee.get(placeholder, "N/A")
            if value is None:
                value = "N/A"
            personalized_content = personalized_content.replace(f"{{{placeholder}}}", str(value))

        # Faylı yaz
        output_filename = f"output_{index}.txt"
        try:
            with open(output_filename, 'w') as f:
                f.write(personalized_content)
            print(f"Generated {output_filename}")
        except Exception as e:
            print(f"Error writing {output_filename}: {e}")

