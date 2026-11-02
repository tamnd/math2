---
tag: 7VJGH5BKKA
kind: example
name: Affine space as an algebra
msc: [08A99, 51N10, 15A03]
instance_of: [09XNAPTJQ7]
uses: [000AYPA9AJ, 04C5ZBG1WT, WC47MFR6GW, Y203PPTS61, 06HYY6DK6X]
sources:
  - url: https://en.wikipedia.org/wiki/Affine_space
---

## Example

Let $F$ be a [[field|04C5ZBG1WT]] and let $V$ be a [[vector space|000AYPA9AJ]] over $F$.
The [[affine space|09XNAPTJQ7]] of $V$, seen as an algebra in the sense of universal algebra, is the set $V$ with these operations:

1. the [[ternary operation|WC47MFR6GW]] $p(x, y, z) = x - y + z$;
2. for each $r \in F$, the binary operation $b_r(x, y) = (1 - r)x + ry$.

There is no constant and no addition of two points.
Each operation is an [[affine combination|06HYY6DK6X]], since its coefficients sum to $1$.

Check that every affine combination is a term in these operations.
Take $x_1, \dots, x_n \in V$ and $\lambda_1, \dots, \lambda_n \in F$ with $\lambda_1 + \cdots + \lambda_n = 1$.
Then $\sum_i \lambda_i x_i = x_1 + \sum_{i \ge 2} \lambda_i (x_i - x_1)$.
Each point $b_{\lambda_i}(x_1, x_i) = x_1 + \lambda_i (x_i - x_1)$ is a term.
For points $x_1 + a$ and $x_1 + c$, the term $p(x_1 + a, x_1, x_1 + c)$ equals $x_1 + a + c$.
Applying $p$ repeatedly therefore gives $x_1 + \sum_{i \ge 2} \lambda_i (x_i - x_1)$.
So the subalgebras are exactly the subsets closed under affine combinations, that is, the affine subspaces and the empty set.

## Remarks

Every translation $x \mapsto x + v$ is an automorphism of this algebra, because each operation is an affine combination.
A translation by $v \ne 0$ does not fix $0$, so it is not a linear map of $V$.
This shows that the algebra forgets the origin of $V$.
The term $p$ satisfies $p(x, x, y) = y$ and $p(x, y, y) = x$, so it is a [[Mal'cev term|Y203PPTS61]].

## Explanations

### L1 human

A vector space has a special point, the zero vector, but a plane in space has no special point.
The affine space keeps only the operations that do not depend on where zero is.
One may take weighted averages of points, such as the midpoint, but one may not add two points.
For example, in $\R^2$ the midpoint of $(0, 0)$ and $(2, 4)$ is $b_{1/2}((0,0), (2,4)) = (1, 2)$.
Moving every point by the same vector keeps all these operations, so such a move is a symmetry of the algebra.
