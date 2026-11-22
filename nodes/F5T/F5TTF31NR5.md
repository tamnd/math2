---
tag: F5TTF31NR5
kind: example
name: Polynomials in a projection of the plane
msc: ["15A18", "15A24"]
topics: [6R1D6QPY3S]
audience: ug1
instance_of: [0E3MV6E6MG, 0PBN8VEKY8, 03NDVCSHSB, 0J5EMJRRFM]
illustrates: [0VTAD25A3G, 093X6MN6Y6]
uses: [0BNEXSKNRV, 052M4SX57M, 0V58FPM3EQ, 0BZ81AJNWF, 0VTAD25A3G, 0MES3KS0ZC]
sources:
  - url: https://en.wikipedia.org/wiki/Minimal_polynomial_(linear_algebra)
    locator: Properties
  - book: isbn:9780135367971
---

## Example

Let $P = \begin{pmatrix} 1 & 1 \\ 0 & 0 \end{pmatrix}$ over $\mathbb{R}$.
It is the projection of $\mathbb{R}^2$ onto the line spanned by $(1, 0)$ along the line spanned by $(1, -1)$, because $P(1, 0) = (1, 0)$ and $P(1, -1) = (0, 0)$.
We find its annihilating polynomials, its characteristic and minimal polynomials, and a formula for every polynomial in $P$.

1. Square the matrix:
$$P^2 = \begin{pmatrix} 1 \cdot 1 + 1 \cdot 0 & 1 \cdot 1 + 1 \cdot 0 \\ 0 \cdot 1 + 0 \cdot 0 & 0 \cdot 1 + 0 \cdot 0 \end{pmatrix} = \begin{pmatrix} 1 & 1 \\ 0 & 0 \end{pmatrix} = P.$$
   So $x^2 - x$ is an [[annihilating polynomial|052M4SX57M]] of $P$.
2. Then $P^3 = P \cdot P^2 = P \cdot P = P$, so $P^3 - P = 0$ and $x^3 - x$ annihilates $P$ too.
3. The [[characteristic polynomial|0BZ81AJNWF]] is
$$\det(tI - P) = \det \begin{pmatrix} t - 1 & -1 \\ 0 & t \end{pmatrix} = (t - 1) t = t^2 - t.$$
   Check: $\operatorname{tr} P = 1$ and $\det P = 0$, so $t^2 - (\operatorname{tr} P) t + \det P = t^2 - t$.
4. By the theorem that the [[minimal polynomial divides every annihilating polynomial|0VTAD25A3G]], the minimal polynomial is a monic divisor of $x^2 - x$, so it is $1$, $x$, $x - 1$ or $x^2 - x$.
   The first three fail, because $I \ne 0$, $P \ne 0$ and $P - I = \begin{pmatrix} 0 & 1 \\ 0 & -1 \end{pmatrix} \ne 0$.
5. So the [[minimal polynomial|0V58FPM3EQ]] is $m_P(x) = x^2 - x$, and it equals the characteristic polynomial.
6. The polynomial of step 2 factors as $x^3 - x = (x + 1)(x^2 - x)$, so $m_P$ divides it, as the theorem requires.
7. Let $p \in \mathbb{R}[x]$ and [[divide|0MES3KS0ZC]] it by $x^2 - x$, which gives $p(x) = q(x)(x^2 - x) + a + bx$.
   Put $x = 0$ to get $a = p(0)$, and put $x = 1$ to get $a + b = p(1)$.
8. Since $P^2 - P = 0$, the [[value p(P)|0BNEXSKNRV]] is the value of the remainder:
$$p(P) = p(0) I + \big(p(1) - p(0)\big) P = p(0)(I - P) + p(1) P.$$

## Remarks

Step 8 says that a polynomial in $P$ depends only on the two numbers $p(0)$ and $p(1)$, the values at the two eigenvalues.
For example, $p(x) = x^5 + 3$ has $p(0) = 3$ and $p(1) = 4$, so $P^5 + 3I = 3(I - P) + 4P = 3I + P$.
Check: $P^5 = P$, so $P^5 + 3I = P + 3I$.
Applying step 8 to the partial sums of the exponential series gives $e^P = (I - P) + eP = I + (e - 1)P$.

The matrix $I - P = \begin{pmatrix} 0 & -1 \\ 0 & 1 \end{pmatrix}$ is the complementary projection, onto the line spanned by $(1, -1)$ along the line spanned by $(1, 0)$.
Every projection other than $0$ and $I$ has minimal polynomial $x^2 - x$, by the argument of step 4.
If $P$ is replaced by $0$ or by $I$, the minimal polynomial drops to $x$ or to $x - 1$, while the characteristic polynomial becomes $t^2$ or $(t - 1)^2$.

## Explanations

### L1 human

A projection is like a shadow: doing it twice gives the same shadow as doing it once.
So $P^2 = P$, and every higher power of $P$ is also just $P$.
This means that any polynomial in $P$ shrinks to a mix of $I$ and $P$.
The two amounts in the mix come from the values of the polynomial at $0$ and at $1$.

### L2 human

Here is a typical use: compute $p(P)$ for $p(x) = 2x^3 - x + 5$.
The values are $p(0) = 5$ and $p(1) = 2 - 1 + 5 = 6$, so step 8 gives
$$p(P) = 5(I - P) + 6P = 5I + P = \begin{pmatrix} 6 & 1 \\ 0 & 5 \end{pmatrix}.$$
Check: $2P^3 - P + 5I = 2P - P + 5I = P + 5I$.
Watch out: $x^3 - x$ annihilates $P$, but it is not the minimal polynomial, because it has the extra factor $x + 1$ and $-1$ is not an eigenvalue of $P$.
