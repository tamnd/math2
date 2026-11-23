---
tag: YQXE13QY9Z
kind: example
name: Reduction to the unit case for an inhomogeneous inequality
msc: ["00A35", "26D05"]
topics: [MEKKHHQTKB]
audience: ug1
not_instance_of:
  - target: DX2H7AD66G
    note: the two sides of the inequality have different degrees, so scaling does not preserve the statement and the unit case does not imply the general case
uses: [DX2H7AD66G, 2C3PAQ7H50]
sources:
  - url: https://en.wikipedia.org/wiki/Homogeneous_function
    locator: lead section
---

## Example

A student wants to prove $x^2 \ge x$ for every real $x \neq 0$ and argues in two steps.
First: "scaling changes nothing, so we may assume $\lvert x \rvert = 1$".
Second: "for $x = 1$ the claim is $1 \ge 1$, and for $x = -1$ it is $1 \ge -1$".
The claim is false, and we find where the [[reduction to a special case|DX2H7AD66G]] breaks.

1. At $x = \tfrac12$, $x^2 = \tfrac14 < \tfrac12$, so the claim fails.
2. The special case is correct: for $\lvert x \rvert = 1$ the claim holds.
3. The reduction needs a scaling $x \mapsto sx$, $s > 0$, that preserves the statement.
   Under it the left side becomes $s^2 x^2$ and the right side $s x$.
4. So the scaled claim is $s x^2 \ge x$ after division by $s$, a different inequality when $s \neq 1$.
5. The scaling with $s = 2$ moves $\tfrac12$ to $1$, and the true $1^2 \ge 1$ there corresponds to $2 \cdot \tfrac14 \ge \tfrac12$ at the old point, not to $\tfrac14 \ge \tfrac12$.
6. So the first step is false: the two sides are not [[homogeneous|2C3PAQ7H50]] of the same degree, since the left has degree $2$ and the right degree $1$.

## Remarks

The correct statement comes from $x^2 - x = x(x - 1)$: $x^2 \ge x$ exactly when $x \le 0$ or $x \ge 1$, and it fails exactly on $0 < x < 1$.
The general test replaces each variable $x$ by $sx$ and checks that both sides gain the same factor $s^d$; here they gain $s^2$ and $s$.
The reduction does apply to $x^2 \ge 0$, where $0$ counts as homogeneous of every degree.

A new variable can make an inhomogeneous statement homogeneous.
Here $x^2 \ge x$ becomes $x^2 \ge xy$ at $y = 1$.
The homogeneous claim fails at $x = 1$, $y = 2$, and scaling by $\tfrac12$ moves that point to $x = \tfrac12$, $y = 1$, the original counterexample.

## Explanations

### L1 human

The square of a number is not always at least the number.
Half squared is a quarter, and a quarter is less than a half.
For $1$ and $-1$ the claim is true, but these two numbers do not stand for all numbers here.
Doubling a number makes its square four times as large, so the two sides change by different factors.
A check at size $1$ therefore says nothing about other sizes.

### L2 human

We compare with $x^2 + 1 \ge 2x$, which becomes homogeneous after a new variable is added.

1. This statement is not homogeneous either, with degrees $2$, $0$ and $1$, so the reduction to $\lvert x \rvert = 1$ is not valid for it.
2. The statement is still true, since $x^2 + 1 - 2x = (x - 1)^2 \ge 0$.
3. Its homogeneous form $x^2 + y^2 \ge 2xy$ can be reduced to $y = 1$ for $y \neq 0$, since every term gains the factor $s^2 > 0$.
   The reduced claim $t^2 + 1 \ge 2t$ is the original statement.
4. So for this statement the special case $y = 1$ is the whole problem, while $\lvert x \rvert = 1$ is not.

Before any scaling step, compare the degrees of all the terms.
Watch out: checking the special case with care does not replace the check that the transformation preserves the statement.
