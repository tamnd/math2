---
tag: Q0DXKAQXE1
kind: definition
name: Parametric model
msc: [62A01, 62F99]
defines: MSC0MR8VMH
uses: [JZ6R7J36K5]
sources:
  - url: https://en.wikipedia.org/wiki/Parametric_model
    locator: Definition
---

## Definition

Let $\mathcal{P} = \set{P_\theta : \theta \in \Theta}$ be a [[statistical model|JZ6R7J36K5]] on a measurable space $(S, \mathcal{S})$.
The model is a *parametric model* if its parameter space $\Theta$ is a subset of $\R^k$ for some finite $k \ge 1$.
The number $k$ is the dimension of the parameter.

## Remarks

Example: the normal model on $S = \R$ with $P_{(\mu, \sigma^2)} = \mathcal{N}(\mu, \sigma^2)$ and $\Theta = \R \times (0, \infty) \subseteq \R^2$ is parametric with $k = 2$.
Non-example: the model of all probability measures on $\R$ with finite variance is not given by a natural finite-dimensional parameter, and it is called nonparametric.
In practice one also asks that the map $\theta \mapsto P_\theta$ is regular, for example that the densities depend smoothly on $\theta$.
Without such a condition the definition is weak, since any set of at most continuum many laws can be indexed by a subset of $\R$.
