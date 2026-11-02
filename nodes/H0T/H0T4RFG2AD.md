---
tag: H0T4RFG2AD
kind: definition
name: Steenrod square
msc: [55S10, 55S05]
defines: VR7RHP41M0
uses: [K8T15QHN3W, 6N7BC70CX0, JX47MS1R1H]
sources:
  - url: https://en.wikipedia.org/wiki/Steenrod_algebra
---

## Definition

Write $H^*(X, A)$ for [[singular cohomology|6N7BC70CX0]] of a pair of spaces with coefficients in $\Z/2\Z$.
The *Steenrod squares* are the [[cohomology operations|K8T15QHN3W]]
$$\operatorname{Sq}^i \colon H^n(X, A) \to H^{n+i}(X, A), \quad i \ge 0, \ n \ge 0,$$
defined for all pairs $(X, A)$, that satisfy:

1. Naturality: $f^* \operatorname{Sq}^i = \operatorname{Sq}^i f^*$ for every map of pairs $f$.
2. Additivity: $\operatorname{Sq}^i(x + y) = \operatorname{Sq}^i x + \operatorname{Sq}^i y$.
3. Cartan formula: $\operatorname{Sq}^k(x \smile y) = \sum_{i + j = k} \operatorname{Sq}^i x \smile \operatorname{Sq}^j y$, with $\smile$ the [[cup product|JX47MS1R1H]].
4. Stability: $\operatorname{Sq}^i$ commutes with the connecting homomorphism $\delta \colon H^n(A) \to H^{n+1}(X, A)$.
5. $\operatorname{Sq}^0$ is the identity.
6. If $x$ has degree $n$, then $\operatorname{Sq}^n x = x \smile x$, and $\operatorname{Sq}^i x = 0$ for $i > n$.

There is exactly one family of operations with these properties.

## Remarks

The total square is $\operatorname{Sq} = \operatorname{Sq}^0 + \operatorname{Sq}^1 + \operatorname{Sq}^2 + \cdots$; on each class only finitely many terms are nonzero.
The square $\operatorname{Sq}^1$ is the [[Bockstein homomorphism|H7PCM776GR]] of the sequence $0 \to \Z/2\Z \to \Z/4\Z \to \Z/2\Z \to 0$.

Example: in $H^*(\R P^\infty) = (\Z/2\Z)[a]$ with $\deg a = 1$, one has $\operatorname{Sq} a = a + a^2$ by clauses 5 and 6.
By the Cartan formula, $\operatorname{Sq}(a^n) = (a + a^2)^n$, so $\operatorname{Sq}^i(a^n) = \binom{n}{i} a^{n+i}$.
For instance $\operatorname{Sq}^1(a^2) = 2a^3 = 0$ and $\operatorname{Sq}^1(a^3) = a^4$.

Non-example: the family with $\operatorname{Sq}^0 = \id$ and $\operatorname{Sq}^i = 0$ for all $i \ge 1$ satisfies clauses 1 to 5 but fails clause 6, since $\operatorname{Sq}^1 a$ would be $0$ instead of $a^2$ in $H^2(\R P^\infty)$.
