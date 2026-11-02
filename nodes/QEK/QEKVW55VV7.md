---
tag: QEKVW55VV7
kind: definition
name: Operator theory
msc: [47A05, 47B01, 47B02]
defines: YG9NR68ZH3
uses: [0NRYHJPQG2, 03J5RAKB30, 03TM135G0N, 06GZ956657, HM2HHE3J51]
sources:
  - url: https://en.wikipedia.org/wiki/Operator_theory
---

## Definition

Let $X$ and $Y$ be [[normed spaces|03J5RAKB30]], and let $D(T)$ be a linear subspace of $X$.
An *operator* from $X$ to $Y$ is a [[linear map|0NRYHJPQG2]] $T \colon D(T) \to Y$.
*Operator theory* is the branch of mathematics that studies operators.
Its main objects are the [[continuous linear maps|03TM135G0N]] between [[Banach spaces|06GZ956657]] and the operators on a [[Hilbert space|HM2HHE3J51]].
Its central questions concern invertibility, the spectrum, adjoints, invariant subspaces and the classification of operators.

## Remarks

Example: the right shift $S(x_1, x_2, \ldots) = (0, x_1, x_2, \ldots)$ on the space $\ell^2$ of square-summable sequences is an operator.
It preserves norms, so it is bounded with norm $1$.
It is injective but not surjective, since every vector in its image has first coordinate $0$.

Non-example: the map $x \mapsto \norm{x}^2 x$ on $\ell^2$ is not an operator in this sense, since it is not linear.
Such maps belong to nonlinear functional analysis.

On a finite-dimensional space, operator theory reduces to the linear algebra of matrices.

## Explanations

### L1 human

Operator theory is linear algebra for spaces of infinite dimension.
It studies maps that respect sums and scalar multiples, and that act on sequences or functions instead of finite lists of numbers.
