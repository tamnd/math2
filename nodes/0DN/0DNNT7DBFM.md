---
tag: 0DNNT7DBFM
kind: definition
name: Linear equation
msc: ["15A06"]
topics: [DXSXFVDMXQ]
audience: school
defines: 0Q3ZT8J05R
uses: [04C5ZBG1WT, 0XM8BZD76G]
sources:
  - url: https://en.wikipedia.org/wiki/Linear_equation
    locator: lead section
  - book: isbn:9780321982384
    locator: Section 1.1
inventory: [E8TJ2QYVQK]
---

## Definition

Let $F$ be a [[field|04C5ZBG1WT]] and let $n \ge 1$ be an integer.
A *linear equation* over $F$ in the unknowns $x_1, \dots, x_n$ is an equation of the form
$$a_1 x_1 + a_2 x_2 + \cdots + a_n x_n = b,$$
where the coefficients $a_1, \dots, a_n$ are elements of $F$.
The constant term $b$ is also an element of $F$.
A *solution* of the equation is a tuple $(s_1, \dots, s_n) \in F^n$ such that $a_1 s_1 + \cdots + a_n s_n = b$.
The *solution set* is the set of all solutions, a subset of the [[coordinate space|0XM8BZD76G]] $F^n$.

## Notation

With $a = (a_1, \dots, a_n)$ and $x = (x_1, \dots, x_n)$ the equation is often written $a \cdot x = b$.
The equation is *homogeneous* when $b = 0$.

## Remarks

The equation $2x + 3y = 6$ over $\R$ is linear, and $(3, 0)$ is a solution.
The equation $xy = 1$ is not linear, because it has a product of two unknowns.
Over $\R$ with $n = 2$, the solutions of a linear equation with $(a_1, a_2) \ne (0, 0)$ form a line in the plane.
The coefficients may all be zero: then the solution set is $F^n$ if $b = 0$, and empty if $b \ne 0$.
The field matters: $2x = 1$ has the solution $x = 1/2$ over $\mathbb{Q}$, but over $\mathbb{F}_2$ it reads $0 = 1$ and has no solution.

## Explanations

### L1 human

A linear equation adds up the unknowns, each one times a fixed number, and sets the sum equal to a fixed number.
No unknown is squared, and no two unknowns are multiplied together.
With two unknowns over the real numbers, the solutions usually draw a straight line, and this gives the name "linear".

### L2 human

We test whether $(1, 2, 0)$ solves $3x_1 - x_2 + 5x_3 = 1$ over $\R$.

1. Put the values in the left side: $3 \cdot 1 - 2 + 5 \cdot 0$.
2. This equals $1$, which is the right side.
3. So $(1, 2, 0)$ is a solution.

A trap: an equation such as $x + y = 2x - 3$ is linear even though unknowns appear on both sides.
Move every term with an unknown to the left before you read off the coefficients: here $-x + y = -3$.

### L3 human

A linear equation over $F$ says that a [[linear form|07YQ1C78G0]] on $F^n$ takes a given value.
Several linear equations together form a [[system of linear equations|0GT4WWGWH2]], the main object of this topic.
