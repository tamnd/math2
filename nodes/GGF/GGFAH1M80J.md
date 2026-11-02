---
tag: GGFAH1M80J
kind: statement
role: theorem
name: Atiyah–Patodi–Singer index theorem
msc: [58J20, 58J28, 58J32]
uses: [7DS6B2BFK8, 7CBT4SM83Y, MT9P2X85V8, 44GBFZ16SG, PRJCH788AM, TEG1ZX1AGJ]
about: [44GBFZ16SG, PRJCH788AM]
sources:
  - url: https://en.wikipedia.org/wiki/Eta_invariant
---

## Statement

Let $M$ be a compact oriented Riemannian [[manifold with boundary|7DS6B2BFK8]] $Y = \partial M$, whose metric is a product $du^2 + g_Y$ on a collar $[0, 1) \times Y$ of the boundary.
Let $D \colon C^\infty(M; E) \to C^\infty(M; F)$ be a first-order [[elliptic operator|MT9P2X85V8]].
Assume that on the collar it has the form
$$D = \sigma \left( \frac{\partial}{\partial u} + A \right).$$
Here $\sigma \colon E|_Y \to F|_Y$ is a bundle isomorphism and $A$ is a self-adjoint elliptic operator on $Y$, both independent of $u$.
Impose the boundary condition $P_{\ge 0}(s|_Y) = 0$, where $P_{\ge 0}$ is the spectral projection of $A$ onto the span of its eigenvectors with eigenvalue $\ge 0$.
Then $D$ with this boundary condition is Fredholm, and its [[index|44GBFZ16SG]] is
$$\operatorname{ind} D = \int_M \alpha_0 - \frac{h + \eta_A(0)}{2}.$$
Here $\alpha_0$ is the local index density of $D$, the same density as for closed manifolds.
Also $h = \dim \ker A$, and $\eta_A(0)$ is the [[eta invariant|PRJCH788AM]] of $A$.

## Remarks

Idea of the proof: glue the half-infinite cylinder $(-\infty, 0] \times Y$ to $M$ along $Y$.
The boundary condition corresponds to $L^2$ solutions on the elongated manifold, and on the cylinder the heat kernel is computed exactly by separation of variables, which produces the eta invariant.
For operators such as the signature operator there is no elliptic local boundary condition, which is why a global spectral projection is used.
Example: for the signature operator on a $4k$-manifold with boundary, the theorem gives
$$\sigma(M) = \int_M L(p) - \eta(0).$$
Here $L(p)$ is the Hirzebruch $L$-form of the metric, and $\eta(0)$ is the eta invariant of an operator on the even forms of $Y$.
So the [[Hirzebruch signature theorem|TEG1ZX1AGJ]] fails on manifolds with boundary, and the eta invariant measures the defect.

## Explanations

### L1 human

On a closed manifold the index of an elliptic operator is an integral of a curvature expression.
On a manifold with boundary this integral is usually not an integer, so a correction from the boundary is needed.
The correction is the eta invariant, which measures how asymmetric the spectrum of the boundary operator is between positive and negative eigenvalues.

### L2 human

The theorem extends the Atiyah–Singer index theorem to manifolds with boundary.
It introduced the eta invariant into geometry, with uses for the signature defects of $3$-manifolds, for Chern–Simons invariants and for spectral flow.
