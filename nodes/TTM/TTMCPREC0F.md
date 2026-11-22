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

We prove that the only integers $x$, $y$, $z$ with
$$x^3 + 2 y^3 + 4 z^3 = 0$$
are $x = y = z = 0$.
The proof is an [[infinite descent|0EFYCFHYFG]], and the size of a solution is the natural number $s = |x| + |y| + |z|$, a sum of [[absolute values|0FFXKTKKQC]].

1. First a fact about cubes.
   If $n = 2k + 1$ is odd, then $n^3 = 8k^3 + 12k^2 + 6k + 1$ is odd.
   So if $n^3$ is even, then $n$ is even.
2. Let $(x, y, z)$ be a solution other than $(0, 0, 0)$.
   Then $s \ge 1$.
3. We have $x^3 = -2y^3 - 4z^3 = 2(-y^3 - 2z^3)$, so $x^3$ is even, and $x$ is even by step 1.
   Write $x = 2x_1$.
4. Substitute and divide by $2$:
   $$8x_1^3 + 2y^3 + 4z^3 = 0 \quad \Longrightarrow \quad y^3 + 2z^3 + 4x_1^3 = 0.$$
5. Now $y^3 = 2(-z^3 - 2x_1^3)$ is even, so $y$ is even.
   Write $y = 2y_1$, substitute and divide by $2$:
   $$z^3 + 2x_1^3 + 4y_1^3 = 0.$$
6. Now $z^3 = 2(-x_1^3 - 2y_1^3)$ is even, so $z$ is even.
   Write $z = 2z_1$, substitute and divide by $2$:
   $$x_1^3 + 2y_1^3 + 4z_1^3 = 0.$$
7. So $(x_1, y_1, z_1) = (x/2, y/2, z/2)$ is again an integer solution, and it is not the zero solution.
   Its size is $s/2$, a positive integer smaller than $s$.
8. So each nonzero solution gives a nonzero solution whose size is a smaller positive integer.
   A strictly decreasing sequence of positive integers cannot go on forever, so there is no nonzero solution.

Check: a computer search finds no nonzero solution with $|x|, |y|, |z| \le 20$.

## Remarks

The three divisions rotate the equation.
After each one the equation has the same shape, with the variables in a new order, and after three rounds it is the first equation again.
Each step also stays inside the integers: the halves $x_1$, $y_1$, $z_1$ are integers because steps 3, 5 and 6 proved that $x$, $y$, $z$ are even.
That check is what keeps the descent inside the natural numbers.

The claim contains the irrationality of $\sqrt[3]{2}$.
If $\sqrt[3]{2} = p/q$ with integers $p$ and $q \neq 0$, then $p^3 = 2q^3$, and $(p, -q, 0)$ is a nonzero solution.

The coefficients matter.
The equation $x^3 + y^3 + 2z^3 = 0$ has the nonzero solution $(1, 1, -1)$, because $1 + 1 - 2 = 0$.
There the descent fails at the first step, since $x^3 = -y^3 - 2z^3$ need not be even.

## Explanations

### L1 human

Suppose that three whole numbers solve this equation and are not all zero.
Looking at even and odd numbers, we find that all three must be even.
Halving all three gives another solution with smaller numbers.
We can halve again and again, but whole numbers cannot be halved forever and stay whole.
So the only solution is $0$, $0$, $0$.

### L2 human

The descent can also be written with a least element, in the style of a [[minimal counterexample|JGRCNPKNGG]].
Suppose that $(x, y, z)$ is a nonzero solution, and let $2^e$ be the largest power of $2$ that divides all of $x$, $y$ and $z$.
It exists, because one entry is not $0$ and a nonzero integer has only finitely many powers of $2$ as divisors.
Each term of the equation has degree $3$, so we can divide the whole equation by $2^{3e}$:
$$\left(\frac{x}{2^e}\right)^3 + 2\left(\frac{y}{2^e}\right)^3 + 4\left(\frac{z}{2^e}\right)^3 = 0.$$
So $(x/2^e, y/2^e, z/2^e)$ is again a nonzero integer solution.
By steps 3 to 6 of the example, its entries are all even.
Then $2^{e+1}$ divides $x$, $y$ and $z$, which contradicts the choice of $e$.

The typical use of this form is a homogeneous equation, where a common factor of a solution can be divided out.
Watch out: for an equation that is not homogeneous, such as $x^3 + 2y^3 = 4$, half of a solution is not a solution, and the descent does not start.
