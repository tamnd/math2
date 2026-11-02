---
tag: RPN59B2XSR
kind: concept
name: c-cyclical monotonicity
msc: [49Q22, 49N15]
sources:
  - url: https://en.wikipedia.org/wiki/Transportation_theory_(mathematics)
---

## Summary

Let $c$ be a cost function.
A set of pairs $(x, y)$ is $c$-cyclically monotone if no cyclic reassignment of finitely many of its pairs lowers the total cost.
It is the condition that an optimal transport plan must satisfy on its support: one cannot improve the plan by swapping destinations along a cycle.
For the quadratic cost on $\R^n$ it is the cyclical monotonicity of Rockafellar.
That notion characterizes the subsets of the graph of the subdifferential of a convex function.
Under mild hypotheses, a [[coupling|HTR7J0W66V]] with finite cost is optimal exactly when it is concentrated on a $c$-cyclically monotone set.

## Explanations

### L1 human

Suppose bakeries send bread to cafés, and each pair (bakery, café) on the delivery list has a cost.
The list is $c$-cyclically monotone if no group of bakeries can save money by passing their deliveries around in a circle.
On the real line with cost $(x - y)^2$, sending $0 \to 0$ and $1 \to 1$ passes the test.
Sending $0 \to 1$ and $1 \to 0$ fails, since swapping the two destinations lowers the cost from $2$ to $0$.
An optimal transport plan can never contain such a wasteful cycle.
