import re

text = """Lorem ipsum dolor sit amet, 31-123 consectetur adipiscing elit. Vestibulum pellentesque non mauris quis 12-222 viverra. Vestibulum fermentum pulvinar nulla, sed commodo tellus gravida auctor. Proin aliquam 00-123 egestas elit volutpat sollicitudin. Ut non auctor nisl. Nullam eget dui in ante interdum pulvinar. Sed hendrerit pharetra quam nec efficitur. Pellentesque vel dapibus sem."""

# I'd like to find all postal codes in the text
# when writing regular expression in python use r-string or raw-string
# when using this approach Python will not change any character in a string
results = re.findall(r"\d{2}-\d{3}", text)
print(results)

print('-' * 30)

text = r"Lorem ipsum dolor sit amet, 12/10/2023 consectetur adipiscing 6/18/2023 elit. Vestibulum 11/12/1990 eleifend lorem dui, sit amet posuere sem ultricies ut. Phasellus lacinia congue faucibus. Nulla eleifend aliquam pulvinar. Integer vestibulum urna ut vulputate vehicula. Phasellus in elit malesuada, luctus ligula congue, tincidunt tortor. Aliquam erat volutpat. Vivamus molestie sapien commodo dolor varius tincidunt dictum nec magna. Nullam lobortis accumsan ante nec cursus. Nulla et lorem non quam tempus fringilla."

# pattern, replacement, string we analyze
result = re.sub(r"(\d{1,2})/(\d{1,2})/(\d{4})", r"\2.\1.\3", text)

print(result)






