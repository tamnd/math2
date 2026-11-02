---
tag: WMVAT9MBZ1
kind: statement
role: theorem
name: Riemann–Roch theorem
msc: [14C40, 14H05, 30F10]
uses: [XJM2MT4S3Y, 6W8TDV9VVN, Z9DN23DAE2, W05VYY4HBR, 0PF6TM8TWT]
about: [XJM2MT4S3Y, Z9DN23DAE2]
sources:
  - url: https://en.wikipedia.org/wiki/Riemann%E2%80%93Roch_theorem
same_as:
  wikidata: Q379048
  wikipedia: Riemann–Roch theorem
---

## Statement

Let $k$ be an [[algebraically closed field|0PF6TM8TWT]], and let $X$ be a smooth projective [[algebraic curve|XJM2MT4S3Y]] over $k$ of [[genus|6W8TDV9VVN]] $g$.
Let $k(X)$ be the field of rational functions on $X$.
For a [[divisor|Z9DN23DAE2]] $D$ on $X$, let
$$L(D) = \set{f \in k(X)^\times : \operatorname{div}(f) + D \ge 0} \cup \set{0},$$
which is a finite-dimensional vector space over $k$, and let $\ell(D) = \dim_k L(D)$.
Let $K$ be a [[canonical divisor|W05VYY4HBR]] of $X$.
Then for every divisor $D$ on $X$,
$$\ell(D) - \ell(K - D) = \deg D - g + 1.$$

## Remarks

In sheaf language, $\ell(D) = h^0(X, \mathcal{O}_X(D))$ and $\ell(K - D) = h^1(X, \mathcal{O}_X(D))$ by Serre duality, so the formula reads $\chi(\mathcal{O}_X(D)) = \deg D + 1 - g$.
One proof checks the formula for $D = 0$, where it says $h^1(\mathcal{O}_X) = g$.
Then it shows that both sides change by $1$ when a point $P$ is added to $D$.
This uses the exact sequence $0 \to \mathcal{O}_X(D) \to \mathcal{O}_X(D + P) \to k_P \to 0$.
Taking $D = 0$ and $D = K$ gives $\ell(K) = g$ and $\deg K = 2g - 2$.
If $\deg D > 2g - 2$, then $\deg(K - D) < 0$, so $\ell(K - D) = 0$ and $\ell(D) = \deg D - g + 1$ exactly.
Example: on the projective line, $g = 0$ and $K = -2P$ for any point $P$.
For $D = nP$ with $n \ge 0$ the formula gives $\ell(D) = n + 1$.
This is the dimension of the space of polynomials of degree at most $n$ in an affine coordinate.

## Explanations

### L1 human

A divisor prescribes where a function may have poles and how bad they may be, and where it must vanish.
The theorem counts how many independent functions obey such a prescription.
The answer is the degree of the prescription, corrected by the genus of the curve and by a second count that involves the canonical divisor.
For prescriptions of large degree the correction term disappears, and the count is simply $\deg D - g + 1$.

### L2 human

Riemann–Roch is the main computational tool of the theory of curves.
It shows that a divisor of degree at least $2g + 1$ gives an embedding into projective space.
It also shows that every curve of genus $0$ is the projective line, and that every curve of genus $1$ with a point is a plane cubic.
It feeds directly into [[Clifford's theorem|RSW29AVKGM]], the [[Riemann–Hurwitz formula|42A5ZT6AWN]] and Brill–Noether theory.
Its higher-dimensional generalizations are the Hirzebruch–Riemann–Roch and Grothendieck–Riemann–Roch theorems.
