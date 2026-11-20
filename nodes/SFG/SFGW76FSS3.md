---
tag: SFGW76FSS3
kind: example
name: The trace of the derivative on polynomials of degree at most 2
msc: ["15A04", "15A15"]
topics: [S6559D61BP]
audience: ug1
instance_of: [0KZDNGA561]
illustrates: [0WCPH5Z7FA]
uses: [0RPDTWY2JS, 0YQSGNYE3K, 07PTPSZPME]
sources:
  - url: https://en.wikipedia.org/wiki/Trace_(linear_algebra)
    locator: Trace of a linear operator
---

## Example

Let $V = \mathcal{P}_2$ be the real polynomials of degree at most $2$, and let $D \colon V \to V$, $D(p) = p'$.
We compute the [[trace|0RPDTWY2JS]] of $D$ in two bases.

1. Standard basis $B = (1, x, x^2)$. $D(1) = 0$, $D(x) = 1$ and $D(x^2) = 2x$.
2. The coordinate vectors of these images are $(0, 0, 0)$, $(1, 0, 0)$ and $(0, 2, 0)$. They are the columns of the [[matrix|0YQSGNYE3K]]
$$[D]_B = \begin{pmatrix} 0 & 1 & 0 \\ 0 & 0 & 2 \\ 0 & 0 & 0 \end{pmatrix}.$$
3. The [[trace|07PTPSZPME]] is $0 + 0 + 0 = 0$.
4. Second basis $B' = (b_1, b_2, b_3) = (1 + x,\ 1 - x,\ x^2)$. These are linearly independent, since $1 = (b_1 + b_2)/2$ and $x = (b_1 - b_2)/2$ recover the standard basis.
5. $D(b_1) = 1 = \tfrac{1}{2} b_1 + \tfrac{1}{2} b_2$. Check: $\tfrac{1}{2}(1 + x) + \tfrac{1}{2}(1 - x) = 1$.
6. $D(b_2) = -1 = -\tfrac{1}{2} b_1 - \tfrac{1}{2} b_2$.
7. $D(b_3) = 2x = b_1 - b_2$. Check: $(1 + x) - (1 - x) = 2x$.
8. So
$$[D]_{B'} = \begin{pmatrix} 1/2 & -1/2 & 1 \\ 1/2 & -1/2 & -1 \\ 0 & 0 & 0 \end{pmatrix}.$$
9. The trace is $\tfrac{1}{2} + (-\tfrac{1}{2}) + 0 = 0$.
10. The two matrices are different, but both traces are $0$. So $\tr D = 0$.

## Remarks

- In the basis $B'$ the diagonal entries are not $0$, but their sum is $0$.
- $D$ is nilpotent, since $D^3 = 0$. Every nilpotent endomorphism has trace $0$.

## Explanations

### L1 human

The derivative has a different matrix in each basis.
The diagonal sum is the same for every basis, and here it is $0$.

### L2 human

The two matrices are similar, through the change of basis matrix from $B$ to $B'$.
Similar matrices have the same trace, so the trace of $D$ does not depend on the basis.
