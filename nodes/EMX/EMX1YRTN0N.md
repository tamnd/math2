---
tag: EMX1YRTN0N
kind: proof
name: Proof of the polarization identity
msc: ["46C05", "15A63"]
topics: [1D4JTZ9VS3]
audience: ug1
proves: 05FKHRT0B4
methods: [0NTF6DMVAP, 0WCP0PVET6]
uses: [01EK923SKP, 0VGSYBWHV2, 0KG4D8AP6G, 0BJV24C4SY, 0RJF668P1T]
sources:
  - url: https://en.wikipedia.org/wiki/Polarization_identity
    locator: Polarization identities
  - url: https://en.wikipedia.org/wiki/Polarization_identity
    locator: Isometries
---

## Proof

Write $\bar a$ for the [[complex conjugate|0BJV24C4SY]] of a scalar $a$.
Over $\mathbb{R}$, $\bar a = a$.

1. By axioms 1 and 2 of the [[inner product|0VGSYBWHV2]], for $u, v, w \in V$ and a scalar $a$, we get $\langle w, u + a v \rangle = \overline{\langle u, w \rangle + a \langle v, w \rangle}$. This equals $\langle w, u \rangle + \bar a \langle w, v \rangle$.
2. Let $a$ be a scalar with $a \bar a = 1$. By the [[induced norm|0KG4D8AP6G]], axiom 1 and step 1, $\norm{x + a y}^2 = \langle x + a y, x + a y \rangle$.
3. Expanding, $\norm{x + a y}^2 = \langle x, x \rangle + \bar a \langle x, y \rangle + a \langle y, x \rangle + a \bar a \langle y, y \rangle$. Since $a \bar a = 1$, the last term is $\norm{y}^2$.
4. Real case. Over $\mathbb{R}$, axiom 2 gives $\langle y, x \rangle = \langle x, y \rangle$. Step 3 with $a = 1$ gives $\norm{x + y}^2 = \norm{x}^2 + 2 \langle x, y \rangle + \norm{y}^2$.
5. Step 3 with $a = -1$ gives $\norm{x - y}^2 = \norm{x}^2 - 2 \langle x, y \rangle + \norm{y}^2$. Subtracting from step 4, $\norm{x + y}^2 - \norm{x - y}^2 = 4 \langle x, y \rangle$.
6. Dividing by $4$ gives the first real formula. Step 4, solved for $\ip{x}{y}$, gives the second real formula. This proves part 1.
7. Complex case: let $a = i^k$ with $k \in \set{0, 1, 2, 3}$. Then $\bar a = (-i)^k$, so $a \bar a = 1^k = 1$. Step 3 applies.
8. Multiply step 3 by $a$ and use $a \bar a = 1$. This gives $a \norm{x + a y}^2 = a \bigl( \norm{x}^2 + \norm{y}^2 \bigr) + \langle x, y \rangle + a^2 \langle y, x \rangle$.
9. Sum step 8 over $k = 0, 1, 2, 3$. We have $\sum_{k=0}^{3} i^k = 1 + i - 1 - i = 0$.
10. Also $\sum_{k=0}^{3} i^{2k} = 1 - 1 + 1 - 1 = 0$. So only the term $\langle x, y \rangle$ survives, four times.
11. Hence $\sum_{k=0}^{3} i^k \norm{x + i^k y}^2 = 4 \langle x, y \rangle$. Dividing by $4$ gives the complex identity. Writing out the four terms, with $i^2 = -1$ and $i^3 = -i$, gives the second form of part 2.
12. Part 3. Let $T \colon V \to W$ be [[linear|0RJF668P1T]] with $\norm{Tz} = \norm{z}$ for all $z \in V$. For each scalar $a$, linearity gives $Tx + aTy = T(x + ay)$, so $\norm{Tx + aTy} = \norm{x + ay}$.
13. Over $\mathbb{R}$, apply part 1 in $W$ and in $V$, with $a = 1$ and $a = -1$: $\ip{Tx}{Ty} = \frac14(\norm{Tx + Ty}^2 - \norm{Tx - Ty}^2) = \frac14(\norm{x + y}^2 - \norm{x - y}^2) = \ip{x}{y}$.
14. Over $\mathbb{C}$, apply part 2 in the same way, with $a = i^k$ for $k = 0, 1, 2, 3$. Each of the four norms is the same in $W$ and in $V$, by step 12. So $\ip{Tx}{Ty} = \ip{x}{y}$, and this proves part 3.

## Idea

Expanding $\norm{x + ay}^2$ gives $\norm{x}^2 + \norm{y}^2$ plus the mixed terms $\bar a\ip{x}{y} + a\ip{y}{x}$.
Weighting by the fourth roots of unity and summing cancels everything except $\ip{x}{y}$.
Over $\mathbb{R}$, the weights $\pm 1$ are enough, since the inner product is symmetric.
Part 3 follows, because a linear map that keeps norms keeps every term of the formula.

## Variants

- Over $\mathbb{C}$ one can also derive part 2 from part 1. The real part of $\ip{x}{y}$ is $\frac14(\norm{x + y}^2 - \norm{x - y}^2)$. The imaginary part is the real part of $\ip{x}{iy}$.
- For part 3 over $\mathbb{R}$, the expansion $\norm{x + y}^2 = \norm{x}^2 + 2\ip{x}{y} + \norm{y}^2$ in $V$ and in $W$ gives the result with one formula.
