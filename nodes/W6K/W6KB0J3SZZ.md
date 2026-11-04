---
kind: statement
msc:
- 15A04
name: A map from R^n to R^m is a matrix transformation if and only if it is linear
role: proposition
sources:
- locator: src/section2-6.xml:465
  url: https://github.com/davidaustinm/ula/blob/b6ea263ef23703072b7007485bb7a2d89c5f399b/src/section2-6.xml#L465
tag: W6KB0J3SZZ
uses:
- 0NRYHJPQG2
about:
- 0NRYHJPQG2
---

## Statement

Let $T \colon \mathbb{R}^n \to \mathbb{R}^m$ be a function. There is an $m \times n$ matrix $A$ with $T(x) = Ax$ for all $x \in \mathbb{R}^n$ if and only if $T$ is a [[linear map|0NRYHJPQG2]]. That is, $T(cv) = cT(v)$ and $T(v+w) = T(v) + T(w)$ for all scalars $c$ and all vectors $v, w$.

When this holds, the matrix $A$ is the one whose $j$-th column is $T(e_j)$, where $e_1, \dots, e_n$ are the standard basis vectors of $\mathbb{R}^n$. So $A = [\,T(e_1)\ \ T(e_2)\ \cdots\ T(e_n)\,]$.

## Remarks

Multiplication by a matrix always respects sums and scalar multiples. The converse holds because each $x = \sum_j x_j e_j$ is sent to $\sum_j x_j T(e_j)$, which is the product of the matrix of these columns with $x$.
