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

1. $p_I(x) = \det(xI - I) = (x - 1)^2$. Second method: $\tr I = 2$ and $\det I = 1$, so $p_I(x) = x^2 - 2x + 1$.
2. $I - I = 0$. So $x - 1$ annihilates $I$.
3. The only proper monic divisor of $x - 1$ is $1$, and $1$ does not annihilate $I$, since $I \ne 0$.
4. So the [[minimal polynomial|0V58FPM3EQ]] is $m_I(x) = x - 1$, and $p_I = (x - 1)^2$ is not the minimal polynomial.
5. The eigenvalue $1$ has [[algebraic multiplicity|0S7A0EMPF4]] $2$, but its exponent in $m_I$ is $1$.

## Remarks

- In general, the exponent of $x - \lambda$ in $m_A$ is the size of the largest Jordan block for $\lambda$, not the algebraic multiplicity.
- For $I_n$, $m = x - 1$ and $p = (x - 1)^n$. So $p$ divides $m^k$ only for $k \ge n$.

## Explanations

### L1 human

The identity matrix already satisfies $I - I = 0$.
So its minimal polynomial is $x - 1$, of degree $1$.
Its characteristic polynomial $(x - 1)^2$ has degree $2$.

### L2 human

The typical lesson is that $m_A$ can be a proper divisor of $p_A$.
A trap is to copy the exponents of $p_A$ into $m_A$.
