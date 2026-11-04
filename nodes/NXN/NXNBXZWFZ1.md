---
tag: NXNBXZWFZ1
kind: proof
name: Proof of the quadratic formula by completing the square
msc: [12D10]
proves: 0KYZXYDGQZ
uses: [0FRSR10DWF, 09FTAET5Z4]
sources:
  - url: https://en.wikipedia.org/wiki/Quadratic_formula
    locator: Derivation by completing the square
---

## Proof

We complete the square and then factor a difference of two squares.

1. Let $a, b, c \in \C$ with $a \ne 0$, and let $s \in \C$ satisfy $s^2 = b^2 - 4ac$. Fix $x \in \C$.
2. The [[complex numbers|09FTAET5Z4]] [[form a field|0FRSR10DWF]]. So the usual rules of algebra hold, and each nonzero number has an inverse.
3. Expanding gives $(2ax + b)^2 = 4a^2x^2 + 4abx + b^2$.
4. By Step 3, $4a(ax^2 + bx + c) = (2ax + b)^2 - (b^2 - 4ac)$.
5. Since $s^2 = b^2 - 4ac$, Step 4 becomes $4a(ax^2 + bx + c) = (2ax + b)^2 - s^2$.
6. For all $u, v \in \C$ we have $u^2 - v^2 = (u - v)(u + v)$, by expanding the right side.
7. By Steps 5 and 6, $4a(ax^2 + bx + c) = (2ax + b - s)(2ax + b + s)$.
8. If $u, v \in \C$ and $uv = 0$, then $u = 0$ or $v = 0$. Indeed, if $u \ne 0$, then $v = u^{-1}(uv) = u^{-1} \cdot 0 = 0$.
9. The number $4a$ is nonzero, since $4 \ne 0$ and $a \ne 0$, by Step 8. Likewise $2a \ne 0$.
10. If $ax^2 + bx + c = 0$, then $4a(ax^2 + bx + c) = 0$. Conversely, if $4a(ax^2 + bx + c) = 0$, then $ax^2 + bx + c = 0$ by Steps 8 and 9. So the two equations are equivalent.
11. By Steps 7, 8 and 10, $ax^2 + bx + c = 0$ holds if and only if $2ax + b - s = 0$ or $2ax + b + s = 0$.
12. Since $2a \ne 0$, the equation $2ax + b - s = 0$ is equivalent to $x = \frac{-b + s}{2a}$. We add $s - b$ to both sides and multiply by $(2a)^{-1}$.
13. In the same way, $2ax + b + s = 0$ is equivalent to $x = \frac{-b - s}{2a}$.
14. By Steps 11, 12 and 13, $ax^2 + bx + c = 0$ if and only if $x = \frac{-b + s}{2a}$ or $x = \frac{-b - s}{2a}$.

## Idea

Multiplying the equation by $4a$ turns its left side into the perfect square $(2ax + b)^2$ minus the discriminant.
Since the discriminant is $s^2$, the result is a difference of two squares, which factors into two linear factors.
A product in a field is zero only when a factor is zero, so the roots are the zeros of the two linear factors.
