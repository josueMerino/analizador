# . - Para acerc lo ud quieras"
print("Analizador léxico")

componentsOfLanguage = "aaa=as1<=22;"
# est terminal ; az 09 = > < !
esttrans = [[0, 0, 1, 2, 3, 4, 5, 6, 7],
            [1, 1, -1, -1, -1, -1, -1, -1, -1],
            [2, 1, -1, 2, 2, -1, -1, -1, -1],
            [3, 1, -1, -1, 3, -1, -1, -1, -1],
            [4, 1, -1, -1, -1, 8, -1, -1, -1],
            [5, 1, -1, -1, -1, 9, -1, -1, -1],
            [6, 1, -1, -1, -1, 10, -1, -1, -1],
            [7, 0, -1, -1, -1, 11, -1, -1, -1],
            [8, 1, -1, -1, -1, -1, -1, -1, -1],
            [9, 1, -1, -1, -1, -1, -1, -1, -1],
            [10, 1, -1, -1, -1, -1, -1, -1, -1],
            [11, 1, -1, -1, -1, -1, -1, -1, -1]
            ]

est_act = 0
id = ""
resultado = ""
col = []
identifier = ""
index = 0
corresp = ["<TERM>", "<var>", "<num>", "<eqTo>", "<GreatT>",
           "<LessT", " ", "<EqualT>", "<GreEqT>", "<LesEqT>", "<DiffT>"]

ncar = len(componentsOfLanguage)

# Traducir el input a numeros para identificar de mejor manera
for i in range(0, ncar):
    posicionEstTransCode = ord(componentsOfLanguage[i])

    posicionEstTrans = componentsOfLanguage[i]

    if posicionEstTrans == ";":
        col.append(esttrans[0][2])

    elif (((posicionEstTransCode >= 97) and (posicionEstTransCode <= 122)) or ((posicionEstTransCode >= 65) and (posicionEstTransCode <= 90))):
        col.append(esttrans[0][3])

    elif (posicionEstTransCode >= 48) and (posicionEstTransCode <= 57):
        col.append(esttrans[0][4])

    elif posicionEstTrans == "=":
        col.append(esttrans[0][5])

    elif posicionEstTrans == ">":
        col.append(esttrans[0][6])

    elif posicionEstTrans == "<":
        col.append(esttrans[0][7])

    elif posicionEstTrans == "!":
        col.append(esttrans[0][8])

    else:
        print("ERROR")

    index = index + 1

for i in range(0, ncar):
    est_act = esttrans[est_act][col[i]]
    id = id + componentsOfLanguage[i]

    if i == ncar - 1:
        if esttrans[est_act + 1][1]:
            resultado = resultado + id
            id = ""
            if est_act == 1:
                identifier = identifier + corresp[0]
            elif est_act == 2:
                identifier = identifier + corresp[1]
            elif est_act == 3:
                identifier = identifier + corresp[2]
            elif est_act == 4:
                identifier = identifier + corresp[3]
            elif est_act == 5:
                identifier = identifier + corresp[4]
            elif est_act == 6:
                identifier = identifier + corresp[5]
            elif est_act == 7:
                identifier = identifier + corresp[6]
            elif est_act == 8:
                identifier = identifier + corresp[7]
            elif est_act == 9:
                identifier = identifier + corresp[8]
            elif est_act == 10:
                identifier = identifier + corresp[9]
            elif est_act == 11:
                identifier = identifier + corresp[10]
        else:
            print("Error léxico")
            print("No pertenece al lenguaje")
    else:
        if (esttrans[est_act][2]) and (esttrans[est_act][col[i + 1]] < 0):
            resultado = resultado + id
            id = ""
            identifier = identifier + corresp[est_act]
            est_act = 0
        else:
            if est_act == 1:
                identifier = identifier + corresp[0]
            elif est_act == 2:
                identifier = identifier + corresp[1]
            elif est_act == 3:
                identifier = identifier + corresp[2]
            elif est_act == 4:
                identifier = identifier + corresp[3]
            elif est_act == 5:
                identifier = identifier + corresp[4]
            elif est_act == 6:
                identifier = identifier + corresp[5]
            elif est_act == 7:
                identifier = identifier + corresp[6]
            elif est_act == 8:
                identifier = identifier + corresp[7]
            elif est_act == 9:
                identifier = identifier + corresp[8]
            elif est_act == 10:
                identifier = identifier + corresp[9]
            elif est_act == 11:
                identifier = identifier + corresp[10]
            est_act = 0

resultado = resultado + id
print(identifier)
