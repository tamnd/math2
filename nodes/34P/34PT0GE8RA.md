---
tag: 34PT0GE8RA
kind: statement
role: theorem
name: Remmert–Stein theorem
msc: [32D15, 32B15, 32C25]
uses: [VMDTGTMN9P, C2R5Q2Q717, JSGWAN2RJV]
about: [GB7M582M5Y]
sources:
  - url: https://en.wikipedia.org/wiki/Remmert%E2%80%93Stein_theorem
same_as:
  wikidata: Q7312009
  wikipedia: Remmert–Stein theorem
---

## Statement

Let $X$ be a [[complex manifold|JSGWAN2RJV]], let $E$ be an [[analytic subset|VMDTGTMN9P]] of $X$, and let $k \ge 1$ be an integer.
Let $A$ be an analytic subset of $X \setminus E$ of [[pure dimension|C2R5Q2Q717]] $k$.
Suppose that $\dim E < k$.
Then the closure $\overline{A}$ of $A$ in $X$ is an analytic subset of $X$, of pure dimension $k$.

## Remarks

The question is local, so one may assume that $X$ is a neighbourhood of a point of $E$ in $\C^n$.
The proof is by induction on the dimension of $E$ and uses projections.
After a generic linear change of coordinates, the projection of $\overline{A}$ to $\C^k$ is proper near the point.
Then $\overline{A}$ is described by the canonical defining polynomials of this branched covering.
Their coefficients are bounded holomorphic functions outside a thin set, so they extend by the Riemann extension theorem.
Example: $A = \set{z_2 = 0} \setminus \set{0}$ is an analytic subset of $\C^2 \setminus \set{0}$ of pure dimension $1$, and $E = \set{0}$ has dimension $0$, so $\overline{A}$, the $z_1$-axis, is analytic.
The hypothesis $\dim E < k$ is necessary.
Let $E = \set{z_1 = 0}$ in $\C^2$ and $A = \set{(z_1, e^{1/z_1}) : z_1 \ne 0}$, an analytic subset of $\C^2 \setminus E$ of pure dimension $1 = \dim E$.
Since $e^{1/z_1}$ takes every nonzero value, and tends to $0$ along the negative real axis, in every neighbourhood of $z_1 = 0$, the closure $\overline{A}$ is $A \cup E$.
It is not analytic: the components of an analytic curve other than $E$ would meet $E$ in a discrete set, but $A$ accumulates at every point of $E$.

## Explanations

### L1 human

Suppose an analytic set is known away from a smaller exceptional set.
The theorem says that if the exceptional set is of strictly smaller dimension, the analytic set extends across it: just add its limit points.
For instance, a curve defined outside a single point extends to a curve through that point.

### L2 human

The theorem is a basic extension result in complex analytic geometry, in the spirit of the Riemann extension theorem for functions.
It gives a short proof of Chow's theorem, by extending the cone over an analytic subset of projective space across the origin.
Bishop's theorem replaces the dimension condition on $E$ by a volume condition on $A$, and Shiffman's theorem by a Hausdorff measure condition on $E$.
