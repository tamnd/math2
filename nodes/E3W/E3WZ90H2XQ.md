---
tag: E3WZ90H2XQ
kind: problem
name: H-infinity control
msc: [93B36, 93B35, 93C05]
uses: [QVREFP7BH7, 86JKV3TRFD, 6J9MPVHSMF]
about: [QVREFP7BH7, 5MGHZRFCVR]
sources:
  - url: https://en.wikipedia.org/wiki/H-infinity_methods_in_control_theory
same_as:
  wikidata: Q1293742
  wikipedia: H-infinity methods in control theory
history:
  posed_by: "George Zames"
  first_stated: "1981"
---

## Problem

Let $P$ be the proper real-rational [[transfer function|86JKV3TRFD]] matrix of a finite-dimensional [[linear time-invariant system|6J9MPVHSMF]], the *generalized plant*.
Its inputs are the exogenous input $w$ and the control input $u$.
Its outputs are the error output $z$ and the measured output $y$:
$$\begin{pmatrix} z \\ y \end{pmatrix} = \begin{pmatrix} P_{11} & P_{12} \\ P_{21} & P_{22} \end{pmatrix} \begin{pmatrix} w \\ u \end{pmatrix}.$$
For a proper real-rational controller $u = K y$, the closed-loop transfer function from $w$ to $z$ is
$$F_\ell(P, K) = P_{11} + P_{12} K (I - P_{22} K)^{-1} P_{21}.$$
The *H-infinity control problem* asks for an internally stabilizing controller $K$ that minimizes the [[H-infinity norm|QVREFP7BH7]] $\norm{F_\ell(P, K)}_\infty$.
The *suboptimal* version asks, for a given $\gamma > 0$, whether some internally stabilizing $K$ gives $\norm{F_\ell(P, K)}_\infty < \gamma$, and for such a $K$ if it exists.

## Remarks

The problem is solved for finite-dimensional linear time-invariant plants.
In 1989 Doyle, Glover, Khargonekar and Francis gave a state-space solution of the suboptimal problem.
Assume standard conditions on a state-space realization of $P$.
Then a suitable $K$ exists if and only if two algebraic Riccati equations have stabilizing positive semidefinite solutions $X$ and $Y$ with spectral radius $\rho(X Y) < \gamma^2$.
In that case an explicit formula gives a controller of the same order as $P$.
The optimal value is approached by decreasing $\gamma$, for example by bisection.
Choosing $z$ as weighted sensitivity and complementary sensitivity turns performance and [[robust control|5MGHZRFCVR]] goals into one bound on the H-infinity norm.
By the [[small-gain theorem|1CF728E75M]], the bound guarantees stability for all stable perturbations of norm at most $1/\gamma$ closing the loop from $z$ back to $w$.
Zames posed the problem in 1981 in the form of minimizing a weighted sensitivity.

## Explanations

### L1 human

A controller must keep working when disturbances of unknown shape hit the system.
The H-infinity problem asks for the controller that minimizes the worst-case amplification from disturbances to errors, over all possible disturbance signals of given energy.
Its answer is a controller that is guaranteed to perform, not only on average, but against the worst disturbance.
