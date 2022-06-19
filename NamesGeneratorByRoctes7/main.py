import random


class Constants:
    n = 10
    scaleX = 2
    DrawnLetter = "#"
    EmptySpace = " "

    random_mode_enabled = True
    choices = ["0", "1"]
    inner_name_choices_enabled = True
    fix_corners_enabled = True


class Conditions:
    def condition_A(line, cell):
        n = Constants.n
        if line == 1:
            if cell <= n / 5 or cell > n - n / 5:
                return False
            else:
                return True
        elif line == 2 or line == 3 or line == 5:
            if cell <= n / 5 or cell > n - n / 5:
                return True
            else:
                return False
        else:
            return True

    def condition_D(line, cell):
        n = Constants.n
        if line == 1 or line == 5:
            if cell <= n - n / 5:
                return True
            else:
                return False
        else:
            if cell <= n / 5 or cell > n - n / 5:
                return True
            else:
                return False

    def condition_O(line, cell):
        n = Constants.n
        if line == 1 or line == 5:
            if cell <= n / 5 or cell > n - n / 5:
                return False
            else:
                return True
        else:
            if cell <= n / 5 or cell > n - n / 5:
                return True
            else:
                return False

    def condition_B(line, cell):
        n = Constants.n
        if line == 1 or line == 3 or line == 5:
            if cell <= n - n / 5:
                return True
            else:
                return False
        else:
            if cell <= n / 5 or cell > n - n / 5:
                return True

    def condition_E(line, cell):
        n = Constants.n
        if line == 1 or line == 5:
            return True
        elif line == 3:
            if cell <= n - n / 5:
                return True
            else:
                return False
        else:
            if cell <= n / 5:
                return True
            else:
                return False

    def condition_C(line, cell):
        n = Constants.n
        if line == 1 or line == 5:
            if cell <= n / 5 or cell > n - n / 5:
                return False
            else:
                return True
        else:
            if cell <= n / 5:
                return True
            else:
                return False

    def condition_F(line, cell):
        n = Constants.n
        if line == 1:
            return True
        elif line == 2 or line == 4 or line == 5:
            if cell <= n / 5:
                return True
            else:
                return False
        else:
            if cell > n - n / 5:
                return False
            else:
                return True

    def condition_L(line, cell):
        n = Constants.n
        if line == 5:
            if cell > n - n / 5:
                return False
            else:
                return True
        else:
            if cell <= n / 5:
                return True
            else:
                return False

    def condition_T(line, cell):
        n = Constants.n
        if line == 1:
            return True
        else:
            if cell <= (n - n / 5) / 2 or cell > n - (n - n / 5) / 2:
                return False
            else:
                return True

    def condition_H(line, cell):
        n = Constants.n
        if line == 3:
            return True
        else:
            if cell > n - n / 5 or cell <= n / 5:
                return True
            else:
                return False

    def condition_Space(line, cell):
        return False

    def condition_K(line, cell):
        n = Constants.n
        if line == 1 or line == 5:
            if cell <= n / 5:
                return True
            elif cell > n - n / 5:
                return False
            elif cell > n - (n - n / 5) / 2:
                return True
            else:
                return False
        elif line == 2 or line == 4:
            if cell <= n / 5:
                return True
            elif cell <= (n - n / 5) / 2 or cell > n - (n - n / 5) / 2:
                return False
            else:
                return True
        else:
            if cell <= (n - n / 5) / 2:
                return True
            else:
                return False

    def condition_R(line, cell):
        n = Constants.n
        if line == 1 or line == 3:
            if cell > n - n / 5:
                return False
            else:
                return True
        elif line == 4:
            if cell <= n / 5:
                return True
            elif cell <= (n - n / 5) / 2 or cell > n - (n - n / 5) / 2:
                return False
            else:
                return True

        elif line == 2:
            if cell <= n / 5 or cell > n - n / 5:
                return True
            else:
                return False

        else:
            if cell <= n / 5:
                return True
            elif cell > n - n / 5:
                return False
            elif cell > n - (n - n / 5) / 2:
                return True
            else:
                return False

    def condition_M(line, cell):
        n = Constants.n
        if line == 1:
            if cell <= n / 5 or cell > n - n / 5:
                return False
            elif cell <= (n - n / 5) / 2 or cell > n - (n - n / 5) / 2:
                return True
            else:
                return False
        else:
            if cell <= n / 5 or cell > n - n / 5:
                return True
            elif cell <= (n - n / 5) / 2 or cell > n - (n - n / 5) / 2:
                return False
            else:
                return True

    def condition_Y(line, cell):
        n = Constants.n
        if line == 1:
            if cell <= n / 5 or cell > n - n / 5:
                return True
            else:
                return False
        elif line == 2:
            if cell <= n / 5 or cell > n - n / 5:
                return False
            elif cell <= (n - n / 5) / 2 or cell > n - (n - n / 5) / 2:
                return True
            else:
                return False
        else:
            if cell <= (n - n / 5) / 2 or cell > n - (n - n / 5) / 2:
                return False
            else:
                return True

    def condition_N(line, cell):
        n = Constants.n
        if line == 1 or line == 5:
            if cell <= n / 5 or cell > n - n / 5:
                return True
            else:
                return False
        elif line == 2:
            if cell <= (n - n / 5) / 2 or cell > n - n / 5:
                return True
            else:
                return False
        elif line == 3:
            if cell <= n / 5 or cell > n - n / 5:
                return True
            elif cell <= (n - n / 5) / 2 or cell > n - (n - n / 5) / 2:
                return False
            else:
                return True
        else:
            if cell <= n / 5 or cell > n - (n - n / 5) / 2:
                return True
            else:
                return False

    def condition_G(line, cell):
        n = Constants.n
        if line == 1 or line == 5:
            if cell <= n / 5 or cell > n - n / 5:
                return False
            else:
                return True
        elif line == 2:
            if cell <= n / 5:
                return True
            else:
                return False
        elif line == 3:
            if cell <= n / 5:
                return True
            elif cell <= (n - n / 5) / 2 or cell > n - n / 5:
                return False
            else:
                return True
        else:
            if cell <= n / 5:
                return True
            elif cell > n - n / 5:
                return False
            elif cell > n - (n - n / 5) / 2:
                return True
            else:
                return False

    def condition_I(line, cell):
        n = Constants.n
        if line == 1 or line == 5:
            if cell <= n / 5 or cell > n - n / 5:
                return False
            else:
                return True
        else:
            if cell <= (n - n / 5) / 2 or cell > n - (n - n / 5) / 2:
                return False
            else:
                return True

    def condition_U(line, cell):
        n = Constants.n
        if line == 5:
            if cell <= n / 5 or cell > n - n / 5:
                return False
            else:
                return True
        else:
            if cell <= n / 5 or cell > n - n / 5:
                return True
            else:
                return False

    def condition_S(line, cell):
        n = Constants.n
        if line == 1:
            if cell <= n / 5:
                return False
            else:
                return True
        elif line == 2:
            if cell <= n / 5:
                return True
            else:
                return False
        elif line == 3:
            if cell <= n / 5 or cell > n - n / 5:
                return False
            else:
                return True
        elif line == 4:
            if cell > n - n / 5:
                return True
            else:
                return False
        else:
            if cell > n - n / 5:
                return False
            else:
                return True

    def condition_X(line, cell):
        n = Constants.n
        if line == 1 or line == 5:
            if cell <= n / 5 or cell > n - n / 5:
                return True
            else:
                return False
        elif line == 2 or line == 4:
            if cell <= n / 5 or cell > n - n / 5:
                return False
            elif cell <= (n - n / 5) / 2 or cell > n - (n - n / 5) / 2:
                return True
            else:
                return False
        else:
            if cell <= (n - n / 5) / 2 or cell > n - (n - n / 5) / 2:
                return False
            else:
                return True

    def condition_Z(line, cell):
        n = Constants.n
        if line == 1 or line == 5:
            return True
        elif line == 2:
            if cell > n - n / 5:
                return False
            elif cell > n - (n - n / 5) / 2:
                return True
            else:
                return False
        elif line == 3:
            if cell <= (n - n / 5) / 2 or cell > n - (n - n / 5) / 2:
                return False
            else:
                return True
        else:
            if cell <= n / 5:
                return False
            elif cell <= (n - n / 5) / 2:
                return True
            else:
                return False

    def condition_J(line, cell):
        n = Constants.n
        if line == 1:
            return True
        elif line == 2 or line == 3:
            if cell > n - n / 5 or cell <= (n - n / 5) / 2:
                return False
            else:
                return True
        elif line == 4:
            if cell <= n / 5:
                return True
            elif cell > n - n / 5 or cell <= (n - n / 5) / 2:
                return False
            else:
                return True
        else:
            if cell > n - n / 5:
                return False
            else:
                return True

    def condition_P(line, cell):
        n = Constants.n
        if line == 1 or line == 3:
            if cell > n - n / 5:
                return False
            else:
                return True
        elif line == 2:
            if cell <= n / 5 or cell > n - n / 5:
                return True
            else:
                return False

        else:
            if cell <= n / 5:
                return True
            else:
                return False

    def condition_Q(line, cell):
        n = Constants.n
        if line == 1:
            if cell <= n / 5 or cell > n - n / 5:
                return False
            else:
                return True
        elif line == 2 or line == 3:
            if cell <= n / 5 or cell > n - n / 5:
                return True
            else:
                return False
        elif line == 4:
            if cell <= n / 5:
                return True
            elif cell > n - n / 5:
                return False
            elif cell > n - (n - n / 5) / 2:
                return True
            else:
                return False
        else:
            if cell < n / 5:
                return False
            elif cell > n - n / 5:
                return True
            elif cell <= (n - n / 5) / 2:
                return True
            elif cell > n - (n - n / 5) / 2:
                return False
            else:
                return True

    def condition_V(line, cell):
        n = Constants.n
        if line == 1 or line == 2:
            if cell <= n / 5 or cell > n - n / 5:
                return True
            else:
                return False
        elif line == 3 or line == 4:
            if cell <= n / 5 or cell > n - n / 5:
                return False
            elif cell <= (n - n / 5) / 2 or cell > n - (n - n / 5) / 2:
                return True
            else:
                return False
        else:
            if cell <= (n - n / 5) / 2 or cell > n - (n - n / 5) / 2:
                return False
            else:
                return True


