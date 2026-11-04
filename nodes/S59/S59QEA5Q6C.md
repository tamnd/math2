---
tag: S59QEA5Q6C
kind: proof
name: Proof that repeating decimals are rational
msc: [11A63]
proves: 065S5B9HF1
uses: [06XY4X9430, 0K0H5E3Z5N, 09G6KHS6GY, 0RAM4E07NR, 0734RSVF2V, 0ZXJ2455NJ, 0C4JS9RF5M, 0NCJ5WXN6Z]
sources:
  - url: https://en.wikipedia.org/wiki/Repeating_decimal
    locator: Every repeating or terminating decimal is a rational number
---

## Proof

1. Let $x \ge 0$ have the [[decimal expansion|06XY4X9430]] $x = a_0 + \sum_{k=1}^{\infty} d_k 10^{-k}$. Let $N \ge 0$ and $p \ge 1$ with $d_{k+p} = d_k$ for each $k > N$.
2. For $K \ge 0$, let $S_K = a_0 + \sum_{k=1}^{K} d_k 10^{-k}$. By the definition of the [[sum of a series|0K0H5E3Z5N]], $S_K - a_0 \to x - a_0$. By the [[limit of a sum|0RAM4E07NR]], $S_K \to x$ as $K \to \infty$.
3. Also $S_{K+p} \to x$. Indeed, by the [[epsilon-N form of the limit|09G6KHS6GY]], if $\abs{S_K - x} < \varepsilon$ for $K \ge M$, then also $\abs{S_{K+p} - x} < \varepsilon$ for $K \ge M$.
4. Fix $K > N$. Multiply $S_{K+p}$ by $10^{N+p}$ and split the sum at $k = N + p$:
$$10^{N+p} S_{K+p} = 10^{N+p} a_0 + \sum_{k=1}^{N+p} d_k 10^{N+p-k} + \sum_{k=N+p+1}^{K+p} d_k 10^{N+p-k}.$$
5. In the last sum, write $k = j + p$ with $N + 1 \le j \le K$. Since $j > N$, $d_{j+p} = d_j$. So the last sum is $\sum_{j=N+1}^{K} d_j 10^{N-j}$.
6. In the same way, $10^N S_K = 10^N a_0 + \sum_{k=1}^{N} d_k 10^{N-k} + \sum_{j=N+1}^{K} d_j 10^{N-j}$.
7. Subtract step 6 from steps 4 and 5. The last sums cancel, and $10^{N+p} S_{K+p} - 10^N S_K = M$, where
$$M = 10^{N+p} a_0 + \sum_{k=1}^{N+p} d_k 10^{N+p-k} - 10^N a_0 - \sum_{k=1}^{N} d_k 10^{N-k}.$$
8. The number $M$ does not depend on $K$. It is an [[integer|0C4JS9RF5M]], since $a_0$ and the $d_k$ are integers and all the exponents of $10$ are at least $0$.
9. Use the [[limit of a product|0734RSVF2V]] with constant sequences and the [[limit of a sum|0RAM4E07NR]]. The left side of step 7 tends to $10^{N+p} x - 10^N x$ as $K \to \infty$.
10. The right side is the constant sequence $M$, which tends to $M$. By the [[uniqueness of limits|0ZXJ2455NJ]], $10^N (10^p - 1) x = M$.
11. Since $p \ge 1$, the integer $10^N (10^p - 1)$ is at least $9$, so it is nonzero. Thus $x = M / (10^N (10^p - 1))$ is a [[rational number|0NCJ5WXN6Z]].

## Idea

Shifting the decimal point by one period moves the repeating tail onto itself. Subtracting the two shifted copies cancels the tail and leaves an integer. So a nonzero integer multiple of $x$ is an integer.
