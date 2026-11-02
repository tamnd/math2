---
tag: G0EDYEDG4S
kind: statement
role: theorem
name: Gauss–Seidel method
msc: [65F10]
uses: [0GT4WWGWH2, 89P5GTKW87, 0KX66CZMBB, 9V7YQA85PC, 2RPE77ACER, B8FVHNXAN1]
about: [2RPE77ACER]
sources:
  - url: https://en.wikipedia.org/wiki/Gauss%E2%80%93Seidel_method
same_as:
  wikidata: Q1069090
  wikipedia: Gauss–Seidel method
---

## Statement

Let $A$ be a real $n \times n$ matrix with nonzero diagonal entries, and let $b \in \R^n$.
Write $A = L_* + U$, where $L_*$ is the lower triangular part of $A$ with the diagonal, and $U$ is the strictly upper triangular part.
The *Gauss–Seidel method* for the [[linear system|0GT4WWGWH2]] $A x = b$ starts from any $x^{(0)} \in \R^n$ and sets
$$x^{(k+1)} = L_*^{-1} \left( b - U x^{(k)} \right), \quad \text{that is,} \quad x^{(k+1)}_i = \frac{1}{a_{ii}} \Big( b_i - \sum_{j < i} a_{ij} x^{(k+1)}_j - \sum_{j > i} a_{ij} x^{(k)}_j \Big).$$
Suppose that one of the following holds:

1. $A$ is strictly [[diagonally dominant|89P5GTKW87]] by rows;
2. $A$ is symmetric and [[positive definite|0KX66CZMBB]].

Then $A$ is invertible, and for every $b$ and every $x^{(0)}$ the iterates converge to $A^{-1} b$.

## Remarks

The error satisfies $e_{k+1} = G e_k$ with $G = -L_*^{-1} U$, and convergence for all starts means that the [[spectral radius|9V7YQA85PC]] of $G$ is less than $1$.
In case 1, an eigenvector argument bounds each eigenvalue $\lambda$ of $G$ by $\abs{\lambda} \le \max_i \frac{\sum_{j > i} \abs{a_{ij}}}{\abs{a_{ii}} - \sum_{j < i} \abs{a_{ij}}} < 1$.
In case 2, the energy $\norm{e}_A^2 = e^T A e$ strictly decreases along the iteration, by a computation with $L_*^T + L_* - A = D$, where $D$ is the positive diagonal of $A$.
Example: for $A$ with rows $(2, 1)$ and $(1, 2)$ and $b = (3, 3)$, starting at $0$ gives $(1.5, 0.75)$, then $(1.125, 0.9375)$, tending to $(1, 1)$.
The error is multiplied by $1/4$ at each step, the square of the [[Jacobi|B8FVHNXAN1]] factor $1/2$.
Without the hypotheses the method can diverge: for $A$ with rows $(1, 2)$ and $(2, 1)$, which is symmetric but indefinite, $G$ has spectral radius $4$.

## Explanations

### L1 human

Gauss–Seidel is the [[Jacobi method|B8FVHNXAN1]] with one change: each new value is used as soon as it is computed.
One sweeps through the equations in order, and each equation sees the freshest values of the unknowns before it.
This usually converges faster than Jacobi and needs only one copy of the vector in memory.

### L2 human

In matrix form Gauss–Seidel is the [[iterative method|2RPE77ACER]] of the splitting $A = M - N$ with $M = L_*$, so each step is a forward substitution.
For symmetric positive definite $A$ it is a coordinate-wise minimization of the energy $\frac12 x^T A x - b^T x$.
Its sweeps depend on the order of the unknowns, which makes it harder to parallelize than Jacobi.
Successive over-relaxation adds a weight to each update and can converge much faster.
