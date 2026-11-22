---
tag: SWDMY3XJKF
kind: example
name: The equation x² + y² = 3z² has only the zero solution
msc: ["00A35", "11D09"]
topics: [EEH2F76CYQ]
audience: ug1
instance_of: [0EFYCFHYFG]
uses: [0EFYCFHYFG, 0WAY5WX8NY, 0PG2H7WKGG, 08B1RTW7VZ]
sources:
  - url: https://en.wikipedia.org/wiki/Proof_by_infinite_descent
    locator: lead section
  - url: https://en.wikipedia.org/wiki/Quadratic_residue
    locator: lead section
---

## Example

We prove that the only integers $x$, $y$, $z$ with
$$x^2 + y^2 = 3z^2$$
are $x = y = z = 0$.
The proof is an [[infinite descent|0EFYCFHYFG]], and the size of a solution is the natural number $|z|$.

1. First a fact about squares [[modulo 3|0WAY5WX8NY]].
   Every integer $n$ is congruent to $0$, $1$ or $2$, so $n^2$ is congruent to $0$, $1$ or $4 \equiv 1$.
   So $n^2 \equiv 0 \pmod 3$ exactly when $n \equiv 0 \pmod 3$.
2. Let $(x, y, z)$ be a solution other than $(0, 0, 0)$.
   If $z = 0$, then $x^2 + y^2 = 0$, so $x = y = 0$.
   Hence $z \neq 0$, and $|z| \ge 1$.
3. The right side $3z^2$ is divisible by $3$, so $x^2 + y^2 \equiv 0 \pmod 3$.
4. By step 1, each of $x^2$ and $y^2$ is $0$ or $1$ modulo $3$.
   The sums are $0 + 0 = 0$, $0 + 1 = 1$ and $1 + 1 = 2$, so only $0 + 0$ works.
   So $3$ [[divides|0PG2H7WKGG]] both $x$ and $y$.
5. Write $x = 3x_1$ and $y = 3y_1$.
   Then $9x_1^2 + 9y_1^2 = 3z^2$, so $z^2 = 3(x_1^2 + y_1^2)$.
6. So $z^2 \equiv 0 \pmod 3$, and $3$ divides $z$ by step 1.
   Write $z = 3z_1$.
7. Then $9z_1^2 = 3(x_1^2 + y_1^2)$, so
   $$x_1^2 + y_1^2 = 3z_1^2,$$
   and $(x_1, y_1, z_1)$ is again an integer solution.
8. It is not the zero solution, because $z_1 = z/3 \neq 0$, and its size is $|z_1| = |z|/3 < |z|$.
9. So each nonzero solution gives a nonzero solution whose size is a smaller positive integer.
   A strictly decreasing sequence of positive integers cannot go on forever, so there is no nonzero solution.

Check: a computer search finds no nonzero solution with $|x|, |y|, |z| \le 39$.

## Remarks

The descent stays inside the integers because steps 4 and 6 prove divisibility by $3$ before the proof divides by $3$.
Without those steps, $(x/3, y/3, z/3)$ would be a triple of rationals, and rationals can shrink forever.

The claim has a geometric meaning.
The circle $u^2 + v^2 = 3$ has no point with rational coordinates, because a point $(a/c, b/c)$ on it would give the nonzero solution $(a, b, c)$.
With $x = 0$ the claim says that $y^2 = 3z^2$ has only the zero solution, so $\sqrt{3}$ is irrational.

The number $3$ cannot be replaced by $2$.
The equation $x^2 + y^2 = 2z^2$ has the solution $(1, 1, 1)$, and the descent fails in step 4, because $1 + 1 \equiv 0 \pmod 2$.
The number $7$ works: the squares modulo $7$ are $0$, $1$, $2$ and $4$, and no two of the nonzero ones add up to a multiple of $7$.

## Explanations

### L1 human

We want whole numbers where the first squared plus the second squared is three times the third squared.
A square leaves the remainder $0$ or $1$ on division by $3$, never $2$.
So the left side is a multiple of $3$ only if both numbers are multiples of $3$.
Then the third number is a multiple of $3$ too, and dividing all three by $3$ gives a smaller answer.
Whole numbers cannot shrink forever, so the only answer is $0$, $0$, $0$.

### L2 human

We watch the same argument fail for $x^2 + y^2 = 5z^2$, which has the solution $(1, 2, 1)$.
The squares modulo $5$ come from
$$0^2, 1^2, 2^2, 3^2, 4^2 \equiv 0, 1, 4, 4, 1 \pmod 5.$$
So $1 + 4 \equiv 0 \pmod 5$ is a sum of two nonzero squares, and $5 \mid x^2 + y^2$ does not force $5 \mid x$.
Step 4 of the example has no analogue, and the descent cannot start.

Check: $1^2 + 2^2 = 5 = 5 \cdot 1^2$.
The typical use of descent with congruences is to find a prime $p$ such that every solution has all entries divisible by $p$, and then to divide by $p$.
Watch out: after the division, check that the new triple solves the same equation, as step 7 does.