class Letter:
    key = "-1"

    def __init__(self, key, func):
        self.con = func
        self.key = key

    def Draw(self):
        out = ""
        current_line = 1
        moves = Constants.n / 5
        move = 0
        for line in range(1, Constants.n + 1):

            for cell in range(1, Constants.n + 1):
                if self.con(current_line, cell):
                    if Constants.random_mode_enabled:
                        for i in range(Constants.scaleX):
                            out += random.choice(Constants.choices)
                    else:
                        out += Constants.DrawnLetter * Constants.scaleX
                else:
                    out += Constants.EmptySpace * Constants.scaleX

            move += 1
            if move == moves:
                move = 0
                current_line += 1

            out += "\n"
        if Constants.fix_corners_enabled:
            for i in range(int(Constants.n / 5) - 1):
                out = FixCorners(out.split("\n"))

        return out


supportedLetters = []

space = Letter(" ", Conditions.condition_Space)
a = Letter("A", Conditions.condition_A)
b = Letter("B", Conditions.condition_B)
c = Letter("C", Conditions.condition_C)
d = Letter("D", Conditions.condition_D)
e = Letter("E", Conditions.condition_E)
f = Letter("F", Conditions.condition_F)
kk = Letter("K", Conditions.condition_K)
o = Letter("O", Conditions.condition_O)
h = Letter("H", Conditions.condition_H)
ll = Letter("L", Conditions.condition_L)
t = Letter("T", Conditions.condition_T)
r = Letter("R", Conditions.condition_R)
m = Letter("M", Conditions.condition_M)
y = Letter("Y", Conditions.condition_Y)
nn = Letter("N", Conditions.condition_N)
g = Letter("G", Conditions.condition_G)
ii = Letter("I", Conditions.condition_I)
u = Letter("U", Conditions.condition_U)
s = Letter("S", Conditions.condition_S)
xx = Letter("X", Conditions.condition_X)
z = Letter("Z", Conditions.condition_Z)
jj = Letter("J", Conditions.condition_J)
p = Letter("P", Conditions.condition_P)
q = Letter("Q", Conditions.condition_Q)
v = Letter("V", Conditions.condition_V)

