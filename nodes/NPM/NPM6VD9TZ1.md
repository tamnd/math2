---
tag: NPM6VD9TZ1
kind: concept
name: Value iteration and policy iteration
msc: [90C40, 90C39]
sources:
  - url: https://en.wikipedia.org/wiki/Markov_decision_process
    locator: Algorithms
---

## Summary

Value iteration and policy iteration are the two classical algorithms that compute an optimal policy of a finite discounted [[Markov decision process|WCNHWTJXYD]].
Value iteration applies the Bellman optimality operator again and again to an estimate of the optimal value function.
Policy iteration alternates between computing the exact value of the current policy and improving the policy greedily with respect to that value.
Both rest on the [[Bellman equation|Z94Z6BY8JG]] and are the starting point of many reinforcement learning methods.

## Explanations

### L1 human

Value iteration is like improving a map of how good each place is.
At every round, each place looks one step ahead and updates its score from the scores of its neighbours.
After many rounds the scores stop changing, and then the best move from each place is the one that leads to the best score.
Policy iteration instead fixes a plan, works out exactly how good it is, and then changes the plan wherever a different first move looks better.
Each new plan is at least as good as the old one, and after finitely many changes no improvement is possible.
