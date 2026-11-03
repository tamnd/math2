---
tag: Q925HEYDY7
kind: definition
name: Quasispecies model
msc: [92D15]
defines: G3428M6P36
uses: [0P97V20RW7, 0ZND7NQ970, 62NS7PV1M9]
sources:
  - url: https://en.wikipedia.org/wiki/Quasispecies_model
---

## Definition

Let there be $n$ genotypes $1, \dots, n$.
Let $f_j > 0$ be the replication rate of genotype $j$.
Let $Q = (Q_{ij})$ be an $n \times n$ matrix with $Q_{ij} \ge 0$ and $\sum_i Q_{ij} = 1$ for each $j$.
Here $Q_{ij}$ is the probability that a copy of $j$ is of genotype $i$.
The *quasispecies model* is the system of [[ordinary differential equations|0P97V20RW7]]
$$\frac{dx_i}{dt} = \sum_{j=1}^n Q_{ij} f_j x_j - \phi(x) \, x_i, \quad i = 1, \dots, n,$$
for the relative frequencies $x_i \ge 0$, $\sum_i x_i = 1$, where $\phi(x) = \sum_j f_j x_j$ is the mean replication rate.
A *quasispecies* is an equilibrium of this system.

## Remarks

The equilibria are the eigenvectors $x$ of $W = Q \operatorname{diag}(f_1, \dots, f_n)$ with $x \ge 0$ and $\sum_i x_i = 1$, and the [[eigenvalue|0ZND7NQ970]] is $\phi(x)$.
If all $Q_{ij} > 0$, then $W$ has positive entries, and by the [[Perron–Frobenius theorem|62NS7PV1M9]] there is exactly one such equilibrium; it is the Perron eigenvector.
Example: with $n = 2$, $f = (2, 1)$ and $Q_{11} = Q_{22} = 0.9$, the matrix $W$ has rows $(1.8, 0.1)$ and $(0.2, 0.9)$, and its Perron eigenvalue is $(2.7 + \sqrt{0.89})/2 \approx 1.82$.
Non-example: a matrix $Q$ whose columns do not sum to $1$ breaks the model.
Copies are then created or destroyed outside the replication rates, and $\sum_i x_i = 1$ is not preserved.
With $Q$ the identity matrix the model reduces to pure selection, the replicator equation with constant fitness.
