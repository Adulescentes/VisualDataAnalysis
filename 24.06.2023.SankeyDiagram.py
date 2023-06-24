# Source Code for Figure 5.2
import plotly.graph_objects as go
import pandas as pd

df = pd.read_excel("db2mini.xlsx")
df = df.drop(labels=[0, 1], axis=0)
df = df.rename({
    'Unnamed: 4'    : 'Country Name',
    "Classification": "Size", 
    "Unnamed: 6"    : "Focus", 
    "Unnamed: 7"    : "Research",
    "Unnamed: 8"    : "Age",
    "Unnamed: 9"    : "Status",
    "Academic Reputation": "Academic Reputation Score",
    "Unnamed: 11"   : "Academic Reputation Rank",
    "Employer Reputation": "Employer Reputation Score",
    "Unnamed: 13"   : "Employer Reputation Rank",
    "Faculty Student": "Faculty Student Score",
    "Unnamed: 15"   : "Faculty Student Rank",
    "Citations per Faculty" : "Citations per Faculty Score",
    "Unnamed: 17"   : "Citations per Faculty Rank",
    "International Faculty": "International Faculty Score",
    "Unnamed: 19"   : "International Faculty Rank",
    "International Students": "International Students Score",
    "Unnamed: 21"   : "International Students Rank",
    "International Research Network": "IRN Score",
    "Unnamed: 23"   : "IRN Rank",
    "Employment Outcomes": "Employment Outcomes Score",
    "Unnamed: 25"   : "Employment Outcomes Rank",
    }, axis=1)
sourceList = []
targetList = [] 
schoolNames = df["Institution Name"].tolist()
schoolNameList = []

recordList = [[] for x in range(len(df["Location"].tolist()))]
# Since the whole database is multidimensional, a multidimensional list is allocated.
# There will be some points that are departure and destination points at the same time.
# The program first will save the appropriate ids for a record from database as a whole.

locationSet = {}
num = 0
locationList = df["Location"].tolist()

for element in locationList:
    if element not in locationSet:
        locationSet[element] = num
        num += 1

