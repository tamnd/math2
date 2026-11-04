---
tag: 3FSD94MMA4
kind: proof
name: Proof of the reciprocal rule
msc: [26A24]
proves: 0QD4E5JYPT
uses: [0F1WR9C83K, 0A61B60B5R, 07EGCNHAVW, 000MXHEY22, 07ZMX4ANJS, 0W8YHHGCJG, 09G6KHS6GY, 0734RSVF2V, 03S6GWWKEZ, 0C9S13WKMF]
sources:
  - url: https://en.wikipedia.org/wiki/Reciprocal_rule
    locator: Proof
---

## Proof

We first find an open interval around $a$ where $1/g$ is defined. Then we use the [[sequential characterization of limits|000MXHEY22]].

1. Since $g$ is differentiable at $a$, it is continuous at $a$ by [[differentiable functions are continuous|07ZMX4ANJS]]. Put $\eta = \abs{g(a)} > 0$.
2. By the [[epsilon-delta form of continuity|0W8YHHGCJG]], there is $\delta_0 > 0$ with $\abs{g(x) - g(a)} < \eta$ for $x \in I$ with $\abs{x - a} < \delta_0$.
3. For such $x$, the [[reverse triangle inequality|0C9S13WKMF]] gives $\abs{g(x)} \ge \abs{g(a)} - \abs{g(x) - g(a)} > 0$. So $g(x) \ne 0$.
4. Let $I_0 = I \cap (a - \delta_0, a + \delta_0)$. It is an open interval containing $a$, and $g$ has no zero on it. So $1/g$ is defined on $I_0$, and we view it as a function $I_0 \to \R$.
5. Let $H = \set{h \ne 0 : a + h \in I_0}$. Since $I_0$ is an open interval containing $a$, $0$ is a [[limit point|07EGCNHAVW]] of $H$.
6. For $h \in H$, write $q_g(h) = \frac{g(a + h) - g(a)}{h}$. Over a common denominator,
$$\frac{1}{h}\left( \frac{1}{g(a + h)} - \frac{1}{g(a)} \right) = \frac{- q_g(h)}{g(a + h) \, g(a)}.$$
7. Let $(h_n)$ be a sequence in $H$ with $h_n \to 0$. Each $h_n$ is a nonzero number with $a + h_n \in I$. By the definition of the [[derivative|0F1WR9C83K]] and the sequential characterization, $q_g(h_n) \to g'(a)$.
8. Claim: $g(a + h_n) \to g(a)$. Let $\varepsilon > 0$, and take $\delta > 0$ from the epsilon-delta form of continuity of $g$ at $a$. By the [[epsilon-N form|09G6KHS6GY]], $\abs{h_n} < \delta$ for all large $n$. Then $\abs{g(a + h_n) - g(a)} < \varepsilon$.
9. The constant sequences $g(a)$ and $-1$ converge to $g(a)$ and $-1$. By the [[limit of a product of sequences|0734RSVF2V]], $g(a + h_n) \, g(a) \to g(a)^2$ and $-q_g(h_n) \to -g'(a)$.
10. We have $g(a)^2 \ne 0$, and $g(a + h_n) g(a) \ne 0$ for all $n$ by step 4. By the [[limit of a quotient of sequences|03S6GWWKEZ]], the right side of step 6 at $h = h_n$ tends to $-\frac{g'(a)}{g(a)^2}$.
11. This holds for every such sequence. By the sequential characterization, the difference quotient of $1/g$ at $a$ tends to $-\frac{g'(a)}{g(a)^2}$ as $h \to 0$.
12. So $1/g$ is [[differentiable|0A61B60B5R]] at $a$, and $\left( \frac{1}{g} \right)'(a) = -\frac{g'(a)}{g(a)^2}$.

## Idea

Subtracting two fractions puts $g(a + h) - g(a)$ in the numerator and $g(a + h) g(a)$ in the denominator. The first gives the derivative of $g$ after dividing by $h$. The second tends to $g(a)^2$, which is not zero, because $g$ is continuous at $a$.
