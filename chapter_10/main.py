import time
import os


start = time.perf_counter()
print(os.listdir())
end = time.perf_counter()
print(end - start)

# format = 'xml'
# if format == 'xml':
#     import xmlreader as reader
# else:
#     import csvreader as reader
#
# reader.read()























