---
tag: D9W79NKYZJ
kind: statement
role: theorem
name: Quantum ergodicity
msc: [58J51, 81Q50, 37D40]
uses: [7CBT4SM83Y, F4NWZNTRMD, B8TYKV7AA1, VF43FTDA1H, AZRPHS478B]
about: [B8TYKV7AA1]
sources:
  - url: https://en.wikipedia.org/wiki/Quantum_ergodicity
same_as:
  wikidata: Q7269044
  wikipedia: Quantum ergodicity
---

## Statement

Let $M$ be a compact connected [[Riemannian manifold|7CBT4SM83Y]] without boundary, with volume measure $dv$ and total volume $V$.
Assume that the [[geodesic flow|VF43FTDA1H]] on the unit cotangent bundle $S^*M$ is [[ergodic|AZRPHS478B]] for the Liouville measure.
Let $(\varphi_j)_{j \ge 0}$ be an orthonormal basis of $L^2(M)$ of real eigenfunctions of the [[Laplace–Beltrami operator|F4NWZNTRMD]], with eigenvalues $\lambda_0 \le \lambda_1 \le \lambda_2 \le \cdots$.
Then there is a set $S \subseteq \N$ of density one, that is, with $\abs{S \cap \set{0, \ldots, N}} / (N + 1) \to 1$ as $N \to \infty$, such that for every continuous function $a$ on $M$
$$\lim_{j \to \infty, \ j \in S} \int_M a \, \varphi_j^2 \, dv = \frac{1}{V} \int_M a \, dv.$$

## Remarks

The full theorem is stated in phase space.
Let $A$ be a pseudodifferential operator of order $0$ with principal symbol $\sigma_A$, and let $\bar{\sigma}_A$ be the average of $\sigma_A$ over $S^*M$ for the normalised Liouville measure.
Then $\ip{A \varphi_j}{\varphi_j}$ tends to $\bar{\sigma}_A$ as $j \to \infty$ in $S$.
The version above is the case of multiplication operators.
The proof combines Egorov's theorem, which relates the quantum evolution to the geodesic flow, with the local [[Weyl law|2JK9YMZV2B]] and the mean ergodic theorem.
These give that the variance $\frac{1}{N} \sum_{j < N} \abs{\ip{A \varphi_j}{\varphi_j} - \bar{\sigma}_A}^2$ over the first $N$ eigenfunctions tends to $0$ as $N \to \infty$, which yields a density-one subsequence.
The result is due to Shnirelman, Zelditch and Colin de Verdière.
The ergodicity hypothesis is needed: on the round sphere $S^2$ the geodesic flow is not ergodic, and there are orthonormal bases of eigenfunctions for which the conclusion fails.
For example, the normalised real parts of $(x_1 + i x_2)^k$ restricted to $S^2$ are eigenfunctions whose mass concentrates on the equator $x_3 = 0$ as $k \to \infty$.
Whether the whole sequence converges, with no exceptional subsequence, is the [[quantum unique ergodicity conjecture|F3EB7WZFAC]].

## Explanations

### L1 human

Eigenfunctions of the Laplacian are the standing waves of a manifold.
If a particle sliding freely along geodesics explores the whole manifold evenly, then almost all high-frequency standing waves also spread their mass evenly.
This is the meaning of quantum ergodicity: classical chaos forces the quantum waves to equidistribute.
The words "almost all" matter, since the theorem allows a thin set of exceptions.

### L2 human

The theorem is the basic bridge between the dynamics of the geodesic flow and the spectral theory of the Laplacian.
It is a statement about averages, proved by a variance estimate, and so it cannot rule out a sparse subsequence of eigenfunctions that concentrates.
Negatively curved compact manifolds satisfy the hypothesis, since their geodesic flows are ergodic.
Possible limits of the measures $\varphi_j^2 \, dv$ along subsequences are called quantum limits, and much later work studies which measures can occur.
