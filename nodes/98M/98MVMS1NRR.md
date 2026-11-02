---
tag: 98MVMS1NRR
kind: statement
role: theorem
name: Thom–Sebastiani theorem
msc: [32S55, 32S40, 32S25]
uses: [VTGYEES3VS, KTFG1S2SMG, 1ZE51P7GRQ, NJQMWVK3QK, C8HD62AB6Q]
about: [KTFG1S2SMG, C8HD62AB6Q]
sources:
  - url: https://en.wikipedia.org/wiki/Milnor_number
---

## Statement

Let $f(x_0, \dots, x_n)$ and $g(y_0, \dots, y_m)$ be holomorphic functions near the origin, each with an [[isolated singularity|VTGYEES3VS]] at $0$.
Let $f \oplus g$ be the function $(x, y) \mapsto f(x) + g(y)$ near $0$ in $\C^{n+1} \times \C^{m+1}$; it also has an isolated singularity at $0$.
Let $F_f$, $F_g$ and $F_{f \oplus g}$ be the Milnor fibres of the [[Milnor fibrations|KTFG1S2SMG]] at $0$, with [[monodromies|C8HD62AB6Q]] $T_f$, $T_g$ and $T_{f \oplus g}$ on [[reduced homology|NJQMWVK3QK]].
Then there is an isomorphism
$$\tilde H_{n+m+1}(F_{f \oplus g}; \Z) \cong \tilde H_n(F_f; \Z) \otimes \tilde H_m(F_g; \Z)$$
under which $T_{f \oplus g} = T_f \otimes T_g$.

## Remarks

Sebastiani and Thom proved the theorem in 1971.
The idea is that $F_{f \oplus g}$ has the homotopy type of the join $F_f * F_g$.
The reduced homology of a join is the tensor product of the reduced homologies, shifted by one degree.
The monodromy of $f \oplus g$ is the join of the two monodromies.

Taking ranks gives $\mu(f \oplus g) = \mu(f) \, \mu(g)$ for the [[Milnor numbers|1ZE51P7GRQ]].
This also follows from algebra, since the local algebra of $f \oplus g$ is the tensor product of the local algebras of $f$ and $g$.

Example: $f(x) = x^p$ and $g(y) = y^q$.
The Milnor fibre of $x^p$ is $p$ points, cyclically permuted by the monodromy, whose eigenvalues on reduced $H_0$ are the $p$-th roots of unity other than $1$.
So the monodromy of $x^p + y^q$ on $H_1$ has as eigenvalues the products $\zeta \eta$ with $\zeta^p = 1 \ne \zeta$ and $\eta^q = 1 \ne \eta$, and $\mu(x^p + y^q) = (p-1)(q-1)$.

## Explanations

### L1 human

If a function is a sum of two functions in separate sets of variables, its singularity is built from the two singularities.
The theorem says how: the topology of the sum is a product, in a precise sense, of the topologies of the summands.
For instance, the Milnor number of the sum is the product of the two Milnor numbers.

### L2 human

The theorem reduces many computations to one-variable functions.
Iterating it, for a Brieskorn–Pham polynomial $z_0^{a_0} + \cdots + z_n^{a_n}$, the monodromy is diagonalizable with eigenvalues $\zeta_0 \cdots \zeta_n$, where $\zeta_j^{a_j} = 1 \ne \zeta_j$, and $\mu = \prod_j (a_j - 1)$.
This is the computation behind the topology of [[Brieskorn manifolds|5E9E5R9RYZ]].
Adding a square $z^2$ in a new variable does not change $\mu$, and it changes the monodromy only by a sign.
This explains the stable behaviour of singularities under adding squares.
