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

A linear equation is an equation in which each unknown appears only multiplied by a constant, and these terms are added.
Let $F$ be a [[field|04C5ZBG1WT]] and let $n \ge 1$ be an integer.
A *linear equation* over $F$ in the unknowns $x_1, \dots, x_n$ is an equation of the form
$$a_1 x_1 + a_2 x_2 + \cdots + a_n x_n = b,$$
where the coefficients $a_1, \dots, a_n$ and the constant term $b$ are elements of $F$.
A *solution* of the equation is a tuple $(s_1, \dots, s_n) \in F^n$ such that $a_1 s_1 + \cdots + a_n s_n = b$.
The *solution set* is the set of all solutions, a subset of the [[coordinate space|0XM8BZD76G]] $F^n$.

## Notation

With $a = (a_1, \dots, a_n)$ and $x = (x_1, \dots, x_n)$ the equation is often written $a \cdot x = b$.
The equation is *homogeneous* when $b = 0$.

## Remarks

The coefficients and the constant term must be elements of the field $F$, and this condition does real work.
It means that the field decides which equations have solutions.
For example, $2x = 1$ has the solution $x = \tfrac12$ over $\mathbb{Q}$, but over $\mathbb{F}_2$ the coefficient $2$ equals $0$, and the equation reads $0 = 1$.

The shape of the left side is the heart of the definition.
Each term is a constant times one unknown, so $2x + 3y = 6$ over $\mathbb{R}$ is linear, and $(3, 0)$ is a solution because $6 + 0 = 6$.
The equation $xy = 1$ fails the condition, because $xy$ is a product of two unknowns and not a constant times one unknown.

The definition allows every coefficient to be zero.
Then the solution set is all of $F^n$ when $b = 0$, and it is empty when $b \ne 0$.
When some coefficient is nonzero and $F = \mathbb{R}$, $n = 2$, the solutions form a line in the plane.
The concept page on the [[linear equation|0Q3ZT8J05R]] counts the solutions and gives more examples.

## Explanations

### L1 human

A linear equation adds up the unknowns, each one times a fixed number, and sets the sum equal to a fixed number.
No unknown is squared, and no two unknowns are multiplied together.
With two real unknowns, the solutions usually draw a straight line, and this gives the name "linear".

### L2 human

Does $(1, 2, 0)$ solve $3x_1 - x_2 + 5x_3 = 1$ over $\mathbb{R}$?
Put the values into the left side:
$$3 \cdot 1 - 2 + 5 \cdot 0 = 1.$$
This is the right side, so $(1, 2, 0)$ is a solution.
Watch out for equations such as $x + y = 2x - 3$, with unknowns on both sides.
They are linear, but you read off the coefficients only after you move every unknown to the left, here $-x + y = -3$.

### L3 human

A linear equation over $F$ says that a [[linear form|07YQ1C78G0]] on $F^n$ takes a given value.
Several linear equations together form a [[system of linear equations|0GT4WWGWH2]], the main object of the sub-area.
