---
tag: TBBMVHAA48
kind: proof
name: Proof of the product rule
msc: [26A24]
proves: 0V9A43H7WV
uses: [0F1WR9C83K, 0A61B60B5R, 07EGCNHAVW, 000MXHEY22, 07ZMX4ANJS, 0W8YHHGCJG, 09G6KHS6GY, 0RAM4E07NR, 0734RSVF2V]
sources:
  - url: https://en.wikipedia.org/wiki/Product_rule
    locator: Limit definition of derivative
---

## Proof

We use the [[sequential characterization of limits|000MXHEY22]] and the limit laws for sequences.

1. Let $H = \set{h \ne 0 : a + h \in I}$. As $I$ is an open interval containing $a$, $0$ is a [[limit point|07EGCNHAVW]] of $H$.
2. For $u \colon I \to \R$ and $h \in H$, write $q_u(h) = \frac{u(a + h) - u(a)}{h}$. By the definition of the [[derivative|0F1WR9C83K]], $q_f(h) \to f'(a)$ and $q_g(h) \to g'(a)$ as $h \to 0$.
3. For $h \in H$, add and subtract $f(a) g(a + h)$ in the numerator of $q_{fg}(h)$. This gives $q_{fg}(h) = q_f(h) \, g(a + h) + f(a) \, q_g(h)$.
4. Let $(h_n)$ be a sequence in $H$ with $h_n \to 0$. By the sequential characterization, $q_f(h_n) \to f'(a)$ and $q_g(h_n) \to g'(a)$.
5. Claim: $g(a + h_n) \to g(a)$. Since $g$ is differentiable at $a$, it is continuous at $a$ by [[differentiable functions are continuous|07ZMX4ANJS]].
6. Let $\varepsilon > 0$. By the [[epsilon-delta form of continuity|0W8YHHGCJG]], there is $\delta > 0$ with $\abs{g(x) - g(a)} < \varepsilon$ for $x \in I$ with $\abs{x - a} < \delta$.
7. By the [[epsilon-N form|09G6KHS6GY]], there is $N$ with $\abs{h_n} < \delta$ for $n \ge N$. Then $\abs{g(a + h_n) - g(a)} < \varepsilon$ for $n \ge N$, which proves the claim.
8. The constant sequence $f(a)$ converges to $f(a)$. By the [[limit of a product of sequences|0734RSVF2V]], $q_f(h_n) \, g(a + h_n) \to f'(a) g(a)$ and $f(a) \, q_g(h_n) \to f(a) g'(a)$.
9. By the [[limit of a sum of sequences|0RAM4E07NR]] and step 3, $q_{fg}(h_n) \to f'(a) g(a) + f(a) g'(a)$.
10. This holds for every such sequence. By the sequential characterization, $q_{fg}(h) \to f'(a) g(a) + f(a) g'(a)$ as $h \to 0$.
11. So $f g$ is [[differentiable|0A61B60B5R]] at $a$, and $(f g)'(a) = f'(a) g(a) + f(a) g'(a)$.

## Idea

Adding and subtracting $f(a) g(a + h)$ splits the change of $f g$ into a change of $f$ and a change of $g$. Each piece becomes a difference quotient times a factor. The factor $g(a + h)$ tends to $g(a)$ because differentiable functions are continuous.
