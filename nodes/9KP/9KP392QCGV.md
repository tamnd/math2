---
tag: 9KP392QCGV
kind: definition
name: Distinguished triangle
msc: [18G80]
defines: ADKK56VZHW
uses: [T2V7GJJ2EN]
sources:
  - url: https://en.wikipedia.org/wiki/Triangulated_category
---

## Definition

Let $(\mathcal{T}, \Sigma)$ be a [[triangulated category|T2V7GJJ2EN]].
A *triangle* in $\mathcal{T}$ is a diagram $X \xrightarrow{u} Y \xrightarrow{v} Z \xrightarrow{w} \Sigma X$ of objects and morphisms of $\mathcal{T}$.
A *distinguished triangle*, or *exact triangle*, is a triangle in the class of distinguished triangles that is part of the structure of $\mathcal{T}$.

## Remarks

In a distinguished triangle, consecutive maps compose to zero: $v u = 0$, $w v = 0$ and $(\Sigma u) w = 0$.
For each object $W$, applying $\Hom(W, -)$ gives a long exact sequence $\cdots \to \Hom(W, X) \to \Hom(W, Y) \to \Hom(W, Z) \to \Hom(W, \Sigma X) \to \cdots$.
By TR1 and TR3, the third object $Z$ is determined by $u$ up to a non-unique isomorphism; it is called a cone of $u$.
Example: $X \xrightarrow{\id} X \to 0 \to \Sigma X$ is distinguished for every $X$, by the axiom TR1.
Non-example: if $X \ne 0$, then $X \to 0 \to 0 \to \Sigma X$ is not distinguished.
Indeed, the long exact sequence for $W = \Sigma X$ would give $\Hom(\Sigma X, 0) \to \Hom(\Sigma X, \Sigma X) \to \Hom(\Sigma X, \Sigma 0)$ exact, which forces $\Hom(\Sigma X, \Sigma X) = 0$, but $\id_{\Sigma X} \ne 0$.
In the homotopy category of complexes, the distinguished triangles are those isomorphic to $X \xrightarrow{f} Y \to \operatorname{Cone}(f) \to X[1]$ for a chain map $f$.
