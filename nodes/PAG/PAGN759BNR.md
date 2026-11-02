---
tag: PAGN759BNR
kind: definition
name: Laplace–Beltrami operator
msc: [58J05, 53C20]
defines: F4NWZNTRMD
uses: [7CBT4SM83Y, CAZYGE1T4E, FZBA1HA9ZM]
sources:
  - url: https://en.wikipedia.org/wiki/Laplace%E2%80%93Beltrami_operator
---

## Definition

Let $(M, g)$ be a [[Riemannian manifold|7CBT4SM83Y]] with [[Levi-Civita connection|CAZYGE1T4E]] $\nabla$.
For a smooth function $f$ on $M$, the gradient $\operatorname{grad} f$ is the vector field with $g(\operatorname{grad} f, X) = df(X)$ for every vector field $X$.
For a vector field $Y$, the divergence $\operatorname{div} Y$ is the function $\tr(X \mapsto \nabla_X Y)$.
The *Laplace–Beltrami operator* is the operator $\Delta$ on smooth functions given by
$$\Delta f = \operatorname{div}(\operatorname{grad} f).$$

## Remarks

In local coordinates $x^1, \dots, x^n$, with $g_{ij}$ the metric, $g^{ij}$ its inverse and $\abs{g} = \det(g_{ij})$,
$$\Delta f = \frac{1}{\sqrt{\abs{g}}} \sum_{i,j} \partial_i \bigl(\sqrt{\abs{g}} \, g^{ij} \partial_j f\bigr).$$
Equivalently $\Delta f = \sum_{i,j} g^{ij} \bigl(\partial_i \partial_j f - \sum_k \Gamma^k_{ij} \partial_k f\bigr)$, with $\Gamma^k_{ij}$ the [[Christoffel symbols|FZBA1HA9ZM]].

Example: on the unit sphere $S^2$ with coordinates $(\theta, \varphi)$ and metric $d\theta^2 + \sin^2\theta \, d\varphi^2$, one has $\sqrt{\abs{g}} = \sin\theta$ and
$$\Delta f = \frac{1}{\sin\theta} \partial_\theta(\sin\theta \, \partial_\theta f) + \frac{1}{\sin^2\theta} \partial_\varphi^2 f.$$
For $f = \cos\theta$ this gives $\frac{1}{\sin\theta} \partial_\theta(-\sin^2\theta) = -2\cos\theta$.

Non-example: on $\R^2 \setminus \set{0}$ in polar coordinates $(r, \theta)$, the operator $\partial_r^2 + \partial_\theta^2$ is not the Laplace–Beltrami operator of the Euclidean metric $dr^2 + r^2 d\theta^2$.
The formula above gives $\Delta f = \partial_r^2 f + \frac{1}{r} \partial_r f + \frac{1}{r^2} \partial_\theta^2 f$.

With this sign convention $\Delta$ is the usual Laplacian $\sum_i \partial_i^2$ on $\R^n$ and $-\Delta$ has nonnegative spectrum on a compact manifold.
Many geometers use the opposite sign, $\Delta = -\operatorname{div} \operatorname{grad}$.
On functions, $-\Delta$ equals the Hodge Laplacian $\delta d$.
