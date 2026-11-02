---
tag: C2SRBS1CX3
kind: definition
name: Cohomology operation
msc: [55S05, 55S10]
defines: K8T15QHN3W
uses: [6N7BC70CX0, 0X3WGX95FE, 082GHNPJ53]
sources:
  - url: https://en.wikipedia.org/wiki/Cohomology_operation
---

## Definition

Let $G$ and $H$ be [[abelian groups|082GHNPJ53]] and let $n, m \ge 0$ be integers.
Write $H^n(X; G)$ for [[singular cohomology|6N7BC70CX0]] with coefficients in $G$.
A *cohomology operation* of type $(G, n; H, m)$ is a family of functions $\theta_X \colon H^n(X; G) \to H^m(X; H)$, one for each topological space $X$.
The family must be natural.
That is, $f^* \circ \theta_X = \theta_Y \circ f^*$ for every [[continuous map|0X3WGX95FE]] $f \colon Y \to X$.
Here $f^*$ denotes the induced maps in cohomology.

## Remarks

In the language of categories, a cohomology operation is a natural transformation between the functors $H^n(-; G)$ and $H^m(-; H)$ to sets.
The functions $\theta_X$ need not be homomorphisms.
Operations of type $(G, n; H, m)$ correspond bijectively to elements of $H^m(K(G, n); H)$, through $\theta \mapsto \theta(\iota_n)$, where $\iota_n \in H^n(K(G, n); G)$ is the fundamental class of the Eilenberg–MacLane space.

Example: the cup square $\theta_X(x) = x \smile x$ is an operation of type $(\Z, n; \Z, 2n)$.
The check: $f^*(x \smile x) = f^* x \smile f^* x$, because $f^*$ is a ring homomorphism.
It is not additive in general: $(x + y)^2 = x^2 + x y + y x + y^2$.

Non-example: on $H^0(-; \Z)$, let $\theta_X(x) = x$ if $X$ is path-connected and $\theta_X(x) = 0$ otherwise.
Take $X = \set{a, b}$ discrete, $Y$ a point, $f$ the map to $a$, and $x = (1, 1) \in H^0(X; \Z) \cong \Z^2$.
Then $f^* \theta_X(x) = 0$ but $\theta_Y(f^* x) = 1$, so the naturality condition fails.
