---
tag: 45P2SEGGR1
kind: statement
role: theorem
name: Minakshisundaram–Pleijel asymptotic expansion
msc: [58J35, 58J50, 35K08]
uses: [327NP6S7H5, 7CBT4SM83Y, ZHX2VYQDZ3, B8TYKV7AA1]
about: [327NP6S7H5]
sources:
  - url: https://en.wikipedia.org/wiki/Minakshisundaram–Pleijel_zeta_function
---

## Statement

Let $(M, g)$ be a closed [[Riemannian manifold|7CBT4SM83Y]] of dimension $n$, and let $K(t, x, y)$ be its [[heat kernel|327NP6S7H5]].
Then there are smooth functions $a_0, a_1, a_2, \ldots$ on $M$ such that for every integer $N \ge 0$
$$K(t, x, x) = (4\pi t)^{-n/2} \left( \sum_{k = 0}^{N} a_k(x) \, t^k + O(t^{N+1}) \right) \quad \text{as } t \to 0^+,$$
uniformly in $x \in M$.
Each $a_k(x)$ is a universal polynomial in the curvature tensor and its covariant derivatives at $x$.
The first two are $a_0 = 1$ and $a_1 = \tfrac16 S$, where $S$ is the [[scalar curvature|ZHX2VYQDZ3]].
Integrating over $M$, the heat trace satisfies
$$\sum_{j \ge 0} e^{-t\lambda_j} \sim (4\pi t)^{-n/2} \sum_{k \ge 0} t^k \int_M a_k \, dv,$$
where $\lambda_0 \le \lambda_1 \le \cdots$ is the [[spectrum of the Laplace–Beltrami operator|B8TYKV7AA1]].

## Remarks

Idea of the proof: build an approximate heat kernel near the diagonal as the Euclidean Gaussian in normal coordinates times a power series $\sum u_k(x, y) t^k$.
The coefficients $u_k$ solve transport equations along geodesics, and $a_k(x) = u_k(x, x)$.
A Duhamel argument shows that the true heat kernel differs from the truncated approximation by $O(t^{N + 1 - n/2})$.
Consequences: the spectrum determines the dimension $n$, the volume $\int_M a_0 = \operatorname{vol}(M)$ and the total scalar curvature $\int_M S$.
The next integrated coefficient is $\int_M a_2 = \frac{1}{360} \int_M \left( 2\abs{\mathrm{Rm}}^2 - 2\abs{\mathrm{Ric}}^2 + 5 S^2 \right) dv$.
Example: on a flat torus $\R^n / \Gamma$, $K(t, x, x) = (4\pi t)^{-n/2} \sum_{\gamma \in \Gamma} e^{-\abs{\gamma}^2 / 4t}$, so $a_0 = 1$ and $a_k = 0$ for $k \ge 1$, with an exponentially small error.

## Explanations

### L1 human

For a very short time, heat spreading from a point only feels a tiny neighbourhood, which looks almost flat.
So the heat kernel at the point is close to the flat-space value $(4\pi t)^{-n/2}$.
The corrections come in powers of $t$, and each coefficient is computed from the curvature at the point.

### L2 human

Minakshisundaram and Pleijel used the expansion to continue the spectral zeta function of the Laplacian meromorphically.
It shows that the spectrum determines the volume and the total scalar curvature.
This answers some spectral rigidity questions.
For example, a closed surface with the spectrum of the round sphere is a round sphere.
The same construction works for Laplace-type operators on vector bundles, and the coefficients there are the Seeley–DeWitt coefficients.
Combined with the McKean–Singer formula it leads to the heat equation proof of the index theorem.
