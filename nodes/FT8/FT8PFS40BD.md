---
tag: FT8PFS40BD
kind: definition
name: NK groups
msc: [19D35]
defines: TV0GX7AQWT
uses: [0B1261B5ED, 5GVFZWMWC8, 0SDC934R52, 0W88CEGQP1]
sources:
  - url: https://en.wikipedia.org/wiki/Fundamental_theorem_of_algebraic_K-theory
---

## Definition

Let $R$ be a [[ring|0B1261B5ED]] with identity, and let $R[t]$ be the [[polynomial ring|0SDC934R52]] in one variable.
Let $n$ be an integer for which the [[K-group|5GVFZWMWC8]] $K_n$ is defined.
Let $\varepsilon \colon R[t] \to R$ be the ring homomorphism with $\varepsilon(t) = 0$ that is the identity on $R$.
The group $NK_n(R)$ is the [[kernel|0W88CEGQP1]] of the induced homomorphism
$$\varepsilon_* \colon K_n(R[t]) \to K_n(R).$$

## Remarks

The inclusion $R \to R[t]$ followed by $\varepsilon$ is the identity of $R$.
So $K_n(R)$ is a direct summand of $K_n(R[t])$, and
$$K_n(R[t]) \cong K_n(R) \oplus NK_n(R).$$
The construction is a functor of $R$.

Example: let $k$ be a field and $R = k[\varepsilon]/(\varepsilon^2)$.
The element $u = 1 + \varepsilon t$ is a unit of the commutative ring $R[t]$, with inverse $1 - \varepsilon t$.
The determinant $K_1(R[t]) \to R[t]^\times$ sends the class of $u$ to $u \ne 1$, so the class is not zero.
Since $\varepsilon_*(u) = 1$, the class of $u$ is a nonzero element of $NK_1(R)$.

Non-example: for a regular Noetherian ring $R$, such as a field or $\Z$, the map $\varepsilon_*$ is an isomorphism, so $NK_n(R) = 0$ for all $n$.
Then $K_n(R[t])$ has no part outside $K_n(R)$.

Some authors write $N K_n(R)$ as the cokernel of $K_n(R) \to K_n(R[t])$; it is isomorphic to the kernel above by the splitting.
