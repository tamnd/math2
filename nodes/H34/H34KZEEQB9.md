---
tag: H34KZEEQB9
kind: proof
name: Proof that Cauchy sequences are bounded
msc: [40A05]
proves: 0G6D8E7CTA
uses: [0QZMTN5AXX, 05FQ3VGAR9, 03HF5PMY5T]
sources:
  - url: https://www.jirka.org/ra/html/sec_cauchy.html
    locator: Proposition 2.4.4
---

## Proof

1. Since $(a_n)$ is a [[Cauchy sequence|0QZMTN5AXX]], take $\varepsilon = 1$. There is $N$ with $|a_m - a_n| < 1$ for all $m, n \ge N$.
2. For $n \ge N$, the [[triangle inequality|03HF5PMY5T]] gives $|a_n| \le |a_n - a_N| + |a_N| < 1 + |a_N|$.
3. Let $K = \max(|a_0|, |a_1|, \dots, |a_{N-1}|, |a_N| + 1)$. This is a maximum of finitely many real numbers, so it exists, and $K \ge 0$.
4. For $n < N$, $|a_n|$ is one of the numbers in the maximum, so $|a_n| \le K$. For $n \ge N$, step 2 gives $|a_n| < |a_N| + 1 \le K$.
5. So $|a_n| \le K$ for all $n \in \mathbb{N}$, and $(a_n)$ is [[bounded|05FQ3VGAR9]].

## Idea

From some index $N$ on, all terms lie within $1$ of the term $a_N$. Only finitely many terms come before $N$, and they have a largest absolute value.
