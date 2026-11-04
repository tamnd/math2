---
tag: EW3RMDX14G
kind: proof
name: Proof of Fermat's Last Theorem for n = 4
msc: [11D25]
proves: 0E741HSMJ1
uses: [086BE0J3FZ]
sources:
  - url: https://en.wikipedia.org/wiki/Fermat%27s_right_triangle_theorem
---

## Proof

We reduce to the equation $x^4 - y^4 = z^2$.

1. Suppose $a$, $b$ and $c$ are positive integers with $a^4 + b^4 = c^4$.
2. Then $c^4 - b^4 = a^4 = (a^2)^2$.
3. So $x = c$, $y = b$ and $z = a^2$ are positive integers with $x^4 - y^4 = z^2$.
4. This contradicts [[Fermat's right triangle theorem|086BE0J3FZ]], which says that $x^4 - y^4 = z^2$ has no solution in positive integers.
5. Hence there are no positive integers $a$, $b$ and $c$ with $a^4 + b^4 = c^4$.

## Idea

A fourth power is a square. So a solution of $a^4 + b^4 = c^4$ is a solution of the stronger equation $c^4 - b^4 = z^2$ with $z = a^2$. Fermat's descent rules that out.
