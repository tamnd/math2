---
tag: M9SW4NVP2H
kind: concept
name: Sylvester equation
msc: [15A24, 65F45]
sources:
  - url: https://en.wikipedia.org/wiki/Sylvester_equation
same_as:
  wikidata: Q3730848
  wikipedia: Sylvester equation
---

## Summary

The Sylvester equation is the linear matrix equation $AX + XB = C$, in which the matrices $A$, $B$, $C$ are given and the matrix $X$ is unknown.
It has a unique solution exactly when $A$ and $-B$ have no common [[eigenvalue|0BQAA2BK3Q]].
It appears in block diagonalisation, in control theory, and as the general form of the [[Lyapunov equation|92GVPZH9FT]].

## Explanations

### L1 human

The equation asks for a matrix $X$ such that multiplying it by $A$ on the left and by $B$ on the right, and adding, gives $C$.
Although $X$ is a matrix, the equation is linear in its entries, so it is a large system of ordinary linear equations.
For $1 \times 1$ matrices it reads $ax + xb = c$, with the solution $x = c / (a + b)$ when $a + b \ne 0$.
The condition $a + b \ne 0$ becomes the condition on eigenvalues for larger matrices.
