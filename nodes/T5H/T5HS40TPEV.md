---
tag: T5HS40TPEV
kind: proof
name: Proof that convergent sequences are bounded
msc: [40A05]
proves: 0S4JF619V7
uses: [0AZ3R52593, 05FQ3VGAR9, 09G6KHS6GY, 03HF5PMY5T]
sources:
  - url: https://www.jirka.org/ra/html/sec_seqsandlims.html
    locator: Proposition 2.1.7
---

## Proof

1. Since $(a_n)$ is a [[convergent sequence|0AZ3R52593]], it converges to some real number $L$.
2. By the [[epsilon-N definition|09G6KHS6GY]] with $\varepsilon = 1$, there is a natural number $N$ with $|a_n - L| < 1$ for all $n \ge N$.
3. For $n \ge N$, the [[triangle inequality|03HF5PMY5T]] gives $|a_n| \le |a_n - L| + |L| < 1 + |L|$.
4. Let $K = \max(|a_0|, |a_1|, \dots, |a_{N-1}|, |L| + 1)$. This is the maximum of finitely many real numbers, so it exists, and $K \ge 0$.
5. For $n < N$, the number $|a_n|$ is one of the numbers in the maximum, so $|a_n| \le K$.
6. For $n \ge N$, step 3 gives $|a_n| < |L| + 1 \le K$.
7. So $|a_n| \le K$ for all $n \in \mathbb{N}$, and $(a_n)$ is [[bounded|05FQ3VGAR9]].

## Idea

From some index on, all terms lie within $1$ of the limit, so they are bounded by $|L| + 1$. Only finitely many terms come before that index, and a finite set of numbers always has a maximum.
