import re

from utils import PATTERN_DICT, input_text, get_input_text
import timeit


rep = dict((re.escape(k), v) for k, v in PATTERN_DICT.items())
pattern = re.compile("|".join(rep.keys()))
#  @"destination.*?([A-Z]+)\b"
new_text = pattern.sub(lambda m: rep[re.escape(m.group(0))], input_text)

print(new_text)
# print(timeit.timeit(lambda: pattern.sub(lambda m: rep[re.escape(m.group(0))], get_input_text() ), number=10000))
