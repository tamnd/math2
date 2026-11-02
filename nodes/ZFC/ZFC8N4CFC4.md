---
tag: ZFC8N4CFC4
kind: definition
name: Dirac operator
msc: [58J60, 47F05, 15A66]
defines: 3DXGJTEQZH
uses: [7CBT4SM83Y, XY8GEQSWPR, 0E0B6RA8K0]
sources:
  - url: https://en.wikipedia.org/wiki/Dirac_operator
---

## Definition

Let $(M, g)$ be a [[Riemannian manifold|7CBT4SM83Y]] and let $E$ be a complex [[vector bundle|P4DZM975BV]] over $M$.
Let $D$ be a first-order linear differential operator acting on smooth sections of $E$.
In a local chart $x = (x_1, \ldots, x_n)$, let $(g^{jk}(x))$ be the inverse of the matrix of the metric $g$.
The operator $D$ is a *Dirac operator* if, in every local chart and every local trivialisation of $E$,
$$D^2 = -\sum_{j,k} g^{jk}(x)\frac{\partial^2}{\partial x_j \partial x_k} + (\text{terms of order at most } 1).$$

## Remarks

Equivalently, the principal symbol of $D^2$ is $\abs{\xi}^2_g$ times the identity, so $D^2$ is a generalised [[Laplacian|0E0B6RA8K0]].
It follows that $D$ is an [[elliptic operator|XY8GEQSWPR]].

Example: on $\R^n$ with the flat metric, let $\gamma_1, \ldots, \gamma_n$ be complex $N \times N$ matrices with $\gamma_j\gamma_k + \gamma_k\gamma_j = -2\delta_{jk} I$, and let $D = \sum_j \gamma_j \partial_j$ act on $\C^N$-valued functions.
Then $D^2 = \sum_{j,k}\gamma_j\gamma_k\partial_j\partial_k = \frac{1}{2}\sum_{j,k}(\gamma_j\gamma_k + \gamma_k\gamma_j)\partial_j\partial_k = -\sum_j \partial_j^2$, so $D$ is a Dirac operator.
For $n = 1$ and $\gamma_1 = -i$, this is $D = -i\, d/dx$.

Non-example: on $\R$, the operator $D = d/dx$ has $D^2 = +d^2/dx^2$, whose second-order term has the wrong sign.

On a spin manifold, the Atiyah–Singer Dirac operator acts on the [[spinor bundle|PYYQQKAZ0C]] through Clifford multiplication and the Levi-Civita connection.
