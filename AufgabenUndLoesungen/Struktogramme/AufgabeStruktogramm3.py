# Grade classification
score = int(input("Enter your score (0-100): "))

if score >= 50:
    print("Pass")
    if score >= 90:
        print("Grade: A")
    elif score >= 75:
        print("Grade: B")
    else:
        print("Grade: C")
else:
    print("Fail")
