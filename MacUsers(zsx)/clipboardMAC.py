import tkinter as tk
import time
from docx import Document
from fuzzywuzzy import fuzz
import os
import sys


path = os.path.dirname(os.path.abspath(sys.argv[0]))
doc = Document(path + "/mayuan.docx")
r = tk.Tk()
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
        NowClipboardData = r.clipboard_get()
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
    print("--------------")
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

        if rgb == "None" and fuzz.partial_ratio(paragraph.text, clipboardData) > 90:
            print("相似度:", fuzz.partial_ratio(paragraph.text, clipboardData), ":", paragraph.text)
            count += 1
            find_ans = True

    if count == 0 and reSearch == False:
        print("未搜索到!")
    if count != 0:
        reSearch = False