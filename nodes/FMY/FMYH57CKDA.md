---
tag: FMYH57CKDA
kind: proof
name: Proof that a quotient of continuous functions is continuous
msc: [26A15]
proves: 0GR2APWTAC
uses: [0P27W9RW0G, 0PAQM3H57X, 0MVDQEAB60, 03S6GWWKEZ, 09G6KHS6GY]
sources:
  - url: https://www.jirka.org/ra/
    locator: Proposition 3.2.5
---

## Proof

We use [[sequential continuity|0PAQM3H57X]] and the quotient rule for limits of sequences.

1. Let $D \subseteq \R$ and let $f, g \colon D \to \R$ be [[continuous|0P27W9RW0G]] with $g(x) \ne 0$ for all $x \in D$. Then $f/g$ is defined on all of $D$.
2. By the equivalence of continuity and sequential continuity, $f$ and $g$ are [[sequentially continuous|0MVDQEAB60]].
3. Let $(x_n)$ be a sequence in $D$ that converges to a point $a \in D$. By step 2, $f(x_n) \to f(a)$ and $g(x_n) \to g(a)$.
4. We have $g(a) \ne 0$. By the [[quotient rule for limits|03S6GWWKEZ]], there is $N$ such that $(f(x_n)/g(x_n))_{n \ge N}$ converges to $f(a)/g(a)$.
5. Let $\varepsilon > 0$. By the [[epsilon-N form|09G6KHS6GY]] for the sequence of step 4, there is $N' \ge N$ with $\abs{f(x_n)/g(x_n) - f(a)/g(a)} < \varepsilon$ for all $n \ge N'$.
6. The same $N'$ works for the whole sequence $(f(x_n)/g(x_n))_{n \ge 0}$, which is defined by step 1. So $(f/g)(x_n) \to (f/g)(a)$.
7. Since $(x_n)$ and $a$ were arbitrary, $f/g$ is sequentially continuous. By the equivalence again, $f/g$ is continuous.

## Idea

Sequential continuity reduces the question to the quotient rule for limits of sequences. The hypothesis $g \ne 0$ on $D$ makes the quotient defined everywhere and makes the limit $g(a)$ nonzero.
