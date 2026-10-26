---
tag: ~eab00ef7
kind: statement
role: theorem
name: Newton's identities
aliases: [girard-newton-formulae]
msc: ["05E05"]
uses: [~71a32e63, ~c5fc6c0d]
sources:
  - url: https://en.wikipedia.org/wiki/Newton%27s_identities
    locator: Formulation in terms of symmetric polynomials
  - url: https://en.wikipedia.org/wiki/Newton%27s_identities
    locator: lead section
same_as:
  wikidata: Q1749812
  wikipedia: Newton's identities
---

## Statement

Let $R$ be a [[commutative ring|~79bc52c4]] and let $n \ge 1$.
Let $e_k$ be the [[elementary symmetric polynomials|~71a32e63]] and $p_k$ the [[power sums|~c5fc6c0d]] in $x_1, \dots, x_n$, with $e_0 = 1$ and $e_k = 0$ for $k > n$.
Then for every $k \ge 1$,
$$k \, e_k = \sum_{i=1}^{k} (-1)^{i-1} e_{k-i} \, p_i.$$

## Remarks

The first cases are $e_1 = p_1$, $2 e_2 = e_1 p_1 - p_2$ and $3 e_3 = e_2 p_1 - e_1 p_2 + p_3$.
For $k > n$, the left side is $0$, and the identity expresses $p_k$ through $p_{k-1}, \dots, p_{k-n}$.
Applied to the roots of a polynomial, the identities compute the power sums of the roots from the coefficients.
Applied to the eigenvalues of a matrix $A$, they relate the traces of the powers of $A$ to the coefficients of its characteristic polynomial.

## History

Isaac Newton found the identities around 1666.
Albert Girard had already found the first four formulas in 1629.

## Explanations

### L1 human

Newton's identities convert between two ways of describing the roots of a polynomial: the sums of their powers, and the coefficients.
Each identity gives the next quantity from the earlier ones.
