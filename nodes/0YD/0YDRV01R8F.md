---
tag: 0YDRV01R8F
kind: statement
role: theorem
name: Universal property of the tensor product
msc: [15A69]
uses: [0G31VJ5YS5, 0P799D6AMN, 0RJF668P1T]
sources:
  - url: https://en.wikipedia.org/wiki/Tensor_product
    locator: Universal property
---

## Statement

Let $F$ be a field, and let $V$, $W$ and $U$ be vector spaces over $F$.
Let $h \colon V \times W \to U$ be a bilinear map.
Then there is exactly one linear map $\tilde h \colon V \otimes W \to U$ such that
$$\tilde h(v \otimes w) = h(v, w) \qquad \text{for all } v \in V \text{ and } w \in W,$$
where $V \otimes W$ is the [[tensor product|0BF2DE2SYK]].

## Remarks

So the bilinear maps $V \times W \to U$ correspond one to one with the [[linear maps|0NRYHJPQG2]] $V \otimes W \to U$.
This property determines $V \otimes W$ up to a unique isomorphism that fixes the vectors $v \otimes w$.
Uniqueness holds because the vectors $v \otimes w$ span $V \otimes W$.

## Explanations

### L1 human

Every bilinear map out of $V \times W$ factors through the tensor product in exactly one way.
So the study of bilinear maps reduces to the study of linear maps.
This property is the usual definition of the tensor product in more abstract settings.
