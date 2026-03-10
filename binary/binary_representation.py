num = int(input("Enter a number: "))
binary = ""
step = 1

while num > 0:
    print(f"\nStep {step}")
    print(f"Current number: {num}")

    remainder = num % 2
    print(f"Remainder when divided by 2: {remainder}")

    binary += str(remainder) 
    print(f"Binary so far: {binary}")

    num = num // 2
    print(f"Number after dividing by 2: {num}")

    step += 1

print("\nFinal Binary:", binary)