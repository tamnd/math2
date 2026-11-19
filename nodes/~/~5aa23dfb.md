---
tag: ~5aa23dfb
kind: concept
name: Common errors in learning linear algebra
msc: ["97H60", "15-01"]
topics: [VKVAJ94SKZ]
audience: ug1
uses: [~0a3756c5, 032Q9FB8MT, 00KDZRW4C0, 0DTY8B9HMS, 0KCQ9Y3QKA, 03AJKXH1AV, 0N6960W0BV]
sources:
  - book: isbn:9780321982384
    locator: Section 2.1
  - book: isbn:9780321982384
    locator: Section 4.3
  - book: isbn:9781733146678
    locator: Chapter 3
  - url: https://en.wikipedia.org/wiki/Matrix_multiplication
    locator: Non-commutativity
  - url: https://en.wikipedia.org/wiki/Eigenvalues_and_eigenvectors
    locator: Formal definition
---

## Summary

This essay lists the errors that students of the [[overview|~0a3756c5]] make most often, each with a counterexample in numbers and the correct rule.
This node gives five main errors.
The first two are the beliefs that matrix products commute and that the determinant is additive.
The third is the confusion of a spanning set with a basis.
The fourth is the belief that row operations keep the column space.
The fifth is the acceptance of the zero vector as an eigenvector.
Each error comes from a rule of numbers that does not carry over to matrices or to vector spaces.
A small counterexample is the fastest way to correct each one.

## Motivation

Students bring the algebra of numbers to linear algebra.
Numbers commute, a product of nonzero numbers is nonzero, and a function of a sum is often the sum of the values.
Matrices and linear maps keep some of these rules and lose others.
The lost rules produce errors that look correct, so they need explicit counterexamples.

## Notation

$I$ is the identity matrix, $\det$ the determinant, $\operatorname{Col} A$ the column space and $\operatorname{Nul} A$ the null space of a matrix $A$.

## Remarks

### Examples

- [[Matrix products|032Q9FB8MT]] do not commute. For $A = \begin{pmatrix} 1 & 1 \\ 0 & 1 \end{pmatrix}$ and $B = \begin{pmatrix} 1 & 0 \\ 1 & 1 \end{pmatrix}$, $AB = \begin{pmatrix} 2 & 1 \\ 1 & 1 \end{pmatrix}$ but $BA = \begin{pmatrix} 1 & 1 \\ 1 & 2 \end{pmatrix}$. As a result, $(A + B)^2 = A^2 + AB + BA + B^2$, which is not $A^2 + 2AB + B^2$ in general.
- The [[determinant|00KDZRW4C0]] is not additive. For $A = B = I_2$, $\det(A + B) = \det(2 I_2) = 4$, but $\det A + \det B = 2$. The correct rules are $\det(AB) = \det A \det B$ and $\det(cA) = c^n \det A$ for $n \times n$ matrices.
- A [[spanning set|0DTY8B9HMS]] is not always a [[basis|0KCQ9Y3QKA]]. The vectors $(1, 0)$, $(0, 1)$, $(1, 1)$ span $\mathbb{R}^2$, but they are dependent: $(1, 1) = (1, 0) + (0, 1)$. A basis must span and be independent.
- Row operations change the [[column space|03AJKXH1AV]]. For $A = \begin{pmatrix} 1 & 2 \\ 2 & 4 \end{pmatrix}$, the operation $R_2 - 2R_1$ gives $R = \begin{pmatrix} 1 & 2 \\ 0 & 0 \end{pmatrix}$. Then $\operatorname{Col} A$ is the line through $(1, 2)$, but $\operatorname{Col} R$ is the line through $(1, 0)$.
- [[Eigenvectors|0N6960W0BV]] are nonzero. The equation $A \cdot 0 = \lambda \cdot 0$ holds for every $\lambda$, so the definition requires $v \neq 0$. The eigenvalue $0$ is allowed: $\begin{pmatrix} 1 & 1 \\ 1 & 1 \end{pmatrix} (1, -1) = (0, 0) = 0 \cdot (1, -1)$.

### Non-examples

- The rule $(AB)^{\mathsf{T}} = B^{\mathsf{T}} A^{\mathsf{T}}$ reverses the order. The rule $(A + B)^{\mathsf{T}} = A^{\mathsf{T}} + B^{\mathsf{T}}$ keeps it, so it is not an instance of the errors above.
- Some products do commute, for example $A$ with $I$, with $A^2$, or with $cI$. So a single commuting pair does not refute the first error.

### Basic properties

- Row operations keep the [[null space|0PHDYNR24D]] and the [[row space|069MCGX635]], and they keep the linear relations among the columns.
- So the pivot columns of the original $A$, not of its echelon form, give a basis of $\operatorname{Col} A$. In the example, $(1, 2)$ is a basis.
- A product of nonzero matrices can be $0$: $\begin{pmatrix} 0 & 1 \\ 0 & 0 \end{pmatrix}^2 = 0$. So $AB = AC$ does not give $B = C$ unless $A$ is invertible.
- The inverse of a product reverses the order: $(AB)^{-1} = B^{-1} A^{-1}$.

### History

The LACSG recommendations of 1993 and the studies collected by Dorier in 2000 brought these errors into the design of courses.
The essay on [[teaching linear algebra|~48fab349]] describes this work.

### Common errors

- Students check a rule on diagonal matrices only. Diagonal matrices commute with each other, so they hide the first error.
- Students check a claim about the column space on the echelon form and copy the answer back to $A$.

## Explanations

### L1 human

Numbers can be multiplied in either order: $2 \times 3 = 3 \times 2$.
Matrices are tables of numbers with their own product, and for them the order matters.
Several other habits from numbers also fail, and a small example shows each failure.

### L2 human

Worked check of the column space error with $A = \begin{pmatrix} 1 & 2 \\ 2 & 4 \end{pmatrix}$.

1. Is $(1, 0)$ in $\operatorname{Col} A$? Solve $x (1, 2) + y (2, 4) = (1, 0)$.
2. The equations are $x + 2y = 1$ and $2x + 4y = 0$.
3. Twice the first gives $2x + 4y = 2$, which contradicts the second. So $(1, 0) \notin \operatorname{Col} A$.
4. But $(1, 0) \in \operatorname{Col} R$, as the first column of $R$.

The typical use of the correct rule is to read off a basis of $\operatorname{Col} A$: find the pivot positions in $R$, and take those columns of $A$.
A trap: the null spaces of $A$ and $R$ are equal, so the dimension of the column space is the same, but the column spaces themselves are different.

### L3 human

Each error is a failed homomorphism: the determinant is multiplicative but not additive, and matrix multiplication is associative but not commutative.
Row operations are left multiplications by invertible matrices $E$, so $\operatorname{Nul}(EA) = \operatorname{Nul} A$ but $\operatorname{Col}(EA) = E \operatorname{Col} A$.
The sub-areas on [[matrices|Y1ESNQ2V52]], [[systems|DXSXFVDMXQ]], [[determinants|DTBK11SR77]] and [[eigenvalues|6R1D6QPY3S]] treat each rule in full.
