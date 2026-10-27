---
tag: 556HZEYCQF
kind: example
name: The special linear group is the kernel of the determinant
msc: [20G15]
instance_of: [0W88CEGQP1, 0CB0DX5BVV]
illustrates: [0C9ZKYSPYR]
uses: [0FCHE902D7, 0V9PMN0RBH, 0C3CFHDN6R, 0Z424HK8CQ]
sources:
  - url: https://en.wikipedia.org/wiki/Special_linear_group
    locator: lead section
---

## Example

Let $n \ge 1$. The [[determinant|0C3CFHDN6R]] is a homomorphism $\det : \mathrm{GL}_n(\mathbb{R}) \to \mathbb{R}^\times$, because $\det(AB) = \det(A)\det(B)$.
Here $\mathrm{GL}_n(\mathbb{R})$ is the [[general linear group|0FCHE902D7]], and $\mathbb{R}^\times$ is the group of nonzero real numbers under multiplication.
The [[kernel|0Z424HK8CQ]] of $\det$ is the set of matrices with determinant $1$. This is the [[special linear group|0V9PMN0RBH]] $\mathrm{SL}_n(\mathbb{R})$.
Thus $\mathrm{SL}_n(\mathbb{R})$ is a [[normal subgroup|0C9ZKYSPYR]] of $\mathrm{GL}_n(\mathbb{R})$.

## Remarks

For $n \ge 2$, the group $\mathrm{GL}_n(\mathbb{R})$ is not abelian. Thus the normality does not come from commutativity.
