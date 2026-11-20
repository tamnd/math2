---
tag: 5VNTTZGN1A
kind: example
name: The annihilator of a plane and of a line in R^3
msc: ["15A04"]
topics: [9K7FFF26QR]
audience: ug1
instance_of: [0ASHNYF7AG]
uses: [0R6M158SQ9, 06Q1EFVH0Q, 713F6AM1X1]
sources:
  - url: https://en.wikipedia.org/wiki/Dual_space
    locator: Quotient spaces and annihilators
---

## Example

Let $V = \R^3$, and write each form as $f = ax + by + cz$, that is, $f(x, y, z) = ax + by + cz$.
We compute two [[annihilators|0R6M158SQ9]].

*A plane.* Let $U = \set{(x, y, z) : x + y + z = 0}$.

1. $U$ has the basis $u_1 = (1, -1, 0)$ and $u_2 = (1, 0, -1)$. Both satisfy $x + y + z = 0$, they are independent, and $U \ne \R^3$, so $\dim U = 2$.
2. $f \in U^0$ exactly when $f(u_1) = a - b = 0$ and $f(u_2) = a - c = 0$.
3. So $a = b = c$, and $U^0 = \set{a(x + y + z) : a \in \R}$, the line spanned by $x + y + z$.
4. Check with the [[dimension formula|06Q1EFVH0Q]]: $\dim U + \dim U^0 = 2 + 1 = 3$.

*A line.* Let $L$ be the line spanned by $(1, 2, 3)$.

5. $f \in L^0$ exactly when $f(1, 2, 3) = a + 2b + 3c = 0$.
6. The solutions are $(a, b, c) = b(-2, 1, 0) + c(-3, 0, 1)$ with $b, c \in \R$.
7. So $L^0$ is spanned by $f_1 = -2x + y$ and $f_2 = -3x + z$. Check: $f_1(1, 2, 3) = -2 + 2 = 0$ and $f_2(1, 2, 3) = -3 + 3 = 0$.
8. Check with the dimension formula: $\dim L + \dim L^0 = 1 + 2 = 3$.
9. The common kernel of $f_1$ and $f_2$ is the set with $y = 2x$ and $z = 3x$, that is, the points $x(1, 2, 3)$. So $(L^0)_0 = L$.

## Remarks

- The plane $U$ contains $L$ exactly when $L^0 \supseteq U^0$. Here $x + y + z$ takes the value $6$ at $(1, 2, 3)$, so $U^0 \not\subseteq L^0$, and indeed $L \not\subseteq U$.
- The forms $f_1$ and $f_2$ give a system of two equations whose solution set is $L$. Any other basis of $L^0$ gives an equivalent system.

## Explanations

### L1 human

A plane through the origin in space has one equation, up to a factor, so its annihilator is a line of forms.
A line through the origin has two independent equations, so its annihilator is a plane of forms.
In both cases the dimensions add up to $3$.

### L2 human

To compute an annihilator, test a general form on a basis of the subspace.

1. Write a general form with unknown coefficients.
2. Require it to vanish on each basis vector of the subspace.
3. Solve the linear system for the coefficients.

The typical use is to turn a spanning set of a subspace into a system of equations for it.
A trap: testing on vectors that do not span the subspace gives a larger set of forms than the annihilator.
