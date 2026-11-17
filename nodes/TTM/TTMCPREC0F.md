---
tag: TTMCPREC0F
kind: example
name: The equation x³ + 2y³ + 4z³ = 0 has only the zero solution
msc: ["00A35", "11D25"]
topics: [EEH2F76CYQ]
audience: ug1
instance_of: [0EFYCFHYFG]
uses: [0EFYCFHYFG, 0PG2H7WKGG, 08B1RTW7VZ, 0FFXKTKKQC]
sources:
  - url: https://en.wikipedia.org/wiki/Proof_by_infinite_descent
    locator: lead section
---

## Example

Claim: the only integers $x$, $y$, $z$ with
$$x^3 + 2 y^3 + 4 z^3 = 0$$
are $x = y = z = 0$.
We prove the claim by [[infinite descent|0EFYCFHYFG]], with the size $s = |x| + |y| + |z|$, a sum of [[absolute values|0FFXKTKKQC]].

1. Parity of cubes: if $n$ is odd, $n = 2k + 1$, then $n^3 = 8k^3 + 12k^2 + 6k + 1$ is odd. So if $n^3$ is even, then $n$ is even.
2. Let $(x, y, z)$ be a solution other than $(0, 0, 0)$. Then $s \ge 1$.
3. We have $x^3 = -2 y^3 - 4 z^3 = 2(-y^3 - 2 z^3)$. So $x^3$ is even, and $x$ is even by step 1. Write $x = 2 x_1$.
4. Substitute: $8 x_1^3 + 2 y^3 + 4 z^3 = 0$. Divide by $2$: $y^3 + 2 z^3 + 4 x_1^3 = 0$.
5. Now $y^3 = 2(-z^3 - 2 x_1^3)$ is even, so $y$ is even by step 1. Write $y = 2 y_1$.
6. Substitute: $8 y_1^3 + 2 z^3 + 4 x_1^3 = 0$. Divide by $2$: $z^3 + 2 x_1^3 + 4 y_1^3 = 0$.
7. Now $z^3 = 2(-x_1^3 - 2 y_1^3)$ is even, so $z$ is even by step 1. Write $z = 2 z_1$.
8. Substitute: $8 z_1^3 + 2 x_1^3 + 4 y_1^3 = 0$. Divide by $2$: $x_1^3 + 2 y_1^3 + 4 z_1^3 = 0$.
9. So $(x_1, y_1, z_1) = (x/2, y/2, z/2)$ is again an integer solution. Its size is $s/2$, which is a positive integer smaller than $s$.
10. So each nonzero solution gives a nonzero solution of smaller size in the positive integers. By infinite descent, there is no nonzero solution.

A search by computer finds no nonzero solution with $|x|, |y|, |z| \le 20$, as the claim predicts.

## Remarks

1. Steps 4, 6 and 8 rotate the three terms: after each division the equation has the same form with the variables in a new order. After three rounds we are back at the first equation.
2. With $z = 0$ the claim gives the irrationality of $\sqrt[3]{2}$. If $\sqrt[3]{2} = p/q$ with integers $q \neq 0$ and $p$, then $p^3 = 2 q^3$, and $(p, -q, 0)$ is a nonzero solution.
3. With $x = 0$ the claim gives the irrationality of $\sqrt[3]{2}$ again, from $2y^3 = -4z^3$, that is, $y^3 = 2(-z)^3$.
4. The coefficients matter. The equation $x^3 + y^3 + 2 z^3 = 0$ has the nonzero solution $(1, 1, -1)$, because $1 + 1 - 2 = 0$, and the descent fails at the first step: $x^3 = -y^3 - 2z^3$ need not be even.

## Explanations

### L1 human

Suppose that three whole numbers solve this equation and are not all zero.
Looking at even and odd numbers, we find that all three must be even.
Halving all three gives another solution with smaller numbers.
We can halve again and again, but whole numbers cannot be halved forever and stay whole.
So the only solution is $0$, $0$, $0$.

### L2 human

We write the descent in its minimal form, with the number of common factors $2$ in place of the size.

1. Suppose that $(x, y, z)$ is a nonzero solution, and let $2^e$ be the largest power of $2$ that divides all of $x$, $y$ and $z$. It exists because one entry is not $0$.
2. Each term of the equation has degree $3$, so dividing it by $2^{3e}$ shows that $(x/2^e, y/2^e, z/2^e)$ is again a nonzero integer solution.
3. By steps 3 to 7 of the example, applied to this solution, its entries are all even.
4. So $2^{e+1}$ divides $x$, $y$ and $z$, which contradicts the choice of $e$ in step 1.

This is the minimal form of the descent: the "smallest" solution is the one with no common factor $2$.
The typical use of this form is a homogeneous equation, where dividing a solution by a common factor gives a solution again.
A trap is to apply it to an equation that is not homogeneous, such as $x^3 + 2y^3 = 4$, where halving a solution does not give a solution.
