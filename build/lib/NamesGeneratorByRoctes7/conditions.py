n = 10


def condition_A(line, cell):
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
    if line == 1 or line == 3 or line == 5:
        if cell <= n - n / 5:
            return True
        else:
            return False
    else:
        if cell <= n / 5 or cell > n - n / 5:
            return True


def condition_E(line, cell):
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
    if line == 1:
        return True
    else:
        if cell <= (n - n / 5) / 2 or cell > n - (n - n / 5) / 2:
            return False
        else:
            return True


def condition_H(line, cell):
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
