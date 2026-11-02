---
tag: CSETD54YDT
kind: statement
role: theorem
name: Kaczmarz method
msc: [65F10, 65F20]
uses: [0GT4WWGWH2, 0NB0AWGJBW, 0B8KZRT28M, 0ZC9YTXZRY, AB3S6MHJ8X, 2RPE77ACER]
about: [2RPE77ACER]
sources:
  - url: https://en.wikipedia.org/wiki/Kaczmarz_method
same_as:
  wikidata: Q288600
  wikipedia: Kaczmarz method
---

## Statement

Let $A$ be a real $m \times n$ matrix with nonzero rows $a_1^T, \dots, a_m^T$, and let $b \in \R^m$ be such that the [[linear system|0GT4WWGWH2]] $A x = b$ has a solution.
For an index $i$, the *Kaczmarz step* maps $x \in \R^n$ to
$$x + \frac{b_i - \ip{a_i}{x}}{\norm{a_i}^2} \, a_i,$$
the [[orthogonal projection|0B8KZRT28M]] of $x$ onto the hyperplane $\set{y : \ip{a_i}{y} = b_i}$.
Start from any $x_0 \in \R^n$.

1. (Cyclic version) Let $x_{k+1}$ be the Kaczmarz step from $x_k$ with $i = (k \bmod m) + 1$. Then $x_k$ converges to a solution of $A x = b$. If $x_0 = 0$, the limit is the solution of least Euclidean norm.
2. (Randomized version, Strohmer and Vershynin) Suppose $A$ has [[rank|0ZC9YTXZRY]] $n$, and let $x^*$ be the solution. Let $x_{k+1}$ be the Kaczmarz step from $x_k$ with $i$ drawn independently, equal to $j$ with probability $\norm{a_j}^2 / \norm{A}_F^2$. Then $\mathbb{E} \norm{x_k - x^*}^2 \le \left( 1 - \kappa^{-2} \right)^k \norm{x_0 - x^*}^2$, where $\kappa = \norm{A}_F \norm{A^{+}}_2$.

Here $\norm{\cdot}$ is the Euclidean norm, $\norm{A}_F$ is the Frobenius norm and $A^{+}$ is the pseudoinverse.

## Remarks

Each step is a projection onto a convex set that contains every solution.
So for every solution $z$, the distance $\norm{x_k - z}$ never increases, which drives the convergence proof.
Each step adds a multiple of a row $a_i$, so $x_k - x_0$ stays in the row space of $A$.
The solution of least norm is the only solution in the row space, which gives the claim for $x_0 = 0$.
Example: for the system $x_1 = 1$, $x_2 = 1$ in $\R^2$, two cyclic steps from $0$ give $(1, 0)$ and then the solution $(1, 1)$.
For orthogonal rows the method finishes after one sweep; for nearly parallel rows it zigzags and is slow.
The number $\kappa$ is a scaled [[condition number|AB3S6MHJ8X]], and it measures this effect in the randomized bound.

## Explanations

### L1 human

Each equation of a linear system describes a flat set, a line in the plane or a plane in space.
The Kaczmarz method moves the current point straight onto one of these sets, then onto the next, and so on.
The point gets closer to the common intersection at each move.
This simple idea is the algebraic reconstruction technique of computed tomography.

### L2 human

The Kaczmarz method touches one row at a time, so it suits huge systems whose rows are generated on the fly.
It is a row-action [[iterative method|2RPE77ACER]], related to the Gauss–Seidel method applied to $A A^T y = b$ with $x = A^T y$.
Choosing rows at random with probability proportional to their squared norms gives a clean linear rate in expectation.
This randomized version links the method to stochastic gradient descent for least squares.
