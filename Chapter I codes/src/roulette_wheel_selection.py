import random

def random_draw(distribution):
    # step 1: calculate the total probabilities in the distribution
    total_prob = sum(distribution)

    # step 2: pick a random value from 0 to total_prob
    pick = random.uniform(0, total_prob)

    # step 3: construct and find the individual corresponds to the random pick in the cumulative distribution
    curr = 0
    for i in range(len(distribution)):
        curr += distribution[i]
        if(curr > pick):
            return i

if __name__ == '__main__':
    # Simulating the example in the book
    values = ["red", "blue", "green", "yellow"]
    distribution = [0.4, 0.2, 0.2, 0.2]
    
    num_trials = 10000
    freq = {}

    for i in range(num_trials):
        res = random_draw(distribution)
        if values[res] not in freq:
            freq[values[res]] = 1
        freq[values[res]] += 1
    
    for value in values:
        print(f"The probability of face {value} is {freq[value]/num_trials}")
        
       