import docx

b_file = docx.Document('E:/算法学习资料/baiduImage/baiduImage/file/butterfly.docx')
for line in b_file.paragraphs:
    content = str(line.text.split('\t')[0])
    print(content)
