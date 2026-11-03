---
tag: CTQ0V4WKHN
kind: definition
name: Cartan connection
msc: [53C05, 53B15]
defines: QPR7DCHXPG
uses: [8E37E74XVP]
sources:
  - url: https://en.wikipedia.org/wiki/Cartan_connection
---

## Definition

Let $G$ be a [[Lie group|7JBRGCVJRB]] and $H$ a closed [[subgroup|NM8XCPS1Q3]] of $G$, with [[Lie algebras|WKVBS76432]] $\mathfrak{h} \subset \mathfrak{g}$.
Let $M$ be a smooth manifold with $\dim M = \dim G - \dim H$.
A *Cartan connection on $M$ modelled on $(G, H)$* is a [[principal $H$-bundle|8E37E74XVP]] $\pi : P \to M$ together with a smooth $\mathfrak{g}$-valued $1$-form $\omega$ on $P$ such that:

1. $\omega_u : T_uP \to \mathfrak{g}$ is a linear isomorphism for every $u \in P$.
2. $R_h^* \omega = \mathrm{Ad}(h^{-1}) \, \omega$ for every $h \in H$, where $\mathrm{Ad}$ is the [[adjoint representation|P6ZP0TE07M]] of $G$ restricted to $H$.
3. $\omega(X^\#) = X$ for every $X \in \mathfrak{h}$, where $X^\#$ is the fundamental vector field of $X$ on $P$.

## Remarks

The *curvature* of $\omega$ is $\Omega = d\omega + \frac12 [\omega \wedge \omega]$.
Example: the model itself, $P = G \to G/H$ with the left [[Maurer–Cartan form|P1JVA39H5E]] $\omega = \theta$ of $G$.
Clause 1 holds because $\theta_g = dL_{g^{-1}}$ is an isomorphism $T_gG \to \mathfrak{g}$, and clauses 2 and 3 are standard properties of $\theta$.
Its curvature vanishes by the Maurer–Cartan equation, and a Cartan connection is locally isomorphic to this model exactly when $\Omega = 0$.
Non-example: a principal connection form on $P$ has values in $\mathfrak{h}$, so it fails clause 1 unless $\mathfrak{h} = \mathfrak{g}$ and $M$ is a point.
For $G$ the Euclidean group $\R^n \rtimes \mathrm{O}(n)$ and $H = \mathrm{O}(n)$, a torsion-free Cartan connection is the same as a Riemannian metric.
