---
tag: 6ZETVMWH50
kind: proof
name: Proof of the chain rule with an auxiliary difference quotient
msc: [26A24]
proves: 0RXX2PT1MQ
uses: [0F1WR9C83K, 0A61B60B5R, 0GBZDAFPX8, 0W8YHHGCJG, 07ZMX4ANJS, 0NRQPQX3VA, 07EGCNHAVW, 000MXHEY22, 09G6KHS6GY, 0734RSVF2V]
sources:
  - url: https://en.wikipedia.org/wiki/Chain_rule
    locator: First proof
---

## Proof

We replace the difference quotient of $g$ by a function $Q$ that is also defined where the denominator vanishes.

1. Put $b = f(a)$, so $b \in J$. Define $Q \colon J \to \R$ by $Q(y) = \frac{g(y) - g(b)}{y - b}$ for $y \ne b$, and $Q(b) = g'(b)$.
2. For every $y \in J$, we have $g(y) - g(b) = Q(y) (y - b)$. For $y \ne b$ this is the definition of $Q$. For $y = b$ both sides are $0$.
3. Claim: $Q$ is continuous at $b$. Let $\varepsilon > 0$. By the definition of the [[derivative|0F1WR9C83K]] and the [[epsilon-delta form of limits|0GBZDAFPX8]], there is $\delta > 0$ with this property.
4. For $k \ne 0$ with $\abs{k} < \delta$ and $b + k \in J$, we have $\abs{\frac{g(b + k) - g(b)}{k} - g'(b)} < \varepsilon$.
5. Let $y \in J$ with $\abs{y - b} < \delta$. If $y \ne b$, step 4 with $k = y - b$ gives $\abs{Q(y) - Q(b)} < \varepsilon$. If $y = b$, the difference is $0$.
6. By the [[epsilon-delta form of continuity|0W8YHHGCJG]], $Q$ is continuous at $b$, which proves the claim.
7. Since $f$ is differentiable at $a$, it is continuous at $a$ by [[differentiable functions are continuous|07ZMX4ANJS]]. Also $f(I) \subseteq J$. By [[composition of continuous functions|0NRQPQX3VA]], $Q \circ f \colon I \to \R$ is continuous at $a$.
8. Let $H = \set{h \ne 0 : a + h \in I}$. As $I$ is an open interval containing $a$, $0$ is a [[limit point|07EGCNHAVW]] of $H$.
9. For $h \in H$, step 2 with $y = f(a + h)$ and division by $h$ give
$$\frac{g(f(a + h)) - g(f(a))}{h} = Q(f(a + h)) \cdot \frac{f(a + h) - f(a)}{h}.$$
10. Let $(h_n)$ be a sequence in $H$ with $h_n \to 0$. By the [[sequential characterization of limits|000MXHEY22]], $\frac{f(a + h_n) - f(a)}{h_n} \to f'(a)$.
11. Claim: $Q(f(a + h_n)) \to Q(f(a)) = g'(b)$. Let $\varepsilon > 0$, and take $\delta > 0$ from the continuity of $Q \circ f$ at $a$ (step 7).
12. By the [[epsilon-N form|09G6KHS6GY]], $\abs{h_n} < \delta$ for all large $n$. For those $n$, $\abs{Q(f(a + h_n)) - g'(b)} < \varepsilon$. This proves the claim.
13. By the [[limit of a product of sequences|0734RSVF2V]] and step 9, the difference quotient of $g \circ f$ at $h_n$ tends to $g'(b) f'(a)$.
14. This holds for every such sequence. By the sequential characterization, the difference quotient of $g \circ f$ at $a$ tends to $g'(f(a)) f'(a)$.
15. So $g \circ f$ is [[differentiable|0A61B60B5R]] at $a$, and $(g \circ f)'(a) = g'(f(a)) \, f'(a)$.

## Idea

The naive proof divides by $f(a + h) - f(a)$, which may be zero. The function $Q$ is the difference quotient of $g$ at $f(a)$, patched with the value $g'(f(a))$ where the quotient is undefined. The identity $g(y) - g(b) = Q(y)(y - b)$ then holds everywhere, and continuity of $Q$ finishes the argument.
