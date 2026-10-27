---
tag: 0DNNT7DBFM
kind: definition
name: Linear equation
msc: [15A06]
defines: 0Q3ZT8J05R
sources:
  - url: https://en.wikipedia.org/wiki/Linear_equation
    locator: lead section
inventory: [E8TJ2QYVQK]
---

## Definition

Let $F$ be a field and let $n \ge 1$ be an integer.
A *linear equation* over $F$ in the unknowns $x_1, \dots, x_n$ is an equation of the form
$$a_1 x_1 + a_2 x_2 + \cdots + a_n x_n = b,$$
where the coefficients $a_1, \dots, a_n$ are elements of $F$. The constant term $b$ is also an element of the field.
A *solution* of the equation is a tuple $(s_1, \dots, s_n) \in F^n$ such that $a_1 s_1 + \cdots + a_n s_n = b$.

## Remarks

The equation $2x + 3y = 6$ over $\R$ is linear, and $(3, 0)$ is a solution.
The equation $xy = 1$ is not linear, because it has a product of two unknowns.
Over $\R$ with $n = 2$, the solutions of a linear equation with $(a_1, a_2) \ne (0, 0)$ form a line in the plane.

## Explanations

### L1 human

A linear equation adds up the unknowns, each one times a fixed number, and sets the sum equal to a fixed number.
No unknown is squared, and no two unknowns are multiplied together.
With two unknowns over the real numbers, the solutions usually draw a straight line, and this gives the name "linear".
