import win32clipboard as wc
import win32con
import time
from docx import Document
from fuzzywuzzy import fuzz
import os
import sys


path = os.path.dirname(os.path.abspath(sys.argv[0]))
doc = Document(path + "\马原.docx")

rawClipboardData = ""
count = 0
reSearch = False
while True:
    time.sleep(0.2)

    if reSearch:
        clipboardData = rawClipboardData.replace("(", "（")
        clipboardData = clipboardData.replace(")", "）")
        clipboardData = clipboardData.replace("-", "")
        reSearch = False
    else:
        try:
            wc.OpenClipboard()
            NowClipboardData = copy_text = wc.GetClipboardData()
            wc.CloseClipboard()
        except:
            wc.CloseClipboard()
            print("剪切板子秃然挂了")
            continue
        if NowClipboardData == rawClipboardData or NowClipboardData == "":
            continue
        else:
            rawClipboardData = NowClipboardData
            reSearch = True
        clipboardData = rawClipboardData.strip()
        clipboardData = clipboardData.replace(" ", "")
        clipboardData = clipboardData.replace("\n", "")
    count = 0
    find_ans = False
    print("------------------------------------------")

    for paragraph in doc.paragraphs:
        try:
            rgb = paragraph.runs[0].font.color.rgb.__str__()
        except:
            rgb = "None"

        if find_ans and rgb != "None":
            print(paragraph.text)
            continue
        else:
            find_ans = False

        if rgb == "None" and fuzz.partial_ratio(paragraph.text, clipboardData) > 85:
            print("相似度:", fuzz.partial_ratio(paragraph.text, clipboardData), ":", paragraph.text)
            count += 1
            find_ans = True

    if count == 0 and reSearch == False:
        print("未搜索到!")
    if count != 0:
        reSearch = False

wc.CloseClipboard()