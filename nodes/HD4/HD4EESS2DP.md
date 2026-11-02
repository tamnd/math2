---
tag: HD4EESS2DP
kind: definition
name: Todd class
msc: [14C17, 14C40, 57R20]
defines: 2YDB5089FR
uses: [EQSHJPE7H8, P4DZM975BV, PAD37GKDPD, 4HV4WTAX9P]
sources:
  - url: https://en.wikipedia.org/wiki/Todd_class
---

## Definition

Let $X$ be a smooth [[quasi-projective variety|EQSHJPE7H8]] over a field, with rational [[Chow ring|4HV4WTAX9P]] $CH^\bullet(X)_\Q = CH^\bullet(X) \otimes \Q$.
Let $E$ be a [[vector bundle|P4DZM975BV]] of rank $r$ on $X$ with [[Chern classes|PAD37GKDPD]] $c_1, \ldots, c_r$.
Write formally $\sum_{i=0}^r c_i(E) t^i = \prod_{j=1}^r (1 + \alpha_j t)$, where $\alpha_1, \ldots, \alpha_r$ are the *Chern roots* of $E$.
The *Todd class* of $E$ is
$$\operatorname{td}(E) = \prod_{j=1}^r \frac{\alpha_j}{1 - e^{-\alpha_j}} \in CH^\bullet(X)_\Q,$$
where each factor is expanded as the power series $\frac{x}{1 - e^{-x}} = 1 + \frac{x}{2} + \frac{x^2}{12} - \frac{x^4}{720} + \cdots$.
The product is symmetric in the $\alpha_j$, so it is a polynomial in $c_1, \ldots, c_r$ in each degree, and only finitely many degrees are nonzero.
The Todd class of $X$ is $\operatorname{td}(X) = \operatorname{td}(T_X)$, for the tangent bundle $T_X$.

## Remarks

In low degrees,
$$\operatorname{td}(E) = 1 + \frac{c_1}{2} + \frac{c_1^2 + c_2}{12} + \frac{c_1 c_2}{24} + \cdots.$$
The Todd class is multiplicative: $\operatorname{td}(E) = \operatorname{td}(E') \operatorname{td}(E'')$ for an exact sequence $0 \to E' \to E \to E'' \to 0$.
Example: for a smooth projective curve $X$ of genus $g$, $\operatorname{td}(X) = 1 + \frac{1}{2} c_1(T_X)$, and $\deg c_1(T_X) = 2 - 2g$, so the degree of the part in $CH^1$ is $1 - g$.
Non-example: the power series $1 + x$ also gives a multiplicative class, but it is the total Chern class, not the Todd class.
The Todd series, with its coefficient $\frac{1}{12}$ of $x^2$, is the one that makes the Hirzebruch–Riemann–Roch formula hold.
