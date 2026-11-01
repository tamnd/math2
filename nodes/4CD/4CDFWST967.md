---
tag: 4CDFWST967
kind: statement
role: theorem
name: Ramanujan–Petersson conjecture
msc: [11F30, 11F11]
uses: [A50Y012RBP, 1H6R856P3C, S4SV3QZ8B1, 6DNZAGCSQS, 01826KMG2H]
about: [A50Y012RBP, 6DNZAGCSQS]
sources:
  - url: https://en.wikipedia.org/wiki/Ramanujan%E2%80%93Petersson_conjecture
same_as:
  wikidata: Q630650
  wikipedia: Ramanujan–Petersson conjecture
---

## Statement

Let $N \ge 1$ and $k \ge 2$ be integers.
Let $f = \sum_{n \ge 1} a_n q^n$ be a [[cusp form|A50Y012RBP]] of weight $k$ for the [[congruence subgroup|1H6R856P3C]] $\Gamma_0(N)$, with $q = e^{2 \pi i \tau}$.
Assume that $a_1 = 1$ and that $f$ is an eigenvector of the [[Hecke operator|S4SV3QZ8B1]] $T_p$ for every [[prime|01826KMG2H]] $p$ not dividing $N$.
Then for every prime $p$ not dividing $N$,
$$\abs{a_p} \le 2 p^{(k-1)/2}.$$
In particular, the [[Ramanujan tau function|6DNZAGCSQS]] satisfies $\abs{\tau(p)} \le 2 p^{11/2}$ for every prime $p$.

## Remarks

Ramanujan conjectured the bound for $\tau(p)$ in 1916, and Petersson extended the conjecture to other modular forms.
Deligne proved it in 1974 as a consequence of his proof of the Weil conjectures.
Earlier work of Eichler, Shimura and Deligne had identified $a_p$ with the trace of Frobenius on an étale cohomology group, whose eigenvalues have absolute value $p^{(k-1)/2}$ by the Weil conjectures.
Example: $\tau(2) = -24$ and $2 \cdot 2^{11/2} = 2^{13/2} \approx 90.5$; $\tau(3) = 252$ and $2 \cdot 3^{11/2} \approx 841.8$.
The normalization $a_1 = 1$ and the eigenform hypothesis are needed: the cusp form $100\Delta$ has $a_2 = -2400$, which breaks the bound.
The analogous statement for Maass forms is still open.

## Explanations

### L1 human

The coefficients of a Hecke eigenform look random, but they cannot be too large.
At a prime $p$, the coefficient is at most about $2 p^{(k-1)/2}$, roughly the square root of the trivial size $p^{k-1}$.
For Ramanujan's function this says $\abs{\tau(p)} \le 2 p^{11/2}$.
It took almost sixty years, and a revolution in algebraic geometry, to prove it.

### L2 human

For a normalized eigenform, the Euler factor at $p \nmid N$ is $1 - a_p p^{-s} + p^{k-1-2s}$.
Writing it as $(1 - \alpha_p p^{-s})(1 - \beta_p p^{-s})$, the bound is equivalent to $\abs{\alpha_p} = \abs{\beta_p} = p^{(k-1)/2}$.
So the theorem is an analogue of the Riemann hypothesis for the local factors of the L-function of $f$.
Together with multiplicativity, it gives $\abs{a_n} \le d(n)\, n^{(k-1)/2}$ for $n$ prime to $N$, where $d(n)$ is the number of divisors of $n$.
The [[Sato–Tate conjecture|TRGBJYPBXH]] describes how the normalized values $a_p / (2 p^{(k-1)/2}) \in [-1, 1]$ are distributed.
