#!/usr/bin/python3
import sys
try:
    from pdfminer.pdfparser import PDFParser
    from pdfminer.pdfdocument import PDFDocument
except ImportError as e:
    print("[!] install python3 -m pip install pdfminer")
    print("[*] Import Error as {}".format(e))
    sys.exit(1)

if len(sys.argv) == 1:
    print("[*] usage: python3 foo.pdf")
    sys.exit(1)

pdf = sys.argv[1]
fp = open(pdf, 'rb')
parser = PDFParser(fp)
doc = PDFDocument(parser)

list_info = doc.info[0]

for key, item in list_info.items():
    print("[*] {}:{}\n".format(key,str(item, 'latin-1')))