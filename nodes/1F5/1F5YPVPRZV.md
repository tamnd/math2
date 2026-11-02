---
tag: 1F5YPVPRZV
kind: definition
name: Equivariant cohomology
msc: [55N91, 55N25]
defines: C7MZ3SFGYF
uses: [0WCY42EV9V, 1HDH716Z24, WSZ40H5E4T, 6N7BC70CX0]
sources:
  - url: https://en.wikipedia.org/wiki/Equivariant_cohomology
---

## Definition

Let $G$ be a topological group and let $X$ be a space with a continuous left [[action|0WCY42EV9V]] of $G$.
Let $EG \to BG$ be a [[universal principal $G$-bundle|1HDH716Z24]]: $EG$ is a contractible space with a free right action of $G$, and $BG = EG / G$ is the [[classifying space|WSZ40H5E4T]].
The *Borel construction* (or homotopy quotient) is
$$X_G = EG \times_G X = (EG \times X) / \sim, \qquad (e g, x) \sim (e, g x) \text{ for } g \in G.$$
For a commutative ring $R$, the *equivariant cohomology* of $X$ is
$$H^\ast_G(X; R) = H^\ast(X_G; R),$$
the [[singular cohomology|6N7BC70CX0]] of the Borel construction.

## Remarks

Up to isomorphism, $H^\ast_G(X; R)$ does not depend on the choice of $EG$.
The projection $X_G \to BG$ makes $H^\ast_G(X; R)$ an algebra over $H^\ast(BG; R) = H^\ast_G(\mathrm{pt}; R)$.

Example: let $G = S^1$ act on a point.
One can take $EG = S^\infty$, the unit sphere in $\C^\infty$, so $X_G = BS^1 = \C P^\infty$ and $H^\ast_{S^1}(\mathrm{pt}; \Z) \cong \Z[u]$ with $u$ of degree $2$.

Non-example: the ordinary cohomology of the orbit space $X / G$ is not the equivariant cohomology in general.
For $S^1$ acting on a point, $X / G$ is a point with cohomology $\Z$ in degree $0$ only, unlike $\Z[u]$.
If $G$ is a compact Lie group acting freely on $X$, then the map $X_G \to X/G$ is a fibration with contractible fibre $EG$, and $H^\ast_G(X; R) \cong H^\ast(X/G; R)$.
