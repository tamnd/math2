---
tag: ZZFTPP8JTG
kind: definition
name: Inverse mean curvature flow
msc: ["53E10", "53C21"]
defines: 5XVEF5DKAG
uses: [PA78NFEPCF, 7CBT4SM83Y]
sources:
  - url: https://en.wikipedia.org/wiki/Inverse_mean_curvature_flow
---

## Definition

Let $(N, g)$ be a [[Riemannian manifold|7CBT4SM83Y]] of dimension $n + 1$, let $M$ be a closed manifold of dimension $n$, and let $T > 0$.
A family of immersions $F \colon M \times [0, T) \to N$ is a solution of *inverse mean curvature flow* if for every $t \in [0, T)$:

1. the hypersurface $M_t = F(M, t)$ has an outward unit normal $\nu(\cdot, t)$;
2. the [[mean curvature|PA78NFEPCF]] $H(\cdot, t)$ of $M_t$ with respect to $\nu$, the sum of the principal curvatures, is positive everywhere;
3. for all $x \in M$,
$$\frac{\partial F}{\partial t}(x, t) = \frac{1}{H(x, t)}\, \nu(x, t).$$

## Remarks

Example: in $N = \R^{n+1}$ take $M_t$ the sphere of radius $r(t) = r_0 e^{t/n}$ about the origin.
Its mean curvature is $H = n/r$, so the speed required by clause 3 is $r/n$, and indeed $r'(t) = r(t)/n$.
Its area is $e^t$ times the area of $M_0$.
Non-example: a hypersurface with a point where $H \le 0$ fails clause 2, and the flow cannot start from it.
A torus of revolution in $\R^3$ with tube radius $r$ and center circle of radius $R < 2r$ has such points on its inner circle.
Under the flow the area element is multiplied by $e^t$ in general, since its time derivative is $H \cdot (1/H) = 1$ times itself.
