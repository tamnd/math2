---
tag: 0VHAVXW08V
kind: statement
role: proposition
name: Subsequences of a convergent sequence converge to the same limit
msc: [40A05]
uses: [0R8J3ZQMJS, 0XKWSSY8P2, 09G6KHS6GY]
sources:
  - url: https://en.wikipedia.org/wiki/Limit_of_a_sequence
    locator: Properties
  - url: https://en.wikipedia.org/wiki/Subsequence
    locator: lead section
---

## Statement

Let $(a_n)$ be a real sequence that converges to a real number $L$.
Let $(a_{n_k})_{k \in \mathbb{N}}$ be a [[subsequence|0R8J3ZQMJS]] of $(a_n)$.
Then $a_{n_k} \to L$ as $k \to \infty$.

## Remarks

For the proof, let $\varepsilon > 0$ and take $N$ with $|a_n - L| < \varepsilon$ for $n \ge N$. Since $n_k \ge k$, we get $|a_{n_k} - L| < \varepsilon$ for all $k \ge N$.
It gives a test for divergence. If two subsequences have different limits, the sequence diverges. For $(-1)^n$ the even terms tend to $1$ and the odd terms tend to $-1$.

## Explanations

### L1 human

If all terms eventually stay close to $L$, then the terms that you keep also stay close to $L$.
Deleting terms cannot change where the sequence is going.
