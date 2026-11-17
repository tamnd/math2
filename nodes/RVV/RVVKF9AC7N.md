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
We [[transform one side into the other|XP5SDYKJX0]]: we start from the right side, because it is the side with more structure, and we expand it.
Let $a$, $b$ and $c$ be arbitrary real numbers, and write $Q = a^2 + b^2 + c^2 - ab - bc - ca$.

1. By the distributive law, $(a + b + c) Q = aQ + bQ + cQ$.
2. We expand the first product: $aQ = a^3 + ab^2 + ac^2 - a^2b - abc - a^2c$.
3. We expand the second product: $bQ = a^2b + b^3 + bc^2 - ab^2 - b^2c - abc$.
4. We expand the third product: $cQ = a^2c + b^2c + c^3 - abc - bc^2 - ac^2$.
5. We add the three lines. The terms $ab^2$ and $-ab^2$ cancel, and so do $ac^2$ and $-ac^2$, $a^2b$ and $-a^2b$, $a^2c$ and $-a^2c$, $bc^2$ and $-bc^2$, and $b^2c$ and $-b^2c$.
6. The terms that remain are $a^3 + b^3 + c^3$ and three copies of $-abc$.
7. So the right side equals $a^3 + b^3 + c^3 - 3abc$, the left side.

A check with numbers: for $a = 1$, $b = 2$ and $c = 3$, the left side is $1 + 8 + 27 - 18 = 18$.
The right side is $6 \cdot (1 + 4 + 9 - 2 - 6 - 3) = 6 \cdot 3 = 18$.

## Remarks

1. The direction of the proof matters for the reader. Expanding a product is a routine step with a clear reason, while factoring the left side needs an idea that the reader cannot check line by line.
2. The second factor has another form: $Q = \frac12 \big( (a - b)^2 + (b - c)^2 + (c - a)^2 \big)$. Expand the three squares to check it: their sum is $2a^2 + 2b^2 + 2c^2 - 2ab - 2bc - 2ca = 2Q$.
3. So $Q \ge 0$ for all real $a$, $b$, $c$. If $a, b, c \ge 0$, then $a + b + c \ge 0$, and the identity gives $a^3 + b^3 + c^3 \ge 3abc$. This is the [[inequality of arithmetic and geometric means|0DRF0F3XC9]] for three numbers, applied to $a^3$, $b^3$ and $c^3$.
4. If $a + b + c = 0$, the identity gives $a^3 + b^3 + c^3 = 3abc$. For $1$, $2$ and $-3$: $1 + 8 - 27 = -18$ and $3 \cdot 1 \cdot 2 \cdot (-3) = -18$.
5. The proof uses only the laws of a commutative ring, so the identity holds in every commutative ring, for example for integers, complex numbers and polynomials.

## Explanations

### L1 human

The left side is a sum of cubes with a correction term, and the right side is a product of two brackets.
To show that they are always equal, we multiply out the brackets.
We get eighteen terms, and twelve of them cancel in pairs.
The six terms that remain are exactly the left side.
With $a = 1$, $b = 2$ and $c = 3$, both sides give $18$.

### L2 human

We use the identity to factor $x^3 + y^3 - 1 + 3xy$, for real $x$ and $y$.

1. We match the expression with $a^3 + b^3 + c^3 - 3abc$. Take $a = x$, $b = y$ and $c = -1$.
2. Then $c^3 = -1$ and $-3abc = -3 \cdot x \cdot y \cdot (-1) = 3xy$. So the expression is exactly $a^3 + b^3 + c^3 - 3abc$.
3. The identity gives $(x + y - 1)(x^2 + y^2 + 1 - xy + y + x)$.
4. Check at $x = 2$ and $y = 1$: the expression is $8 + 1 - 1 + 6 = 14$, and the product is $2 \cdot (4 + 1 + 1 - 2 + 1 + 2) = 2 \cdot 7 = 14$.

The typical use of the identity is to factor a symmetric expression of degree $3$, or to prove an inequality.
A trap is a sign error in step 3: $-bc$ and $-ca$ with $c = -1$ give $+y$ and $+x$, not $-y$ and $-x$.
