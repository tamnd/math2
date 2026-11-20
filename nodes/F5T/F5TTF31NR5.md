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

Let $P = \begin{pmatrix} 1 & 1 \\ 0 & 0 \end{pmatrix}$, the projection of $\R^2$ onto the line spanned by $(1, 0)$ along the line spanned by $(1, -1)$.

1. $P^2 = \begin{pmatrix} 1 \cdot 1 + 1 \cdot 0 & 1 \cdot 1 + 1 \cdot 0 \\ 0 & 0 \end{pmatrix} = P$. So $x^2 - x$ is an [[annihilating polynomial|052M4SX57M]] of $P$.
2. Also $P^3 - P = P \cdot P^2 - P = P^2 - P = 0$. So $x^3 - x$ annihilates $P$ too.
3. The [[characteristic polynomial|0BZ81AJNWF]] is $p_P(t) = t^2 - t$, since $\tr P = 1$ and $\det P = 0$. Second method: $\det(tI - P) = (t - 1)t$.
4. The proper monic divisors of $x^2 - x$ are $1$, $x$ and $x - 1$. None annihilates $P$, because $I \ne 0$, $P \ne 0$ and $P - I \ne 0$.
5. So the [[minimal polynomial|0V58FPM3EQ]] is $m_P(x) = x^2 - x = p_P(x)$.
6. $x^3 - x = (x + 1)(x^2 - x)$, so $m_P$ divides $x^3 - x$, as the theorem that the [[minimal polynomial divides every annihilating polynomial|0VTAD25A3G]] requires.
7. Let $p \in \R[x]$. [[Divide|0MES3KS0ZC]] $p$ by $x^2 - x$: $p(x) = q(x)(x^2 - x) + a + bx$. Putting $x = 0$ and $x = 1$ gives $a = p(0)$ and $a + b = p(1)$.
8. So the [[value p(P)|0BNEXSKNRV]] is $p(P) = p(0)I + (p(1) - p(0))P = p(0)(I - P) + p(1)P$.

## Remarks

- For example, $e^{P} = I + (e - 1)P$, by the same reduction applied to the partial sums of the exponential series.
- $I - P$ is the complementary projection, onto the line spanned by $(1, -1)$ along the line spanned by $(1, 0)$.
- Every projection other than $0$ and $I$ has minimal polynomial $x^2 - x$.

## Explanations

### L1 human

Applying a projection twice gives the same result as applying it once.
So $P^2 = P$, and every polynomial in $P$ reduces to a combination of $I$ and $P$.
The coefficients come from the values of the polynomial at $0$ and at $1$.

### L2 human

The typical use is to compute $p(P)$ from the two numbers $p(0)$ and $p(1)$.
A trap is to think that $x^3 - x$ is the minimal polynomial because it annihilates $P$: it has the extra factor $x + 1$.
