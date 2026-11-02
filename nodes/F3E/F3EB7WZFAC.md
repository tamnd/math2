---
tag: F3EB7WZFAC
kind: conjecture
name: Quantum unique ergodicity conjecture
msc: [58J51, 81Q50, 11F72]
uses: [7CBT4SM83Y, F4NWZNTRMD, B8TYKV7AA1, 1X42JAA349, D9W79NKYZJ]
about: [B8TYKV7AA1]
sources:
  - url: https://en.wikipedia.org/wiki/Quantum_ergodicity
history:
  posed_by: "Zeév Rudnick and Peter Sarnak"
  first_stated: "1994"
---

## Statement

Let $M$ be a compact connected [[Riemannian manifold|7CBT4SM83Y]] without boundary and with negative [[sectional curvature|1X42JAA349]], with volume measure $dv$ and total volume $V$.
Let $(\varphi_j)$ be any sequence of $L^2$-normalised eigenfunctions of the [[Laplace–Beltrami operator|F4NWZNTRMD]] with eigenvalues $\lambda_j \to \infty$.
The conjecture says that for every continuous function $a$ on $M$
$$\lim_{j \to \infty} \int_M a \, \abs{\varphi_j}^2 \, dv = \frac{1}{V} \int_M a \, dv.$$
In its full form it says that the microlocal lifts of the measures $\abs{\varphi_j}^2 \, dv$ converge to the normalised Liouville measure on the unit cotangent bundle.

## Remarks

[[Quantum ergodicity|D9W79NKYZJ]] gives this convergence along a subsequence of density one; the conjecture asks that there be no exceptional subsequence at all.
The conjecture is open in general.
Lindenstrauss proved the analogue for compact arithmetic hyperbolic surfaces and joint eigenfunctions of the Laplacian and the Hecke operators.
Together with work of Soundararajan that rules out escape of mass, this also covers the modular surface.
Anantharaman proved that on compact manifolds with Anosov geodesic flow every quantum limit has positive entropy, so eigenfunctions cannot concentrate entirely on a closed geodesic.
For some ergodic billiards the analogue fails: Hassell proved that for almost every stadium-shaped billiard there are exceptional sequences of eigenfunctions.

## Explanations

### L1 human

On a negatively curved surface, a freely moving particle explores every region evenly.
The conjecture says that every high-frequency standing wave on such a surface also spreads its mass evenly, with no exceptions at all.
Quantum ergodicity already proves this for almost all waves; the conjecture removes the word "almost".
