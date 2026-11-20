---
tag: ~a158bffe
kind: example
name: Powers of a 2 by 2 matrix by reduction
msc: ["15A24"]
topics: [6R1D6QPY3S]
audience: ug1
instance_of: [~1ddc1825]
illustrates: [0F765KFC2J]
uses: [~1ddc1825, 0F765KFC2J, 0MES3KS0ZC, 0BNEXSKNRV]
sources:
  - url: https://en.wikipedia.org/wiki/Cayley%E2%80%93Hamilton_theorem
    locator: n-th power of matrix
  - book: isbn:9780134860244
---

## Example

We reduce powers of two matrices modulo their characteristic polynomials, as in [[inverse and powers by the Cayley-Hamilton theorem|~1ddc1825]].

1. Let $A = \begin{pmatrix} 1 & 2 \\ 3 & 4 \end{pmatrix}$, with $p_A(x) = x^2 - 5x - 2$. By the [[Cayley-Hamilton theorem|0F765KFC2J]], $A^2 = 5A + 2I$.
2. [[Divide|0MES3KS0ZC]] each power of $x$ by $p_A$: $x^2 \equiv 5x + 2$. Then $x^3 \equiv 5x^2 + 2x \equiv 27x + 10$.
3. $x^4 \equiv 27x^2 + 10x \equiv 145x + 54$, and $x^5 \equiv 145x^2 + 54x \equiv 779x + 290$.
4. So $A^5 = 779A + 290I = \begin{pmatrix} 1069 & 1558 \\ 2337 & 3406 \end{pmatrix}$.
5. Check by direct products: $A^2 = \begin{pmatrix} 7 & 10 \\ 15 & 22 \end{pmatrix}$ and $A^4 = (A^2)^2 = \begin{pmatrix} 199 & 290 \\ 435 & 634 \end{pmatrix} = 145A + 54I$.
6. $A^5 = A^4 A = \begin{pmatrix} 199 + 870 & 398 + 1160 \\ 435 + 1902 & 870 + 2536 \end{pmatrix} = \begin{pmatrix} 1069 & 1558 \\ 2337 & 3406 \end{pmatrix}$.
7. Now let $B = \begin{pmatrix} 2 & 1 \\ 1 & 2 \end{pmatrix}$, with $p_B(x) = (x - 1)(x - 3)$. Write $x^k \equiv a_k x + b_k$ modulo $p_B$.
8. The remainder takes the same values as $x^k$ at the roots $1$ and $3$. So $a_k + b_k = 1$ and $3a_k + b_k = 3^k$.
9. Hence $a_k = (3^k - 1)/2$ and $b_k = (3 - 3^k)/2$, and $B^k = \frac{3^k - 1}{2}B + \frac{3 - 3^k}{2}I$ for all $k \ge 0$.
10. Check for $k = 3$: the formula gives $13B - 12I = \begin{pmatrix} 14 & 13 \\ 13 & 14 \end{pmatrix}$. Directly, $B^2 = \begin{pmatrix} 5 & 4 \\ 4 & 5 \end{pmatrix}$ and $B^3 = B^2 B = \begin{pmatrix} 14 & 13 \\ 13 & 14 \end{pmatrix}$.

## Remarks

- The recursion $x^{k+1} \equiv x(a_k x + b_k) = a_k x^2 + b_k x$ gives $a_{k+1} = 5a_k + b_k$ and $b_{k+1} = 2a_k$ for $A$.
- The interpolation in step 8 needs distinct roots. With a repeated root, the derivative of $x^k$ at that root gives the second equation.
- The formula for $B^k$ was also checked for $k = 1, 2, 4, 5$.

## Explanations

### L1 human

The equation $A^2 = 5A + 2I$ lets us replace each $A^2$ by $5A + 2I$.
Repeating this, every power of $A$ becomes a combination of $A$ and $I$.
Only two numbers need to be tracked at each step.

### L2 human

The typical use is to compute a high power of a small matrix by hand.
A trap is to reduce $x^3$ as $5x + 2$ times $x$ and stop: the term $5x^2$ must also be reduced.
