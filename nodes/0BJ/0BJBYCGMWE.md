---
tag: 0BJBYCGMWE
kind: statement
role: proposition
name: A linear map is injective iff its kernel is trivial
msc: [15A04]
uses: [02YFME3RGW, 0RJF668P1T]
sources:
  - url: https://en.wikipedia.org/wiki/Kernel_(linear_algebra)
    locator: Properties
---

## Statement

Let $F$ be a field, let $V$ and $W$ be vector spaces over $F$, and let $T \colon V \to W$ be a [[linear map|0NRYHJPQG2]].
Then $T$ is injective if and only if $\ker T = \{0\}$, where $\ker T$ is the [[kernel|0S23E6YE83]] of $T$.

## Remarks

The key step is $T(u) = T(v) \iff T(u - v) = 0 \iff u - v \in \ker T$.
Thus each nonempty fibre $T^{-1}(w)$ is a coset $v + \ker T$.
For a matrix $A$, the map $x \mapsto Ax$ is injective if and only if $Ax = 0$ has only the trivial solution.

## Explanations

### L1 human

To test if a linear map is one to one, we only need to look at the vectors that go to zero.
If two vectors have the same image, then their difference goes to zero.
So if only $0$ goes to $0$, then no two vectors share an image.
