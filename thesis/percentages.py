vals = {
    "Total":        [90214500,84101961,7535293],
    "Java":         [26157106,26077227,501827],
    "C":            [16519085,11530315,991275],
    "Python":       [16472714,16248323,3987109],
    "JavaScript":   [14798610,14088493,425887],
    "C#":           [7446313,7400280,810354],
    "PHP":          [5356751,5319176,191508],
    "C++":          [1583611,1571530,142663],
    "Ruby":         [867301,858255,397823],
    "TypeScript":   [630778,627370,16178],
    "Shell":        [382231,380992,70669], 
}

percentages = {}
for key,val in vals.items():
    percentages[key] = []
    for num in range(len(val)):
        percentages[key].append(round(100*(vals[key][num]/vals["Total"][num]), 4))

for p in percentages:
    print(p, ": ", percentages[p])