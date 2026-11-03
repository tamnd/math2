---
tag: EC0HKSBVQ7
kind: definition
name: Markov decision process
msc: [90C40, "93E20", 60J20]
defines: WCNHWTJXYD
uses: [0G48PYM96Q, 0B77KZCQ51, 0WQNRCNY3M]
sources:
  - url: https://en.wikipedia.org/wiki/Markov_decision_process
    locator: Definition
---

## Definition

A *discounted Markov decision process* is a tuple $(S, A, P, r, \gamma)$ where:

1. $S$ is a finite set, the set of states;
2. $A$ is a finite set, the set of actions;
3. $P$ gives, for each $s \in S$ and $a \in A$, a probability distribution $P(\cdot \mid s, a)$ on $S$, the transition law;
4. $r \colon S \times A \to \R$ is the reward function;
5. $\gamma \in [0, 1)$ is the discount factor.

A *policy* $\pi$ chooses at each time $t$ an action $a_t$, possibly at random, as a function of the history $s_0, a_0, \dots, s_{t-1}, a_{t-1}, s_t$.
Fix a policy and an initial state $s_0 = s$.
Then the states and actions form a random sequence in which $s_{t+1}$ has law $P(\cdot \mid s_t, a_t)$ given the history up to time $t$.
The *value* of $\pi$ at $s$ is
$$V^\pi(s) = \mathbb{E}^\pi_s\Big[\sum_{t=0}^{\infty} \gamma^t r(s_t, a_t)\Big],$$
and the *optimal value* is $V^*(s) = \sup_\pi V^\pi(s)$.
A policy $\pi$ is *optimal* if $V^\pi(s) = V^*(s)$ for every $s \in S$.
A policy is *stationary deterministic* if it is given by a map $f \colon S \to A$ with $a_t = f(s_t)$ for all $t$.

## Remarks

Example: $S = \set{\text{up}, \text{down}}$, $A = \set{\text{wait}, \text{repair}}$.
From up, both actions give reward $1$ and lead to down with probability $1/10$.
From down, wait gives reward $0$ and stays down, while repair gives reward $-2$ and leads to up.
Each $P(\cdot \mid s, a)$ is a probability law on $S$, $r$ is real-valued, and with $\gamma = 0.9$ all five clauses hold.

Non-example: taking $\gamma = 1$ fails clause 5, and then the series defining $V^\pi$ may diverge.
This happens for the policy that always repairs in the example.
Each visit to down costs $2$ but is followed by about ten steps of reward $1$, so the undiscounted total is $+\infty$.

Under a stationary deterministic policy $f$, the states form a [[Markov chain|0G48PYM96Q]] with transition matrix $P(s' \mid s, f(s))$.
Other standard variants allow infinite state or action spaces, action sets $A(s)$ that depend on the state, a finite horizon, or the long-run average reward instead of the discounted sum.
Costs to be minimized are handled by taking $r$ to be minus the cost.
