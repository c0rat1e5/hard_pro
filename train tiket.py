def solve(A, op):
    result = [0] * 4
    result[0] = A[0]
    for i in range(2):
        if i == 0:
            result[1] = result[0] + A[1]
            op[0] = "+"
        else:
            result[1] = result[0] - A[1]
            op[0] = "-"
        for j in range(2):
            if j == 0:
                result[2] = result[1] + A[2]
                op[1] = "+"
            else:
                result[2] = result[1] - A[2]
                op[1] = "-"
            for k in range(2):
                if k == 0:
                    result[3] = result[2] + A[3]
                    op[2] = "+"
                else:
                    result[3] = result[2] - A[3]
                    op[2] = "-"
                # print("{}{}{}{}{}{}{}?7".format(A[0],op[0],A[1],op[1],A[2],op[2],A[3]))
                # print(result[3])
                if result[3] == 7:
                    print("{}{}{}{}{}{}{}=7".format(
                        A[0], op[0], A[1], op[1], A[2], op[2], A[3]))
                    return


def main():
    A = [0] * 4
    op = [""] * 3
    A = list(map(int, input()))
    solve(A, op)


if __name__ == "__main__":
    main()
