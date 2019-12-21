
import re

some_text = 'alpha, beta,,,, gamma        delta'
# Use of '+' as wildcard option to suppress multiple ',,'
revised = re.split('[, ]+', some_text)
print(revised)
