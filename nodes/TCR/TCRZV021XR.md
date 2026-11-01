---
tag: TCRZV021XR
kind: definition
name: Cotangent space of a local ring
msc: [13H99, 14B05]
defines: Z1CGB483J6
uses: [MZ02BKPHJA, NJ3APQ8BHH, 000AYPA9AJ]
sources:
  - url: https://en.wikipedia.org/wiki/Zariski_tangent_space
---

## Definition

Let $(R, \mathfrak m)$ be a [[local ring|MZ02BKPHJA]] with [[residue field|NJ3APQ8BHH]] $k = R/\mathfrak m$.
The quotient $\mathfrak m / \mathfrak m^2$ is an $R$-module killed by $\mathfrak m$, hence a [[vector space|000AYPA9AJ]] over $k$ with $(a + \mathfrak m)(x + \mathfrak m^2) = ax + \mathfrak m^2$.
The *cotangent space* of $R$ is this $k$-vector space $\mathfrak m / \mathfrak m^2$.
Its dual $\Hom_k(\mathfrak m / \mathfrak m^2, k)$ is the *Zariski tangent space* of $R$.

## Remarks

The scalar multiplication is well defined because $\mathfrak m \cdot \mathfrak m \subseteq \mathfrak m^2$.

Example: let $k$ be a field and $R = k[x, y]_{(x, y)}$, the [[localization|X6JD4AG973]] of the polynomial ring at $(x, y)$.
Then $\mathfrak m = (x, y)R$ and $\mathfrak m / \mathfrak m^2$ has the basis given by the classes of $x$ and $y$, so it has dimension $2$.
For the cusp $R = k[x, y]_{(x, y)} / (y^2 - x^3)$, the classes of $x$ and $y$ still form a basis, because $y^2 - x^3 \in \mathfrak m^2$; the dimension is $2$ although the cusp is a curve.

Non-example: the quotient $\mathfrak m / \mathfrak m^3$ is in general not a vector space over $k$.
In $k[\![t]\!]$ with $\mathfrak m = (t)$, the element $t$ acts on $\mathfrak m / \mathfrak m^3$ by sending the class of $t$ to the nonzero class of $t^2$, so $\mathfrak m$ does not kill it.
