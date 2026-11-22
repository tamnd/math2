---
tag: PHA4SATHWE
kind: example
name: Polynomials modulo the multiples of x²
msc: ["15A03"]
topics: [QHKTJ89V6S]
audience: ug1
instance_of: [0BR3FY5Q8M]
uses: [0SVR29SV1V, 0Q9EZS90GY, 0VTQTPQGAV]
sources:
  - url: https://en.wikipedia.org/wiki/Quotient_space_(linear_algebra)
    locator: Examples
---

## Example

Let $V = \R[x]$, the [[polynomials|0Q9EZS90GY]] with real coefficients, and let
$$U = x^2 \R[x] = \{x^2 q(x) : q \in \R[x]\}.$$
We find a basis of the [[quotient space|0SVR29SV1V]] $V / U$.

1. The set $U$ is a subspace.
   It contains $0 = x^2 \cdot 0$, and $x^2 q + x^2 r = x^2 (q + r)$ and $a\, x^2 q = x^2 (aq)$.
2. The set $U$ consists of the polynomials whose constant and linear coefficients are both $0$.
   Indeed, $x^2 q$ has no terms of degree below $2$, and a polynomial $c_2 x^2 + c_3 x^3 + \dots$ equals $x^2 (c_2 + c_3 x + \dots)$.
3. Every polynomial is $p = a + bx + x^2 q$ for some $a, b \in \R$ and $q \in \R[x]$.
   So $p + U = (a + bx) + U = a(1 + U) + b(x + U)$.
4. Hence the cosets $1 + U$ and $x + U$ span $V / U$.
5. If $a(1 + U) + b(x + U) = 0 + U$, then $a + bx \in U$.
   By step 2, $a = b = 0$, so the two cosets are independent.
6. So $1 + U$, $x + U$ is a [[basis|0VTQTPQGAV]] of $V / U$, and $\dim(V / U) = 2$.

For instance, $(x^2 + 3x + 1) + U = (3x + 1) + U$, since the difference $x^2$ lies in $U$.
In the basis, this coset has coordinates $(1, 3)$.

## Remarks

Here $V$ and $U$ both have countably infinite dimension, and the quotient has dimension $2$.
So the formula $\dim(V / U) = \dim V - \dim U$ has no meaning here, which is why the [[dimension of a quotient space|0SXDQ6TN00]] is stated for finite-dimensional $V$.
The number $2$ is the [[codimension|JJCGJ1EGCQ]] of $U$ in $V$.
In the same way, $\R[x] / x^n \R[x]$ has the basis $1 + U, x + U, \dots, x^{n-1} + U$ and dimension $n$.

Since $U$ is an ideal of the ring $\R[x]$, the quotient is also a ring.
In it $x^2 = 0$, and it is the ring of dual numbers $a + b\varepsilon$ with $\varepsilon^2 = 0$.

## Explanations

### L1 human

Working modulo $x^2$ means that we throw away every term of degree $2$ or more.
What remains of a polynomial is a constant and a multiple of $x$.
Two numbers describe it, so the quotient looks like the plane.

### L2 human

The coset of $p$ is determined by the two numbers $p(0)$ and $p'(0)$.
Indeed, for $p = a + bx + x^2 q$ we get $p(0) = a$ and $p'(0) = b$, since the derivative of $x^2 q$ is $2xq + x^2 q'$, which vanishes at $0$.
So the map $p + U \mapsto (p(0), p'(0))$ is a well-defined isomorphism $V / U \cong \R^2$, and it sends the basis $1 + U$, $x + U$ to the standard basis.
For $p = x^2 + 3x + 1$ it gives $(1, 3)$, which matches the coordinates above.
This is the typical use of a quotient of polynomials: it keeps exactly the part of a polynomial that a question needs, here its first-order behavior at $0$.
