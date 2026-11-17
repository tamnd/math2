---
tag: ~a66c7eef
kind: example
name: Rounding the solution of a linear programming relaxation
msc: ["00A35", "90C10"]
topics: [X1NSTVGDNQ]
audience: ug1
not_instance_of:
  - target: ~a5a06d23
    note: the relaxation drops the integrality condition, so it is not equivalent to the original problem, and rounding its solution gives a point that breaks a constraint
uses: [~a5a06d23, PYMHHM5Z6F, 9GX3WH5EQF]
sources:
  - url: https://en.wikipedia.org/wiki/Linear_programming_relaxation
    locator: lead section
  - url: https://en.wikipedia.org/wiki/Integer_programming
    locator: lead section
---

## Example

Problem: find integers $x$ and $y$ that make $y$ as large as possible under the conditions
$$-x + y \leq 1, \qquad 3x + 2y \leq 12, \qquad 2x + 3y \leq 12, \qquad x \geq 0, \qquad y \geq 0.$$
This is an [[integer programming|9GX3WH5EQF]] problem.
A tempting [[auxiliary problem|~a5a06d23]] drops the condition that $x$ and $y$ are integers.
The result is the [[linear programming relaxation|PYMHHM5Z6F]], which allows all real $x$ and $y$.
We follow the plan "solve the relaxation, then round" and see where it misleads.

1. Solve the relaxation. The conditions $y \leq 1 + x$ and $y \leq \frac{12 - 2x}{3}$ bound $y$ from above. The first bound grows with $x$ and the second falls, so the largest $y$ is where they meet.
2. From $1 + x = \frac{12 - 2x}{3}$ we get $3 + 3x = 12 - 2x$, so $x = \frac{9}{5} = 1.8$ and $y = 2.8$.
3. Check the third condition: $3 \cdot 1.8 + 2 \cdot 2.8 = 5.4 + 5.6 = 11 \leq 12$. So $(1.8, 2.8)$ is the optimum of the relaxation, with $y = 2.8$.
4. Round to the nearest integers: $(2, 3)$.
5. Check $(2, 3)$: $-2 + 3 = 1 \leq 1$ and $3 \cdot 2 + 2 \cdot 3 = 12 \leq 12$, but $2 \cdot 2 + 3 \cdot 3 = 13 > 12$. The rounded point breaks a condition.
6. In fact no point with $y = 3$ is allowed: $-x + 3 \leq 1$ needs $x \geq 2$, and $2x + 9 \leq 12$ needs $x \leq 1.5$.
7. The true answer is $y = 2$, reached at $(1, 2)$ and at $(2, 2)$. For $(1, 2)$: $1 \leq 1$, $7 \leq 12$, $8 \leq 12$. For $(2, 2)$: $0 \leq 1$, $10 \leq 12$, $10 \leq 12$.

## Remarks

The relaxation is an auxiliary problem that is not equivalent to the original problem.
Pólya calls such a passage a unilateral reduction: a solution of the original problem is a solution of the relaxation, but not the other way round.
So the relaxation gives a bound, not an answer.
Here the bound is useful: every allowed integer point has $y \leq 2.8$, so $y \leq 2$, and the point $(1, 2)$ shows that $2$ is reached.
The error is the rounding, which treats the auxiliary problem as if it were equivalent.

The gap between the relaxation and the integer problem depends on the data.
If the third condition were $2x + 3y \leq 13$, the relaxation would give the point $(2, 3)$ itself, which is an integer point, and rounding would do no harm.

## Explanations

### L1 human

We want whole numbers that satisfy three rules and make $y$ as large as we can.
A simpler problem lets $x$ and $y$ be any numbers, also fractions.
That problem has its best point at $x = 1.8$ and $y = 2.8$.
Rounding gives $x = 2$ and $y = 3$, but this point breaks one of the rules.
The simpler problem was not the same problem, so its answer could not just be rounded.

### L2 human

We use the relaxation correctly, as a bound.

1. Every integer solution is also a real solution, so its $y$ is at most the optimum of the relaxation, $2.8$.
2. An integer $y$ with $y \leq 2.8$ has $y \leq 2$.
3. We search the row $y = 2$: the conditions become $x \geq 1$, $3x \leq 8$ and $2x \leq 6$.
4. The integers with $1 \leq x \leq \frac{8}{3}$ are $x = 1$ and $x = 2$.
5. So the maximum of $y$ is $2$, reached at $(1, 2)$ and $(2, 2)$.

The typical use: a relaxation is an auxiliary problem whose answer bounds the answer of the original problem.

A trap: a bound is not a solution; the bound must be matched by an allowed point, as in step 3.
