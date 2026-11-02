---
tag: TX5AV1JTF5
kind: statement
role: theorem
name: Contiguous relations
msc: ["33C05"]
uses: [463X5V31D9, 428M453CR2]
about: [463X5V31D9]
sources:
  - url: https://en.wikipedia.org/wiki/Hypergeometric_function
---

## Statement

Let $a, b, c \in \C$ with $c \notin \set{1, 0, -1, -2, \ldots}$.
Write $F = {}_2F_1(a, b; c; z)$ for the [[hypergeometric function|463X5V31D9]].
Write $F(a \pm 1)$, $F(b \pm 1)$, $F(c \pm 1)$ for the six *contiguous* functions obtained by changing one parameter by $\pm 1$.

1. (Gauss) Let $G$ and $H$ be two of the six contiguous functions.
Then $F$, $G$, $H$ satisfy a linear relation whose coefficients are polynomials in $a, b, c, z$, not all zero.
2. In particular, for all $z \in \C \setminus [1, \infty)$,
$$(c - a) \, F(a - 1) + \big(2a - c + (b - a) z\big) F + a (z - 1) \, F(a + 1) = 0,$$
$$(a - b) \, F = a \, F(a + 1) - b \, F(b + 1).$$

## Remarks

The second relation in part 2 can be checked on the [[hypergeometric series|428M453CR2]] directly.
Write $t_n = \frac{(a)_n (b)_n}{(c)_n \, n!}$ for the coefficients of $F$.
Since $a \, (a+1)_n = (a)_n (a + n)$, the coefficient of $z^n$ in $a F(a + 1)$ is $t_n (a + n)$, and in the same way the coefficient in $b F(b + 1)$ is $t_n (b + n)$.
Their difference is $t_n (a - b)$, the coefficient of $(a - b) F$.
The other relations follow by similar coefficient comparisons, and they extend from $\abs{z} < 1$ to the cut plane by analytic continuation.
There are $\binom{6}{2} = 15$ such relations, and Gauss listed them all.

Example: for $a = 1$, $b = 2$ the second relation gives $-F(1, 2; c; z) = F(2, 2; c; z) - 2 F(1, 3; c; z)$, a relation between three explicit series.

By combining contiguous relations, for generic parameters the function $F(a + m, b + n; c + l; z)$ for integers $m, n, l$ is a combination of $F$ and one contiguous function, with coefficients rational in $a, b, c, z$.

## Explanations

### L1 human

Changing one parameter of a hypergeometric function by $1$ gives a closely related function.
Gauss found that the original function and any two of its six neighbours are tied by a simple linear equation.
This is like the three-term recurrence of orthogonal polynomials, and it lets one step through parameters one unit at a time.

### L2 human

Contiguous relations give recurrences for orthogonal polynomials that are terminating ${}_2F_1$ series, such as Jacobi and Legendre polynomials.
They lead to Gauss's continued fraction for ratios of hypergeometric functions.
They also show that the vector $(F, F')$ at shifted parameters is obtained from the original one by a matrix with rational entries.
This is the starting point of the theory of hypergeometric difference equations.
