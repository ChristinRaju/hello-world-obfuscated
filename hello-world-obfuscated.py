#print((lambda A,B,C,D,E,F: ''.join(map(chr,((A<<C)+(A<<F), A + (A<<B)+(A<<E)+(A<<F), (A<<B)+(A<<C)+(A<<E)+(A<<F), (A<<B)+(A<<C)+(A<<E)+(A<<F), A+(A<<A)+(A<<B)+(A<<C)+(A<<E)+(A<<F), (A<<E), A+(A<<A)+(A<<B)+(A<<D)+(A<<F), A+(A<<A)+(A<<B)+(A<<C)+(A<<E)+(A<<F), (A<<A)+(A<<D)+(A<<E)+(A<<F), (A<<B)+(A<<C)+(A<<E)+(A<<F), (A<<B)+(A<<E)+(A<<F)))))(True, True+True, True+True+True, (True+True)+(True+True), ((True+True)+(True+True))+True, ((True+True)+(True+True))+(True+True)))

def main():
    A, B, C, D, E, F = 1, 2, 3, 4, 5, 6

    values = (
        (A << C) + (A << F),
        A + (A << B) + (A << E) + (A << F),
        (A << B) + (A << C) + (A << E) + (A << F),
        (A << B) + (A << C) + (A << E) + (A << F),
        A + (A << A) + (A << B) + (A << C) + (A << E) + (A << F),
        (A << E),
        A + (A << A) + (A << B) + (A << D) + (A << F),
        A + (A << A) + (A << B) + (A << C) + (A << E) + (A << F),
        (A << A) + (A << D) + (A << E) + (A << F),
        (A << B) + (A << C) + (A << E) + (A << F),
        (A << B) + (A << E) + (A << F),
    )

    message = ''.join(map(chr, values))
    print(message)


if __name__ == "__main__":
    main()
