---
tag: 01APZ8GDQH
kind: statement
role: theorem
name: Chapman–Kolmogorov equation
aliases: [chapman-kolmogorov-equations]
msc: [60J10]
uses: [033TJBZDG0, 0F1KBVY161, 0E5G5FMT2R, 0HB8SXHPFA]
sources:
  - url: https://en.wikipedia.org/wiki/Chapman–Kolmogorov_equation
    locator: Application to time-dilated Markov chains
same_as:
  wikidata: Q722882
  wikipedia: Chapman–Kolmogorov equation
---

## Statement

Let $(X_n)_{n \ge 0}$ be a time-homogeneous [[Markov chain|033TJBZDG0]] on a countable state space $S$. For $n \ge 0$, let $p^{(n)}_{ij} = P(X_{m+n} = j \mid X_m = i)$ be the $n$-step transition probabilities.
Then for all $m, n \ge 0$ and $i, j \in S$,
$$p^{(m+n)}_{ij} = \sum_{k \in S} p^{(m)}_{ik} \, p^{(n)}_{kj}.$$
In matrix form, $P^{(m+n)} = P^{(m)} P^{(n)}$, so $P^{(n)} = P^n$ for the [[transition matrix|0F1KBVY161]] $P$.

## Remarks

Proof: condition on the state $X_m = k$ at the intermediate time, with the [[law of total probability|0E5G5FMT2R]], and use the [[Markov property|0HB8SXHPFA]].
The equation says that to go from $i$ to $j$ in $m + n$ steps, the chain must be at some state $k$ after $m$ steps.
For a Markov process with transition kernels $p_{s,t}(x, dy)$, the equation reads $p_{s,u}(x, A) = \int p_{s,t}(x, dy) \, p_{t,u}(y, A)$ for $s \le t \le u$.

## History

The equation is named after Sydney Chapman and Andrey Kolmogorov.

## Explanations

### L1 human

The chances for several steps come from multiplying the one-step transition matrix with itself.
For example, the chance of rain in two days, given sun today, sums over the two possible states of tomorrow.
