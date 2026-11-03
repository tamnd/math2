---
tag: PRFJJNX482
kind: statement
role: theorem
name: Existence of optimal stationary policies
msc: [90C40, "93E20"]
uses: [EC0HKSBVQ7, Z94Z6BY8JG, 0QN69YA357, 0VK6VEH345]
about: [WCNHWTJXYD]
sources:
  - url: https://en.wikipedia.org/wiki/Markov_decision_process
---

## Statement

Let $(S, A, P, r, \gamma)$ be a discounted [[Markov decision process|WCNHWTJXYD]] with finite state set $S$ and finite action set $A$.
Its transition law is $P$, its reward is $r \colon S \times A \to \R$, and its discount factor is $\gamma \in [0, 1)$.
Let $V^*(s) = \sup_\pi V^\pi(s)$, where the supremum runs over all policies, including history-dependent and randomized ones.
Then:

1. $V^*$ is the unique function $V \colon S \to \R$ that satisfies the Bellman optimality equation
$$V(s) = \max_{a \in A} \Big( r(s, a) + \gamma \sum_{s' \in S} P(s' \mid s, a) V(s') \Big) \quad \text{for all } s \in S.$$
2. Let $f \colon S \to A$ be a map such that, for every $s$, the action $f(s)$ attains the maximum in this equation for $V = V^*$.
Then the stationary deterministic policy $f$ is optimal: $V^f(s) = V^*(s)$ for all $s$.

In particular, an optimal stationary deterministic policy exists.

## Remarks

The Bellman operator $\mathcal{T}$ on the right-hand side is a [[contraction mapping|0QN69YA357]] of modulus $\gamma$ for the maximum norm on $\R^S$.
So by the [[Banach fixed point theorem|0VK6VEH345]] it has a unique fixed point $V$.
For a greedy map $f$, the value $V^f$ is the fixed point of the contraction $\mathcal{T}_f$, and $\mathcal{T}_f V = \mathcal{T} V = V$ gives $V^f = V$.
Conversely, let $W$ be the constant function $\max \abs{r} / (1 - \gamma)$.
For any policy $\pi$ and $n \ge 1$, the expected discounted reward of the first $n$ steps plus the largest possible tail is at most $(\mathcal{T}^n W)(s)$.
Letting $n \to \infty$ gives $V^\pi \le V$ for every policy $\pi$, hence $V = V^*$.
Example: take one state, two actions of reward $1$ and $2$, and $\gamma = 1/2$.
The equation reads $V = \max(1, 2) + V/2$, so $V^* = 4$, attained by always choosing the second action.
Without discounting or another stability condition the result can fail.
With countably many states and without discounting, optimal policies may not exist, or may need to be non-stationary.

## Explanations

### L1 human

In a problem that goes on forever with discounted rewards, it is enough to look for a rule of the form "in state $s$, do $f(s)$".
Remembering the past or flipping coins never helps.
The best rule is found by solving one fixed-point equation for the values of the states and then acting greedily.

### L2 human

This theorem justifies [[value iteration and policy iteration|NPM6VD9TZ1]].
Both search only among stationary deterministic policies, and both converge to $V^*$.
The contraction argument extends to countable or general state spaces with bounded rewards, with measurability conditions on the maximizers.
For the long-run average reward on finite models, optimal stationary deterministic policies still exist.
The proof is harder and goes through limits of discounted problems as $\gamma \to 1$.
