from tokenizer.extractor import Extractor
from tokenizer.processor import Processor

pr = Processor()
ex = Extractor()

phrase = Extractor().extract("os amores amam")

x = pr.run(phrase)
print(x)