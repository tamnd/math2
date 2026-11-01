---
tag: C9Z22J9SQE
kind: definition
name: Witt vectors
msc: [13F35]
defines: 6N3X2QX4W9
uses: [0310REJJY8, 0VTH8KPCG2, 0SDC934R52]
sources:
  - url: https://en.wikipedia.org/wiki/Witt_vector
---

## Definition

Let $p$ be a prime number and let $A$ be a [[commutative ring|0310REJJY8]].
For $n \ge 0$, the $n$-th ghost polynomial is
$$w_n(X_0, \ldots, X_n) = \sum_{i=0}^{n} p^i X_i^{p^{n-i}} = X_0^{p^n} + p X_1^{p^{n-1}} + \cdots + p^n X_n.$$
There are unique sequences of [[polynomials|0SDC934R52]] $S_n, P_n \in \Z[X_0, \ldots, X_n, Y_0, \ldots, Y_n]$ such that for every $n \ge 0$:
$$w_n(S_0, \ldots, S_n) = w_n(X) + w_n(Y), \qquad w_n(P_0, \ldots, P_n) = w_n(X) \, w_n(Y).$$
The ring of *$p$-typical Witt vectors* $W(A)$ is the set $A^{\N}$ of sequences $a = (a_0, a_1, a_2, \ldots)$ with entries in $A$, with the operations
$$(a + b)_n = S_n(a_0, \ldots, a_n, b_0, \ldots, b_n), \qquad (ab)_n = P_n(a_0, \ldots, a_n, b_0, \ldots, b_n).$$
With these operations $W(A)$ is a commutative ring with zero $(0, 0, \ldots)$ and identity $(1, 0, 0, \ldots)$.

## Remarks

The first sum polynomials are $S_0 = X_0 + Y_0$ and $S_1 = X_1 + Y_1 + \frac{X_0^p + Y_0^p - (X_0 + Y_0)^p}{p}$, which has integer coefficients.
The ghost map $a \mapsto (w_0(a), w_1(a), \ldots)$ is a [[ring homomorphism|0VTH8KPCG2]] $W(A) \to A^{\N}$, and it is an isomorphism when $p$ is a unit in $A$.
A ring homomorphism $f \colon A \to B$ induces $W(f) \colon W(A) \to W(B)$ by applying $f$ to each entry.

Example: $W(\F_p)$ is isomorphic to the ring $\Z_p$ of [[p-adic integers|V6TJAFZ4MD]].
For $p = 2$, compute $(1, 0, \ldots) + (1, 0, \ldots)$ in $W(\Z)$ through ghost components: $w_0 = 1 + 1 = 2$ and $w_1 = 1 + 1 = 2$.
So $a_0 = 2$ and $a_0^2 + 2 a_1 = 2$, which gives $a_1 = -1$.
Reducing modulo $2$, in $W(\F_2)$ the sum is $(0, 1, \ldots)$, which corresponds to $2 \in \Z_2$.

Non-example: the componentwise addition on $\F_2^{\N}$ gives $(1, 0, \ldots) + (1, 0, \ldots) = (0, 0, \ldots)$.
This is not the Witt sum, because it does not respect the ghost components $w_1$ over $\Z$.

The Teichmüller representative of $x \in A$ is $[x] = (x, 0, 0, \ldots)$, and it satisfies $[xy] = [x][y]$.
