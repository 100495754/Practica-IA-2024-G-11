from main.variables.Age import Age
from main.read_classes.MFIS_Read_Functions import readApplicationsFile, readFuzzySetsFile
from main.read_classes.MFIS_Read_Functions import readApplicationsFile
from main.variables.Amount import Amount
from main.variables.Assets import Assets
from main.variables.History import History
from main.variables.IncomeLevel import IncomeLevel
from main.variables.Job import Job

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

    amount = app[j].data[3][1]
    print(amount)
    algo = Amount(amount)
    algo.amount()

    job = app[j].data[4][1]
    print(job)
    algo = Job(job)
    algo.job()

    history = app[j].data[5][1]
    print(history)
    algo = History(history)
    algo.history()

    j += 1
    print("")
    print("")

"""app = readFuzzySetsFile("read_classes/InputVarSets.txt")
print(app.printFuzzySetsDict())"""
