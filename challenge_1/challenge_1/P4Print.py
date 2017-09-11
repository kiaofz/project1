#this modules prints a tabular version of lenfreq(from P4Search)
from P4Search import lenfreq
ColOne = "Word Length"
ColTwo = "Apperances"
print(":",ColOne,":",ColTwo,":")
for n in lenfreq:
    print(":",n," "*(len(ColOne)-len(str(n))),
          ":",lenfreq[n]," "*(len(ColTwo)-len(str(lenfreq[n]))),":")