supportedLetters.append(space)
supportedLetters.append(a)
supportedLetters.append(b)
supportedLetters.append(c)
supportedLetters.append(d)
supportedLetters.append(e)
supportedLetters.append(f)
supportedLetters.append(h)
supportedLetters.append(ii)
supportedLetters.append(g)
supportedLetters.append(kk)
supportedLetters.append(ll)
supportedLetters.append(m)
supportedLetters.append(nn)
supportedLetters.append(o)
supportedLetters.append(jj)
supportedLetters.append(p)
supportedLetters.append(q)
supportedLetters.append(v)
supportedLetters.append(t)
supportedLetters.append(r)
supportedLetters.append(y)
supportedLetters.append(u)
supportedLetters.append(s)
supportedLetters.append(xx)
supportedLetters.append(z)


def FixCorners(arr):
    for i in range(len(arr)):
        for j in range(len(arr[i])):
            l = []
            l[:0] = arr[i]
            try:
                if i > 0 and j > 0:
                    if arr[i][j] == Constants.EmptySpace and arr[i + 1][j] != Constants.EmptySpace and arr[i][
                        j - 1] != Constants.EmptySpace and \
                            arr[i - 1][j - 1] != Constants.EmptySpace and arr[i + 1][j + 1] != Constants.EmptySpace:
                        if Constants.random_mode_enabled:
                            l[j] = random.choice(Constants.choices)
                        else:
                            l[j] = Constants.DrawnLetter
                    elif arr[i][j] == Constants.EmptySpace and arr[i + 1][j] != Constants.EmptySpace and arr[i + 1][
                        j - 1] != Constants.EmptySpace and \
                            arr[i][j + 1] != Constants.EmptySpace and arr[i - 1][j + 1] != Constants.EmptySpace:
                        if Constants.random_mode_enabled:
                            l[j] = random.choice(Constants.choices)
                        else:
                            l[j] = Constants.DrawnLetter
                    elif arr[i][j] == Constants.EmptySpace and arr[i - 1][j] != Constants.EmptySpace and arr[i - 1][
                        j + 1] != Constants.EmptySpace and \
                            arr[i][j - 1] != Constants.EmptySpace and arr[i + 1][j - 1] != Constants.EmptySpace:
                        if Constants.random_mode_enabled:
                            l[j] = random.choice(Constants.choices)
                        else:
                            l[j] = Constants.DrawnLetter
                    elif arr[i][j] == Constants.EmptySpace and arr[i - 1][j - 1] != Constants.EmptySpace and arr[i + 1][
                        j + 1] != Constants.EmptySpace and \
                            arr[i][j + 1] != Constants.EmptySpace and arr[i - 1][j] != Constants.EmptySpace:
                        if Constants.random_mode_enabled:
                            l[j] = random.choice(Constants.choices)
                        else:
                            l[j] = Constants.DrawnLetter

                    else:
                        pass

            except:
                pass
            arr[i] = l
    text = ""
    for i in range(len(arr)):
        for j in range(len(arr[i])):
            text += arr[i][j]
        text += "\n"
    return text


def MergeString(str1, str2):
    ls1 = str1.split("\n")
    ls2 = str2.split("\n")
    val = ""
    for i in range(len(ls2)):
        val += ls1[i] + (Constants.EmptySpace * 2 * int(Constants.scaleX * Constants.n / 5)) + ls2[i]
        val += "\n"

    return val


def Output(Name):
    doneText = "-1"
    for x in Name:
        for l in supportedLetters:
            if x.upper() == (l.key + "").upper():
                if doneText == "-1":
                    doneText = l.Draw()
                else:
                    doneText = MergeString(doneText, l.Draw())

    print(doneText)


def init(n, scalx, DrawnLetter, EmptySpace, random_mode, choices, inner_name_choices_mode):
    Constants.n = n
    Constants.scaleX = scalx
    Constants.DrawnLetter = DrawnLetter
    Constants.EmptySpace = EmptySpace
    Constants.random_mode_enabled = random_mode
    Constants.choices = choices
    Constants.inner_name_choices_enabled = inner_name_choices_mode
    letters = []
    for letter in supportedLetters:
        letters.append((letter.key + "").upper())