academicRepScoreList = df["Academic Reputation Score"].tolist()
academicRepScoreList = [(x // 5) * 5 for x in academicRepScoreList]

academicRepScoreSet = {}

for element in academicRepScoreList:
    if element not in academicRepScoreSet:
        academicRepScoreSet[element] = num
        num += 1

employerRepList = df["Employer Reputation Score"].tolist()
employerRepList = [(x // 5) * 5 for x in employerRepList]

employerRepSet = {}

for element in employerRepList:
    if element not in employerRepSet:
        employerRepSet[element] = num
        num += 1

# Faculty Student Score
facultyStudentList = df["Faculty Student Score"].tolist()
facultyStudentList = [(x // 5) * 5 for x in facultyStudentList]

facultyStudentSet = {}

for element in facultyStudentList:
    if element not in facultyStudentSet:
        facultyStudentSet[element] = num
        num += 1

# Citations per Faculty Score
citationFacultyList = df["Citations per Faculty Score"].tolist()
citationFacultyList = [(x // 5) * 5 for x in citationFacultyList]

citationFacultySet = {}

for element in citationFacultyList:
    if element not in citationFacultySet:
        citationFacultySet[element] = num
        num += 1

# International Faculty Score
internationalFacultyList = df["International Faculty Score"].tolist()
internationalFacultyList = [(x // 5) * 5 for x in internationalFacultyList]
internationalFacultySet = {}

for element in internationalFacultyList:
    if element not in internationalFacultySet:
        internationalFacultySet[element] = num
        num += 1

# International Students Score
internationalStudentList = df["International Students Score"].tolist()
internationalStudentList = [(x // 5) * 5 for x in internationalStudentList]

internationalStudentSet = {}
for element in internationalStudentList:
    if element not in internationalStudentSet:
        internationalStudentSet[element] = num
        num += 1

# IRN Score
irnList = df["IRN Score"].tolist()
irnList = [(x // 5) * 5 for x in irnList]

irnSet = {}
for element in irnList:
    if element not in irnSet:
        irnSet[element] = num
        num += 1

# Employment Outcomes Score
employmentOutcomeList = df["Employment Outcomes Score"].tolist()
employmentOutcomeList = [(x // 5) * 5 for x in employmentOutcomeList]

employmentOutcomeSet = {}
for element in employmentOutcomeList:
    if element not in employmentOutcomeSet:
        employmentOutcomeSet[element] = num
        num += 1

# Overall
overallList = df["Overall"].tolist()
for i in range(len(overallList)):
		# Some of the elements have the "-" for their value,
		# but this disrupts the flow of the program
    if overallList[i] != "-":
        overallList[i] = (overallList[i] // 5) * 5
    else:
        overallList[i] = 0

overallSet = {}
for element in overallList:
    if element not in overallSet:
        overallSet[element] = num
        num += 1

for i in range(len(locationList)):
    recordList[i].append(locationSet[locationList[i]])
    recordList[i].append(academicRepScoreSet[academicRepScoreList[i]])
    recordList[i].append(employerRepSet[employerRepList[i]])
    recordList[i].append(facultyStudentSet[facultyStudentList[i]])
    recordList[i].append(citationFacultySet[citationFacultyList[i]])
    recordList[i].append(internationalFacultySet[internationalFacultyList[i]])
    recordList[i].append(internationalStudentSet[internationalStudentList[i]])
    recordList[i].append(irnSet[irnList[i]])
    recordList[i].append(employmentOutcomeSet[employmentOutcomeList[i]])
    recordList[i].append(overallSet[overallList[i]])
		# All id information of a record in the database is stored sequentially in the same element in recordList.

for i in range(10):
    schoolNameList.extend(schoolNames)
		# This is for hover mode

start_color = [0, 0, 255]  
end_color = [0, 255, 0] 

colorDict = []
colorStep = len(df["Institution Name"].tolist())
colordivision = colorStep-1

for i in range(colorStep):
    r = start_color[0] + int((end_color[0] - start_color[0]) * (i / colordivision))
    g = start_color[1] + int((end_color[1] - start_color[1]) * (i / colordivision))
    b = start_color[2] + int((end_color[2] - start_color[2]) * (i / colordivision))
    color_str = f'rgba({r}, {g}, {b}, 0.8)'
    colorDict.append(color_str)
		# This code creates HTML color codes.

colorList = []

for i in range(len(recordList[0])-1):
    for j, element in enumerate(recordList):
        sourceList.append(element[i])
        targetList.append(element[i+1])
        colorList.append(colorDict[j % len(colorDict)])
				# This loop goes over all of the records
				# and selects nth index as departure point and n+1th index as destination.

labelList = []
labelList.extend(list(locationSet.keys()))
labelList.extend(list(academicRepScoreSet.keys()))
labelList.extend(list(employerRepSet.keys()))
labelList.extend(list(facultyStudentSet.keys()))
labelList.extend(list(citationFacultySet.keys()))
labelList.extend(list(internationalFacultySet.keys()))
labelList.extend(list(internationalStudentSet.keys()))
labelList.extend(list(irnSet.keys()))
labelList.extend(list(employmentOutcomeSet.keys()))
labelList.extend(list(overallSet.keys()))

fig = go.Figure(data=[go.Sankey(
    valueformat = ".0f",
    node = dict(
      pad = 15,
      thickness = 15,
      line = dict(color = "black", width = 0.5),
      label =  labelList,
    ),
    link = dict(
        source =  sourceList,
        target =  targetList,
        value =  [1 for x in range(len(sourceList))],
        label =  schoolNameList,
        color =  colorList 
))])
columnNames = [
    "Location",                             #0
    "Academic", "Reputation", "Score",      #1
    "Employer", "Reputation", "Score",      #2
    "Faculty", "Student", "Score",          #3
    "Citations", "per Faculty", "Score",    #4
    "International", "Faculty", "Score",    #5
    "Interational", "Students", "Score",    #6
    "IRN Score",                            #7
    "Employment", "Outcomes", "Score",      #8
    "Overall"                               #9
]
# These are headers for columns that will be displayed
x_coordinates = [
    0,              #0
    1, 1, 1,        #1
    2, 2, 2,        #2
    3, 3, 3,        #3
    4, 4, 4,        #4
    5, 5, 5,        #5
    6, 6, 6,        #6
    7,              #7
    8, 8, 8,        #8
    9               #9
]
# These are horizontal coordinates that headers will be printed.
y_coordinates = [
    -0.05, 
    -0.05, -0.09, -0.13,
    -0.05, -0.09, -0.13,
    -0.05, -0.09, -0.13,
    -0.05, -0.09, -0.13,
    -0.05, -0.09, -0.13,
    -0.05, -0.09, -0.13,
    -0.05, 
    -0.05, -0.09, -0.13, 
    -0.05
]
# These are vertical coordinates that headers will be printed.

for x_coordinate, column_name in enumerate(columnNames):
    fig.add_annotation(
        x= x_coordinates[x_coordinate],
        # y=1.05 + x_coordinate/75,
        y = y_coordinates[x_coordinate],
        xref="x",
        yref="paper",
        text=column_name,
        showarrow=False,
        font=dict(
            family="Courier New, monospace",
            size=16,
            color="black"
        ),
        align="center"
    )

fig.update_layout(
    xaxis=dict(
        showgrid=False,
        zeroline=False,
        visible=False
    ),
    yaxis=dict(
        showgrid=False,
        zeroline=False,
        visible=False
    ),
    plot_bgcolor='rgba(0,0,0,0)'
)
# This update_layout function is for cleaning the background.
fig.show()
