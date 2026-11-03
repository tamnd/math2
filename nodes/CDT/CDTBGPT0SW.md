---
tag: CDTBGPT0SW
kind: problem
name: Optimal stopping
msc: [60G40, 62L15, "93E20"]
uses: [0NFPJVJJHX, HNK1Y62G7V, YRNFE016FF, WND87FBAKC, 0TTDGTEFMN]
about: [WND87FBAKC, SXE9KQ02YE]
sources:
  - url: https://en.wikipedia.org/wiki/Optimal_stopping
same_as:
  wikidata: Q7098950
  wikipedia: Optimal stopping
history:
  posed_by: "J. Laurie Snell"
  first_stated: "1952"
  notes: "Snell first formulated and solved a general discrete-time optimal stopping problem in 1952, describing the value by what is now called the Snell envelope. Special cases arose earlier in Abraham Wald's sequential analysis of the 1940s."
---

## Problem

Let $(\Omega, \mathcal{F}, P)$ be a [[probability space|0NFPJVJJHX]] with a [[filtration|HNK1Y62G7V]] $\mathcal{F}_0 \subseteq \mathcal{F}_1 \subseteq \cdots \subseteq \mathcal{F}_N \subseteq \mathcal{F}$, where $N \ge 0$ is an integer.
Let $(G_n)_{0 \le n \le N}$ be an [[adapted process|YRNFE016FF]] of integrable random variables; $G_n$ is the reward for stopping at time $n$.
Let $\mathcal{T}$ be the set of [[stopping times|WND87FBAKC]] $\tau$ with values in $\set{0, 1, \dots, N}$.
The *optimal stopping problem* asks for the value
$$V = \sup_{\tau \in \mathcal{T}} E[G_\tau]$$
and for a stopping time $\tau^* \in \mathcal{T}$ with $E[G_{\tau^*}] = V$.
The same question is asked with an infinite horizon and in continuous time, for example for a reward $g(X_t)$ of a Markov process $X$.

## Remarks

In the finite-horizon discrete-time form the problem is solved by backward induction.
Define the Snell envelope by $S_N = G_N$ and $S_n = \max(G_n, E[S_{n+1} \mid \mathcal{F}_n])$ for $n < N$, with the [[conditional expectation|0TTDGTEFMN]].
Then $\tau^* = \min\set{n : S_n = G_n}$ is an optimal stopping time, and $V = E[S_0]$.
The process $(S_n)$ is the smallest supermartingale that dominates $(G_n)$.
The rule says: stop as soon as the reward on offer is at least the expected value of going on.

Example: a fair die may be rolled at most twice, and after each roll the player may stop and receive the number shown.
After a first roll the value of going on is $E[\text{second roll}] = 7/2$.
So the optimal rule stops on a first roll of $4$, $5$ or $6$ and rolls again otherwise.
Its value is $\frac{4 + 5 + 6}{6} + \frac{3}{6} \cdot \frac{7}{2} = \frac{17}{4}$.

The [[secretary problem|SXE9KQ02YE]] is a well-known special case.
In infinite horizon or continuous time the Snell envelope still describes the solution under integrability conditions, but an optimal stopping time need not exist.
For a Markov process the problem becomes a free-boundary problem: one looks for the region of states where it is optimal to stop.
The pricing of American options in mathematical finance is an optimal stopping problem.

## Explanations

### L1 human

You watch a random process and, at each moment, you may stop and collect the current reward, or wait in the hope of something better.
Once you stop, you cannot go back.
The problem is to find the rule that gives the largest reward on average.
The key idea is to compare what you have now with what you can expect if you keep going, and to work backwards from the last moment.
Selling a house, hiring a candidate and exercising a financial option are all problems of this kind.
