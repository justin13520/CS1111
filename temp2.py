import re

nospace = re.compile(r"([\S]+)")

quotation = re.compile(r"(\"[\S]+[\s]*[^\"]*[\S]+\")")

twonum = re.compile(r"(([-]?[0-9]+(\.)?[0-9]*)(\s|,|,\s)([-]?[0-9]+(\.)?[0-9]*))")

