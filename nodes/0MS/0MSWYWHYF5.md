---
tag: 0MSWYWHYF5
kind: definition
name: Alternating multilinear map
msc: ["15A69", "15A75"]
topics: [DTBK11SR77]
audience: ug2
defines: 0K6CH0MT0F
uses: [0SDMPMCN43, 09VDS2W1E8, 0GYGHKX834]
sources:
  - url: https://en.wikipedia.org/wiki/Alternating_multilinear_map
    locator: Definition
---

## Definition

Let $K$ be a [[commutative ring|0GYGHKX834]], let $M$ and $N$ be [[modules|09VDS2W1E8]] over $K$, and let $n \ge 1$.
A [[multilinear map|0SDMPMCN43]] $f \colon M^n \to N$ is *alternating* when $f(v_1, \dots, v_n) = 0$ for each family $(v_1, \dots, v_n)$ with $v_i = v_j$ for some $i \neq j$.
When $N = K$, an alternating multilinear map is an *alternating $n$-linear form* on $M$.
When $K$ is a field, $M$ and $N$ are vector spaces, and this is the usual definition of linear algebra.

## Notation

The set of alternating multilinear maps $M^n \to N$ is written $\operatorname{Alt}^n(M; N)$.
It is a $K$-module under pointwise addition and scalar multiplication.
For a square matrix, "alternating in the rows" means that the map is alternating as a function of the $n$ rows in $K^n$.

## Remarks

The condition is about equal arguments in any two positions, not only in adjacent positions.
For a multilinear map, zero on equal adjacent arguments already implies zero on all equal pairs, because an exchange of adjacent arguments changes the sign.
An alternating map changes sign when two arguments are exchanged, by the [[antisymmetry theorem|~188b0ad5]].
The converse needs that $2$ is not a zero divisor on $N$; it fails over $\mathbb{F}_2$, as the [[form $xy$ on $\mathbb{F}_2$|~a63aeed2]] shows.

## Explanations

### L1 human

An alternating map gives zero as soon as two inputs are the same.
It follows that swapping two inputs changes the sign of the value.
The signed area of the parallelogram of two plane vectors is an alternating bilinear map.

### L2 human

To check that a multilinear map $f$ is alternating, put the same vector $u$ in two positions and show that the value is $0$ for each $u$.
For $f(u, v) = u_1 v_2 - u_2 v_1$ on $\mathbb{R}^2$ this gives $u_1 u_2 - u_2 u_1 = 0$.
A trap: it is not enough to check the basis vectors, since $f(e_1, e_1) = f(e_2, e_2) = 0$ also holds for the non-alternating form $u_1 v_2 + u_2 v_1$, which gives $f(e_1 + e_2, e_1 + e_2) = 2$.

### L3 human

Alternating maps $M^n \to N$ are the same as linear maps $\Lambda^n M \to N$ from the exterior power.
In characteristic $2$, alternating forms are a proper subset of the symmetric forms.
This is why some books define alternating forms by the zero condition, as here, and not by the sign rule.
