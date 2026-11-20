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

Let $V = \R[x]$, the [[polynomials|0Q9EZS90GY]] with real coefficients, and let $U = x^2 \R[x] = \{x^2 q(x) : q \in \R[x]\}$.
We find a basis of the [[quotient space|0SVR29SV1V]] $V / U$.

1. $U$ is a subspace: it contains $0 = x^2 \cdot 0$, and $x^2 q + x^2 r = x^2 (q + r)$ and $a x^2 q = x^2 (a q)$.
2. $U$ is the set of polynomials whose constant and linear coefficients are both $0$.
3. Every polynomial is $p = a + bx + x^2 q$ for some $a, b \in \R$ and $q \in \R[x]$. So $p + U = (a + bx) + U = a(1 + U) + b(x + U)$.
4. So $1 + U$ and $x + U$ span $V / U$.
5. If $a(1 + U) + b(x + U) = 0 + U$, then $a + bx \in U$. By step 2, $a = b = 0$. So the two cosets are independent.
6. Hence $1 + U$, $x + U$ is a [[basis|0VTQTPQGAV]] of $V / U$, and $\dim(V / U) = 2$.

For instance, $(x^2 + 3x + 1) + U = (3x + 1) + U$, since the difference $x^2$ lies in $U$.

## Remarks

Here $V$ and $U$ are infinite-dimensional, and the quotient is finite-dimensional.
So the formula $\dim(V / U) = \dim V - \dim U$ makes no sense here, and the [[dimension of a quotient|0SXDQ6TN00]] is stated for finite-dimensional $V$.
The subspace $U$ has codimension $2$ in $V$.
Since $U$ is an ideal of the ring $\R[x]$, the quotient is also a ring, in which $x^2 = 0$: this is the ring of dual numbers.

## Explanations

### L1 human

Working modulo $x^2$ means that we throw away every term of degree $2$ or more.
What remains is a constant and a multiple of $x$, so the quotient looks like the plane.

### L2 human

The coset of $p$ is determined by $p(0)$ and $p'(0)$.
The map $p + U \mapsto (p(0), p'(0))$ is an isomorphism $V / U \cong \R^2$, which sends the basis $1 + U$, $x + U$ to the standard basis.
