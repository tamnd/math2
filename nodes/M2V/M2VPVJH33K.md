---
tag: M2VPVJH33K
kind: definition
name: Primary decomposition
msc: ["13A15", "13C05"]
defines: ZD34THCXQ0
uses: [0GYGHKX834, 0MYSA6MYNA, V026AAV8E6, 437YRCNYRJ]
sources:
  - url: https://en.wikipedia.org/wiki/Primary_decomposition
---

## Definition

Let $R$ be a [[commutative ring|0GYGHKX834]] and let $I$ be an [[ideal|0MYSA6MYNA]] of $R$.
A *primary decomposition* of $I$ is an expression $I = Q_1 \cap \cdots \cap Q_n$, with $n \ge 1$, in which each $Q_i$ is a [[primary ideal|V026AAV8E6]].
The decomposition is *minimal* if these two conditions hold:

1. The [[radicals|437YRCNYRJ]] $\sqrt{Q_1}, \dots, \sqrt{Q_n}$ are pairwise distinct.
2. For each $i$, the intersection of the $Q_j$ with $j \ne i$ is not contained in $Q_i$.

## Remarks

Example: in $k[x, y]$ over a field $k$, $(x^2, xy) = (x) \cap (x^2, y)$, where $(x)$ is prime and $(x^2, y)$ is $(x, y)$-primary; the radicals differ and neither term contains the other, so the decomposition is minimal.
Non-example: $(6) = (2) \cap (6)$ in $\Z$ is not a primary decomposition, because $(6)$ is not primary.
The decomposition $(x^2, xy) = (x) \cap (x^2, xy, y^2)$ is another minimal one, so the primary components need not be unique.
In the same way one defines a primary decomposition of a submodule $N$ of a module $M$, with primary submodules.

## Explanations

### L1 human

A primary decomposition writes an ideal as an intersection of finitely many primary ideals, like writing a number as a product of prime powers.
