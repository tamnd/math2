---
tag: X898DPBSY7
kind: statement
role: theorem
name: Baker–Campbell–Hausdorff formula
msc: ["22E60", 17B01]
uses: [7JBRGCVJRB, H3QX1ZFC8K, 020M04FN1H]
about: [H3QX1ZFC8K]
sources:
  - url: https://en.wikipedia.org/wiki/Baker%E2%80%93Campbell%E2%80%93Hausdorff_formula
same_as:
  wikidata: Q804316
  wikipedia: Baker–Campbell–Hausdorff formula
---

## Statement

Let $G$ be a real [[Lie group|7JBRGCVJRB]] with Lie algebra $\mathfrak{g}$ and [[exponential map|H3QX1ZFC8K]] $\exp \colon \mathfrak{g} \to G$.
There is a neighbourhood $U$ of $0$ in $\mathfrak{g}$ such that for all $X, Y \in U$,
$$\exp(X)\exp(Y) = \exp(Z(X, Y)),$$
where $Z(X, Y)$ is the sum of a convergent series
$$Z(X, Y) = X + Y + \tfrac12 [X, Y] + \tfrac1{12}[X, [X, Y]] - \tfrac1{12}[Y, [X, Y]] - \tfrac1{24}[Y, [X, [X, Y]]] + \cdots.$$
Each term of the series is a rational multiple of an iterated Lie bracket of $X$ and $Y$.
The coefficients do not depend on $G$.

## Remarks

The formula is first proved for formal power series in two non-commuting variables, where one shows that $\log(e^X e^Y)$ is a series of Lie polynomials.
Dynkin gave an explicit formula for all the coefficients.
Convergence for $X$ and $Y$ near $0$ then follows from estimates on the norms of iterated brackets.
For matrices, $e^X e^Y = e^{Z(X, Y)}$ with the [[matrix exponential|020M04FN1H]] when $X$ and $Y$ have small enough norm.
If $X$ and $Y$ commute, all brackets vanish and the formula reduces to $e^X e^Y = e^{X + Y}$.
If $[X, Y]$ commutes with both $X$ and $Y$, as in the Heisenberg group, the series stops after the first bracket: $e^X e^Y = e^{X + Y + \frac12[X, Y]}$.
Without the smallness condition the formula can fail.
In $SL_2(\R)$, take $X = \begin{pmatrix} 0 & -\pi \\ \pi & 0 \end{pmatrix}$ and $Y = \begin{pmatrix} 0 & 1 \\ 0 & 0 \end{pmatrix}$; then $e^X = -I$ and $e^X e^Y = \begin{pmatrix} -1 & -1 \\ 0 & -1 \end{pmatrix}$, which is not the exponential of any matrix of trace $0$.

## Explanations

### L1 human

For numbers, $e^x e^y = e^{x + y}$.
For matrices, and in Lie groups generally, this rule fails because the order of multiplication matters.
The formula says how to repair it: the exponent of the product is $X + Y$ plus correction terms built only from commutators $[X, Y] = XY - YX$ and commutators of commutators.

### L2 human

The formula shows that the group law near the identity is determined by the Lie bracket alone.
This is the key step in proving that a Lie algebra homomorphism integrates to a local homomorphism of groups, and in building a local Lie group from a Lie algebra.
For nilpotent Lie algebras the series is finite, so it defines a group law on the whole Lie algebra; this gives the simply connected nilpotent Lie groups.
Related formulas, such as the Lie product formula $e^{X + Y} = \lim_{n \to \infty} (e^{X/n} e^{Y/n})^n$, also express the interplay between the group and the bracket.
