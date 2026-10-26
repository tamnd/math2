---
tag: 0VPCJWGMP9
kind: definition
name: Space of linear maps
msc: [15A04]
defines: 0X9MBPP2Z3
uses: [0RJF668P1T]
sources:
  - url: https://en.wikipedia.org/wiki/Linear_map
    locator: Vector space of linear maps
---

## Definition

Let $F$ be a field and let $V$ and $W$ be vector spaces over $F$.
The *space of linear maps* $\Hom_F(V, W)$, also written $L(V, W)$, is the set of all [[linear maps|0NRYHJPQG2]] $V \to W$, with the operations
$$(S + T)(v) = S(v) + T(v), \qquad (aT)(v) = a\, T(v)$$
for $S, T \in \Hom_F(V, W)$, $a \in F$ and $v \in V$.
It is a vector space over $F$, with the zero map as zero vector.

## Remarks

For $V = F^n$ and $W = F^m$, the matrix map is an isomorphism $\Hom_F(F^n, F^m) \cong M_{m \times n}(F)$.
The [[dimension of the space of linear maps|0Z9N1ER0W0]] is $\dim V \cdot \dim W$ in finite dimensions.
For $W = F$, it is the [[dual space|07JBSZE0V4]] of $V$, and for $W = V$, it is the space of [[endomorphisms|0J7H0YBFDJ]] of $V$.

## Explanations

### L1 human

Linear maps can be added and scaled, value by value, and the result is again linear.
So the linear maps from $V$ to $W$ form a vector space themselves.
In coordinates, this is the vector space of matrices of a fixed size.
