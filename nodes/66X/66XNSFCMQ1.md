---
tag: 66XNSFCMQ1
kind: example
name: A transvection that is not an elementary matrix
msc: ["15A23"]
topics: [P8J6QR66TJ]
audience: ug2
instance_of: [0DTCBCKEJP]
not_instance_of:
  - target: 01REXW3WWE
    note: the matrix has diagonal entries 2 and 0, so it is not of the form I + cE_ij in the standard basis, although it is a transvection in the coordinate-free sense
uses: [0NMN00FNW1, 0KCQ9Y3QKA, 0YQSGNYE3K, 0CCQV3884B]
sources:
  - url: https://en.wikipedia.org/wiki/Shear_mapping
    locator: Definition
  - url: https://en.wikipedia.org/wiki/Special_linear_group
    locator: Generators and relations
---

## Example

Let $\varphi(x) = x_1 - x_2$ on $\mathbb{R}^2$ and $v = (1, 1)^{\mathsf{T}}$.
Let $\tau(x) = x + \varphi(x) v$, a [[transvection|0NMN00FNW1]] in the coordinate-free sense.

1. $\varphi(v) = 1 - 1 = 0$, $\varphi \ne 0$ and $v \ne 0$, as the definition asks.
2. $\tau(e_1) = e_1 + 1 \cdot v = (2, 1)^{\mathsf{T}}$ and $\tau(e_2) = e_2 - 1 \cdot v = (-1, 0)^{\mathsf{T}}$. So the matrix of $\tau$ is $A = \begin{pmatrix} 2 & -1 \\ 1 & 0 \end{pmatrix} = I_2 + v\varphi$, where $\varphi = (1, -1)$ as a row.
3. $\det A = 2 \cdot 0 - (-1) \cdot 1 = 1$.
4. $\tau$ fixes the line $x_1 = x_2$ pointwise: $A(t, t)^{\mathsf{T}} = (2t - t, \; t)^{\mathsf{T}} = (t, t)^{\mathsf{T}}$.
5. $A$ is not of the form $I_2 + cE_{ij}$, because its diagonal entries are $2$ and $0$.
6. In the [[basis|0KCQ9Y3QKA]] $b_1 = v = (1, 1)^{\mathsf{T}}$, $b_2 = (1, 0)^{\mathsf{T}}$: $\tau(b_1) = b_1$ by step 4, and $\tau(b_2) = (2, 1)^{\mathsf{T}} = b_1 + b_2$.
7. So the [[matrix of $\tau$|0YQSGNYE3K]] in this basis is $\begin{pmatrix} 1 & 1 \\ 0 & 1 \end{pmatrix} = T_{12}(1)$.
8. Check with $P = [b_1 \; b_2] = \begin{pmatrix} 1 & 1 \\ 1 & 0 \end{pmatrix}$: $AP = \begin{pmatrix} 2 - 1 & 2 \\ 1 & 1 \end{pmatrix} = \begin{pmatrix} 1 & 2 \\ 1 & 1 \end{pmatrix}$ and $P\, T_{12}(1) = \begin{pmatrix} 1 & 1 + 1 \\ 1 & 1 + 0 \end{pmatrix} = \begin{pmatrix} 1 & 2 \\ 1 & 1 \end{pmatrix}$. So $A = P\, T_{12}(1)\, P^{-1}$.

## Remarks

The example shows that "transvection" is a property of a linear map, while $T_{ij}(c)$ is a matrix in one particular basis.
Each transvection is conjugate to $T_{12}(1)$, by the same choice of basis.
If we take $v$ with $\varphi(v) \ne 0$, for example $v = (1, 0)^{\mathsf{T}}$, then $I_2 + v\varphi = \begin{pmatrix} 2 & -1 \\ 0 & 1 \end{pmatrix}$ has determinant $2$ and is a dilation, not a transvection.

## Explanations

### L1 human

This map slides each point along the direction $(1, 1)$, by an amount that depends on how far the point is from the line $x_1 = x_2$.
In tilted coordinates, it is an ordinary shear.

### L2 human

The point is the condition $\varphi(v) = 0$: the direction of the slide lies in the fixed line.
A trap: a matrix can be a transvection even if no entry looks like a shear.
