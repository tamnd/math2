---
tag: 71XBFB49HE
kind: statement
role: theorem
name: Kiefer–Wolfowitz equivalence theorem
msc: [62K05]
uses: [PM5PQX6TVP, 41FVC4P5JB, G1Z3WSTE8Q, 00KDZRW4C0, 059TJN0NZ1]
about: [PM5PQX6TVP]
sources:
  - url: https://en.wikipedia.org/wiki/Optimal_experimental_design
---

## Statement

Let $\mathcal{X}$ be a compact metric space, the design region.
Let $f \colon \mathcal{X} \to \R^p$ be continuous, and consider the [[linear regression|41FVC4P5JB]] model $E[y(x)] = \theta^T f(x)$ with $\theta \in \R^p$ and uncorrelated errors of equal variance.
A design is a [[probability measure|059TJN0NZ1]] $\xi$ on the Borel sets of $\mathcal{X}$.
Its information matrix is $M(\xi) = \int_{\mathcal{X}} f(x) f(x)^T \, d\xi(x)$.
When $M(\xi)$ is nonsingular, its standardized variance function is $d(x, \xi) = f(x)^T M(\xi)^{-1} f(x)$.
Assume that some design has a nonsingular information matrix.
For a design $\xi^*$ with $M(\xi^*)$ nonsingular, the following three conditions are equivalent:

1. $\xi^*$ is D-optimal: it maximizes $\det M(\xi)$ over all designs $\xi$.
2. $\xi^*$ is G-optimal: it minimizes $\max_{x \in \mathcal{X}} d(x, \xi)$ over all designs $\xi$ with $M(\xi)$ nonsingular.
3. $\max_{x \in \mathcal{X}} d(x, \xi^*) = p$.

Moreover, all D-optimal designs have the same information matrix, and $d(x, \xi^*) = p$ at every support point $x$ of a D-optimal design $\xi^*$.

## Remarks

For every design with nonsingular information matrix, $\int d(x, \xi) \, d\xi(x) = \tr(M(\xi)^{-1} M(\xi)) = p$.
So $\max_x d(x, \xi) \ge p$ always holds, and this explains the number $p$ in condition 3.
The function $\xi \mapsto \log \det M(\xi)$ is concave on the convex set of designs, and its directional derivative at $\xi$ towards the point mass $\delta_x$ equals $d(x, \xi) - p$.
So condition 3 says that no direction increases $\log \det M$, which for a concave function means a maximum.
Example: for the line $f(x) = (1, x)^T$ on $\mathcal{X} = [-1, 1]$, the design $\xi^* = \frac12 \delta_{-1} + \frac12 \delta_{1}$ has $M(\xi^*) = I_2$.
Then $d(x, \xi^*) = 1 + x^2 \le 2 = p$, so $\xi^*$ is D-optimal and G-optimal.
The theorem was proved by Jack Kiefer and Jacob Wolfowitz in 1960.

## Explanations

### L1 human

An experimenter chooses where to take measurements in order to fit a regression model.
One goal is to make the joint uncertainty about the parameters small, measured by the [[determinant|00KDZRW4C0]] of the [[information matrix|G1Z3WSTE8Q]].
Another goal is to make the worst prediction variance over the whole region small.
The theorem says that these two goals give the same best designs, and it gives a simple test for being best.

### L2 human

The equivalence theorem turns a hard optimization over probability measures into a checkable condition: compute $d(x, \xi)$ and see whether it stays below $p$.
It is the basis of the Fedorov–Wynn type algorithms, which add weight at the point where $d(x, \xi)$ is largest.
Similar equivalence theorems hold for other concave criteria of [[optimal experimental design|PM5PQX6TVP]], with the variance function replaced by the corresponding directional derivative.
