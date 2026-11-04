---
tag: YQRMB9HE0Q
kind: proof
name: Proof that slopes of a convex function are increasing
msc: [26A51]
proves: 0BY5FTHEEE
uses: [0VV0HSW1ZS]
sources:
  - url: https://proofwiki.org/wiki/Equivalence_of_Definitions_of_Convex_Real_Function
---

## Proof

We write the middle point as a convex combination of the outer points and rearrange the convexity inequality.

1. Let $x < y < z$ be points of $I$. Put $t = \dfrac{z - y}{z - x}$. Then $0 < t < 1$ and $1 - t = \dfrac{y - x}{z - x}$.
2. We have $t x + (1 - t) z = \dfrac{(z - y) x + (y - x) z}{z - x} = \dfrac{y (z - x)}{z - x} = y$.
3. By the definition of a [[convex function|0VV0HSW1ZS]], $f(y) \le t f(x) + (1 - t) f(z)$.
4. Multiplying by $z - x > 0$ gives $(z - x) f(y) \le (z - y) f(x) + (y - x) f(z)$. Call this inequality $(\ast)$.
5. Subtract $(z - x) f(x)$ from both sides of $(\ast)$. Since $(z - y) - (z - x) = -(y - x)$, we get $(z - x)(f(y) - f(x)) \le (y - x)(f(z) - f(x))$.
6. Dividing by $(z - x)(y - x) > 0$ gives $\dfrac{f(y) - f(x)}{y - x} \le \dfrac{f(z) - f(x)}{z - x}$.
7. Subtract $(z - x) f(z)$ from both sides of $(\ast)$. Since $(y - x) - (z - x) = -(z - y)$, we get $(z - x)(f(y) - f(z)) \le (z - y)(f(x) - f(z))$.
8. Multiplying by $-1$ reverses the inequality: $(z - x)(f(z) - f(y)) \ge (z - y)(f(z) - f(x))$.
9. Dividing by $(z - x)(z - y) > 0$ gives $\dfrac{f(z) - f(x)}{z - x} \le \dfrac{f(z) - f(y)}{z - y}$.
10. Steps 6 and 9 together are the two claimed inequalities.

## Idea

The point $y$ splits $[x, z]$ in the ratio of the weights $t$ and $1 - t$. Convexity says the graph at $y$ lies below the chord from $x$ to $z$. Seen from $x$, this makes the chord to $y$ less steep. Seen from $z$, it makes the chord from $y$ steeper.
