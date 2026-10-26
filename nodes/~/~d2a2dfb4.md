---
tag: ~d2a2dfb4
kind: statement
role: proposition
name: Triangle inequality for norms
msc: [46B20]
uses: [~1826249d]
sources:
  - url: https://en.wikipedia.org/wiki/Triangle_inequality
    locator: Normed vector space
---

## Statement

Let $V$ be a vector space over $\R$ or $\C$ with a [[norm|~52650b5f]] $\norm{\cdot}$.
Then, for all $x, y \in V$,
$$\norm{x + y} \le \norm{x} + \norm{y} \qquad \text{and} \qquad \bigl| \norm{x} - \norm{y} \bigr| \le \norm{x - y}.$$

## Remarks

The first inequality is an axiom of a norm; the second, the *reverse triangle inequality*, follows from it.
For the norm induced by an inner product, the first inequality follows from the [[Cauchy–Schwarz inequality|~70433a5a]].
In $\R^n$, it says that one side of a triangle is at most the sum of the other two sides.

## Explanations

### L1 human

The straight way from $0$ to $x + y$ is never longer than the way through $x$.
This is the triangle inequality.
The reverse form says that two vectors with a small difference have almost equal lengths.
