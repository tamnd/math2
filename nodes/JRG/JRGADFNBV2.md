---
tag: JRGADFNBV2
kind: statement
role: theorem
name: Cheeger's inequality for the first eigenvalue
msc: [58J50, 35P15, 53C21]
uses: [7CBT4SM83Y, F4NWZNTRMD, B8TYKV7AA1]
about: [B8TYKV7AA1]
sources:
  - url: https://en.wikipedia.org/wiki/Cheeger_constant
---

## Statement

Let $M$ be a compact connected [[Riemannian manifold|7CBT4SM83Y]] without boundary, of dimension $n \ge 2$.
Consider the compact smooth hypersurfaces $\Sigma$ that divide $M$ into two disjoint open sets $A$ and $B$ with $M = A \cup \Sigma \cup B$.
Let $\operatorname{area}(\Sigma)$ be the $(n-1)$-dimensional volume of $\Sigma$.
The *Cheeger constant* of $M$ is
$$h(M) = \inf_{\Sigma} \frac{\operatorname{area}(\Sigma)}{\min(\operatorname{vol}(A), \operatorname{vol}(B))}.$$
Let $\lambda_1$ be the smallest nonzero eigenvalue of the [[Laplace–Beltrami operator|F4NWZNTRMD]] of $M$.
Then
$$\lambda_1 \ge \frac{h(M)^2}{4}.$$

## Remarks

The proof starts from the variational characterisation of $\lambda_1$ as the infimum of $\int_M \abs{\nabla f}^2 / \int_M f^2$ over nonzero smooth functions $f$ with $\int_M f = 0$.
One applies the coarea formula to $g^2$, where $g$ is the positive part of an eigenfunction shifted so that its support has at most half the volume.
The bound from $h(M)$ on each level set, together with the Cauchy–Schwarz inequality, gives the factor $1/4$.
The inequality shows that a small $\lambda_1$ forces a small Cheeger constant, that is, a narrow bottleneck.
A dumbbell, two round spheres joined by a thin tube, has a small Cheeger constant and also a small $\lambda_1$.
The reverse bound needs more hypotheses: Buser proved an upper bound for $\lambda_1$ in terms of $h(M)$ under a lower bound on the Ricci curvature.
The [[Cheeger constant of a graph|Y7S6W12N64]] satisfies a discrete analogue of the inequality.

## Explanations

### L1 human

The Cheeger constant measures the narrowest bottleneck of a shape: the smallest cut that splits it into two big pieces.
The first eigenvalue measures how fast heat evens out over the shape.
Cheeger's inequality says that a shape without narrow bottlenecks must have a large first eigenvalue.
So geometry, the size of cuts, controls analysis, the rate of mixing.

### L2 human

The inequality gives a lower bound on $\lambda_1$ from purely geometric data, without assumptions on curvature.
Its discrete version for graphs is a basic tool for expander graphs, where the spectral gap and the edge expansion control each other.
It complements curvature bounds such as the [[Lichnerowicz–Obata theorem|TK1PT9FDV0]], which need a positive lower bound on the Ricci curvature.
