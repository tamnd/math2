---
tag: 5GBQ7XW6HC
kind: definition
name: Anyon
msc: [81V27, 20F36, 81V70]
defines: CSX5R1RAPN
uses: [BNR4H5GCTP, 0515A6D2Y1]
sources:
  - url: https://en.wikipedia.org/wiki/Anyon
---

## Definition

Let $n \ge 2$, and let $C_n(\R^2)$ be the configuration space of $n$ identical particles in the plane, the space of $n$-element subsets of $\R^2$.
Its fundamental group is the [[braid group|BNR4H5GCTP]] $B_n$, with generators $\sigma_1, \ldots, \sigma_{n-1}$, where $\sigma_i$ exchanges particles $i$ and $i+1$ counterclockwise.
The exchange statistics of $n$ identical particles in the plane is a unitary representation $\rho$ of $B_n$.
It acts on a finite-dimensional complex inner product space of internal states.
The particles are *anyons* if $\rho(\sigma_i)^2 \ne \id$ for some $i$, that is, if $\rho$ does not factor through the [[symmetric group|0515A6D2Y1]] $S_n$.
They are *abelian anyons* if $\rho$ is one-dimensional, and *non-abelian anyons* if the matrices $\rho(\sigma_i)$ do not all commute.

## Remarks

The generators $\sigma_i$ are all conjugate in $B_n$, so a one-dimensional representation sends every $\sigma_i$ to the same phase $e^{i\theta}$, the statistics angle.
The angle $\theta = 0$ gives bosons and $\theta = \pi$ gives fermions; in both cases $\rho(\sigma_i)^2 = 1$.

Example: $\theta = \pi/3$ gives abelian anyons, since $\rho(\sigma_i)^2 = e^{2\pi i/3} \ne 1$; quasiparticles of the quantum Hall state at filling $1/3$ are predicted to have this angle.

Non-example: $\theta = \pi$ fails the defining condition, since $\rho(\sigma_i)^2 = e^{2\pi i} = 1$; these particles are fermions.

In $\R^d$ with $d \ge 3$ the fundamental group of the configuration space is $S_n$ itself, so $\rho(\sigma_i)^2 = \id$ always and anyons cannot occur.
