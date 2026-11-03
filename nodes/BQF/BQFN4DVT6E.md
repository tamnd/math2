---
tag: BQFN4DVT6E
kind: statement
role: theorem
name: Maximum theorem
msc: [49J53, 90C31, 54C60]
uses: [0CQHFPGJ45, 03CPD1HGF3, XNMKX7H4FD, 0R6EWFKRCF, 0X3WGX95FE]
about: [XNMKX7H4FD, 03CPD1HGF3]
sources:
  - url: https://en.wikipedia.org/wiki/Maximum_theorem
same_as:
  wikidata: Q6795920
  wikipedia: Maximum theorem
---

## Statement

Let $X$ and $\Theta$ be [[topological spaces|0CQHFPGJ45]].
Let $f \colon X \times \Theta \to \R$ be a [[continuous function|0X3WGX95FE]].
Let $C$ be a [[multivalued function|03CPD1HGF3]] from $\Theta$ to $X$ such that $C(\theta)$ is a nonempty [[compact|0R6EWFKRCF]] subset of $X$ for each $\theta \in \Theta$.
Assume that $C$ is both upper and lower [[hemicontinuous|XNMKX7H4FD]].
Define the value function and the set of maximisers by
$$f^*(\theta) = \max_{x \in C(\theta)} f(x, \theta), \qquad C^*(\theta) = \set{x \in C(\theta) : f(x, \theta) = f^*(\theta)}.$$
Then:

1. $f^*$ is a continuous function from $\Theta$ to $\R$.
2. $C^*(\theta)$ is nonempty and compact for each $\theta \in \Theta$, and $C^*$ is upper hemicontinuous.

## Remarks

The maximum in $f^*$ exists because a continuous function attains its maximum on a nonempty compact set.
Upper hemicontinuity of $C$ gives that $f^*$ is upper semicontinuous: near $\theta_0$ the feasible sets do not suddenly grow, so the maximum cannot jump up.
Lower hemicontinuity of $C$ gives that $f^*$ is lower semicontinuous: a maximiser at $\theta_0$ can be approached by feasible points at nearby parameters.
Upper hemicontinuity of $C^*$ then follows from the continuity of $f$ and $f^*$ together with the compactness of the values of $C$.

Example: let $X = \Theta = \R$, $C(\theta) = [-1, 1]$ and $f(x, \theta) = \theta x$.
Then $f^*(\theta) = \abs{\theta}$, which is continuous.
The maximisers are $C^*(\theta) = \set{1}$ for $\theta > 0$, $C^*(\theta) = \set{-1}$ for $\theta < 0$ and $C^*(0) = [-1, 1]$.
So $C^*$ is upper hemicontinuous, but it is not lower hemicontinuous at $0$, and it is not single-valued.

Lower hemicontinuity of $C$ is needed.
Let $C(0) = [0, 1]$, $C(\theta) = \set{0}$ for $\theta \ne 0$, and $f(x, \theta) = x$.
This $C$ is upper but not lower hemicontinuous, and $f^*(0) = 1$ while $f^*(\theta) = 0$ for $\theta \ne 0$, so $f^*$ is not continuous.
Compactness is needed too: for $C(\theta) = (0, 1)$ and $f(x, \theta) = x$ the maximum is not attained.

If moreover $X$ is a subset of $\R^n$, each $C(\theta)$ is convex and each $f(\cdot, \theta)$ is concave, then each $C^*(\theta)$ is convex.
If each $f(\cdot, \theta)$ is strictly concave, then $C^*$ is single-valued and so it is a continuous function.

## Explanations

### L1 human

Many problems ask for the best choice under constraints that depend on a parameter, such as a price or an income.
The maximum theorem says that, under mild conditions, the best value changes continuously when the parameter changes.
The set of best choices also behaves well: it cannot suddenly jump far away, although it may suddenly become larger.
For example, maximising $\theta x$ over $x \in [-1, 1]$ gives the best value $\abs{\theta}$, which has no jumps.

### L2 human

The theorem is a basic tool of parametric optimisation and of mathematical economics.
It shows that demand correspondences and value functions in consumer theory are well behaved.
Combined with the [[Kakutani fixed-point theorem|7V3HWGR32Z]], it gives the existence of Nash equilibria and of competitive equilibria.
The best-response correspondence is upper hemicontinuous by the maximum theorem, and convex-valued under concavity.
In dynamic programming it shows that the Bellman operator maps continuous functions to continuous functions.
