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

Let $V = \mathbb{R}^3$, the [[coordinate space|713F6AM1X1]] of dimension $3$.
Write each linear form as $f = ax + by + cz$, which means $f(x, y, z) = ax + by + cz$.
We compute the [[annihilator|0R6M158SQ9]] of a plane and of a line.

*The plane.* Let $U = \{ (x, y, z) : x + y + z = 0 \}$.

1. The vectors $u_1 = (1, -1, 0)$ and $u_2 = (1, 0, -1)$ satisfy $x + y + z = 0$, so they lie in $U$.
2. They are independent, since neither is a multiple of the other, and $U \ne \mathbb{R}^3$ because $(1, 0, 0) \notin U$. So $\dim U = 2$ and $u_1, u_2$ is a basis of $U$.
3. A form vanishes on $U$ exactly when it vanishes on the basis:
$$f(u_1) = a - b = 0, \qquad f(u_2) = a - c = 0.$$
4. So $a = b = c$, and $U^0 = \{ a(x + y + z) : a \in \mathbb{R} \}$ is the line spanned by $x + y + z$.
5. Check with the [[dimension formula|06Q1EFVH0Q]]: $\dim U + \dim U^0 = 2 + 1 = 3$.

*The line.* Let $L$ be the line spanned by $(1, 2, 3)$.

6. A form lies in $L^0$ exactly when it vanishes at the spanning vector:
$$f(1, 2, 3) = a + 2b + 3c = 0.$$
7. This one equation in three unknowns has the solutions $(a, b, c) = b(-2, 1, 0) + c(-3, 0, 1)$ with $b, c \in \mathbb{R}$.
8. So $L^0$ is spanned by $f_1 = -2x + y$ and $f_2 = -3x + z$. Check: $f_1(1, 2, 3) = -2 + 2 = 0$ and $f_2(1, 2, 3) = -3 + 3 = 0$.
9. Check with the dimension formula: $\dim L + \dim L^0 = 1 + 2 = 3$.
10. The common kernel of $f_1$ and $f_2$ is given by $y = 2x$ and $z = 3x$, so it is the set of points $x(1, 2, 3)$, which is $L$ again.

## Remarks

The example shows the two directions of the annihilator.
From a basis of a subspace we found its equations, and step 10 shows that those equations give the subspace back.
So the two equations $y = 2x$ and $z = 3x$ describe $L$, and any other basis of $L^0$ gives an equivalent system.

The example also shows how inclusions reverse.
A line lies in a plane exactly when the annihilator of the line contains the annihilator of the plane.
Here $x + y + z$ takes the value $6$ at $(1, 2, 3)$, so $x + y + z \notin L^0$, and so $L$ does not lie in $U$.
If we change the line to the span of $(1, 2, -3)$, then $x + y + z$ gives $1 + 2 - 3 = 0$, so this line does lie in $U$.

## Explanations

### L1 human

A plane through the origin in space has one equation, and every other equation of the plane is a multiple of it.
So its annihilator is a line of forms.
A line through the origin needs two independent equations, so its annihilator is a plane of forms.
In both cases the two dimensions add up to $3$.

### L2 human

The method works for any subspace given by a spanning set.
Write a general form with unknown coefficients, ask that it vanish on each spanning vector, and solve the resulting linear system for the coefficients.
For the line through $(1, 2, 3)$ that system was the single equation $a + 2b + 3c = 0$, and its two free unknowns gave the two equations of the line.
This is the standard way to turn a spanning set of a subspace into a system of equations for it.
Watch out: if you test on vectors that do not span the subspace, you get a set of forms that is larger than the annihilator.
