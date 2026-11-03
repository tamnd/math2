---
tag: BE64PXZSEE
kind: proof
name: Proof that subsequences of a convergent sequence converge to the same limit
msc: [40A05]
proves: 0VHAVXW08V
uses: [0R8J3ZQMJS, 09G6KHS6GY, 0ASJVEFA9J]
sources:
  - url: https://www.jirka.org/ra/html/sec_seqsandlims.html
    locator: Proposition 2.1.17
---

## Proof

1. By the definition of a [[subsequence|0R8J3ZQMJS]], the indices satisfy $n_0 < n_1 < n_2 < \cdots$, and they are natural numbers.
2. We show $n_k \ge k$ for all $k$, by [[induction|0ASJVEFA9J]] on $k$. For $k = 0$, $n_0 \ge 0$ because $n_0$ is a natural number.
3. If $n_k \ge k$, then $n_{k+1} > n_k \ge k$. Since $n_{k+1}$ is an integer, $n_{k+1} \ge k + 1$.
4. Let $\varepsilon > 0$. By the [[epsilon-N definition|09G6KHS6GY]], there is $N$ with $|a_n - L| < \varepsilon$ for all $n \ge N$.
5. Let $k \ge N$. By steps 2 and 3, $n_k \ge k \ge N$. So $|a_{n_k} - L| < \varepsilon$.
6. By the epsilon-N definition, $a_{n_k} \to L$ as $k \to \infty$.

## Idea

The $k$-th term of a subsequence sits at position $n_k \ge k$ of the original sequence. So once $k$ passes the index $N$ that works for the sequence, all later terms of the subsequence are within $\varepsilon$ of $L$.
