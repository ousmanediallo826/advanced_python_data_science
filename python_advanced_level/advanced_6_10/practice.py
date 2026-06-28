import re

html_data = '<p class="public">Phone: 111-2223333</p> <p class="secure">Phone: 800-5551234</p>'

pattern = r'(?<=<p class="secure">Phone: )(?P<Area_Code>\d{3})-(?P<Line_Number>\d{7})'

for match in re.finditer(pattern, html_data):
    print(f"Secure Phone Detected!")
    print(f"Area Code: {match.group('Area_Code')}")
    print(f"Line Number: {match.group('Line_Number')}")



#===============Project 1: The AI Content Moderation Filter============
from functools import reduce
raw_list = ["I love this python tutorial!", "This product is trash and an absolute scam", "Hey, check out this cool AI assistant"]
BANNED_WORDS = {"trash", "scam", "horrible"}

mapping_transformation = map(
    lambda comment : {
        "text": comment,
        "is_toxic": any(word.lower() in BANNED_WORDS for word in comment.split()),
        "word_count": len(comment.split()),
    },
    raw_list
)


processed_comments = list(mapping_transformation)

clean_comments = filter(lambda comment: comment["is_toxic"] is False, processed_comments)
filtered_comment = list(clean_comments)


total_toxic_words = reduce(
    lambda acc, comment: acc + sum(1 for word in comment["text"].split() if word.lower() in BANNED_WORDS),
    processed_comments,
    0
)




import pprint
pprint.pprint(processed_comments)
pprint.pprint(filtered_comment)
pprint.pprint(total_toxic_words)



#===========Challenge 1: The Cybersecurity Log Analyst==============
from functools import reduce

BANNED_IPS = {"192.168.1.50", "10.0.0.99"}
server_logs = [
    "LOG: ip:192.168.1.50 bytes:4500 status:failed",
    "LOG: ip:172.16.0.5 bytes:120 status:success",
    "LOG: ip:10.0.0.99 bytes:9800 status:failed",
    "LOG: ip:192.168.1.12 bytes:300 status:success"
]

mapped_logs = list(map(
    lambda log: {
        "ip": log.split()[1].replace("ip:", ""),
        "bytes": int(log.split()[2].replace("bytes:", "")),
        "is_threat": log.split()[1].replace("ip:", "") in BANNED_IPS
    },
    server_logs
))

print("1. Mapped Output:")
import pprint; pprint.pprint(mapped_logs)


clean_logs = list(filter(
    lambda log:
    mapped_logs
))

print("\n2. Filtered Clean Logs:")
print(clean_logs)
