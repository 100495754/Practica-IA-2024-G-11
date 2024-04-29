from main.variables.Age import Age
from main.read_classes.MFIS_Read_Functions import readApplicationsFile
from main.variables.Assets import Assets
from main.variables.IncomeLevel import IncomeLevel

app = readApplicationsFile()
j = 0
for i in app:

    edad = app[j].data[0][1]
    print(edad)
    algo = Age(edad)
    algo.age()


    incomelevel = app[j].data[1][1]
    print(incomelevel)
    algo = IncomeLevel(incomelevel)
    algo.incomelevel()

    assets = app[j].data[2][1]
    print(assets)
    algo = Assets(assets)
    algo.asset()

    j += 1
    print("")
    print("")

