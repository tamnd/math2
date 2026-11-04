---
tag: GK54EWGGR4
kind: proof
name: Proof of the sequential characterization of limits
msc: [26A03]
proves: 000MXHEY22
uses: [0TXTSEMHR5, 0GBZDAFPX8, 09G6KHS6GY, 0WH916TJNY, 0XKWSSY8P2]
sources:
  - url: https://www.jirka.org/ra/
    locator: Lemma 3.1.7
---

## Proof

We use the [[epsilon-delta form of the limit|0GBZDAFPX8]] and the [[epsilon-N form|09G6KHS6GY]] for sequences. The converse is proved by contraposition.

1. Let $D \subseteq \R$, let $f \colon D \to \R$, let $a$ be a limit point of $D$, and let $L \in \R$.
2. Assume first that $\lim_{x \to a} f(x) = L$, in the sense of the [[limit of a function|0TXTSEMHR5]]. Let $(x_n)$ be a sequence in $D \setminus \set{a}$ with $x_n \to a$. Let $\varepsilon > 0$.
3. The epsilon-delta form gives $\delta > 0$ with $\abs{f(x) - L} < \varepsilon$ for all $x \in D$ with $0 < \abs{x - a} < \delta$.
4. Since $x_n \to a$, the epsilon-N form gives $N$ with $\abs{x_n - a} < \delta$ for all $n \ge N$.
5. For $n \ge N$, also $x_n \ne a$, so $0 < \abs{x_n - a} < \delta$. Step 3 gives $\abs{f(x_n) - L} < \varepsilon$.
6. So [[$f(x_n) \to L$|0XKWSSY8P2]] by the epsilon-N form. This proves the first direction.
7. Conversely, assume that $\lim_{x \to a} f(x) = L$ fails. We show that the sequence condition fails.
8. By the epsilon-delta form, there is $\varepsilon > 0$ with this property: for each $\delta > 0$ there is $x \in D$ with $0 < \abs{x - a} < \delta$ and $\abs{f(x) - L} \ge \varepsilon$.
9. For each natural number $n$, apply step 8 with $\delta = 1/(n+1)$. This gives $x_n \in D$ with $0 < \abs{x_n - a} < 1/(n+1)$ and $\abs{f(x_n) - L} \ge \varepsilon$.
10. Each $x_n$ lies in $D \setminus \set{a}$, since $x_n \ne a$.
11. Let $\eta > 0$. There is $m \ge 1$ with [[$1/m < \eta$|0WH916TJNY]]. For $n \ge m$, $\abs{x_n - a} < 1/(n+1) < 1/m < \eta$. So $x_n \to a$.
12. But $\abs{f(x_n) - L} \ge \varepsilon$ for every $n$. So no $N$ works for this $\varepsilon$ in the epsilon-N form, and $f(x_n) \not\to L$.
13. So the sequence condition fails. By contraposition, the sequence condition implies $\lim_{x \to a} f(x) = L$.

## Idea

If $f(x)$ is close to $L$ near $a$, then $f(x_n)$ is close to $L$ once $x_n$ is near $a$. If the limit fails, one $\varepsilon$ is violated arbitrarily close to $a$. Picking one bad point within $1/(n+1)$ of $a$ for each $n$ gives a sequence that witnesses the failure.
