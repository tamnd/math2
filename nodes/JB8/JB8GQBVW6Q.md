---
tag: JB8GQBVW6Q
kind: statement
role: theorem
name: Kojima–Schur theorem
msc: [40C05, 40D05]
uses: [RKFB6AHPBE, 0AZ3R52593]
about: [M6311DWJ1E]
sources:
  - url: https://en.wikipedia.org/wiki/Silverman–Toeplitz_theorem
---

## Statement

Let $A = (a_{nk})_{n, k \ge 0}$ be an infinite complex matrix.
Every [[convergent sequence|0AZ3R52593]] $s$ is [[$A$-summable|RKFB6AHPBE]], that is, $(As)_n = \sum_k a_{nk} s_k$ is defined for all $n$ and converges as $n \to \infty$, if and only if:

1. $\sup_{n} \sum_{k=0}^{\infty} \abs{a_{nk}} < \infty$;
2. for every $k$, the limit $\alpha_k = \lim_{n \to \infty} a_{nk}$ exists;
3. the limit $\alpha = \lim_{n \to \infty} \sum_{k=0}^{\infty} a_{nk}$ exists.

In that case $\sum_k \abs{\alpha_k} < \infty$, and for every convergent $s$ with limit $L$,
$$\lim_{n \to \infty} (As)_n = \alpha L + \sum_{k=0}^{\infty} \alpha_k (s_k - L).$$

## Remarks

Such matrices are called *conservative*.
Conditions 2 and 3 are needed because the unit sequences $e_k$ and the constant sequence $1$ are convergent; condition 1 follows from the uniform boundedness principle.
The limit formula comes from writing $s = L \cdot \mathbf{1} + (s - L \cdot \mathbf{1})$, where the second sequence tends to $0$.
Example: let $a_{nk} = 1$ if $k = 0$, $a_{nk} = \frac{1}{n+1}$ if $1 \le k \le n$, and $a_{nk} = 0$ otherwise.
Then $\alpha_0 = 1$, $\alpha_k = 0$ for $k \ge 1$ and $\alpha = 2$.
The formula gives $\lim (As)_n = 2L + (s_0 - L) = s_0 + L$, which one can also check directly.
With $\alpha_k = 0$ for all $k$ and $\alpha = 1$ the limit formula gives $L$, and one recovers the [[Silverman–Toeplitz theorem|S4J7SRPXMZ]].

## Explanations

### L1 human

The theorem tells exactly which infinite matrices turn every convergent sequence into a convergent sequence.
It also gives the new limit in terms of the old limit and of the limits of the columns.

### L2 human

Conservative matrices are exactly the bounded linear maps from the space of convergent sequences to itself that are given by matrices.
The new limit is a continuous linear functional of $s$, and the formula above is its general form.
Regular matrices are the conservative ones for which this functional is the ordinary limit.
