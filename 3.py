def Titleholder(T, test_cases):
    match_results = []
    for case in test_cases:
        N, names, powers = case
        Contenders = list(zip(names, powers))
        
        while len(Contenders) > 1:
            Upcoming_round = []
            for i in range(0, len(Contenders), 2):
                name1, power1 = Contenders[i]
                name2, power2 = Contenders[i+1]
                
                if power1 > power2:
                    Upcoming_round.append((name1, power1 + power2))
                elif power2 > power1:
                    Upcoming_round.append((name2, power1 + power2))
                else:  
                    Upcoming_round.append((name1 + name2, power1 + power2))
            Contenders = Upcoming_round
        
        champion_name = Contenders[0][0]
        match_results.append(champion_name)
    return match_results

# Reading input
T = int(input())
test_cases = []

for _ in range(T):
    N = int(input())
    names = input().split()
    powers = list(map(int, input().split()))
    test_cases.append((N, names, powers))

champions = Titleholder(T, test_cases)
for champ in champions:
    print(champ)