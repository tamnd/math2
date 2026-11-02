---
tag: KRWE7P7FHP
kind: definition
name: Associativity equation
msc: [39B52, 20N02]
defines: 2JMA7DZMG8
uses: [SRAN4EKWS0, 0M418FE7BB]
sources:
  - url: https://en.wikipedia.org/wiki/Associative_property
---

## Definition

Let $X$ be a set.
The *associativity equation* on $X$ is the [[functional equation|SRAN4EKWS0]]
$$F(F(x, y), z) = F(x, F(y, z)) \quad \text{for all } x, y, z \in X,$$
for an unknown [[binary operation|0M418FE7BB]] $F \colon X \times X \to X$.
A solution is an associative operation on $X$.

## Remarks

Example: $F(x, y) = x + y + xy$ on $X = (-1, \infty)$ is a solution, since both sides equal $(1 + x)(1 + y)(1 + z) - 1$.
Non-example: $F(x, y) = x - y$ on $\R$ is not a solution, since $F(F(0, 0), 1) = -1$ while $F(0, F(0, 1)) = 1$.
Every operation $F(x, y) = g^{-1}(g(x) + g(y))$, with $g \colon X \to \R$ injective and $g(X)$ closed under addition, is a solution.
On a real interval, the continuous solutions that are strictly increasing in each variable are all of this form, with $g$ continuous and strictly monotone.
