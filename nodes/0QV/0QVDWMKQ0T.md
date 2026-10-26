---
tag: 0QVDWMKQ0T
kind: definition
name: Homothety
msc: [51N10]
defines: 0ZG1PNEP35
uses: [09XNAPTJQ7, 0JF0TVYGWT]
sources:
  - url: https://en.wikipedia.org/wiki/Homothety
    locator: lead section
---

## Definition

Let $K$ be a field, and let $A$ be an [[affine space|09XNAPTJQ7]] over a $K$-vector space $V$. Let $c$ be a point of $A$ and let $k$ be a nonzero element of $K$.
The homothety with the centre $c$ and the ratio $k$ is the map $h : A \to A$ with
$$h(p) = c + k (p - c) \quad \text{for each point } p \text{ of } A.$$

## Remarks

A homothety is an [[affine map|0JF0TVYGWT]] with the linear part $v \mapsto k v$. It fixes its centre, and it sends each line to a parallel line.
The ratio $k = 1$ gives the identity. The ratio $k = -1$ gives the point reflection in $c$.
In a Euclidean space, a homothety with the ratio $k$ multiplies each distance by $|k|$, each area by $k^2$ and each volume by $|k|^3$.
Mathlib's `AffineMap.homothety` allows each $k$, also $k = 0$, which gives the constant map with the value $c$.

## Explanations

### L1 human

A homothety is a zoom centred at a point. With $k = 2$, each point moves to twice its distance from the centre, on the same ray. A triangle becomes a triangle with sides twice as long, and the same angles.
