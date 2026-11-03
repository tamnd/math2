---
tag: J6CYFY8EWC
kind: definition
name: Normalized Haar measure on a compact group
msc: [28C10, 43A05, 22C05]
defines: 9T4PJJ60JE
uses: [EVHCE5VR6Y, VY0HXD3GC4, KB792QTG4F]
sources:
  - url: https://en.wikipedia.org/wiki/Haar_measure
---

## Definition

Let $G$ be a [[compact group|EVHCE5VR6Y]], that is, a compact Hausdorff topological group.
The *normalized Haar measure* of $G$ is the unique left [[Haar measure|VY0HXD3GC4]] $\mu$ on $G$ with $\mu(G) = 1$.

## Remarks

It exists and is unique.
A Haar measure $\nu$ is finite on compact sets, so $0 < \nu(G) < \infty$, where $\nu(G) > 0$ because $G$ is a nonempty open set.
Then $\mu = \nu / \nu(G)$ has total mass $1$.
Uniqueness follows from the [[existence and uniqueness of Haar measure|KB792QTG4F]]: two Haar measures differ by a constant $c > 0$, and equal total mass forces $c = 1$.

The normalized Haar measure is also right-invariant and invariant under $x \mapsto x^{-1}$, because compact groups are unimodular.
One often writes $\int_G f(x) \, dx$ for the integral against it.

Example: for a finite group $G$ of order $n$ with the discrete topology, $\mu(A) = \abs{A}/n$.
It is left-invariant, since $\abs{gA} = \abs{A}$, and $\mu(G) = 1$.

Non-example: on $(\R, +)$ every Haar measure is $c\lambda$ with $c > 0$ and $\lambda$ Lebesgue measure, so it has infinite total mass.
No Haar measure of $\R$ can be normalized; the hypothesis that $G$ is compact fails.
A locally compact group has a finite Haar measure exactly when it is compact.
