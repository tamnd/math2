---
tag: 94GSMEWPTN
kind: problem
name: Gauss variational problem
msc: [31B15, 31A15]
uses: [0R6EWFKRCF, DCMFQ01QGS, SFSRQCM3EG, 4YZVFGJVSZ]
about: [464NN2K4FZ]
sources:
  - url: https://en.wikipedia.org/wiki/Capacity_of_a_set
history:
  posed_by: "Carl Friedrich Gauss"
  first_stated: "1840"
---

## Problem

Let $n \ge 3$, let $K \subseteq \R^n$ be a [[compact set|0R6EWFKRCF]] of positive [[capacity|4YZVFGJVSZ]], and let $f \colon K \to \R$ be a continuous function.
For a positive Borel measure $\mu$ on $K$, let $U^\mu(x) = \int_K \abs{x - y}^{2-n} \, d\mu(y)$ be its [[Newtonian potential|DCMFQ01QGS]].
The *Gauss integral* of $\mu$ is
$$G_f(\mu) = \int_K \left( U^\mu - 2 f \right) d\mu,$$
that is, the [[energy|SFSRQCM3EG]] of $\mu$ minus twice the integral of $f$.
The problem asks for a positive Borel measure $\mu$ on $K$ with $\mu(K) = 1$ that makes $G_f(\mu)$ as small as possible.

## Remarks

Under these hypotheses a minimizing measure exists and is unique.
Existence follows from the weak-star compactness of the probability measures on $K$ and the lower semicontinuity of the energy.
Uniqueness follows from the strict positive definiteness of the Newtonian energy on signed measures of finite energy.
For $f = 0$ the problem is to minimize the energy among unit measures on $K$, and its solution is the [[equilibrium measure|464NN2K4FZ]] of $K$.
The minimizer $\mu$ is characterized by two inequalities with one constant $c$: $U^\mu - f \ge c$ on $K$ outside a set of capacity zero, and $U^\mu - f \le c$ on the support of $\mu$.
Gauss treated the problem for forces that follow the inverse square law.
Rigorous proofs of existence rely on the measure theory that was developed later.

## Explanations

### L1 human

Put a fixed amount of charge on a conductor $K$ that also feels an outside electric field $f$.
The charges repel each other but are pulled by the field.
The Gauss problem asks where the charge ends up when the total energy is as small as possible.
Without an outside field the answer is the equilibrium distribution, whose total energy measures the capacity of $K$.
