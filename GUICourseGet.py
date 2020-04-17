import tkinter as tk
import CoursesGet

url = 'https://guide.wisc.edu'

# Window setup
window = tk.Tk()
window.title("WISC Course Get")
window.geometry('500x800')

# Search box
searchBox = tk.Entry(window)
searchBox.place(x=20, y=30, width=330, height=25)

# Credit info
creditLable = tk.Label(window, text='CREDIT:')
creditLable.place(x=20, y=30 + 25 + 15, width=100, height=25)

creditTextVar = tk.StringVar()
creditText = tk.Label(window, textvariable=creditTextVar)
creditText.place(x=20 + 100 + 20, y=30 + 25 + 15, width=340, height=25)

# Course discription
courseDiscriptionLable = tk.Label(window, text='COURSE DISCRIPTION')
courseDiscriptionLable.place(x=100, y=30 + 25 + 15 + 25 + 15, width=300, height=25)

courseDiscriptionText = tk.Text(window)
courseDiscriptionText.place(x=20, y=30 + 25 + 15 + 25 + 15 + 25 + 15, width=460, height=150)

# Prerequisite
prerequisiteLable = tk.Label(window, text='PREREQUISITE')
prerequisiteLable.place(x=100, y=30 + 25 + 15 + 25 + 15 + 25 + 15 + 150 + 15, width=300, height=25)

prerequisiteText = tk.Text(window)
prerequisiteText.place(x=20, y=30 + 25 + 15 + 25 + 15 + 25 + 15 + 150 + 15 + 25 + 15, width=460, height=150)

# Related course list
courseListVar = tk.StringVar()
relatedCourseList = tk.Listbox(window, listvariable=courseListVar)
relatedCourseList.place(x=20, y=30 + 25 + 15 + 25 + 15 + 25 + 15 + 150 + 15 + 25 + 15 + 150 + 15, width=460, height=150)


# Search function
def Search():
    # Keyword search
    keyWords = searchBox.get()
    searchUrl = CoursesGet.GenerateSearchUrl(url, keyWords)
    searchResult = CoursesGet.SearchOnePage(url, searchUrl)
    print(searchResult)

    # Credit
    creditTextVar.set(searchResult[0])

    # Course discription
    courseDiscriptionText.delete('1.0', 'end')
    courseDiscriptionText.insert('end', searchResult[1])

    # Prerequisite
    prerequisiteText.delete('1.0', 'end')
    prerequisiteText.insert('end', searchResult[2])

    relatedCourseList.delete(0, 'end')
    for relatedCourse in searchResult[4]:
        relatedCourseList.insert('end', relatedCourse)

def FurtherSearch():
    if (relatedCourseList.size() != 0):
        chooseIndex = relatedCourseList.curselection()[0]
        searchBox.delete(0, 'end')
        searchBox.insert('end', relatedCourseList.get(chooseIndex))

        Search()
    else:
        print(None)

search1 = tk.Button(window,text="SEARCH",command=Search)
search1.place(x=370, y=30, width=110, height=25)

search2 = tk.Button(window, text="FURTHER SEARCH", command=FurtherSearch)
search2.place(x=100, y=30 + 25 + 15 + 25 + 15 + 25 + 15 + 150 + 15 + 25 + 15 + 150 + 15 + 150 + 15, width=300, height=25)

# Show window
window.mainloop()