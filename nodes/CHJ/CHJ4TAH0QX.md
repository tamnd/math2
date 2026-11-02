---
tag: CHJ4TAH0QX
kind: statement
role: theorem
name: Lichnerowicz vanishing theorem
msc: [53C27, 58J20, 53C21]
uses: [QMRAVX14BJ, 4WCJ49Z90S, RSPZ9TCFQ8, ZHX2VYQDZ3, 7CBT4SM83Y, JR2M58RCW3]
about: [QMRAVX14BJ, ZHX2VYQDZ3]
sources:
  - url: https://en.wikipedia.org/wiki/Genus_of_a_multiplicative_sequence
---

## Statement

Let $M$ be a closed manifold of dimension $n$ with a [[spin structure|RSPZ9TCFQ8]].
Suppose that $M$ carries a [[Riemannian metric|7CBT4SM83Y]] whose [[scalar curvature|ZHX2VYQDZ3]] is positive at every point.

1. The [[Dirac operator|QMRAVX14BJ]] of $M$ for this metric has trivial kernel: every harmonic spinor is zero.
2. If $n = 4k$, then the $\hat{A}$-genus of $M$ vanishes: $\hat{A}(M) = 0$.

## Remarks

Let $\psi$ be a spinor with $D\psi = 0$.
Integrating the [[Lichnerowicz formula|4WCJ49Z90S]] $D^2 = \nabla^* \nabla + \frac{R}{4}$ against $\psi$ gives $0 = \int_M \abs{\nabla \psi}^2 + \frac{1}{4} \int_M R \abs{\psi}^2$.
Both terms are nonnegative and $R > 0$, so $\psi = 0$.
By the Atiyah–Singer index theorem, $\hat{A}(M)$ is the [[index of the positive part of the Dirac operator|JR2M58RCW3]], $\dim \ker D^+ - \dim \ker D^-$, which is then $0$.
The argument works as well when $R \ge 0$ everywhere and $R > 0$ at some point.

Example: a K3 surface is a closed spin $4$-manifold with signature $-16$, so $\hat{A} = -\frac{\sigma}{8} = 2 \ne 0$.
Hence a K3 surface has no metric of positive scalar curvature.

The spin hypothesis is necessary.
The complex projective plane $\C P^2$ with the Fubini–Study metric has positive scalar curvature, but $\hat{A}(\C P^2) = -\frac{1}{8}$, computed from its Pontryagin number $p_1 = 3$ by $\hat{A} = -\frac{p_1}{24}$.
This is consistent because $\C P^2$ is not spin.

## Explanations

### L1 human

Positive scalar curvature is incompatible with certain topological invariants of spin manifolds.
The theorem shows that if the $\hat{A}$-genus of a spin manifold is not zero, no metric on it can have positive scalar curvature everywhere.
The proof is short: positive curvature forces the Dirac operator to have no kernel, and the index theorem turns this into a statement about topology.

### L2 human

This is the first and basic obstruction to metrics of positive scalar curvature.
Hitchin refined it to a $KO$-theoretic invariant.
Gromov and Lawson extended the method to Dirac operators twisted by bundles, which shows for example that tori admit no metric of positive scalar curvature.
For simply connected manifolds of dimension at least $5$, the refined invariant decides the question for spin manifolds.
