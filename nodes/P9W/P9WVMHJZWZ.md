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

In analytic geometry, the plane is $\mathbb{R}^2$, the [[Cartesian product|09CEDJYBKP]] of the [[real numbers|08J2M1JYAG]] with themselves.
Here a point and a [[line|0MP9BCF6DP]] are defined, so they are not [[primitive notions|QMQEJKFEYZ]].

1. A point is a pair $(x, y)$ of real numbers.
2. A line is a set $\ell = \{(x, y) \in \mathbb{R}^2 : ax + by = c\}$ for real numbers $a$, $b$, $c$ with $(a, b) \neq (0, 0)$.
3. "The point $P$ lies on $\ell$" means $P \in \ell$.
4. Axiom I1 of incidence geometry becomes a theorem. Let $(x_1, y_1) \neq (x_2, y_2)$.
5. Existence: take $a = y_2 - y_1$, $b = x_1 - x_2$ and $c = a x_1 + b y_1$. Then $(a, b) \neq (0, 0)$, and both points satisfy $ax + by = c$, by direct substitution.
6. Uniqueness: if both points satisfy $a'x + b'y = c'$, then $a'(x_2 - x_1) + b'(y_2 - y_1) = 0$. So $(a', b')$ is a multiple of $(a, b)$, and $c'$ is the same multiple of $c$, which gives the same set.

So in this setting "line" has a definition, and the axioms of incidence geometry are theorems about real numbers.

## Remarks

1. The real numbers are themselves defined in set theory, so the chain of definitions ends at the primitive notions of set theory.
2. The condition $(a, b) \neq (0, 0)$ is part of the definition. Without it, $0x + 0y = 0$ would give the whole plane, and $0x + 0y = 1$ would give the empty set.
3. This model of geometry shows that the axioms of incidence geometry are consistent, if the real numbers are.
4. Compare the [[three-point model|RF12XC7AY0]], where lines are sets with two elements.

## Explanations

### L1 human

On graph paper, each point has two coordinates, such as $(2, 3)$.
A straight line is the set of points whose coordinates satisfy an equation like $y = 2x + 1$.
So with coordinates, we can say exactly what a point and a line are.
In pure geometry, without coordinates, the same words are not defined, and only the rules about them are given.

### L2 human

We find the line through $(1, 2)$ and $(3, 6)$ with the formula from step 5.

1. Take $a = 6 - 2 = 4$ and $b = 1 - 3 = -2$.
2. Then $c = 4 \cdot 1 + (-2) \cdot 2 = 0$. So the line is $4x - 2y = 0$, that is, $y = 2x$.
3. Check: $4 \cdot 3 - 2 \cdot 6 = 0$, so $(3, 6)$ lies on it.

The typical use: in coordinates, statements about lines become equations that we can solve.
A trap is to think that the equation is unique.
The equations $4x - 2y = 0$ and $2x - y = 0$ define the same line.
