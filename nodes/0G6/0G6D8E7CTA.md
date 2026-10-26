---
tag: 0G6D8E7CTA
kind: statement
role: proposition
name: Cauchy sequences are bounded
msc: [40A05]
uses: [0QZMTN5AXX, 05FQ3VGAR9]
sources:
  - url: https://en.wikipedia.org/wiki/Cauchy_sequence
    locator: Other properties
---

## Statement

Let $(a_n)$ be a [[Cauchy sequence|0QZMTN5AXX]] of real numbers.
Then $(a_n)$ is [[bounded|05FQ3VGAR9]].

## Remarks

Take $\varepsilon = 1$ to get $N$ with $|a_n - a_N| < 1$ for all $n \ge N$. Then $|a_n| \le \max(|a_0|, \dots, |a_{N-1}|, |a_N| + 1)$ for all $n$.
The statement holds in each metric space.
The proof of the [[Cauchy criterion|0ZA4AX4MW3]] uses this fact.

## Explanations

### L1 human

From some index on, all terms are within distance $1$ of one fixed term.
The finitely many terms before that index are bounded too, so the whole sequence is bounded.
