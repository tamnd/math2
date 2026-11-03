---
tag: NDABCTQQFK
kind: statement
role: theorem
name: Berge's maximum theorem
msc: [90C31, 54C60, 91B02]
uses: [XNMKX7H4FD, 0R6EWFKRCF, 0X3WGX95FE, 0VKD1TP7F3]
about: [XNMKX7H4FD]
sources:
  - url: https://en.wikipedia.org/wiki/Maximum_theorem
same_as:
  wikidata: Q6795920
  wikipedia: Maximum theorem
---

## Statement

Let $X$ and $\Theta$ be [[metric spaces|0VKD1TP7F3]].
Let $f \colon X \times \Theta \to \R$ be a [[continuous function|0X3WGX95FE]].
Let $C$ be a set-valued map that assigns to each $\theta \in \Theta$ a nonempty [[compact|0R6EWFKRCF]] subset $C(\theta) \subseteq X$.
Suppose that $C$ is both upper and lower [[hemicontinuous|XNMKX7H4FD]].
Define the value function and the set of maximizers by
$$f^*(\theta) = \max_{x \in C(\theta)} f(x, \theta), \qquad C^*(\theta) = \set{x \in C(\theta) : f(x, \theta) = f^*(\theta)}.$$
Then $f^*$ is continuous on $\Theta$, and $C^*$ has nonempty compact values and is upper hemicontinuous.

## Remarks

The maximum exists because a continuous function attains its maximum on a nonempty compact set.
Upper hemicontinuity of $C$ gives that $f^*$ is upper semicontinuous, and lower hemicontinuity gives that $f^*$ is lower semicontinuous.
Upper hemicontinuity of $C^*$ then follows because $C^*$ has a closed graph and lies inside the compact-valued, upper hemicontinuous map $C$.

The maximizer set need not be lower hemicontinuous.
For $\Theta = [-1, 1]$, $C(\theta) = [-1, 1]$ and $f(x, \theta) = \theta x$, one has $C^*(\theta) = \set{1}$ for $\theta > 0$, $\set{-1}$ for $\theta < 0$ and $[-1, 1]$ for $\theta = 0$.
The value $f^*(\theta) = \abs{\theta}$ is continuous, as the theorem says.

Lower hemicontinuity of $C$ is needed.
Take $C(0) = [0, 1]$ and $C(\theta) = \set{0}$ for $\theta \ne 0$, with $f(x, \theta) = x$.
Then $C$ is upper but not lower hemicontinuous, and $f^*$ jumps from $1$ at $\theta = 0$ to $0$ elsewhere.

## Explanations

### L1 human

Think of a choice problem that depends on a parameter, like a consumer whose prices and income can change.
The theorem says that if the objective and the set of allowed choices change continuously with the parameter, then the best value changes continuously too.
The set of best choices may jump, but only by suddenly growing, never by suddenly losing its limit points.

### L2 human

The theorem is a basic tool of mathematical economics.
Applied to the [[utility maximization problem|A56BG7XYM6]], it shows that the indirect utility function is continuous and that Marshallian demand is upper hemicontinuous.
When the objective is quasiconcave in $x$ and $C(\theta)$ is convex, $C^*$ also has convex values, so the [[Kakutani fixed-point theorem|7V3HWGR32Z]] can be applied to it.
This is how best-reply maps are handled in existence proofs for Nash equilibria and for competitive equilibria.
