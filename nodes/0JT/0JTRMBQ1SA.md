---
tag: 0JTRMBQ1SA
kind: definition
name: System of linear equations
msc: [15A06]
defines: 0GT4WWGWH2
uses: [0DNNT7DBFM]
sources:
  - url: https://en.wikipedia.org/wiki/System_of_linear_equations
    locator: lead section
---

## Definition

Let $F$ be a field and let $m, n \ge 1$ be integers.
Consider a *system of linear equations* over $F$, with $m$ equations in the unknowns $x_1, \dots, x_n$. Such a system is a list of [[linear equations|0Q3ZT8J05R]]
$$\begin{aligned} a_{11} x_1 + a_{12} x_2 + \cdots + a_{1n} x_n &= b_1, \\ &\ \ \vdots \\ a_{m1} x_1 + a_{m2} x_2 + \cdots + a_{mn} x_n &= b_m, \end{aligned}$$
where all $a_{ij}$ and $b_i$ are elements of $F$.
A *solution* of the system is a tuple $(s_1, \dots, s_n) \in F^n$ that is a solution of each of the $m$ equations.
The *solution set* of the system is the set of all its solutions.

## Remarks

With the [[coefficient matrix|0HQFZAP3ND]] $A = (a_{ij})$, the vector $b = (b_1, \dots, b_m)^T$ and $x = (x_1, \dots, x_n)^T$, the system is the single equation $Ax = b$.
Over a field, a system has no solution, exactly one solution, or more than one solution.
When $F$ is infinite, "more than one" means infinitely many.

## Explanations

### L1 human

A system of linear equations asks for values of the unknowns that make several linear equations true together.
For example, $x + y = 3$ and $x - y = 1$ together have the single solution $x = 2$, $y = 1$.
In the plane, each equation is a line, and a solution is a point on all the lines.
