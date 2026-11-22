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

A transvection can have a matrix that looks nothing like $I + cE_{ij}$.
On $\mathbb{R}^2$ let $\varphi(x) = x_1 - x_2$ and $v = (1, 1)^{\mathsf{T}}$, and let $\tau(x) = x + \varphi(x)v$.
Here $\varphi \ne 0$, $v \ne 0$ and $\varphi(v) = 1 - 1 = 0$, so $\tau$ is a [[transvection|0NMN00FNW1]] in the coordinate-free sense.

On the standard basis,
$$\tau(e_1) = e_1 + 1 \cdot v = \begin{pmatrix} 2 \\ 1 \end{pmatrix}, \qquad \tau(e_2) = e_2 - 1 \cdot v = \begin{pmatrix} -1 \\ 0 \end{pmatrix},$$
so the matrix of $\tau$ is
$$A = \begin{pmatrix} 2 & -1 \\ 1 & 0 \end{pmatrix} = I_2 + \begin{pmatrix} 1 \\ 1 \end{pmatrix} \begin{pmatrix} 1 & -1 \end{pmatrix}.$$
Its diagonal entries are $2$ and $0$, so it is not of the form $I_2 + cE_{ij}$.
Still, $\det A = 2 \cdot 0 - (-1) \cdot 1 = 1$, and $A$ fixes the line $x_1 = x_2$ pointwise, since $A(t, t)^{\mathsf{T}} = (2t - t, t)^{\mathsf{T}} = (t, t)^{\mathsf{T}}$.

In a better [[basis|0KCQ9Y3QKA]], $\tau$ is an ordinary shear.
Take $b_1 = v = (1, 1)^{\mathsf{T}}$ and $b_2 = (1, 0)^{\mathsf{T}}$.
Then $\tau(b_1) = b_1$, and $\tau(b_2) = (2, 1)^{\mathsf{T}} = b_1 + b_2$, so the [[matrix of $\tau$|0YQSGNYE3K]] in this basis is $T_{12}(1) = \begin{pmatrix} 1 & 1 \\ 0 & 1 \end{pmatrix}$.
Check with $P = [b_1 \; b_2]$:
$$AP = \begin{pmatrix} 2 & -1 \\ 1 & 0 \end{pmatrix} \begin{pmatrix} 1 & 1 \\ 1 & 0 \end{pmatrix} = \begin{pmatrix} 1 & 2 \\ 1 & 1 \end{pmatrix} = \begin{pmatrix} 1 & 1 \\ 1 & 0 \end{pmatrix} \begin{pmatrix} 1 & 1 \\ 0 & 1 \end{pmatrix} = P\,T_{12}(1),$$
so $A = P\,T_{12}(1)\,P^{-1}$.

## Remarks

Being a transvection is a property of a linear map, while the form $T_{ij}(c)$ belongs to one particular basis.
The same choice of basis, $v$ first and then a vector on which $\varphi$ is $1$, shows that every transvection of the plane is conjugate to $T_{12}(1)$.

The condition $\varphi(v) = 0$ cannot be dropped.
With $v = (1, 0)^{\mathsf{T}}$, for which $\varphi(v) = 1$, the same recipe gives
$$I_2 + \begin{pmatrix} 1 \\ 0 \end{pmatrix} \begin{pmatrix} 1 & -1 \end{pmatrix} = \begin{pmatrix} 2 & -1 \\ 0 & 1 \end{pmatrix},$$
which has determinant $2$ and is a dilation, not a transvection.

## Explanations

### L1 human

This map slides each point along the direction $(1, 1)$, by an amount proportional to how far the point is from the line $x_1 = x_2$.
In tilted coordinates, it is an ordinary shear.

### L2 human

The point is the condition $\varphi(v) = 0$: the direction of the slide lies in the fixed line.
To recognize a transvection from its matrix, check that $A - I$ has rank $1$ and $(A - I)^2 = 0$; here $A - I = \begin{pmatrix} 1 & -1 \\ 1 & -1 \end{pmatrix}$, whose square is $0$.
A trap: a matrix can be a transvection even if no entry looks like a shear.
