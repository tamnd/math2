---
tag: EMX1YRTN0N
kind: proof
name: Proof of the polarisation identity
msc: [46C05, 15A63]
proves: 05FKHRT0B4
uses: [0QVNCJXRY3, 0NB0AWGJBW, 0MFJJV97RJ, 0BJV24C4SY]
sources:
  - url: https://en.wikipedia.org/wiki/Polarization_identity
    locator: Polarization identities
---

## Proof

Write $\bar a$ for the [[complex conjugate|0BJV24C4SY]] of a scalar $a$. Over $\R$, $\bar a = a$.

1. By axioms 1 and 2 of the [[inner product|0NB0AWGJBW]], for $u, v, w \in V$ and a scalar $a$, we get $\langle w, u + a v \rangle = \overline{\langle u, w \rangle + a \langle v, w \rangle}$. This equals $\langle w, u \rangle + \bar a \langle w, v \rangle$.
2. Let $a$ be a scalar with $a \bar a = 1$. By the [[induced norm|0MFJJV97RJ]], axiom 1 and step 1, $\norm{x + a y}^2 = \langle x + a y, x + a y \rangle$.
3. Expanding, $\norm{x + a y}^2 = \langle x, x \rangle + \bar a \langle x, y \rangle + a \langle y, x \rangle + a \bar a \langle y, y \rangle$. Since $a \bar a = 1$, the last term is $\norm{y}^2$.
4. Real case. Over $\R$, axiom 2 gives $\langle y, x \rangle = \langle x, y \rangle$. Step 3 with $a = 1$ gives $\norm{x + y}^2 = \norm{x}^2 + 2 \langle x, y \rangle + \norm{y}^2$.
5. Step 3 with $a = -1$ gives $\norm{x - y}^2 = \norm{x}^2 - 2 \langle x, y \rangle + \norm{y}^2$. Subtracting from step 4, $\norm{x + y}^2 - \norm{x - y}^2 = 4 \langle x, y \rangle$.
6. Dividing by $4$ gives the real identity.
7. Complex case. Let $a = i^k$ with $k \in \set{0, 1, 2, 3}$. Then $\bar a = (-i)^k$, so $a \bar a = 1^k = 1$. Step 3 applies.
8. Multiply step 3 by $a$ and use $a \bar a = 1$. This gives $a \norm{x + a y}^2 = a \bigl( \norm{x}^2 + \norm{y}^2 \bigr) + \langle x, y \rangle + a^2 \langle y, x \rangle$.
9. Sum step 8 over $k = 0, 1, 2, 3$. We have $\sum_{k=0}^{3} i^k = 1 + i - 1 - i = 0$.
10. Also $\sum_{k=0}^{3} i^{2k} = 1 - 1 + 1 - 1 = 0$. So only the term $\langle x, y \rangle$ survives, four times.
11. Hence $\sum_{k=0}^{3} i^k \norm{x + i^k y}^2 = 4 \langle x, y \rangle$. Dividing by $4$ gives the complex identity.

## Idea

Expanding $\norm{x + a y}^2$ gives $\norm{x}^2 + \norm{y}^2$ plus the mixed terms $\bar a \langle x, y \rangle + a \langle y, x \rangle$. Weighting by suitable roots of unity and summing cancels everything except $\langle x, y \rangle$. Over $\R$, the weights $\pm 1$ are enough, since the inner product is symmetric.
