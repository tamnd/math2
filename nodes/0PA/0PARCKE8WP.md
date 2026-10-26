---
tag: 0PARCKE8WP
kind: example
name: Sup norm on bounded continuous functions
aliases: [uniform-norm, supremum-norm]
msc: ["46E15"]
instance_of: [06GZ956657]
uses: [09GRCZVR5E, 06HE9J7DXF, 0BTMQ04556]
sources:
  - url: https://en.wikipedia.org/wiki/Uniform_norm
    locator: Definition
  - url: https://en.wikipedia.org/wiki/Uniform_norm
    locator: Properties
same_as:
  wikidata: Q1202673
  wikipedia: Uniform norm
---

## Example

Let $X$ be a [[topological space|0CNQXVBHCX]] and let $C_b(X)$ be the real vector space of bounded [[continuous maps|0SY9ECQ19Q]] $f \colon X \to \mathbb{R}$.
For $f \in C_b(X)$, let $\|f\|_\infty = \sup_{x \in X} |f(x)|$, with $\|f\|_\infty = 0$ when $X$ is empty.
Then $\|\cdot\|_\infty$ is a norm on $C_b(X)$, the sup norm, and $C_b(X)$ is a [[Banach space|0BDTTM24DP]] with this norm.

## Remarks

The [[supremum|0BTMQ04556]] is finite because $f$ is bounded.
The metric $\|f - g\|_\infty$ is the [[uniform metric|06HE9J7DXF]]. Its completeness is [[completeness of the space of bounded continuous functions|09GRCZVR5E]].
A sequence converges in the sup norm if and only if it converges uniformly.
For a compact space $X$, each continuous real function is bounded, so $C_b(X) = C(X)$.

## Explanations

### L1 human

The sup norm of a function is the height of the highest point of its graph, in absolute value.
Two functions are close in this norm when their graphs are close everywhere.
