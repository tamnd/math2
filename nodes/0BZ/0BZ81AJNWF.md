---
tag: 0BZ81AJNWF
kind: definition
name: Characteristic polynomial of a linear map
msc: [15A04, 15A18]
defines: 0J5EMJRRFM
uses: [039HF58KQ5, 0PTF1PTJK0, 0YYMY95FWS]
sources:
  - url: https://en.wikipedia.org/wiki/Characteristic_polynomial
    locator: Formal definition
---

## Definition

Let $F$ be a field, let $V$ be a finite-dimensional vector space over $F$, and let $T \colon V \to V$ be an [[endomorphism|0J7H0YBFDJ]].
The *characteristic polynomial* of $T$ is
$$p_T(t) = p_{[T]_B}(t) = \det(t I_n - [T]_B),$$
the [[characteristic polynomial|0VSSPAFM2C]] of the [[matrix of $T$|0YQSGNYE3K]] in a basis $B$ of $V$, where $n = \dim V$.

## Remarks

The polynomial does not depend on $B$, see [[the invariance of the characteristic polynomial|0TYMASG33Y]].
Its degree is $\dim V$.
For the identity map of $V$, it is $(t - 1)^n$.

## Explanations

### L1 human

A linear map has a matrix in each basis.
All these matrices have the same characteristic polynomial.
So we can call it the characteristic polynomial of the map.
