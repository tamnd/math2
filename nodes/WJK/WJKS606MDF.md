---
tag: WJKS606MDF
kind: statement
role: lemma
name: Lebesgue's lemma on near-best approximation
msc: [41A05, 41A35, 41A50]
uses: [03J5RAKB30, 06EKW1AKXF, 033DA1WE8Y, 7V7KWNK9HN]
about: [7V7KWNK9HN]
sources:
  - url: https://en.wikipedia.org/wiki/Lebesgue_constant
---

## Statement

Let $X$ be a [[normed vector space|03J5RAKB30]] and let $V \subseteq X$ be a linear subspace.
Let $P \colon X \to X$ be a bounded linear map with image in $V$ and $P v = v$ for all $v \in V$, with [[operator norm|06EKW1AKXF]] $\norm{P}$.
Then for every $f \in X$,
$$\norm{f - P f} \le (1 + \norm{P}) \inf_{v \in V} \norm{f - v}.$$

## Remarks

Proof: for any $v \in V$, $P v = v$ gives $f - P f = (f - v) - P(f - v)$.
So $\norm{f - P f} \le (1 + \norm{P}) \norm{f - v}$, and taking the infimum over $v$ gives the claim.

Example: let $P$ be polynomial interpolation at $n + 1$ nodes in $[a, b]$, acting on $C[a, b]$ with the uniform norm.
Then $\norm{P}$ is the [[Lebesgue constant|7V7KWNK9HN]] $\Lambda_n$, and the lemma gives $\norm{f - P f}_\infty \le (1 + \Lambda_n) E_n(f)$, where $E_n(f)$ is the error of best uniform approximation by polynomials of degree at most $n$.
For Chebyshev nodes, $\Lambda_n \le \frac{2}{\pi} \log(n + 1) + 1 < 4$ for $n < 100$, so interpolation loses less than a factor $5$ compared with the best polynomial.

The same lemma applies to Fourier partial sums, with $\Lambda_n$ the Lebesgue constants of the Dirichlet kernel.

## Explanations

### L1 human

A linear [[projection|033DA1WE8Y]] onto a space of approximants is never much worse than the best approximation from that space.
The loss factor is at most one plus the norm of the projection.
So a cheap method like interpolation is nearly optimal whenever its Lebesgue constant is small.

### L2 human

This is how Lebesgue constants enter convergence proofs.
Combined with Jackson's inequality, it shows that interpolation at Chebyshev nodes converges uniformly when $\omega(f, 1/n) \log n \to 0$, the Dini–Lipschitz condition.
Conversely, unbounded norms of projections lead through the uniform boundedness principle to divergence results such as Faber's theorem.
