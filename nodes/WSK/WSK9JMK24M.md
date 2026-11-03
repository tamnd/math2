---
tag: WSK9JMK24M
kind: definition
name: Pfister form
msc: ["11E81", "11E04"]
defines: 7HMTK6P4W7
uses: [0RBQS1JJCR, 0F6ES3BRYP, ZWXW0T3EAC]
sources:
  - url: https://en.wikipedia.org/wiki/Pfister_form
---

## Definition

Let $F$ be a field whose [[characteristic|0F6ES3BRYP]] is not $2$.
For $b_1, \ldots, b_m \in F^\times$, write $\langle b_1, \ldots, b_m \rangle$ for the diagonal [[quadratic form|0RBQS1JJCR]] $b_1 x_1^2 + \cdots + b_m x_m^2$.
For $a_1, \ldots, a_n \in F^\times$, the *$n$-fold Pfister form* is the tensor product
$$\langle\langle a_1, \ldots, a_n \rangle\rangle = \langle 1, -a_1 \rangle \otimes \cdots \otimes \langle 1, -a_n \rangle.$$
A *Pfister form* is a quadratic form isometric to $\langle\langle a_1, \ldots, a_n \rangle\rangle$ for some $n \ge 0$ and some $a_1, \ldots, a_n \in F^\times$.
The $0$-fold Pfister form is $\langle 1 \rangle$.

## Remarks

The form $\langle\langle a_1, \ldots, a_n \rangle\rangle$ is the diagonal form whose $2^n$ coefficients are the products $\prod_{i \in S} (-a_i)$ over all subsets $S \subseteq \set{1, \ldots, n}$.
Example: $\langle\langle a, b \rangle\rangle = \langle 1, -a, -b, ab \rangle$, the norm form of the [[quaternion algebra|ZWXW0T3EAC]] $(a, b)_F$.
For $a = b = -1$ this is $x_1^2 + x_2^2 + x_3^2 + x_4^2$.
Non-example: $\langle 1, 1, 1 \rangle$ is not a Pfister form, since every Pfister form has dimension a power of $2$.
A Pfister form is either anisotropic or hyperbolic.
Its nonzero values form a subgroup of $F^\times$, and they are exactly its similarity factors.
Some authors, such as Lam, write $\langle\langle a \rangle\rangle$ for $\langle 1, a \rangle$ instead of $\langle 1, -a \rangle$.
