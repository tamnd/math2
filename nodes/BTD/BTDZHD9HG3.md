---
tag: BTDZHD9HG3
kind: example
name: Projective special linear group
msc: [20G40, 20D06]
instance_of: [G5S1M9]
sources:
  - url: https://en.wikipedia.org/wiki/Projective_linear_group
---

## Example

Let $F$ be a field and let $n \ge 2$ be an integer.
The *projective special linear group* is the [[quotient group|0KYX2N69J0]]
$$PSL_n(F) = SL_n(F) / Z,$$
where $SL_n(F)$ is the [[special linear group|0V9PMN0RBH]] and $Z$ is its [[centre|0DZ93493VN]].
The centre $Z$ consists of the scalar matrices $\lambda I_n$ with $\lambda^n = 1$.
For a [[finite field|0ZXZ82FTX2]] $\F_q$ with $q$ elements, write $PSL_n(q)$.

Take $n = 2$ and $q = 7$.
The order of $SL_2(7)$ is $q(q^2 - 1) = 7 \cdot 48 = 336$.
The scalars $\lambda I_2$ with $\lambda^2 = 1$ are $\pm I_2$, so $\abs{Z} = 2$.
Hence $PSL_2(7)$ has order $168$.
It is a [[simple group|0YMYMNQ0QZ]], and it is the second smallest non-abelian simple group, after the alternating group $A_5$ of order $60$.

## Remarks

The group $PSL_n(q)$ has order
$$\frac{1}{\gcd(n, q - 1)} \, q^{n(n-1)/2} \prod_{i=2}^{n} (q^i - 1).$$
It is simple for all $n \ge 2$ and all prime powers $q$, except $PSL_2(2) \cong S_3$ and $PSL_2(3) \cong A_4$.
These groups form one of the infinite families of [[groups of Lie type|NPEBABQ49M]] in the [[classification of finite simple groups|06J6P03MG7]].
The group $PSL_n(F)$ acts faithfully on the projective space of lines in $F^n$, which explains the name.

## Explanations

### L1 human

Start with the $n \times n$ matrices of determinant $1$ over a field.
Then declare two matrices equal when one is a scalar multiple of the other.
What is left is the projective special linear group.
Over finite fields these groups give an endless supply of simple groups, the building blocks of all finite groups.
The smallest interesting one, $PSL_2(7)$, has $168$ elements and is the symmetry group of the Fano plane.
