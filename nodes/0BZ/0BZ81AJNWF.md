---
tag: 0BZ81AJNWF
kind: definition
name: Characteristic polynomial of a linear map
msc: ["15A04", "15A18"]
topics: [6R1D6QPY3S]
audience: ug2
defines: 0J5EMJRRFM
uses: [039HF58KQ5, 0PTF1PTJK0, 0YYMY95FWS]
sources:
  - url: https://en.wikipedia.org/wiki/Characteristic_polynomial
    locator: Formal definition
---

## Definition

The characteristic polynomial of a linear map is the characteristic polynomial of its matrix in any one basis.
Let $F$ be a field, let $V$ be a vector space over $F$ with $n = \dim V$ and $1 \le n < \infty$, and let $T \colon V \to V$ be an [[endomorphism|0J7H0YBFDJ]].
Let $B$ be a basis of $V$, and let $[T]_B$ be the [[matrix of T|0YQSGNYE3K]] in $B$, with $B$ used for both the input and the output.
The *characteristic polynomial* of $T$ is
$$p_T(t) = p_{[T]_B}(t) = \det\big(t I_n - [T]_B\big) \in F[t],$$
the [[characteristic polynomial|0VSSPAFM2C]] of the matrix $[T]_B$.

## Notation

Mathlib writes `LinearMap.charpoly T`.
Books use $p_T$, $\chi_T$ or $c_T$.

## Remarks

The definition makes a choice, the basis $B$, and so it is sound only because the result does not depend on that choice.
That is the first part of the theorem on the [[characteristic polynomial of an endomorphism|C98TZ6ZAXC]]: two bases give similar matrices, and similar matrices have the same characteristic polynomial.
The space must have finite dimension, since otherwise $T$ has no square matrix and there is no determinant.
The same basis must be used on both sides, because only then does a change of basis act by $P^{-1} [T]_B P$.

For an example, take the identity map of $V$.
In every basis its matrix is $I_n$, so $p_T(t) = \det\big((t - 1) I_n\big) = (t - 1)^n$.
For a case that fails a condition, take the identity of $\mathbb{R}^2$ with the input basis $((2, 0), (0, 1))$ and the standard output basis.
Its matrix is $\operatorname{diag}(2, 1)$, with polynomial $(t - 2)(t - 1)$, which is not $(t - 1)^2$, so two different bases give a wrong answer.
The [[concept page|0J5EMJRRFM]] has more examples.

## Explanations

### L1 human

A linear map has one matrix for each choice of axes.
All these matrices have the same characteristic polynomial.
So we may call it the characteristic polynomial of the map, and compute it with whichever axes are most convenient.
