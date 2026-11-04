---
tag: V5S2RW52HK
kind: proof
name: Proof that continuity is equivalent to sequential continuity
msc: [26A15]
proves: 0PAQM3H57X
uses: [0P27W9RW0G, 0MVDQEAB60, 0W8YHHGCJG, 09G6KHS6GY, 0WH916TJNY, 0XKWSSY8P2]
sources:
  - url: https://www.jirka.org/ra/
    locator: Proposition 3.2.2
---

## Proof

We use the [[epsilon-delta form of continuity|0W8YHHGCJG]] and the [[epsilon-N form|09G6KHS6GY]] for sequences. The converse is proved by contraposition.

1. Let $D \subseteq \R$ and $f \colon D \to \R$. By definition, $f$ is [[continuous|0P27W9RW0G]] when it is continuous at each point of $D$.
2. Assume that $f$ is continuous. Let $(x_n)$ be a sequence in $D$ that [[converges|0XKWSSY8P2]] to $a \in D$. Let $\varepsilon > 0$.
3. Continuity at $a$ in epsilon-delta form gives $\delta > 0$ with $\abs{f(x) - f(a)} < \varepsilon$ for all $x \in D$ with $\abs{x - a} < \delta$.
4. Since $x_n \to a$, there is $N$ with $\abs{x_n - a} < \delta$ for all $n \ge N$. Then $\abs{f(x_n) - f(a)} < \varepsilon$ for all $n \ge N$.
5. So $f(x_n) \to f(a)$, and $f$ is [[sequentially continuous|0MVDQEAB60]].
6. Conversely, assume that $f$ is not continuous. Then $f$ is not continuous at some point $a \in D$.
7. By the epsilon-delta form, there is $\varepsilon > 0$ with this property: for each $\delta > 0$ there is $x \in D$ with $\abs{x - a} < \delta$ and $\abs{f(x) - f(a)} \ge \varepsilon$.
8. For each natural number $n$, apply step 7 with $\delta = 1/(n+1)$. This gives $x_n \in D$ with $\abs{x_n - a} < 1/(n+1)$ and $\abs{f(x_n) - f(a)} \ge \varepsilon$.
9. Let $\eta > 0$. There is $m \ge 1$ with [[$1/m < \eta$|0WH916TJNY]]. For $n \ge m$, $\abs{x_n - a} < 1/m < \eta$. So $x_n \to a$.
10. But $\abs{f(x_n) - f(a)} \ge \varepsilon$ for all $n$, so $f(x_n) \not\to f(a)$. Hence $f$ is not sequentially continuous.
11. By contraposition, sequential continuity implies continuity. This proves the equivalence.

## Idea

Continuity at $a$ says that points near $a$ have values near $f(a)$, and a convergent sequence eventually stays near $a$. If continuity fails at $a$, choosing one bad point within $1/(n+1)$ of $a$ for each $n$ gives a sequence that converges to $a$ while its values stay away from $f(a)$.
