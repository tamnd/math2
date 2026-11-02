---
tag: S4J7SRPXMZ
kind: statement
role: theorem
name: Silverman–Toeplitz theorem
msc: [40C05, 40D05]
uses: [RKFB6AHPBE, BXVVXJQV8M]
about: [M6311DWJ1E, 29C7C41A52]
sources:
  - url: https://en.wikipedia.org/wiki/Silverman–Toeplitz_theorem
same_as:
  wikidata: Q7516736
  wikipedia: Silverman–Toeplitz theorem
---

## Statement

Let $A = (a_{nk})_{n, k \ge 0}$ be an infinite complex matrix.
The [[matrix method|RKFB6AHPBE]] given by $A$ is [[regular|BXVVXJQV8M]], that is, every convergent sequence $s$ is $A$-summable to $\lim s_k$, if and only if:

1. $\sup_{n} \sum_{k=0}^{\infty} \abs{a_{nk}} < \infty$;
2. $\lim_{n \to \infty} a_{nk} = 0$ for every $k$;
3. $\lim_{n \to \infty} \sum_{k=0}^{\infty} a_{nk} = 1$.

## Remarks

Necessity of conditions 2 and 3: apply $A$ to the constant sequence $1$ and to the unit sequence $e_k$.
Here $e_k$ has $1$ in place $k$ and $0$ elsewhere, so it tends to $0$.
Necessity of condition 1 uses the uniform boundedness principle, or a direct "gliding hump" construction of a null sequence with unbounded transform.
Sufficiency: write $s_k = L + r_k$ with $r_k \to 0$; condition 3 handles $L$, and for $r$ one splits $\sum_k a_{nk} r_k$ into finitely many terms, small by condition 2, and a tail, small by condition 1.
Example: the Cesàro matrix $a_{nk} = \frac{1}{n+1}$ for $k \le n$ has row sums of absolute values equal to $1$, entries tending to $0$ and row sums $1$, so Cesàro summation is regular.
Non-example: the matrix with $a_{nk} = 1$ for $k \le n$ and $0$ otherwise violates condition 1, and indeed it sends the convergent sequence $s_k = \frac{1}{k+1}$ to the divergent harmonic partial sums.

## Explanations

### L1 human

A weighted-average method gives the right answer on every convergent sequence under three conditions.
The weights stay bounded in total size, each fixed weight fades away, and the weights in each row add up to nearly $1$.

### L2 human

The theorem reduces regularity, a statement about all convergent sequences, to three checks on the matrix.
It is the standard tool for showing that Cesàro, Nörlund, Riesz and Euler methods are regular.
The [[Kojima–Schur theorem|JB8GQBVW6Q]] characterizes the wider class of matrices that only send convergent sequences to convergent sequences, and the Silverman–Toeplitz theorem is its special case with limits $0$ and $1$.
The [[Steinhaus theorem|NG1FPJQHA1]] shows that no regular matrix sums every bounded sequence.
