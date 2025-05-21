def calculate_payout(test_cases):

    final_output = []


    for case in test_cases:

        N, choices = case

        current_price = 1

        total_bill = 0

        

        for choice in choices:

            if choice == 'T':

                total_bill += current_price
                current_price = 1  # Reset to $1

            elif choice == 'D':

                current_price *= 2  # Double the offer

        

        final_output.append(total_bill)

    

    return final_output


# Read input

T = int(input())

test_cases = []


for _ in range(T):

    N = int(input())

    choices = input().strip()

    test_cases.append((N, choices))


# Calculate payouts

final_output = calculate_payout(test_cases)


# Print results

for result in final_output:

    print(result)