p(A) = probability of being offered a job
p(R) = probability of being rejected
p(G|A) = likelihood of feeling good given acceptance
p(B|A) = likelihood of feeling bad given acceptance
p(G|R) = likelihood of feeling good given rejection
p(B|R) = likelihood of feeling bad given rejection

# Importing necessary libraries
import numpy as np

# Defining prior probabilities assuming only 20% of all candidates are accepted and 80% of selected candidates felt good about interview
# These prior probabilities get updated based on actual events like interviews
P(A) = 0.1, P(R) = 0.9, P(G|A) = 0.8, P(B|A) = 0.2, P(G|R) = 0.3, P(B|R) = 0.7

# Function to calculate posterior probability using Bayes' theorem
def posterior (prior, likelihood_accept, likelihood_reject, evidence):
  return (likelihood_accept * prior) / evidence, (likelihood_reject * prior) / evidence

interview_feeling = 'good'

if feeling == 'good':
  # Calculating evidence (total probability of the data)
  evidence = (P(G|A) * P(A)) + (P(G|R) * P(R))
  
  # Updating posterior probability of acceptance and rejection
  P(A), P(R) = posterior(P(A), P(G|A), P(G|R), evidence)

else:
  # Calculating evidence (total probability of the data)
  evidence = (P(B|A) * P(A)) + (P(B|R) * P(R))
  
  # Updating posterior probability of acceptance and rejection
  P(A), P(R) = posterior(P(A), P(B|A), P(B|R), evidence)

# Output the final posterior probabilities
print("The final posterior probability of being offered a job:", P(A))
print("The final posterior probability of being rejected:", P(R))
