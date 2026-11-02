---
tag: 6V8E0AQNHA
kind: concept
name: Compressed sensing
msc: [94A12, 41A46, 94A20]
sources:
  - url: https://en.wikipedia.org/wiki/Compressed_sensing
same_as:
  wikidata: Q2665459
  wikipedia: Compressed sensing
---

## Summary

Compressed sensing is the recovery of a sparse vector from far fewer linear measurements than its length.
Let $x \in \R^N$ have at most $s$ nonzero entries, and let $y = Ax$ for a suitable $m \times N$ matrix $A$ with $m$ much smaller than $N$.
Then $x$ can be found from $y$ by solving a convex problem.
The key sufficient condition on $A$ is the [[restricted isometry property|B0K18PWN2A]], which random matrices satisfy with high probability when $m$ is of order $s \log(N/s)$.
It was developed by Candès, Romberg, Tao and Donoho in the mid-2000s and is used in medical imaging and signal processing.

## Explanations

### L1 human

Usually, to know a vector of length $N$ one must measure $N$ numbers.
If one knows that only a few entries are nonzero, much fewer measurements can be enough, as long as they mix the entries well.
The reconstruction looks for the [[sparse|WC8P971XGW]] vector that agrees with the measurements.
For example, with the $2 \times 3$ matrix $A = \begin{pmatrix} 1 & 0 & 1 \\ 0 & 1 & 1 \end{pmatrix}$, any vector with one nonzero entry is determined by its two measurements $Ax$.
Among such vectors, the measurement $(2, 2)$ can only come from $(0, 0, 2)$, and the measurement $(3, 0)$ only from $(3, 0, 0)$.
