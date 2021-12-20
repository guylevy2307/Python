import pywhatkit as pw
import pandas as pd
import pyautogui as pg
import datetime as date


def main():
    excelPath = (
        "C:/Users/guyle/Desktop/gitProjects/Python/whatsapp message sender/text.xlsx")
# C:/Users/guyle/Desktop/gitProjects/Python/whatsapp message sender/text.xlsx
    df = pd.read_excel(excelPath)

    numbers = list(df['numbers'])

    areaCode = "+972"

    file1 = open("data.txt", 'r', encoding='utf-8')
    message2 = ""
    for x in file1:

        message2 += x
    file1.close()

    for num in numbers:
        newNum = areaCode + str(num)
        import math

        time = int(math.ceil(date.datetime.now().minute+0.1))
        Htime = date.datetime.now().hour
        pw.sendwhatmsg(newNum, message2, Htime, time, 4, True, 5)
        pg.press("enter")
    print("DONE")


if __name__ == '__main__':
    main()
