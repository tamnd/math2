---
tag: VND2T4RZK8
kind: example
name: The diagonal sum with two different bases is not the trace
msc: ["15A04", "15A15"]
topics: [S6559D61BP]
audience: ug1
not_instance_of:
  - target: 0KZDNGA561
    note: for the identity of R^2 with B = (e_1, e_2) and C = (2e_1, e_2), the matrix of the identity from B to C is diag(1/2, 1), with diagonal sum 3/2, but the trace of the identity is 2
uses: [0RPDTWY2JS, 0YQSGNYE3K, 07PTPSZPME]
sources:
  - url: https://en.wikipedia.org/wiki/Trace_(linear_algebra)
    locator: Trace of a linear operator
---

## Example

A matrix of a map with one basis for the input and another for the output can have the wrong diagonal sum.
Let $V = \mathbb{R}^2$, let $B = (e_1, e_2)$ be the standard basis, and let $C = (2e_1, e_2)$.
Let $\mathrm{id} \colon V \to V$ be the identity map.

1. In the basis $B$, $[\mathrm{id}]_B = I_2$, so the [[trace|0RPDTWY2JS]] of $\mathrm{id}$ is $1 + 1 = 2$.
2. Now use $B$ for the domain and $C$ for the codomain.
   Since $\mathrm{id}(e_1) = e_1 = \tfrac{1}{2}(2e_1) + 0 \cdot e_2$, the first column is $(1/2, 0)$.
3. Since $\mathrm{id}(e_2) = e_2 = 0 \cdot (2e_1) + 1 \cdot e_2$, the second column is $(0, 1)$.
4. So the [[matrix|0YQSGNYE3K]] is $[\mathrm{id}]_{C,B} = \operatorname{diag}(1/2, 1)$.
5. Its diagonal sum is $\tfrac{1}{2} + 1 = \tfrac{3}{2} \ne 2$.
6. So the diagonal sum of a matrix of a map with two different bases is not the trace of the map.
7. With the same basis $C$ on both sides, $[\mathrm{id}]_C = I_2$ again, with [[trace|07PTPSZPME]] $2$.

## Remarks

The matrix $[\mathrm{id}]_{C,B}$ has as columns the coordinates of $e_1$ and $e_2$ in $C$.
So it is the change of basis matrix from $C$ to $B$, the inverse of the change of basis matrix $\operatorname{diag}(2, 1)$ from $B$ to $C$.
It is not the matrix of an endomorphism in one basis.
With two bases of $\mathbb{R}^2$, every invertible $2 \times 2$ matrix is a matrix of $\mathrm{id}$, so the diagonal sum can take any real value.
For example, $\operatorname{diag}(t, 1)$ with $t \ne 0$ has diagonal sum $t + 1$, and $\begin{pmatrix} 1 & 1 \\ -1 & 0 \end{pmatrix}$ is invertible with diagonal sum $1$.

## Explanations

### L1 human

The trace of a linear map uses one basis, the same one for the input and the output.
With two bases, the diagonal sum depends on the bases and means nothing for the map.

### L2 human

A change of the codomain basis alone multiplies the matrix on the left by an invertible matrix.
This is not a similarity, so the trace can change.
Only the simultaneous change $P^{-1} M P$ keeps the trace.
