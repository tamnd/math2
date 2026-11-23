---
tag: RVVKF9AC7N
kind: example
name: The factorization of a^3 + b^3 + c^3 - 3abc
msc: ["00A35", "97H20"]
topics: [MEKKHHQTKB]
audience: school
instance_of: [XP5SDYKJX0]
uses: [XP5SDYKJX0, 0DRF0F3XC9]
sources:
  - url: https://en.wikipedia.org/wiki/Identity_(mathematics)
    locator: lead section
---

## Example

We prove that for all real numbers $a$, $b$ and $c$,
$$a^3 + b^3 + c^3 - 3abc = (a + b + c)(a^2 + b^2 + c^2 - ab - bc - ca).$$
We [[transform one side into the other|XP5SDYKJX0]], starting from the right side, because expanding a product is a step that a reader can check line by line.
Let $a$, $b$ and $c$ be arbitrary real numbers, and write $Q = a^2 + b^2 + c^2 - ab - bc - ca$.

1. By the distributive law, $(a + b + c)Q = aQ + bQ + cQ$.
2. Expand each of the three products:
   $$\begin{aligned} aQ &= a^3 + ab^2 + ac^2 - a^2b - abc - a^2c, \\ bQ &= a^2b + b^3 + bc^2 - ab^2 - b^2c - abc, \\ cQ &= a^2c + b^2c + c^3 - abc - bc^2 - ac^2. \end{aligned}$$
3. Add the three lines.
   The six pairs $\pm ab^2$, $\pm ac^2$, $\pm a^2b$, $\pm a^2c$, $\pm bc^2$ and $\pm b^2c$ cancel.
4. What remains is $a^3 + b^3 + c^3$ and three copies of $-abc$.
   So the right side equals $a^3 + b^3 + c^3 - 3abc$, the left side.

Check with $a = 1$, $b = 2$, $c = 3$: the left side is $1 + 8 + 27 - 18 = 18$, and the right side is
$$6 \cdot (1 + 4 + 9 - 2 - 6 - 3) = 6 \cdot 3 = 18.$$

## Remarks

The direction of the proof is a kindness to the reader.
Expanding has a reason at every step, while factoring the left side needs an idea that the reader cannot check.
The proof uses only the laws of a commutative ring, so the identity holds for integers, complex numbers and polynomials too.

The second factor has a useful second form:
$$Q = \tfrac12 \big( (a - b)^2 + (b - c)^2 + (c - a)^2 \big),$$
since the three squares add up to $2a^2 + 2b^2 + 2c^2 - 2ab - 2bc - 2ca = 2Q$.
So $Q \ge 0$, and for $a, b, c \ge 0$ the identity gives $a^3 + b^3 + c^3 \ge 3abc$, which is the [[inequality of arithmetic and geometric means|0DRF0F3XC9]] for $a^3$, $b^3$ and $c^3$.
If $a + b + c = 0$, the identity gives $a^3 + b^3 + c^3 = 3abc$; for $1$, $2$ and $-3$ both sides are $-18$.

## Explanations

### L1 human

The left side is a sum of three cubes with a correction term, and the right side is a product of two brackets.
To show that they always agree, multiply out the brackets.
You get eighteen terms, and twelve of them cancel in pairs.
The six terms that remain are exactly the left side.
With $a = 1$, $b = 2$ and $c = 3$, both sides give $18$.

### L2 human

We use the identity to factor $x^3 + y^3 - 1 + 3xy$ for real $x$ and $y$.

1. Match the expression with $a^3 + b^3 + c^3 - 3abc$ by taking $a = x$, $b = y$ and $c = -1$.
2. Then $c^3 = -1$ and $-3abc = -3 \cdot x \cdot y \cdot (-1) = 3xy$, so the match is exact.
3. The identity gives
   $$x^3 + y^3 - 1 + 3xy = (x + y - 1)(x^2 + y^2 + 1 - xy + y + x).$$
4. Check at $x = 2$, $y = 1$: the left side is $8 + 1 - 1 + 6 = 14$, and the right side is $2 \cdot 7 = 14$.

The identity factors symmetric expressions of degree $3$ and proves inequalities.
Watch out for signs in step 3: with $c = -1$, the terms $-bc$ and $-ca$ become $+y$ and $+x$.
