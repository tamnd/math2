---
tag: B8FVHNXAN1
kind: statement
role: theorem
name: Jacobi method
msc: [65F10]
uses: [0GT4WWGWH2, 89P5GTKW87, 9V7YQA85PC, 54T6Y6DSY4, 2RPE77ACER]
about: [2RPE77ACER, 89P5GTKW87]
sources:
  - url: https://en.wikipedia.org/wiki/Jacobi_method
same_as:
  wikidata: Q1481893
  wikipedia: Jacobi method
---

## Statement

Let $A$ be a real $n \times n$ matrix with nonzero diagonal entries, and let $b \in \R^n$.
Write $A = D + R$, where $D$ is the diagonal part of $A$ and $R = A - D$.
The *Jacobi method* for the [[linear system|0GT4WWGWH2]] $A x = b$ starts from any $x^{(0)} \in \R^n$ and sets
$$x^{(k+1)} = D^{-1} \left( b - R x^{(k)} \right), \quad \text{that is,} \quad x^{(k+1)}_i = \frac{1}{a_{ii}} \Big( b_i - \sum_{j \ne i} a_{ij} x^{(k)}_j \Big).$$
Suppose that $A$ is strictly [[diagonally dominant|89P5GTKW87]] by rows.
Then $A$ is invertible, and for every $b$ and every $x^{(0)}$ the iterates converge to $A^{-1} b$.

## Remarks

The error $e_k = x^{(k)} - A^{-1} b$ satisfies $e_{k+1} = G e_k$ with $G = -D^{-1} R$.
The $i$-th absolute row sum of $G$ is $\sum_{j \ne i} \abs{a_{ij}} / \abs{a_{ii}}$, which is less than $1$ by diagonal dominance.
So the [[matrix norm|54T6Y6DSY4]] $\norm{G}_\infty$ is less than $1$, and $\norm{e_k}_\infty \le \norm{G}_\infty^k \norm{e_0}_\infty \to 0$.
In general, the method converges for every $x^{(0)}$ if and only if the [[spectral radius|9V7YQA85PC]] of $G$ is less than $1$.
Example: for $A$ with rows $(2, 1)$ and $(1, 2)$ and $b = (3, 3)$, starting at $0$ gives $(1.5, 1.5)$, $(0.75, 0.75)$, $(1.125, 1.125)$, tending to $(1, 1)$.
The error is multiplied by $-1/2$ at each step.
Without diagonal dominance the method can diverge.
For $A$ with rows $(1, 2)$ and $(2, 1)$, the matrix $G$ has eigenvalues $\pm 2$.

## Explanations

### L1 human

Each equation of the system is solved for its own unknown, using the old values of all the other unknowns.
All unknowns are updated at once, and the process repeats.
When each diagonal entry outweighs the rest of its row, every equation is dominated by its own unknown.
Then the updates shrink the error at each step.

### L2 human

The Jacobi method is the simplest [[iterative method|2RPE77ACER]] built from a splitting $A = M - N$, here with $M = D$.
Each step costs one matrix-vector product, and all components can be computed in parallel.
It converges slowly on discretized elliptic problems, where the spectral radius tends to $1$ as the mesh is refined.
A damped version is still widely used as a smoother in multigrid methods.
