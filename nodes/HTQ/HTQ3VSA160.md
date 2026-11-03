---
tag: HTQ3VSA160
kind: definition
name: Constructive quantum field theory
msc: [81T08]
defines: FG51Y62J8Y
uses: [YS3ER7BW8W, 5QTZQV6TNG, AES2T5JPFP, P0DV2TCH1N, EGCDMWYKQB]
sources:
  - url: https://en.wikipedia.org/wiki/Constructive_quantum_field_theory
---

## Definition

Let $d \ge 2$ and let $\mathcal{S}'(\R^d)$ be the space of [[tempered distributions|AES2T5JPFP]] on $\R^d$.
A *construction* of a Euclidean scalar quantum field theory in $d$ dimensions is a Borel probability measure $\mu$ on $\mathcal{S}'(\R^d)$ with these properties.

1. Its moments, the Schwinger functions $S_n(f_1, \dots, f_n) = \int \phi(f_1) \cdots \phi(f_n) \, d\mu(\phi)$, exist and satisfy the Osterwalder–Schrader axioms.
2. The measure $\mu$ is not [[Gaussian|P0DV2TCH1N]], so the theory is interacting.

By the [[Osterwalder–Schrader reconstruction theorem|YS3ER7BW8W]], such a $\mu$ gives a field theory on Minkowski space satisfying the [[Wightman axioms|5QTZQV6TNG]].
*Constructive quantum field theory* is the study of such constructions, usually obtained as limits of models with an ultraviolet cutoff and a finite volume.

## Remarks

Example: the $P(\phi)_2$ models in $d = 2$, where the interaction is a polynomial $P$ bounded below.
Their measures are limits of measures with density proportional to $\exp\left(-\int_\Lambda {:}P(\phi(x)){:}\, dx\right)$ relative to the [[Gaussian free field|EGCDMWYKQB]], as the volume $\Lambda$ grows.
These limits exist, for instance at weak coupling by cluster expansions.
They satisfy the axioms, and they are not Gaussian when $P$ has degree at least $4$.

Non-example: the Gaussian free field of mass $m > 0$ satisfies clause 1, but it fails clause 2.
It gives the free field, which describes particles that do not interact.

The same aims can be set in the Minkowski or the algebraic setting, using the Wightman or the [[Haag–Kastler axioms|MGBCX7FH2G]] directly.
Fermionic models and gauge theories need other function spaces or Grassmann integrals, but the goal is the same.
