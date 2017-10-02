'''
Author: Samuel Remedios

Expectation Maximization for flipping a coin
per this paper: ai.stanford.edu/~chuongdo/papers/em_tutorial.pdf

'''
    
# ground truth
theta_A = 0.80
theta_B = 0.52

# chance to choose A or B is even
CHOOSE_COIN = 0.5

def compute_model(theta_A_hat, num_heads_A, theta_B_hat, num_heads_B, num_flips):
    num_tails_A = num_flips - num_heads_A
    num_tails_B = num_flips - num_heads_B
    pr_A = CHOOSE_COIN
    pr_B = 1 - pr_A

    pr_X_A_given_theta = pr_A * theta_A_hat**num_heads_A * (1-theta_A_hat)**num_tails_A
    pr_X_B_given_theta = pr_B * theta_B_hat**num_heads_B * (1-theta_B_hat)**num_tails_B

    pr_X_given_theta = pr_A * (theta_A_hat**num_heads_A * (1-theta_A_hat)**num_tails_A + \
                        theta_B_hat**num_heads_B * (1-theta_B_hat)**num_tails_B)
    pr_A_given_X_theta = pr_X_A_given_theta / pr_X_given_theta
    pr_B_given_X_theta = pr_X_B_given_theta / pr_X_given_theta
    
    return pr_A_given_X_theta, pr_B_given_X_theta


trial_1 = {"H":5,"T":5}
trial_2 = {"H":9,"T":1}
trial_3 = {"H":8,"T":2}
trial_4 = {"H":4,"T":6}
trial_5 = {"H":7,"T":3}

trials = [trial_1,trial_2,trial_3,trial_4,trial_5]

###### "E" step ######

# initial guesses
theta_A_hat = 0.1
theta_B_hat = 0.1
n_epochs = 10
for _ in range(n_epochs):
    expected_A_heads = 0
    expected_A_tails = 0
    expected_B_heads = 0
    expected_B_tails = 0
    for trial in trials:
        theta_A_tmp, theta_B_tmp = compute_model(theta_A_hat, trial["H"], theta_B_hat, trial["T"], 10)
        expected_A_heads += trial["H"] * theta_A_tmp
        expected_A_tails += trial["T"] * theta_A_tmp

        expected_B_heads += trial["H"] * theta_B_tmp
        expected_B_tails += trial["T"] * theta_B_tmp

        print(expected_A_heads, expected_A_tails, expected_B_heads, expected_B_tails)

    ###### "M" Step ######
    theta_A_hat = expected_A_heads / (expected_A_heads+expected_A_tails)
    theta_B_hat = expected_B_heads / (expected_B_heads+expected_B_tails)

    print(theta_A_hat, theta_B_hat)
