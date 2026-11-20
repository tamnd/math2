---
tag: ~fd9dfa32
kind: example
name: R³ modulo the plane x + y + z = 0 is a line
msc: ["15A04"]
topics: [QHKTJ89V6S]
audience: ug1
instance_of: [0BR3FY5Q8M]
illustrates: [0MTBGVZ4XJ]
uses: [0SVR29SV1V, 02YFME3RGW, 0JB228DCWB, 0XSJ25Z9M4]
sources:
  - url: https://en.wikipedia.org/wiki/Isomorphism_theorems
    locator: Theorem A (modules)
---

## Example

Let $f \colon \R^3 \to \R$ be $f(x, y, z) = x + y + z$, and let $U = \{(x, y, z) : x + y + z = 0\}$.
We apply the [[first isomorphism theorem|0MTBGVZ4XJ]] to $f$ and check each step.

1. $f$ is linear, with matrix $\begin{pmatrix} 1 & 1 & 1 \end{pmatrix}$.
2. The [[kernel|02YFME3RGW]] of $f$ is $U$, by definition of $U$.
3. The [[image|0JB228DCWB]] of $f$ is $\R$, since $f(t, 0, 0) = t$ for every $t$.
4. The theorem gives the map $\bar f \colon \R^3 / U \to \R$, $\bar f(v + U) = f(v)$, and it is an [[isomorphism|0XSJ25Z9M4]].
5. Well defined: $(1, 0, 0) + U = (0, 1, 0) + U$, since the difference $(1, -1, 0)$ lies in $U$. Both give $f = 1$.
6. Injective: $\bar f(v + U) = 0$ means $v \in U$, so $v + U$ is the zero coset.
7. Surjective: $\bar f((t, 0, 0) + U) = t$.

So the [[quotient space|0SVR29SV1V]] $\R^3 / U$ is a line, and its points are the parallel planes $x + y + z = c$, labelled by $c$.

## Remarks

The coset of $(x, y, z)$ is the plane through $(x, y, z)$ parallel to $U$.
The dimension count $\dim(\R^3 / U) = 3 - 2 = 1$ agrees with the [[dimension of a quotient|0SXDQ6TN00]].
The line $\R(1, 1, 1)$ is a complement of $U$, and it meets each plane $x + y + z = c$ in the single point $\tfrac{c}{3}(1, 1, 1)$.

## Explanations

### L1 human

The function $x + y + z$ is constant on each plane parallel to $U$.
So the planes are labelled by one number, and the space of planes is a line.

### L2 human

The isomorphism $\bar f$ turns the abstract quotient into the concrete line $\R$.
To add the planes $x + y + z = 2$ and $x + y + z = 5$, add any points on them: the sum lies on $x + y + z = 7$.
