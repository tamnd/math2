---
tag: 0125QVNCFQ
kind: definition
name: Evaluation homomorphism
msc: [13F20]
defines: 0FCCDXH97W
uses: [0GJ7T0NK49, 0GGE0Z0JQ1]
sources:
  - url: https://en.wikipedia.org/wiki/Polynomial_ring
    locator: Polynomial evaluation
---

## Definition

Let $R$ be a [[commutative ring|0GYGHKX834]] and let $c \in R$.
The evaluation homomorphism at $c$ is the map
$$\operatorname{ev}_c \colon R[x] \to R, \qquad \operatorname{ev}_c(f) = f(c),$$
where $f(c)$ is the [[value of $f$ at $c$|0GJ7T0NK49]].
It is a [[ring homomorphism|0GGE0Z0JQ1]].

## Remarks

The map $\operatorname{ev}_c$ is surjective, because $\operatorname{ev}_c(r) = r$ for each constant $r \in R$.
Its [[kernel|0AAHE7GEW6]] is the principal ideal $(x - c)$. This is a form of the [[factor theorem|0K3MWA7DMC]].
The commutativity of $R$ is necessary: in general $(f g)(c) \neq f(c) g(c)$ when $c$ does not commute with the coefficients.

## Explanations

### L1 human

Evaluation at $c$ turns each polynomial into an element of $R$.
It respects sums and products: to evaluate $f g$, you can evaluate $f$ and $g$ and multiply.
