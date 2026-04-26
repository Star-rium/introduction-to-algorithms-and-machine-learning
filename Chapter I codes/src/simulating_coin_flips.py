import random
import math

def sim_probability(num_heads, num_flips, num_trials):
    # Calculating the theoretical probability of getting num_heads heads using Binomial Distribution:
    test_num_heads = math.comb(num_flips, num_heads)*(pow(0.5, num_flips))
    successful_trials = 0

    for trial in range(num_trials):
        heads = 0
        for i in range(num_flips):
            flip = random.random()
            if flip < 0.5:
                heads+=1
        if heads == num_heads:
            successful_trials+=1

    simulated_prob = successful_trials/num_trials
    print(f"Simulated probability of getting EXACTLY {num_heads} heads: {simulated_prob:.6}")
    print(f"Theoretical probability: {test_num_heads}\n")

if __name__ == '__main__':
    print(f"Test 1: 1 head, 1 flip, should return aprox 0.5")
    sim_probability(1, 1, 100000)

    print(f"Test 2: 0 head, 1 flip, should return aprox 0.5")
    sim_probability(0, 1, 100000)

    print(f"Test 3: 2 heads, 2 flips, should return aprox 0.25")
    sim_probability(2, 2, 100000)

    print(f"Test 4: 10 heads, 10 flips, should return aprox 0.000976")
    sim_probability(10, 10, 100000)



    