---
tag: K91VB1DXPR
kind: definition
name: Banach analytic space
msc: [32K05, 46G20]
defines: TY7Y32MCH1
uses: [06GZ956657, E8N3EC0YH5, TB6TM6R4MD, 0S1FJ8VEX9, HXSZA44J5J]
sources:
  - url: https://en.wikipedia.org/wiki/Infinite-dimensional_holomorphy
---

## Definition

A *model* is a triple $(U, F, f)$ where $E$ and $F$ are complex [[Banach spaces|06GZ956657]], $U \subseteq E$ is open and $f \colon U \to F$ is a [[holomorphic map|E8N3EC0YH5]].
Its underlying space is $Z = f^{-1}(0)$ with the topology induced from $U$.
For each complex Banach space $G$, the model defines a [[sheaf|TB6TM6R4MD]] $\mathcal{H}_Z(G)$ on $Z$.
Its stalk at $z \in Z$ is a quotient of the space of germs at $z$ of holomorphic maps $g \colon U \to G$.
Let $L(F, G)$ be the Banach space of continuous linear maps $F \to G$.
One divides by the germs $x \mapsto \varphi(x)\bigl(f(x)\bigr)$, where $\varphi$ is a germ at $z$ of a holomorphic map $U \to L(F, G)$.
These sheaves are the holomorphic maps from $Z$ to $G$.

A *Banach analytic space* is a [[Hausdorff space|0S1FJ8VEX9]] $X$ with the following data and property.
For each complex Banach space $G$ there is a sheaf $\mathcal{H}_X(G)$ of complex vector spaces on $X$, depending functorially on $G$.
Its sections play the role of holomorphic maps to $G$.
Each point of $X$ has an open neighbourhood isomorphic to the underlying space of a model, compatibly with the sheaves $\mathcal{H}(G)$ for all $G$.

## Remarks

Example: if $E = \C^n$ and $F = \C^k$, then a model is a local model of a [[complex analytic space|HXSZA44J5J]], and the sheaf $\mathcal{H}_Z(\C)$ is its structure sheaf.
In this case $\mathcal{H}_Z(G)$ is determined by $\mathcal{H}_Z(\C)$, so complex analytic spaces are Banach analytic spaces.
Also every open subset $U$ of a complex Banach space is a Banach analytic space, given by the model $(U, \set{0}, 0)$.

Non-example: the triple $(\C, \C, f)$ with $f(z) = \bar{z}$ is not a model, because $f$ is not holomorphic.

The definition uses all Banach spaces $G$, not only $G = \C$.
When $F$ is infinite-dimensional, the map $f$ is not given by finitely many scalar equations, and scalar functions alone do not record the structure that $f$ defines.
The notion is due to Douady.
