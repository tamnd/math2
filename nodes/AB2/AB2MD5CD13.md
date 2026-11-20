---
tag: AB2MD5CD13
kind: concept
name: Matrix ring
msc: ["15A99", "16S50"]
topics: [Y1ESNQ2V52]
audience: ug1
specializes: [0B1261B5ED]
uses: [0CP7YY6NAG, 0BVXADM10P, 076JGP6R3T, 0894J980RK]
sources:
  - url: https://en.wikipedia.org/wiki/Matrix_ring
    locator: lead section
  - url: https://en.wikipedia.org/wiki/Matrix_ring
    locator: Properties
  - url: https://en.wikipedia.org/wiki/Matrix_(mathematics)
    locator: Abstract algebraic aspects and generalizations
---

## Summary

For a [[ring|0B1261B5ED]] $R$ and an integer $n \ge 1$, the matrix ring $M_n(R)$ is the set of $n \times n$ [[square matrices|0CP7YY6NAG]] over $R$ with [[matrix addition|0BVXADM10P]] and [[matrix multiplication|076JGP6R3T]].
It is a ring with zero $0_n$ and identity $I_n$; the [[object page|0FHVPRAE60]] describes it.
For $n \ge 2$ and $R \neq 0$, it is not commutative and it has [[zero divisors|0NNRDW10RZ]].
Its [[centre|DVZ1V4A884]] is the set of scalar matrices $cI$ with $c$ central in $R$.
Over a field it has [[no two-sided ideals other than 0 and itself|Z46WD9W1ZS]].
Matrix rings are the standard source of examples and counterexamples in [[ring theory|0B1261B5ED]].

## Motivation

The ring axioms for $M_n(R)$ follow from the [[associativity|073E4XC016]] and the [[distributivity|0RXD6EZYBK]] of the product.
So the $n \times n$ matrices have an algebra of their own: we can form $A^2 + 3A - I$ and solve equations in $A$.
This algebra is the algebra of the linear maps $F^n \to F^n$, written in coordinates.
It shows at once which rules of school algebra survive and which fail: $AB \neq BA$, and $AB = 0$ with $A, B \neq 0$.

## Notation

- Books write $M_n(R)$, $\mathrm{M}_n(R)$, $\operatorname{Mat}_n(R)$ or $R^{n \times n}$.
- For a field $F$, $M_n(F)$ is also written $\mathfrak{gl}_n(F)$ when it is viewed as a Lie algebra with the bracket $AB - BA$.
- In Mathlib, `Matrix (Fin n) (Fin n) R` is a `Ring` when `R` is a ring, and an `Algebra R _` when `R` is commutative.

## Remarks

### Examples

- [[The ring M₂(F₂)|DWKSAB7V4T]] has $16$ elements, and it is not commutative.
- [[The ring M₂(ℝ) contains a copy of ℂ|GHV77C35RT]], the matrices $\begin{pmatrix} a & -b \\ b & a \end{pmatrix}$.
- $M_1(R) \cong R$ by the [[1 × 1 example|WYJ95EEQFJ]].
- $M_n(\mathbb{Z})$ is a ring whose units are the integer matrices with determinant $\pm 1$.

### Non-examples

- [[The set of all matrices of all sizes|Q3FKC0FMXR]] is not a ring, because the sum of two matrices of different sizes is not defined.
- The $2 \times 3$ matrices with addition form a group, but they have no product, so they are not a ring.

### Basic properties

- $M_n(R)$ is a ring with identity $I_n$, by the [[associativity theorem|073E4XC016]] and the [[distributive law|0RXD6EZYBK]].
- For $n \ge 2$ and $R \neq 0$, $E_{12} E_{21} = E_{11} \neq E_{22} = E_{21} E_{12}$, so $M_n(R)$ is not commutative.
- For $n \ge 2$ and $R \neq 0$, $E_{12}^2 = 0$, so $M_n(R)$ has nonzero [[nilpotent elements|0ZB2JG1M9C]].
- The [[centre theorem|DVZ1V4A884]] gives $Z(M_n(R)) = \{cI : c \in Z(R)\}$.
- The [[ideal theorem|Z46WD9W1ZS]] shows that $M_n(F)$ is a [[simple ring|62M0NC3E2T]] for a field $F$; more generally, $M_n(R)$ is [[simple when R is simple|J41Y7CCE6B]].
- Over a commutative ring $R$, $M_n(R)$ is an [[associative algebra|1SENAHZW5A]] over $R$, and over a field $F$ it has dimension $n^2$.
- The units of $M_n(R)$ are the [[invertible matrices|0EB9N0S33C]]; they form the [[general linear group|0FCHE902D7]] $GL_n(R)$.

### History

- Cayley noted in 1858 that matrices can be added and multiplied like numbers, but that the product is not commutative.
- Wedderburn proved in 1908 that every finite-dimensional simple algebra over a field is a matrix ring $M_n(D)$ over a division algebra $D$.

### Common errors

- Using $(A + B)^2 = A^2 + 2AB + B^2$ or $(AB)^k = A^k B^k$ in $M_n(R)$, which need $AB = BA$.
- Concluding $A = 0$ or $B = 0$ from $AB = 0$.
- Concluding $A = \pm I$ from $A^2 = I$: the [[involutory matrices|NH2QE3671N]] include $\begin{pmatrix} 0 & 1 \\ 1 & 0 \end{pmatrix}$.

## Explanations

### L1 human

Square matrices of one fixed size can be added and multiplied, and the result is again a square matrix of that size.
They follow most of the rules of numbers.
The main differences are that $AB$ can differ from $BA$, and that $AB$ can be zero when $A$ and $B$ are not.

### L2 human

A ring is a set with an addition and a multiplication that satisfy the usual laws, except possibly commutativity of the product.
The matrices $M_n(F)$ are the first ring most students meet in which the product is not commutative.
Many questions about one matrix are questions about the subring $F[A]$ of polynomials in $A$, which is commutative.

### L3 human

The ring $M_n(R)$ is isomorphic to the endomorphism ring of the free right module $R^n$.
It is [[Morita equivalent|JEBXXWHW8M]] to $R$, so it has the same category of modules up to equivalence.
Its two-sided ideals are exactly the sets $M_n(I)$ for the two-sided ideals $I$ of $R$.
The polynomial identity of Amitsur and Levitzki, the [[standard identity of degree 2n|YDH60KPTWT]], holds in $M_n(R)$ for commutative $R$.
These facts belong to [[ring theory|0B1261B5ED]], and the special matrix rings of analysis belong to other areas.
