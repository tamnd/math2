---
tag: 0YZ3T5Q7XN
kind: example
name: Determinant as a group homomorphism
msc: ["15A15"]
topics: [E1506A5A55]
audience: ug1
instance_of: [0JYTG5K9Y4]
illustrates: [0CXXJNG5B6]
uses: [0FCHE902D7, 00KDZRW4C0, F5HJCNFJWJ, 0V9PMN0RBH, 0W88CEGQP1, 0C9ZKYSPYR, 0CXXJNG5B6]
sources:
  - url: https://en.wikipedia.org/wiki/Determinant
    locator: Invertibility
  - url: https://en.wikipedia.org/wiki/General_linear_group
    locator: In terms of determinants
  - book: isbn:9780471433347
    locator: Section 11.4
---

## Example

Let $n$ be a positive integer, and let $\mathrm{GL}_n(\mathbb{R})$ be the [[general linear group|0FCHE902D7]] of invertible $n \times n$ real matrices under matrix multiplication.
Let $\mathbb{R}^\times$ be the group of nonzero real numbers under multiplication.
The [[determinant|00KDZRW4C0]] $\det \colon \mathrm{GL}_n(\mathbb{R}) \to \mathbb{R}^\times$ is a surjective [[group homomorphism|0JYTG5K9Y4]] with kernel $\mathrm{SL}_n(\mathbb{R})$.

1. The map has values in $\mathbb{R}^\times$. For $A \in \mathrm{GL}_n(\mathbb{R})$, we have $\det(A)\det(A^{-1}) = \det(AA^{-1}) = \det(I) = 1$, so $\det(A) \ne 0$.
2. The map is a homomorphism, because $\det(AB) = \det(A)\det(B)$ for all $A, B$ by [[the product rule for determinants|F5HJCNFJWJ]].
3. The [[kernel|0W88CEGQP1]] is the set of matrices with determinant $1$. This is the [[special linear group|0V9PMN0RBH]] $\mathrm{SL}_n(\mathbb{R})$.
4. By [[kernels are normal|0C9ZKYSPYR]], $\mathrm{SL}_n(\mathbb{R})$ is a normal subgroup of $\mathrm{GL}_n(\mathbb{R})$.
5. The map is surjective. For $a \in \mathbb{R}^\times$, the diagonal matrix $\operatorname{diag}(a, 1, \ldots, 1)$ is invertible and has determinant $a$.
6. By the [[first isomorphism theorem|0CXXJNG5B6]], $\mathrm{GL}_n(\mathbb{R})/\mathrm{SL}_n(\mathbb{R}) \cong \mathbb{R}^\times$.

A numerical check for $n = 2$: let $A = \begin{pmatrix} 1 & 2 \\ 3 & 4 \end{pmatrix}$ and $B = \begin{pmatrix} 0 & 1 \\ 1 & 1 \end{pmatrix}$.
Then $\det A = 4 - 6 = -2$ and $\det B = 0 - 1 = -1$.
The product is $AB = \begin{pmatrix} 2 & 3 \\ 4 & 7 \end{pmatrix}$, and $\det(AB) = 14 - 12 = 2 = (-2)(-1)$.

## Remarks

The same holds for complex matrices, with $\mathrm{GL}_n(\mathbb{C}) \to \mathbb{C}^\times$.
Over any [[field|04C5ZBG1WT]] $F$, the product rule also holds, so $\det \colon \mathrm{GL}_n(F) \to F^\times$ is a surjective homomorphism and $\mathrm{GL}_n(F)/\mathrm{SL}_n(F) \cong F^\times$.
For $n = 1$, a $1 \times 1$ matrix is a nonzero number, and $\det$ is an isomorphism with trivial kernel.
Over the field $\mathbb{F}_2$ with two elements, $\mathbb{F}_2^\times = \{1\}$, so $\mathrm{SL}_2(\mathbb{F}_2) = \mathrm{GL}_2(\mathbb{F}_2)$, a group of order $6$.
The coset $A\,\mathrm{SL}_n(\mathbb{R})$ is the set of all matrices with the same determinant as $A$.
Since $\mathbb{R}^\times$ is abelian, $\det(PAP^{-1}) = \det(P)\det(A)\det(P)^{-1} = \det(A)$, so [[similar matrices|0E89HQATM8]] have the same determinant.

## Explanations

### L1 human

The determinant turns a product of matrices into a product of numbers.
That is exactly what a homomorphism does.
The matrices that it sends to $1$ form a subgroup, the special linear group.
For real matrices, the determinant tells how the matrix scales areas or volumes, and whether it reverses orientation.
Doing two such maps one after the other multiplies the scale factors.

### L2 human

The kernel $\mathrm{SL}_n(\mathbb{R})$ is normal, so the quotient group $\mathrm{GL}_n(\mathbb{R})/\mathrm{SL}_n(\mathbb{R})$ exists.
Two matrices are in the same coset if and only if they have the same determinant.
So the quotient is a copy of $\mathbb{R}^\times$, as step 6 says.
The shear $\begin{pmatrix} 1 & 1 \\ 0 & 1 \end{pmatrix}$ has determinant $1$, so it lies in the kernel; it is invertible but not the identity, so $\det$ is not injective for $n \ge 2$.
A trap is to think that the determinant is additive.
For $A = B = I_2$, we get $\det(A + B) = \det(2I_2) = 4$, but $\det A + \det B = 2$.
The determinant is a homomorphism for multiplication, not for addition, and the set of all $n \times n$ matrices with addition is not its domain.
