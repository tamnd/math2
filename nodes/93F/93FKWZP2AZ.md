---
tag: 93FKWZP2AZ
kind: definition
name: Fixed-point property
msc: [54H25, 55M20]
defines: JQDHHFXBF3
uses: [0CQHFPGJ45, 0X3WGX95FE, 00KAFBR32E, 060W5CBZP6]
sources:
  - url: https://en.wikipedia.org/wiki/Fixed-point_property
---

## Definition

Let $X$ be a [[topological space|0CQHFPGJ45]].
$X$ has the *fixed-point property* if for every [[continuous map|0X3WGX95FE]] $f \colon X \to X$ there is a point $x \in X$ with $f(x) = x$.

## Remarks

Example: the interval $[0, 1]$ has the fixed-point property.
For continuous $f \colon [0, 1] \to [0, 1]$, the function $g(x) = f(x) - x$ satisfies $g(0) \ge 0$ and $g(1) \le 0$, so $g$ has a zero by the [[intermediate value theorem|00KAFBR32E]].
Non-example: the [[circle|060W5CBZP6]] $S^1 \subseteq \C$ fails it, because the rotation $z \mapsto -z$ is continuous and has no fixed point.
If $X$ has the fixed-point property and $Y$ is homeomorphic to $X$, then $Y$ has it as well.
A retract of a space with the fixed-point property also has it.
The Brouwer fixed-point theorem states that the closed unit ball of $\R^n$ has the fixed-point property.
