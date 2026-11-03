---
tag: 8CHX7JYGFS
kind: proof
name: Proof of the limit of a quotient of sequences
msc: [40A05]
proves: 03S6GWWKEZ
uses: [09G6KHS6GY, 0734RSVF2V, 0C9S13WKMF, 0GMV7GP8W0]
sources:
  - url: https://www.jirka.org/ra/html/sec_factslimsseqs.html
    locator: Proposition 2.2.5
---

## Proof

1. Since $b \ne 0$, the number $|b|/2$ is positive.
2. By the [[epsilon-N definition|09G6KHS6GY]], there is a natural number $N$ with $|b_n - b| < |b|/2$ for all $n \ge N$.
3. For $n \ge N$, the [[reverse triangle inequality|0C9S13WKMF]] gives $|b| - |b_n| \le |b_n - b| < |b|/2$. So $|b_n| > |b|/2 > 0$, and $b_n \ne 0$. This proves the first claim.
4. For $n \ge N$, since the [[absolute value is multiplicative|0GMV7GP8W0]],
$$\left| \frac{1}{b_n} - \frac{1}{b} \right| = \frac{|b - b_n|}{|b_n|\,|b|} < \frac{2 |b_n - b|}{|b|^2}.$$
Here we used $|b_n| > |b|/2$ from step 3.
5. Let $\varepsilon > 0$. Then $\varepsilon |b|^2 / 2 > 0$, so there is $N_1$ with $|b_n - b| < \varepsilon |b|^2 / 2$ for all $n \ge N_1$.
6. For $n \ge \max(N, N_1)$, steps 4 and 5 give $|1/b_n - 1/b| < \varepsilon$. So the sequence $(1/b_n)_{n \ge N}$ converges to $1/b$.
7. The sequence $(a_n)_{n \ge N}$ converges to $a$. Indeed, if $|a_n - a| < \varepsilon$ for all $n \ge M$, this holds for all $n \ge \max(N, M)$.
8. For $n \ge N$ we have $a_n / b_n = a_n \cdot (1/b_n)$. By the [[limit of a product|0734RSVF2V]] and steps 6 and 7, $(a_n / b_n)_{n \ge N}$ converges to $a \cdot (1/b) = a/b$.

## Idea

Since $b_n$ comes close to $b \ne 0$, eventually $|b_n|$ stays above $|b|/2$. This keeps $1/b_n$ away from infinity and makes $1/b_n - 1/b$ at most a constant times $b_n - b$. The product rule then handles $a_n \cdot (1/b_n)$.
