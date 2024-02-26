print("Results")
response = int(input())
thilist = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
nxt = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
for x in thilist[-5:-1]:
    for y in nxt:
        print(f'{x} - {y}')
        scores = x - y
        while response == scores:
            print("You win")
            break
        else:
            print("You loose")
