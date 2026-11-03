---
tag: E1JBPG7E3M
kind: proof
name: Proof of the squeeze theorem for sequences
msc: [40A05]
proves: 0XMF00T4XQ
uses: [09G6KHS6GY, 00S7C68D51]
sources:
  - url: https://www.jirka.org/ra/html/sec_factslimsseqs.html
    locator: Lemma 2.2.1
---

## Proof

1. Let $\varepsilon > 0$.
2. Since $a_n \to L$, the [[epsilon-N definition|09G6KHS6GY]] gives $N_1$ with $|a_n - L| < \varepsilon$ for all $n \ge N_1$.
3. Since $b_n \to L$, it gives $N_2$ with $|b_n - L| < \varepsilon$ for all $n \ge N_2$.
4. Let $M = \max(N, N_1, N_2)$ and let $n \ge M$.
5. By the definition of the [[absolute value|00S7C68D51]], step 2 gives $L - \varepsilon < a_n$, and step 3 gives $b_n < L + \varepsilon$.
6. Since $n \ge N$, the hypothesis gives $a_n \le c_n \le b_n$. So $L - \varepsilon < c_n < L + \varepsilon$.
7. So $|c_n - L| < \varepsilon$ for all $n \ge M$. By the epsilon-N definition, $c_n \to L$.

## Idea

From some index on, $c_n$ is trapped between $a_n$ and $b_n$. Both of these lie in the window $(L - \varepsilon, L + \varepsilon)$, so $c_n$ lies there too.
