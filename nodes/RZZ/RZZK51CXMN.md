---
tag: RZZK51CXMN
kind: statement
role: theorem
name: Cramér's theorem
msc: [60F10]
uses: [00MRN0FARV, 0WQVXP7PDB, MNPWBBNCAD, 140N2PQSTE]
about: [Q702WCDQQ3, 140N2PQSTE]
sources:
  - url: https://en.wikipedia.org/wiki/Cram%C3%A9r%27s_theorem_(large_deviations)
same_as:
  wikidata: Q55647729
  wikipedia: Cramér's theorem (large deviations)
---

## Statement

Let $X_1, X_2, \dots$ be [[i.i.d.|00MRN0FARV]] real random variables.
Assume that the logarithmic [[moment-generating function|0WQVXP7PDB]] $\Lambda(\lambda) = \log E[e^{\lambda X_1}]$ is finite for every $\lambda \in \R$.
Let $\Lambda^*(x) = \sup_{\lambda \in \R} (\lambda x - \Lambda(\lambda))$ be its convex conjugate, and let $\bar X_n = (X_1 + \cdots + X_n)/n$.
Then the laws of $\bar X_n$ satisfy the [[large deviation principle|MNPWBBNCAD]] on $\R$ with the good [[rate function|140N2PQSTE]] $\Lambda^*$.
In particular, for every $x > E[X_1]$,
$$\lim_{n \to \infty} \frac{1}{n} \log P(\bar X_n \ge x) = -\Lambda^*(x).$$

## Remarks

The upper bound is the Chernoff bound.
For $\lambda \ge 0$, Markov's inequality gives $P(\bar X_n \ge x) \le e^{-n \lambda x} E[e^{\lambda S_n}] = e^{-n(\lambda x - \Lambda(\lambda))}$, with $S_n = n \bar X_n$, and one optimises over $\lambda$.
The lower bound uses a change of measure, the tilted law $e^{\lambda y - \Lambda(\lambda)} \, P(X_1 \in dy)$ with $\lambda$ chosen so that its mean is $x$.
Under the tilted law the event $\bar X_n \approx x$ is typical, and the cost of the change of measure is $\Lambda^*(x)$.

The function $\Lambda^*$ is convex, non-negative, and equal to $0$ exactly at the mean $E[X_1]$.

Example: for standard normal $X_k$, $\Lambda(\lambda) = \lambda^2/2$ and $\Lambda^*(x) = x^2/2$.
Example: for fair coin tosses with values $0$ and $1$, $\Lambda^*(x) = x \log x + (1 - x) \log(1 - x) + \log 2$ on $[0, 1]$, and $\Lambda^* = \infty$ outside $[0, 1]$.

On $\R$ the large deviation principle holds for every i.i.d. sequence, with rate function $\Lambda^*$, but without the finiteness assumption $\Lambda^*$ need not be good.

## Explanations

### L1 human

The average of many independent copies of a random number is very likely close to the mean.
Cramér's theorem says how unlikely a given deviation is: the probability falls exponentially in the number of copies.
The exponent is computed from the moment-generating function by a Legendre transform.

### L2 human

The theorem is the first large deviation principle and the model for the others.
Its proof introduces the two main tools of the subject: exponential Chebyshev bounds for the upper bound and exponential tilting for the lower bound.
In $\R^d$ the same result holds with $\lambda x$ replaced by an inner product, and the Gärtner–Ellis theorem extends it to dependent sequences.
[[Sanov's theorem|QWEF2WAXJM]] is the corresponding result for empirical measures; Cramér's theorem for finitely valued variables can be deduced from it by the contraction principle.
