---
tag: 0P21AVFFSP
kind: definition
name: Equivalent matrices
msc: [15A21]
defines: 0CMHSGTWXB
uses: [0TWTS88TWN]
sources:
  - url: https://en.wikipedia.org/wiki/Matrix_equivalence
    locator: lead section
---

## Definition

Let $F$ be a field and let $A$ and $B$ be $m \times n$ matrices over $F$.
The matrix $B$ is *equivalent* to $A$ when there are an [[invertible|0EB9N0S33C]] $n \times n$ matrix $P$ and an invertible $m \times m$ matrix $Q$ over $F$ with
$$B = Q^{-1} A P.$$

## Remarks

Two matrices are equivalent if and only if they represent the same linear map $F^n \to F^m$ in two pairs of bases.
Two $m \times n$ matrices over a field are equivalent if and only if they have the same [[rank|0ZC9YTXZRY]].
A matrix of rank $r$ is equivalent to the block matrix $\begin{pmatrix} I_r & 0 \\ 0 & 0 \end{pmatrix}$.
[[Similarity|0E89HQATM8]] is a finer relation: similar matrices are equivalent, but equivalent square matrices need not be similar.

## Explanations

### L1 human

Matrix equivalence allows independent changes of basis on the input side and on the output side.
With so much freedom, only the rank survives.
Every matrix of rank $r$ becomes the identity of size $r$, padded with zeros.
