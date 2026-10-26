---
tag: 0YZ3T5Q7XN
kind: example
name: Determinant as a group homomorphism
msc: [15A15]
instance_of: [0JYTG5K9Y4]
uses: [0HV9Y7WG5R, 0Z424HK8CQ]
sources:
  - url: https://en.wikipedia.org/wiki/Determinant
    locator: Invertibility
---

## Example

Let $n$ be a positive integer and let $\mathrm{GL}_n(\mathbb{R})$ be the group of invertible $n \times n$ real matrices under multiplication.
The determinant is a map $\det \colon \mathrm{GL}_n(\mathbb{R}) \to \mathbb{R}^\times$ to the group of nonzero real numbers under multiplication.
It is a [[group homomorphism|0JYTG5K9Y4]], because $\det(AB) = \det(A) \det(B)$ for all $A, B$.

## Remarks

The [[kernel|0W88CEGQP1]] of $\det$ is the special linear group $\mathrm{SL}_n(\mathbb{R})$ of matrices of determinant $1$, so this group is normal in $\mathrm{GL}_n(\mathbb{R})$.
The determinant is surjective onto $\mathbb{R}^\times$, so $\mathrm{GL}_n(\mathbb{R}) / \mathrm{SL}_n(\mathbb{R}) \cong \mathbb{R}^\times$.
The same holds over each field $F$, with $\mathrm{GL}_n(F)$, $\mathrm{SL}_n(F)$ and $F^\times$.

## Explanations

### L1 human

The determinant turns a product of matrices into a product of numbers.
That is exactly what a homomorphism does.
The matrices that it sends to $1$ form an important subgroup, the special linear group.
