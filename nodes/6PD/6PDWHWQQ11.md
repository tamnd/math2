---
tag: 6PDWHWQQ11
kind: definition
name: Lie bracket of vector fields
msc: [58A05, 53A45]
defines: 68FGQEBD6J
uses: [F45VQ47GPV, WY6K3P4YCG, WWX7H5W1RP, 0V33BNKZ9S]
sources:
  - url: https://en.wikipedia.org/wiki/Lie_bracket_of_vector_fields
---

## Definition

Let $M$ be a [[smooth manifold|F45VQ47GPV]], and let $C^\infty(M)$ be the algebra of [[smooth functions|0V33BNKZ9S]] on $M$.
A smooth vector field $X$ on $M$ is a smooth [[section|WWX7H5W1RP]] of the [[tangent bundle|WY6K3P4YCG]]; it acts on $f \in C^\infty(M)$ by $(Xf)(p) = X_p(f)$.
For smooth vector fields $X$ and $Y$ on $M$, the *Lie bracket* $[X, Y]$ is the vector field given by
$$[X, Y] f = X(Y f) - Y(X f), \qquad f \in C^\infty(M).$$

## Remarks

In local coordinates, with $X = \sum_i X^i \partial_i$ and $Y = \sum_j Y^j \partial_j$,
$$[X, Y] = \sum_{j} \sum_{i} \left( X^i \frac{\partial Y^j}{\partial x^i} - Y^i \frac{\partial X^j}{\partial x^i} \right) \partial_j.$$
Example on $\R^2$: for $X = \partial_x$ and $Y = x \, \partial_y$, one gets $[X, Y] f = \partial_x(x f_y) - x f_{yx} = f_y$, so $[X, Y] = \partial_y$.

The product $f \mapsto X(Y f)$ alone is not a vector field.
For $X = Y = \partial_x$ on $\R$, it is $f \mapsto f''$, and $(fg)'' = f'' g + 2 f' g' + f g''$, so the product rule fails.
In the bracket the second-order terms cancel, and the product rule holds.

The bracket is bilinear and antisymmetric, and it satisfies the Jacobi identity $[X, [Y, Z]] + [Y, [Z, X]] + [Z, [X, Y]] = 0$.
So the smooth vector fields on $M$ form a Lie algebra.
The bracket $[X, Y]$ equals the [[Lie derivative|PJWK0PKN6Q]] $\mathcal{L}_X Y$.

## Explanations

### L1 human

The Lie bracket of two vector fields is the commutator $XY - YX$ of the two derivations they define, which is again a vector field.
