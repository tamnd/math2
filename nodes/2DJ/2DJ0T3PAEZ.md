---
tag: 2DJ0T3PAEZ
kind: proof
name: Proof of the limit of a sum of sequences
msc: [40A05]
proves: 0RAM4E07NR
uses: [09G6KHS6GY, 03HF5PMY5T]
sources:
  - url: https://www.jirka.org/ra/html/sec_factslimsseqs.html
    locator: Proposition 2.2.5
---

## Proof

1. Let $\varepsilon > 0$. Then $\varepsilon/2 > 0$.
2. Since $a_n \to a$, the [[epsilon-N definition|09G6KHS6GY]] gives $N_1$ with $|a_n - a| < \varepsilon/2$ for all $n \ge N_1$.
3. Since $b_n \to b$, it gives $N_2$ with $|b_n - b| < \varepsilon/2$ for all $n \ge N_2$.
4. Let $N = \max(N_1, N_2)$ and let $n \ge N$.
5. By the [[triangle inequality|03HF5PMY5T]],
$$|(a_n + b_n) - (a + b)| = |(a_n - a) + (b_n - b)| \le |a_n - a| + |b_n - b|.$$
6. By steps 2 and 3, the right side is less than $\varepsilon/2 + \varepsilon/2 = \varepsilon$.
7. So $|(a_n + b_n) - (a + b)| < \varepsilon$ for all $n \ge N$. By the epsilon-N definition, $a_n + b_n \to a + b$.

## Idea

The error of the sum is at most the sum of the two errors. We make each error smaller than half of the allowed error $\varepsilon$.
