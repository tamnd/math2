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

We expand $\norm{x + ay}^2$ for a scalar $a$ of modulus $1$, and we combine the expansions for $a = \pm 1$ over $\mathbb{R}$ and for $a = 1, i, -1, -i$ over $\mathbb{C}$ so that only $\ip{x}{y}$ survives.
Write $\bar a$ for the [[complex conjugate|0BJV24C4SY]] of a scalar $a$, so that $\bar a = a$ over $\mathbb{R}$.
The [[inner product|0VGSYBWHV2]] is linear in the first slot and conjugate symmetric.

*The expansion.*

1. For $u, v, w \in V$ and a scalar $a$, conjugate symmetry and linearity in the first slot give
$$\ip{w}{u + av} = \overline{\ip{u}{w} + a\ip{v}{w}} = \ip{w}{u} + \bar a\ip{w}{v}.$$
2. Let $a$ be a scalar with $a\bar a = 1$.
   By the definition of the [[induced norm|0KG4D8AP6G]], linearity in the first slot and step 1,
$$\norm{x + ay}^2 = \ip{x}{x} + \bar a\ip{x}{y} + a\ip{y}{x} + a\bar a\ip{y}{y} = \norm{x}^2 + \bar a\ip{x}{y} + a\ip{y}{x} + \norm{y}^2.$$

*Part 1, the real case.*

3. Over $\mathbb{R}$, conjugate symmetry reads $\ip{y}{x} = \ip{x}{y}$.
   So step 2 with $a = 1$ and with $a = -1$ gives
$$\norm{x + y}^2 = \norm{x}^2 + 2\ip{x}{y} + \norm{y}^2, \qquad \norm{x - y}^2 = \norm{x}^2 - 2\ip{x}{y} + \norm{y}^2.$$
4. Subtracting the second equation from the first gives $\norm{x + y}^2 - \norm{x - y}^2 = 4\ip{x}{y}$, which is the first real formula.
5. Solving the first equation of step 3 for $\ip{x}{y}$ gives the second real formula, which proves part 1.

*Part 2, the complex case.*

6. Let $a = i^k$ with $k \in \{0, 1, 2, 3\}$.
   Then $\bar a = (-i)^k$ and $a\bar a = 1^k = 1$, so step 2 applies.
7. Multiply step 2 by $a$ and use $a\bar a = 1$:
$$a\norm{x + ay}^2 = a\big(\norm{x}^2 + \norm{y}^2\big) + \ip{x}{y} + a^2\ip{y}{x}.$$
8. Sum step 7 over $k = 0, 1, 2, 3$.
   The coefficients of $\norm{x}^2 + \norm{y}^2$ and of $\ip{y}{x}$ are
$$\sum_{k=0}^{3} i^k = 1 + i - 1 - i = 0, \qquad \sum_{k=0}^{3} i^{2k} = 1 - 1 + 1 - 1 = 0,$$
   so only the term $\ip{x}{y}$ survives, four times.
9. Hence $\sum_{k=0}^{3} i^k\norm{x + i^k y}^2 = 4\ip{x}{y}$, and dividing by $4$ gives the identity of part 2.
   Writing out the four terms with $i^2 = -1$ and $i^3 = -i$ gives its second form.

*Part 3, maps that keep norms.*

10. Let $T \colon V \to W$ be [[linear|0RJF668P1T]] with $\norm{Tz} = \norm{z}$ for all $z \in V$.
    For each scalar $a$, linearity gives $Tx + aTy = T(x + ay)$, so $\norm{Tx + aTy} = \norm{x + ay}$.
11. Over $\mathbb{R}$, apply part 1 in $W$ and in $V$, and use step 10 with $a = \pm 1$:
$$\ip{Tx}{Ty} = \frac14\left(\norm{Tx + Ty}^2 - \norm{Tx - Ty}^2\right) = \frac14\left(\norm{x + y}^2 - \norm{x - y}^2\right) = \ip{x}{y}.$$
12. Over $\mathbb{C}$, apply part 2 in the same way, with $a = i^k$ for $k = 0, 1, 2, 3$.
    Each of the four norms is the same in $W$ and in $V$ by step 10, so $\ip{Tx}{Ty} = \ip{x}{y}$, which proves part 3.

## Idea

Expanding $\norm{x + ay}^2$ gives $\norm{x}^2 + \norm{y}^2$ plus the mixed terms $\bar a\ip{x}{y} + a\ip{y}{x}$.
Over $\mathbb{R}$ the two mixed terms are equal, so the weights $\pm 1$ already isolate $\ip{x}{y}$.
Over $\mathbb{C}$ they differ, and we weight the four expansions by the fourth roots of unity, which sum to zero and so cancel everything except $\ip{x}{y}$.
Part 3 follows, because a linear map that keeps norms keeps every term of the formula.

## Variants

Over $\mathbb{C}$ one can derive part 2 from part 1.
The real formula gives $\operatorname{Re}\ip{x}{y}$, and since $\ip{x}{iy} = -i\ip{x}{y}$, the real part of $\ip{x}{iy}$ is $\operatorname{Im}\ip{x}{y}$.
Putting the two real parts together gives the four-term formula.
For part 3 over $\mathbb{R}$, the single expansion $\norm{x + y}^2 = \norm{x}^2 + 2\ip{x}{y} + \norm{y}^2$ in $V$ and in $W$ already gives the result.
