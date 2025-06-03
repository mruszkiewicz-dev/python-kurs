side_a = int(input("Podaj 1 bok trojkąta: ")) 
side_b = int(input("Podaj 2 bok trojkąta: "))
side_c = int(input("Podaj 3 bok trojkąta: "))


if side_a + side_b > side_c and side_a + side_c > side_b and side_b + side_c > side_a:
    print("Trójkat jest możliwy")

    if side_a == side_b == side_c:
        print("trojkąt równoboczny") 
    elif side_a == side_b or side_a == side_c or side_b == side_c:
        print("Trojkat prostopadły")
    else:
        print("Trojkąt o różnych bokach")
else:
    print("Trójkąt nie jest możliwy do zbudowania")
