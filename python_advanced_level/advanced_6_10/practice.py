import re

html_data = '<p class="public">Phone: 111-2223333</p> <p class="secure">Phone: 800-5551234</p>'

pattern = r'(?<=<p class="secure">Phone: )(?P<Area_Code>\d{3})-(?P<Line_Number>\d{7})'

for match in re.finditer(pattern, html_data):
    print(f"Secure Phone Detected!")
    print(f"Area Code: {match.group('Area_Code')}")
    print(f"Line Number: {match.group('Line_Number')}")