---
tag: FGF275MNQJ
kind: definition
name: Filtered algebra
msc: [16W70]
defines: R1PTHQACWM
uses: [3CTW1P4HBP, 0GYGHKX834]
sources:
  - url: https://en.wikipedia.org/wiki/Filtered_algebra
---

## Definition

Let $K$ be a [[commutative ring|0GYGHKX834]] and let $A$ be an [[associative algebra|3CTW1P4HBP]] over $K$ with unit $1$.
An *(increasing, exhaustive) filtration* of $A$ is a family $(F_i)_{i \ge 0}$ of $K$-submodules of $A$ such that:

1. $F_i \subseteq F_{i+1}$ for all $i \ge 0$.
2. $\bigcup_{i \ge 0} F_i = A$.
3. $F_i F_j \subseteq F_{i+j}$ for all $i, j \ge 0$.
4. $1 \in F_0$.

A *filtered algebra* is an algebra together with such a filtration.

## Remarks

The *associated graded algebra* is $\operatorname{gr} A = \bigoplus_{i \ge 0} F_i / F_{i-1}$ with $F_{-1} = 0$; clause 3 makes the product $(a + F_{i-1})(b + F_{j-1}) = ab + F_{i+j-1}$ well defined.
Example: $A = K[x]$ with $F_i$ the polynomials of degree at most $i$.
Clauses 1, 2 and 4 are clear, and clause 3 holds since $\deg(fg) \le \deg f + \deg g$.
Here $\operatorname{gr} A \cong K[x]$.
Non-example: in $K[x]$ take $F_0 = K + Kx$ and $F_i$ the polynomials of degree at most $i + 1$ for $i \ge 1$.
Clauses 1, 2 and 4 hold, but clause 3 fails: $x \cdot x = x^2 \notin F_0$.
Let $U(\mathfrak{g})$ be the universal enveloping algebra of a Lie algebra $\mathfrak{g}$ over a field, with $F_i$ spanned by products of at most $i$ elements of $\mathfrak{g}$.
Then the Poincaré–Birkhoff–Witt theorem gives $\operatorname{gr} U(\mathfrak{g}) \cong S(\mathfrak{g})$.
