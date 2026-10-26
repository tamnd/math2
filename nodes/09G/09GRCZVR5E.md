---
tag: 09GRCZVR5E
kind: statement
role: theorem
name: Completeness of the space of bounded continuous functions
msc: [54C35]
uses: [08EWT7J0SC, 0SY9ECQ19Q, 06HE9J7DXF]
sources:
  - url: https://en.wikipedia.org/wiki/Uniform_norm
    locator: Properties
  - url: https://en.wikipedia.org/wiki/Complete_metric_space
    locator: Examples
---

## Statement

Let $X$ be a [[topological space|0CNQXVBHCX]] and let $(Y, d_Y)$ be a [[complete metric space|08EWT7J0SC]].
Let $C_b(X, Y)$ be the set of [[continuous maps|0SY9ECQ19Q]] $f \colon X \to Y$ whose image $f(X)$ is [[bounded|0P953MG05E]] in $Y$.
For $f, g \in C_b(X, Y)$, let $d_\infty(f, g) = \sup_{x \in X} d_Y(f(x), g(x))$, with $d_\infty(f, g) = 0$ when $X$ is empty.
Then $(C_b(X, Y), d_\infty)$ is a complete metric space.

## Remarks

For $Y = \mathbb{R}$, the metric $d_\infty$ is the [[uniform metric|06HE9J7DXF]], and it comes from the [[sup norm|0PARCKE8WP]].
Proof sketch: a Cauchy sequence $(f_n)$ in $d_\infty$ is Cauchy at each point $x$, so it has a pointwise limit $f(x)$ in $Y$. The convergence is uniform, and a uniform limit of continuous maps is continuous. The limit is also bounded.
For a compact space $X$, each continuous map to $\mathbb{R}$ is bounded, so $C(X, \mathbb{R})$ is complete with the sup metric.

## Explanations

### L1 human

If continuous functions get closer and closer to each other uniformly, then they converge uniformly to a function.
The key point is that this limit function is again continuous, so the limit stays in the space.
