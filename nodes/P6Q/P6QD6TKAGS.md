---
tag: P6QD6TKAGS
kind: statement
role: theorem
name: Grothendieck–Lefschetz trace formula
msc: [14F20, 14G15, 14G10]
uses: [HV6YBS0YDH, E1DVHN06CR, 7YX76G0838, 0T3WVTD675, 0RPDTWY2JS, SWJYG87QQH]
about: [E1DVHN06CR, SWJYG87QQH]
sources:
  - url: https://en.wikipedia.org/wiki/Grothendieck_trace_formula
same_as:
  wikidata: Q5610732
  wikipedia: Grothendieck trace formula
---

## Statement

Let $q$ be a power of a prime $p$, and let $\ell \ne p$ be another prime.
Let $X$ be a separated [[algebraic variety|HV6YBS0YDH]] over the finite field $\F_q$.
Let $\bar{X} = X \times_{\F_q} \bar{\F}_q$, where $\bar{\F}_q$ is an algebraic closure of $\F_q$.
Let $H^i_c(\bar{X}, \Q_\ell)$ be the [[ℓ-adic cohomology|E1DVHN06CR]] of $\bar{X}$ with compact support.
Let $F$ be the endomorphism of it induced by the [[Frobenius|0T3WVTD675]] morphism of $X$, which raises coordinates to the power $q$.
Then the number of [[rational points|SWJYG87QQH]] of $X$ is
$$\# X(\F_q) = \sum_{i=0}^{2 \dim X} (-1)^i \, \tr\big(F \mid H^i_c(\bar{X}, \Q_\ell)\big),$$
where $\tr$ is the [[trace|0RPDTWY2JS]] of a linear map.

## Remarks

The points of $X(\F_q)$ are the fixed points of the Frobenius morphism of $\bar{X}$, so the formula is a Lefschetz fixed point formula, with the [[Lefschetz number|ZSYCA4EGEZ]] on the right.
Grothendieck proved it in a more general form, for a constructible $\ell$-adic sheaf $\mathcal{F}$ on $X$.
Then the sum over $x \in X(\F_q)$ of the traces of Frobenius on the stalks $\mathcal{F}_{\bar{x}}$ equals the alternating sum of the traces of $F$ on $H^i_c(\bar{X}, \mathcal{F})$.
Example: for $X = \mathbb{A}^1$, the only nonzero group is $H^2_c(\bar{X}, \Q_\ell)$, of dimension $1$, on which $F$ acts by $q$.
The formula gives $\# \mathbb{A}^1(\F_q) = q$.
For $X = \mathbb{P}^1$, the groups $H^0$ and $H^2$ contribute $1$ and $q$, and the count is $q + 1$.
Compact supports are needed when $X$ is not proper: the ordinary cohomology of $\mathbb{A}^1_{\bar{\F}_q}$ is $\Q_\ell$ in degree $0$ only, which would give the wrong count $1$.
Applied to $X \times \F_{q^m}$ for all $m$, the formula expresses the zeta function of $X$ as an alternating product of characteristic polynomials of $F$, which proves its rationality.

## Explanations

### L1 human

Counting the solutions of polynomial equations over a finite field looks like pure arithmetic.
The formula says that this count can be read off from a geometric object: the cohomology of the variety, together with the action of the Frobenius map on it.
The points over $\F_q$ are exactly the points that the Frobenius map does not move, so the count is a count of fixed points, as in topology.

### L2 human

This is the main bridge between point counts over finite fields and $\ell$-adic cohomology.
It gives the rationality and the cohomological form of the zeta function.
Deligne's bounds on the eigenvalues of $F$ then give estimates such as $\abs{\# C(\F_q) - q - 1} \le 2g\sqrt{q}$ for a smooth projective curve $C$ of genus $g$.
In the sheaf version it turns sums of characters, such as Gauss and Kloosterman sums, into traces on cohomology, which is how they are bounded.
