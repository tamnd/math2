---
tag: 556HZEYCQF
kind: example
name: The special linear group is the kernel of the determinant
msc: ["20G15"]
topics: [E1506A5A55]
audience: ug1
instance_of: [0W88CEGQP1, 0CB0DX5BVV]
illustrates: [0C9ZKYSPYR]
uses: [0FCHE902D7, 0V9PMN0RBH, 00KDZRW4C0, F5HJCNFJWJ, 0W88CEGQP1, 0C9ZKYSPYR]
sources:
  - url: https://en.wikipedia.org/wiki/Special_linear_group
    locator: lead section
  - url: https://en.wikipedia.org/wiki/General_linear_group
    locator: Special linear group
---

## Example

Let $n \ge 1$, let $\mathrm{GL}_n(\mathbb{R})$ be the [[general linear group|0FCHE902D7]], and let $\mathbb{R}^\times$ be the nonzero real numbers under multiplication.
Consider the [[determinant|00KDZRW4C0]] $\det \colon \mathrm{GL}_n(\mathbb{R}) \to \mathbb{R}^\times$.

1. The map is a homomorphism, because $\det(AB) = \det(A)\det(B)$ ([[determinant of a product|F5HJCNFJWJ]]).
2. The identity of $\mathbb{R}^\times$ is $1$. So the [[kernel|0W88CEGQP1]] is the set of matrices with determinant $1$, the [[special linear group|0V9PMN0RBH]] $\mathrm{SL}_n(\mathbb{R})$.
3. For $n = 2$, the matrix $\begin{pmatrix} 2 & 0 \\ 0 & 1/2 \end{pmatrix}$ has determinant $2 \cdot \tfrac{1}{2} = 1$, so it lies in the kernel.
4. By [[kernels are normal|0C9ZKYSPYR]], $\mathrm{SL}_n(\mathbb{R})$ is a [[normal subgroup|0CB0DX5BVV]]. Directly, $\det(gAg^{-1}) = \det(g)\det(A)\det(g)^{-1} = \det(A)$.
5. The map is surjective: the diagonal matrix with entries $t, 1, \dots, 1$ has determinant $t$.
6. By the [[first isomorphism theorem|0CXXJNG5B6]], $\mathrm{GL}_n(\mathbb{R})/\mathrm{SL}_n(\mathbb{R}) \cong \mathbb{R}^\times$.

## Remarks

The example shows a normal subgroup in a group that is not abelian.
For $n \ge 2$, the matrices $A = \begin{pmatrix} 1 & 1 \\ 0 & 1 \end{pmatrix}$ and $B = \begin{pmatrix} 1 & 0 \\ 1 & 1 \end{pmatrix}$ give $AB = \begin{pmatrix} 2 & 1 \\ 1 & 1 \end{pmatrix}$ and $BA = \begin{pmatrix} 1 & 1 \\ 1 & 2 \end{pmatrix}$.
So the normality of $\mathrm{SL}_n(\mathbb{R})$ does not come from commutativity.
For $n = 1$, $\mathrm{GL}_1(\mathbb{R}) = \mathbb{R}^\times$, the determinant is the identity map, and the kernel is $\{1\}$.
The same holds over each [[field|04C5ZBG1WT]] $F$: $\mathrm{SL}_n(F)$ is the kernel of $\det \colon \mathrm{GL}_n(F) \to F^\times$.

## Explanations

### L1 human

The determinant of a matrix measures how the matrix scales areas or volumes.
The matrices with determinant $1$ keep all volumes the same.
These matrices are exactly the ones that the determinant sends to the identity $1$.
So they form the kernel of the determinant.

### L2 human

We check normality on a concrete pair in $\mathrm{GL}_2(\mathbb{R})$.

1. Let $A = \begin{pmatrix} 1 & 1 \\ 0 & 1 \end{pmatrix}$, with $\det A = 1$, and let $g = \begin{pmatrix} 2 & 0 \\ 0 & 1 \end{pmatrix}$.
2. Then $g^{-1} = \begin{pmatrix} 1/2 & 0 \\ 0 & 1 \end{pmatrix}$ and $gAg^{-1} = \begin{pmatrix} 1 & 2 \\ 0 & 1 \end{pmatrix}$.
3. The conjugate has determinant $1$, so it lies in $\mathrm{SL}_2(\mathbb{R})$ again.

The typical use is to prove normality with no computation of conjugates: a kernel is always normal.
The trap is the value $0$.
The kernel is the set where $\det = 1$, because $1$ is the identity of $\mathbb{R}^\times$, and no matrix in $\mathrm{GL}_n(\mathbb{R})$ has determinant $0$.
