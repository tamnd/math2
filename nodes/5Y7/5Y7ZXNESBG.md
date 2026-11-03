---
tag: 5Y7ZXNESBG
kind: definition
name: Identity of an algebra
msc: [17A30, 17A01]
defines: TM8ZXES0DJ
uses: [1SENAHZW5A, 9689SFPVE9, PKD440G2XW]
sources:
  - url: https://en.wikipedia.org/wiki/Polynomial_identity_ring
---

## Definition

Let $K$ be a field and let $X = \set{x_1, x_2, \dots}$ be a countable set of variables.
A *nonassociative monomial* is a product of variables from $X$ with a full bracketing, such as $(x_1 x_2) x_1$; these monomials form the free [[magma|9689SFPVE9]] on $X$.
Let $K\{X\}$ be the $K$-vector space with these monomials as a basis, with the product extended bilinearly from the product of monomials.
Let $A$ be an [[algebra|1SENAHZW5A]] over $K$.
An element $f(x_1, \dots, x_n) \in K\{X\}$ is an *identity* of $A$ if
$$f(a_1, \dots, a_n) = 0 \quad \text{for all } a_1, \dots, a_n \in A.$$

## Remarks

Here $f(a_1, \dots, a_n)$ is obtained by replacing each $x_i$ by $a_i$ and computing in $A$.
Example: $(x_1 x_2) x_3 - x_1 (x_2 x_3)$ is an identity of $A$ exactly when $A$ is associative.
Example: $x_1 (x_1 x_2) - (x_1 x_1) x_2$ is an identity of the [[octonions|1HRMT3DSX2]], which are alternative.
Non-example: $x_1 x_2 - x_2 x_1$ is not an identity of the $2 \times 2$ real matrices, since two matrices can fail to commute.
One says that $A$ *satisfies* the identity $f = 0$.
This is the case of algebras over $K$ of an [[identity|PKD440G2XW]] in universal algebra, with $f = 0$ read as $f \approx 0$.
