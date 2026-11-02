---
tag: KH59BQZKCY
kind: definition
name: Orbifold
msc: [57R18, 57M60]
defines: RPAVY0W0XS
uses: [0MXB4CKHFW, 00RE1R4W7N, 0YSE802YCQ, 0B0WE1GKTK, 0V8046R0P9, 05GZ11PWRY, 0HV9Y7WG5R, R2TQ82PCNB]
sources:
  - url: https://en.wikipedia.org/wiki/Orbifold
---

## Definition

Let $n \ge 0$ be an integer and let $X$ be a [[Hausdorff|0MXB4CKHFW]] and [[second-countable|00RE1R4W7N]] topological space.
An *orbifold chart* of dimension $n$ on an open set $U \subseteq X$ is a triple $(\tilde U, G, \varphi)$ with these parts.
The set $\tilde U$ is a connected open subset of $\R^n$.
The group $G$ is finite and has a [[faithful|0B0WE1GKTK]] [[action|0YSE802YCQ]] on $\tilde U$ by diffeomorphisms.
The map $\varphi \colon \tilde U \to U$ is continuous, and $\varphi(g x) = \varphi(x)$ for all $g \in G$ and $x \in \tilde U$.
The induced map from the [[quotient space|0V8046R0P9]] $\tilde U / G$ to $U$ is a [[homeomorphism|05GZ11PWRY]].
An *embedding* of a chart $(\tilde U_i, G_i, \varphi_i)$ into a chart $(\tilde U_j, G_j, \varphi_j)$ is a smooth embedding $\psi \colon \tilde U_i \to \tilde U_j$ with $\varphi_j \circ \psi = \varphi_i$.
An *orbifold atlas* of dimension $n$ on $X$ is a family of charts $(\tilde U_i, G_i, \varphi_i)$ with these properties:

1. The sets $U_i = \varphi_i(\tilde U_i)$ cover $X$.
2. For any two charts and any point $x \in U_i \cap U_j$, there is a chart $(\tilde U_k, G_k, \varphi_k)$ of the atlas with $x \in U_k \subseteq U_i \cap U_j$.
3. Whenever $U_i \subseteq U_j$, there is an embedding of the chart $(\tilde U_i, G_i, \varphi_i)$ into the chart $(\tilde U_j, G_j, \varphi_j)$.

An atlas $\mathcal V$ *refines* an atlas $\mathcal U$ if every chart of $\mathcal V$ has an embedding into some chart of $\mathcal U$.
Two atlases are equivalent if they have a common refinement.
An $n$-dimensional *orbifold* is a space $X$ as above together with an equivalence class of $n$-dimensional orbifold atlases.

## Remarks

An embedding $\psi$ of charts induces an injective [[group homomorphism|0HV9Y7WG5R]] $f \colon G_i \to G_j$ with $\psi(g x) = f(g) \psi(x)$ for all $g \in G_i$ and $x \in \tilde U_i$.
Let $x = \varphi(\tilde x)$ for a chart $(\tilde U, G, \varphi)$.
Up to isomorphism, the stabilizer of $\tilde x$ in $G$ does not depend on the chart; it is the *local group* of $x$.
The point $x$ is *singular* when its local group is not trivial.
Example: let $m \ge 2$ and let $G = \Z / m\Z$ act on $\R^2$ by rotations through multiples of $2\pi / m$.
The quotient $X = \R^2 / G$ is Hausdorff and second countable.
The single chart $(\R^2, G, \varphi)$, with the quotient map $\varphi$, is an atlas: clauses 2 and 3 only ask for the chart itself.
So $X$ is an orbifold, the cone with one cone point of order $m$.
Non-example: let the group $\Q$ act on $\R$ by translations.
Every orbit is dense, so the quotient $\R / \Q$ carries the trivial topology and is not Hausdorff; it is not an orbifold.
A [[smooth manifold|R2TQ82PCNB]] is an orbifold all of whose local groups are trivial.
