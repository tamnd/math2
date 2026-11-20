---
tag: ~cf936aba
kind: example
name: The cube map is a bijection of the real line that is not linear
msc: ["15A04"]
topics: [9080WQTZ3M]
audience: ug1
not_instance_of:
  - target: 0B8T10CE7N
    note: x ↦ x³ is a bijection of R, but (1 + 1)³ = 8 while 1³ + 1³ = 2, so it is not linear
uses: [0XSJ25Z9M4, 0RJF668P1T, 0SNQEF7Z53]
sources:
  - url: https://en.wikipedia.org/wiki/Linear_map
    locator: Examples
---

## Example

Let $f \colon \R \to \R$ be $f(x) = x^3$.

1. $f$ is [[bijective|0SNQEF7Z53]]: it is strictly increasing, and its inverse is $y \mapsto \sqrt[3]{y}$.
2. $f$ is not additive: $f(1 + 1) = 8$, but $f(1) + f(1) = 2$.
3. $f$ is not homogeneous: $f(2 \cdot 1) = 8$, but $2 f(1) = 2$.
4. So $f$ is not a [[linear map|0RJF668P1T]], and it is not a [[linear isomorphism|0XSJ25Z9M4]].

## Remarks

- A bijection between vector spaces is a linear isomorphism only if it is also linear.
- $f$ does respect the zero vector and negatives: $f(0) = 0$ and $f(-x) = -f(x)$.
- $f$ is a homeomorphism of $\R$, so it is an isomorphism of topological spaces, but not of vector spaces.

## Explanations

### L1 human

Cubing is a one-to-one matching of the real numbers with themselves.
But it does not respect sums, since $2^3 = 8$ and $1^3 + 1^3 = 2$.
So it is not a linear isomorphism.

### L2 human

The example separates the two parts of the definition: bijective and linear.
Both are needed, and neither implies the other.
The trap is to call any invertible map between vector spaces an isomorphism.
