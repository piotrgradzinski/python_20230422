import re

text = """Lorem ipsum dolor sit amet, 31-123 consectetur adipiscing elit. Vestibulum pellentesque non mauris quis 12-222 viverra. Vestibulum fermentum pulvinar nulla, sed commodo tellus gravida auctor. Proin aliquam 00-123 egestas elit volutpat sollicitudin. Ut non auctor nisl. Nullam eget dui in ante interdum pulvinar. Sed hendrerit pharetra quam nec efficitur. Pellentesque vel dapibus sem."""

# I'd like to find all postal codes in the text
# when writing regular expression in python use r-string or raw-string
# when using this approach Python will not change any character in a string
results = re.findall(r"\d{2}-\d{3}", text)
print(results)
