import zipfile
import xml.etree.ElementTree as ET
import sys

filename = 'reactjs project 1 step by step_latest.docx'
z = zipfile.ZipFile(filename)
xml_content = z.read('word/document.xml')
root = ET.fromstring(xml_content)
ns = {'w': 'http://schemas.openxmlformats.org/wordprocessingml/2006/main'}

paras = []
for p in root.findall('.//w:p', ns):
    text = ''.join([node.text for node in p.findall('.//w:t', ns) if node.text])
    if text:
        paras.append(text)

with open('docx_latest_clean.txt', 'w', encoding='utf-8') as f:
    f.write('\n'.join(paras))
