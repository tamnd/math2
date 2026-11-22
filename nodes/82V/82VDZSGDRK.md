---
tag: 82VDZSGDRK
kind: example
name: Powers of a 2 by 2 matrix by reduction
msc: ["15A24"]
topics: [6R1D6QPY3S]
audience: ug1
instance_of: [R4CPYXFJEQ]
illustrates: [0F765KFC2J]
uses: [R4CPYXFJEQ, 0F765KFC2J, 0MES3KS0ZC, 0BNEXSKNRV]
sources:
  - url: https://en.wikipedia.org/wiki/Cayley%E2%80%93Hamilton_theorem
    locator: n-th power of matrix
  - book: isbn:9780134860244
---

## Example

We compute powers of two matrices by reducing powers of $x$ modulo the characteristic polynomial, as in [[inverse and powers by the Cayley-Hamilton theorem|R4CPYXFJEQ]].
The first matrix uses step-by-step reduction, and the second uses the values at the roots.

*The fifth power of $A = \begin{pmatrix} 1 & 2 \\ 3 & 4 \end{pmatrix}$.*

1. The trace is $5$ and the determinant is $-2$, so $p_A(x) = x^2 - 5x - 2$.
   By the [[Cayley-Hamilton theorem|0F765KFC2J]], $A^2 = 5A + 2I$.
2. [[Division with remainder|0MES3KS0ZC]] by $p_A$ replaces $x^2$ by $5x + 2$.
   Multiply by $x$ and replace $x^2$ again at each step:
$$x^3 \equiv 5x^2 + 2x \equiv 27x + 10, \qquad x^4 \equiv 27x^2 + 10x \equiv 145x + 54, \qquad x^5 \equiv 145x^2 + 54x \equiv 779x + 290.$$
3. So $A^5 = 779 A + 290 I$, which is
$$\begin{pmatrix} 779 + 290 & 1558 \\ 2337 & 3116 + 290 \end{pmatrix} = \begin{pmatrix} 1069 & 1558 \\ 2337 & 3406 \end{pmatrix}.$$
4. Check by direct products.
   First $A^2 = \begin{pmatrix} 7 & 10 \\ 15 & 22 \end{pmatrix}$, and then
$$A^4 = (A^2)^2 = \begin{pmatrix} 49 + 150 & 70 + 220 \\ 105 + 330 & 150 + 484 \end{pmatrix} = \begin{pmatrix} 199 & 290 \\ 435 & 634 \end{pmatrix},$$
   which is $145A + 54I$, as step 2 predicts.
5. One more product gives the fifth power:
$$A^5 = A^4 A = \begin{pmatrix} 199 + 870 & 398 + 1160 \\ 435 + 1902 & 870 + 2536 \end{pmatrix} = \begin{pmatrix} 1069 & 1558 \\ 2337 & 3406 \end{pmatrix}.$$

*Every power of $B = \begin{pmatrix} 2 & 1 \\ 1 & 2 \end{pmatrix}$.*

6. The trace is $4$ and the determinant is $3$, so $p_B(x) = x^2 - 4x + 3 = (x - 1)(x - 3)$.
   Write $x^k \equiv a_k x + b_k$ modulo $p_B$.
7. The difference $x^k - (a_k x + b_k)$ is a multiple of $p_B$, so it vanishes at the roots $1$ and $3$:
$$a_k + b_k = 1, \qquad 3a_k + b_k = 3^k.$$
8. Subtract the first equation from the second to get $a_k = (3^k - 1)/2$, and then $b_k = 1 - a_k = (3 - 3^k)/2$.
   So for every $k \ge 0$,
$$B^k = \frac{3^k - 1}{2} B + \frac{3 - 3^k}{2} I.$$
9. Check for $k = 3$: the formula gives $13B - 12I = \begin{pmatrix} 14 & 13 \\ 13 & 14 \end{pmatrix}$.
   Directly, $B^2 = \begin{pmatrix} 5 & 4 \\ 4 & 5 \end{pmatrix}$ and $B^3 = B^2 B = \begin{pmatrix} 10 + 4 & 5 + 8 \\ 8 + 5 & 4 + 10 \end{pmatrix} = \begin{pmatrix} 14 & 13 \\ 13 & 14 \end{pmatrix}$.

## Remarks

The step-by-step reduction is a recurrence on two numbers.
If $x^k \equiv a_k x + b_k$ modulo $p_A$, then
$$x^{k+1} \equiv a_k x^2 + b_k x \equiv (5a_k + b_k) x + 2a_k,$$
so $a_{k+1} = 5a_k + b_k$ and $b_{k+1} = 2a_k$, starting from $a_1 = 1$ and $b_1 = 0$.
This costs a few additions per step, while a direct product of $2 \times 2$ matrices costs eight multiplications.

The method of step 7 needs two different roots.
For a repeated root, say $p(x) = (x - 2)^2$, the two conditions are the value and the derivative at $2$: $2a_k + b_k = 2^k$ and $a_k = k \, 2^{k-1}$.
For $C = \begin{pmatrix} 2 & 1 \\ 0 & 2 \end{pmatrix}$ this gives $C^k = k 2^{k-1} C + (1 - k) 2^k I$, whose upper right entry is $k 2^{k-1}$.

## Explanations

### L1 human

The equation $A^2 = 5A + 2I$ is a rewriting rule.
Each time $A^2$ appears, replace it by $5A + 2I$, and repeat.
Every power of $A$ then turns into "a number times $A$ plus a number times $I$", and you only track two numbers at each step.

### L2 human

The typical use is a high power of a small matrix by hand, or a closed formula for $A^k$ when the eigenvalues are known.
For $B$, the formula shows at once that the entries of $B^k$ grow like $3^k / 2$, a fact that step-by-step multiplication hides.
Watch out when you reduce $x^3$: writing $x^3 = x \cdot x^2 \equiv x(5x + 2) = 5x^2 + 2x$ is not the end, because the term $5x^2$ must be reduced again to give $27x + 10$.
