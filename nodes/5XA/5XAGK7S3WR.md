---
tag: 5XAGK7S3WR
kind: proof
name: Proof of the triangle inequality for norms
msc: [46B20]
proves: 0FJZMBX0ZZ
uses: [0V2WP9B1MF, 0KW2X0TFBX]
sources:
  - url: https://en.wikipedia.org/wiki/Triangle_inequality
    locator: Normed vector space
---

## Proof

1. The inequality $\norm{x + y} \le \norm{x} + \norm{y}$ is axiom 1 in the definition of a [[norm|0V2WP9B1MF]].
2. Write $x = (x - y) + y$. By axiom 1, $\norm{x} \le \norm{x - y} + \norm{y}$. So $\norm{x} - \norm{y} \le \norm{x - y}$.
3. In the same way, $y = (y - x) + x$ gives $\norm{y} - \norm{x} \le \norm{y - x}$.
4. Since $y - x = (-1)(x - y)$, axiom 2 gives $\norm{y - x} = \abs{-1} \norm{x - y}$. The [[absolute value|0KW2X0TFBX]] of $-1$ is $1$, so $\norm{y - x} = \norm{x - y}$.
5. Put $t = \norm{x} - \norm{y}$, a real number. By steps 2 to 4, both $t \le \norm{x - y}$ and $-t \le \norm{x - y}$.
6. The absolute value $\abs{t}$ equals $t$ or $-t$. So step 5 gives $\bigl| \norm{x} - \norm{y} \bigr| \le \norm{x - y}$.

## Idea

The first inequality is an axiom of a norm. For the reverse form, apply the axiom to $x = (x - y) + y$ and to $y = (y - x) + x$. Since $\norm{y - x} = \norm{x - y}$, the two bounds together control $\abs{\norm{x} - \norm{y}}$.
