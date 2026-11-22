---
tag: MSQTBBM86Q
kind: example
name: The identity matrix of size 2
msc: ["15A18"]
topics: [6R1D6QPY3S]
audience: ug1
not_instance_of:
  - target: 03NDVCSHSB
    note: The characteristic polynomial (x - 1)^2 annihilates the identity matrix, but it is not its minimal polynomial, which is x - 1
  - target: 0FY42N02DV
    note: The exponent 1 of x - 1 in the minimal polynomial is not the algebraic multiplicity 2 of the eigenvalue 1
uses: [0V58FPM3EQ, 039HF58KQ5, 0S7A0EMPF4]
sources:
  - url: https://en.wikipedia.org/wiki/Minimal_polynomial_(linear_algebra)
    locator: Properties
---

## Example

Let $I = I_2$ be the identity matrix of size $2$ over a field $F$.
We compute its characteristic and minimal polynomials and compare the exponents of $x - 1$.

1. The [[characteristic polynomial|039HF58KQ5]] is
$$p_I(x) = \det(xI - I) = \det \begin{pmatrix} x - 1 & 0 \\ 0 & x - 1 \end{pmatrix} = (x - 1)^2.$$
   Check: $\operatorname{tr} I = 2$ and $\det I = 1$, so $p_I(x) = x^2 - 2x + 1$, which is the same polynomial.
2. The polynomial $x - 1$ annihilates $I$, because substituting $I$ gives $I - I = 0$.
3. The only monic polynomial of smaller degree is the constant $1$, and it does not annihilate $I$, since $1 \cdot I = I \ne 0$.
4. So the [[minimal polynomial|0V58FPM3EQ]] is $m_I(x) = x - 1$, and $p_I = (x - 1)^2$ annihilates $I$ without being minimal.
5. The eigenvalue $1$ has [[algebraic multiplicity|0S7A0EMPF4]] $2$, the exponent in $p_I$, but its exponent in $m_I$ is $1$.

## Remarks

The example shows that the minimal polynomial can be a proper divisor of the characteristic polynomial, and that its exponents need not match the algebraic multiplicities.
In general, the exponent of $x - \lambda$ in $m_A$ is the size of the largest Jordan block for $\lambda$, which can be smaller than the algebraic multiplicity.

Change the size to $n$.
Then $p = (x - 1)^n$ and still $m = x - 1$, so the gap grows with $n$, and $p$ divides $m^k$ only for $k \ge n$.
Now change the matrix to the [[shear|HTAWRAC3QE]] $\begin{pmatrix} 1 & 1 \\ 0 & 1 \end{pmatrix}$, which has the same $p = (x - 1)^2$.
There $A - I \ne 0$, so $x - 1$ no longer annihilates it, and the minimal polynomial is $(x - 1)^2$.
The two matrices share a characteristic polynomial, and the minimal polynomial tells them apart.

## Explanations

### L1 human

The identity matrix changes nothing, so it already satisfies $I - I = 0$.
That makes $x - 1$ the smallest polynomial that the matrix satisfies, and its degree is $1$.
The characteristic polynomial $(x - 1)^2$ has degree $2$, so it is not the smallest one.

### L2 human

The lesson is that $m_A$ can be a proper divisor of $p_A$.
To find $m_A$, try the monic divisors of $p_A$ that contain every eigenvalue, from the smallest degree up, and stop at the first one that gives the zero matrix.
For $I_2$ the first candidate $x - 1$ already works.
Watch out: copying the exponents of $p_A$ into $m_A$ gives the wrong answer $(x - 1)^2$ here.
