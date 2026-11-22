---
tag: P9WVMHJZWZ
kind: example
name: A line in the coordinate plane is a defined notion
msc: ["00A35", "51N20"]
topics: [BP0WAF23HB]
audience: ug1
not_instance_of:
  - target: QMQEJKFEYZ
    note: in analytic geometry a line is defined from real numbers as the solution set of a linear equation
uses: [QMQEJKFEYZ, 0MP9BCF6DP, 08J2M1JYAG, 09CEDJYBKP, RF12XC7AY0]
sources:
  - url: https://en.wikipedia.org/wiki/Line_(geometry)
    locator: Linear equation
  - url: https://en.wikipedia.org/wiki/Line_(geometry)
    locator: In axiomatic systems
---

## Example

In analytic geometry the plane is $\mathbb{R}^2$, the [[Cartesian product|09CEDJYBKP]] of the [[real numbers|08J2M1JYAG]] with themselves.
Here a point and a [[line|0MP9BCF6DP]] have definitions, so they are not [[primitive notions|QMQEJKFEYZ]].
A point is a pair $(x, y)$ of real numbers.
A line is a set
$$\ell = \{(x, y) \in \mathbb{R}^2 : ax + by = c\}$$
for real numbers $a$, $b$, $c$ with $(a, b) \ne (0, 0)$, and "the point $P$ lies on $\ell$" means $P \in \ell$.
With these definitions, the incidence axiom "two distinct points lie on exactly one line" becomes a theorem, which we now prove.

1. Let $(x_1, y_1) \ne (x_2, y_2)$.
2. Existence.
   Take $a = y_2 - y_1$, $b = x_1 - x_2$ and $c = a x_1 + b y_1$.
   Then $(a, b) \ne (0, 0)$, because the points differ.
3. The first point satisfies $a x_1 + b y_1 = c$ by the choice of $c$.
   For the second point, $a x_2 + b y_2 - c = a(x_2 - x_1) + b(y_2 - y_1) = (y_2 - y_1)(x_2 - x_1) - (x_2 - x_1)(y_2 - y_1) = 0$.
4. Uniqueness.
   Suppose that both points also satisfy $a' x + b' y = c'$ with $(a', b') \ne (0, 0)$.
   Subtracting the two equations gives $a'(x_2 - x_1) + b'(y_2 - y_1) = 0$, so $(a', b')$ is perpendicular to the nonzero vector $(x_2 - x_1, y_2 - y_1)$.
5. The vector $(a, b)$ is perpendicular to the same vector, by step 3.
   In $\mathbb{R}^2$ the vectors perpendicular to a nonzero vector form a line through the origin, so $(a', b') = t(a, b)$ with $t \ne 0$.
6. Then $c' = a' x_1 + b' y_1 = t c$, so the equation $a' x + b' y = c'$ is $t$ times the equation $ax + by = c$, and both define the same set.

So in analytic geometry "line" is a defined notion, and the axioms of incidence geometry are theorems about real numbers.

## Remarks

The condition $(a, b) \ne (0, 0)$ is part of the definition for a reason.
Without it, $0x + 0y = 0$ would make the whole plane a "line", and $0x + 0y = 1$ would make the empty set one.

The chain of definitions does not stop at the real numbers, since they are in turn defined sets.
It ends at the primitive notions of set theory, set and membership.
The coordinate plane is also a model of incidence geometry, so the incidence axioms are consistent if the real numbers are.
Compare the [[three-point model|RF12XC7AY0]], another model in which lines are sets with two elements.

## Explanations

### L1 human

On graph paper, each point has two coordinates, such as $(2, 3)$.
A straight line is the set of points whose coordinates satisfy an equation like $y = 2x + 1$.
So with coordinates, we can say exactly what a point and a line are.
In pure geometry, without coordinates, the same words are not defined, and only the rules about them are given.

### L2 human

We find the line through $(1, 2)$ and $(3, 6)$ with the formula of step 2.
It gives
$$a = 6 - 2 = 4, \qquad b = 1 - 3 = -2, \qquad c = 4 \cdot 1 + (-2) \cdot 2 = 0,$$
so the line is $4x - 2y = 0$, which is $y = 2x$.
Check: $4 \cdot 3 - 2 \cdot 6 = 0$, so $(3, 6)$ lies on it.
The typical use is that statements about lines in coordinates become equations that we can solve.
Watch out: the equation of a line is not unique, since $4x - 2y = 0$ and $2x - y = 0$ define the same line, as step 6 predicts with $t = \tfrac{1}{2}$.
