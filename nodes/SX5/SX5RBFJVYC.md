---
tag: SX5RBFJVYC
kind: definition
name: Alexander–Spanier cohomology
msc: [55N05, 55N30]
defines: MGE14ST1YP
uses: [0CQHFPGJ45, 082GHNPJ53, 02BH3MCBQB]
sources:
  - url: https://en.wikipedia.org/wiki/Alexander–Spanier_cohomology
---

## Definition

Let $X$ be a [[topological space|0CQHFPGJ45]] and let $G$ be an [[abelian group|082GHNPJ53]].
For $q \ge 0$, let $C^q(X; G)$ be the group of all functions $f \colon X^{q+1} \to G$.
The coboundary $\delta \colon C^q(X; G) \to C^{q+1}(X; G)$ is
$$(\delta f)(x_0, \ldots, x_{q+1}) = \sum_{i=0}^{q+1} (-1)^i f(x_0, \ldots, \widehat{x_i}, \ldots, x_{q+1}),$$
where the hat means that $x_i$ is left out.
Then $\delta \circ \delta = 0$, so $C^\bullet(X; G)$ is a cochain complex.

A function $f \in C^q(X; G)$ is *locally zero* if there is an open cover $\mathcal{U}$ of $X$ with the following property.
If the points $x_0, \ldots, x_q$ all lie in one member of $\mathcal{U}$, then $f(x_0, \ldots, x_q) = 0$.
The locally zero functions form a subcomplex $C^\bullet_0(X; G)$, because $\delta$ maps locally zero functions to locally zero functions.
Let $\bar{C}^\bullet(X; G) = C^\bullet(X; G) / C^\bullet_0(X; G)$.
The *Alexander–Spanier cohomology* of $X$ with coefficients in $G$ is the cohomology of this cochain complex:
$$\bar{H}^q(X; G) = H^q(\bar{C}^\bullet(X; G)).$$

## Remarks

Example: let $X$ be a single point.
Then $C^q(X; G) \cong G$ for every $q$, and no nonzero function is locally zero.
The coboundary $C^q \to C^{q+1}$ is multiplication by $\sum_{i=0}^{q+1} (-1)^i$, which is $0$ for even $q$ and $1$ for odd $q$.
So $\bar{H}^0(X; G) \cong G$ and $\bar{H}^q(X; G) = 0$ for $q > 0$.

Non-example: a function on $X^{q+1}$ that is nonzero at some diagonal point $(x, \ldots, x)$ is not locally zero, since every cover has a member that contains $x$.

There is a relative version for a pair $(X, A)$ and a version with compact supports.
On paracompact Hausdorff spaces, $\bar{H}^q(X; G)$ is isomorphic to Čech cohomology and to the sheaf cohomology of $X$ with coefficients in the constant sheaf $G$.
