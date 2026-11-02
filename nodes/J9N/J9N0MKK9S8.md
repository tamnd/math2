---
tag: J9N0MKK9S8
kind: definition
name: Directly indecomposable algebra
msc: [08B25, 08A05]
defines: 6B1PSZ42MC
uses: [QJGPT2W0FT, WJ73XYBNE4, 6N268PHKQA]
sources:
  - url: https://en.wikipedia.org/wiki/Direct_product
---

## Definition

Let $\mathbf{A}$ be an [[algebra|QJGPT2W0FT]] whose universe has at least two elements.
The algebra $\mathbf{A}$ is *directly indecomposable* when it is not isomorphic to any [[direct product|WJ73XYBNE4]] $\mathbf{B} \times \mathbf{C}$.
Here $\mathbf{B}$ and $\mathbf{C}$ range over algebras of the same signature with at least two elements each.

## Remarks

Equivalently, the only [[factor congruences|6N268PHKQA]] of $\mathbf{A}$ are $\Delta_A$ and $\nabla_A$.
Every finite algebra is isomorphic to a direct product of finitely many directly indecomposable algebras, by induction on the number of elements.

Example: an algebra $\mathbf{A}$ with a prime number $p$ of elements is directly indecomposable.
If $\mathbf{A} \cong \mathbf{B} \times \mathbf{C}$, then $p = \abs{B} \cdot \abs{C}$, so $\abs{B} = 1$ or $\abs{C} = 1$.

Non-example: the group $\Z/6\Z$ is not directly indecomposable.
The map $k \mapsto (k \bmod 2, k \bmod 3)$ is an isomorphism onto $\Z/2\Z \times \Z/3\Z$, and both factors have at least two elements.

Every subdirectly irreducible algebra is directly indecomposable, but not conversely: the ring $\Z$ is directly indecomposable and not subdirectly irreducible.
