---
tag: 60XZ6DNKKW
kind: statement
role: theorem
name: Levinson recursion
msc: [65F05, 15B05]
uses: [GKY2WSHE26, 0GT4WWGWH2, 0EB9N0S33C, 0BT9BYWVRY, GA46NC0CJZ]
about: [GKY2WSHE26]
sources:
  - url: https://en.wikipedia.org/wiki/Levinson_recursion
same_as:
  wikidata: Q11679774
  wikipedia: Levinson recursion
---

## Statement

Let $T = (t_{i-j})_{1 \le i, j \le N}$ be an $N \times N$ [[Toeplitz matrix|GKY2WSHE26]] over $\mathbb{K}$, where $\mathbb{K}$ is $\R$ or $\C$, and let $y \in \mathbb{K}^N$.
For $n \le N$, let $T^n$ be the leading $n \times n$ submatrix of $T$, and assume that every $T^n$ is [[invertible|0EB9N0S33C]].
Let $f^n, b^n, x^n \in \mathbb{K}^n$ solve $T^n f^n = e_1$, $T^n b^n = e_n$ and $T^n x^n = (y_1, \dots, y_n)^T$, where $e_1, e_n$ are the first and last unit vectors.
Put
$$\varepsilon_f^n = \sum_{j=1}^n t_{n+1-j} f^n_j, \qquad \varepsilon_b^n = \sum_{j=1}^n t_{-j} b^n_j, \qquad \varepsilon_x^n = \sum_{j=1}^n t_{n+1-j} x^n_j.$$
Then $1 - \varepsilon_f^n \varepsilon_b^n \ne 0$, and
$$f^{n+1} = \frac{1}{1 - \varepsilon_f^n \varepsilon_b^n} \left( \begin{pmatrix} f^n \\ 0 \end{pmatrix} - \varepsilon_f^n \begin{pmatrix} 0 \\ b^n \end{pmatrix} \right), \qquad b^{n+1} = \frac{1}{1 - \varepsilon_f^n \varepsilon_b^n} \left( \begin{pmatrix} 0 \\ b^n \end{pmatrix} - \varepsilon_b^n \begin{pmatrix} f^n \\ 0 \end{pmatrix} \right),$$
$$x^{n+1} = \begin{pmatrix} x^n \\ 0 \end{pmatrix} + (y_{n+1} - \varepsilon_x^n) \, b^{n+1}.$$
Starting from $f^1 = b^1 = 1/t_0$ and $x^1 = y_1 / t_0$, the *Levinson recursion* computes the solution $x^N$ of $T x = y$ in $O(N^2)$ arithmetic operations.

## Remarks

The key fact is that both the leading and the trailing $n \times n$ blocks of $T^{n+1}$ equal $T^n$.
So $T^{n+1} (f^n, 0)^T = (1, 0, \dots, 0, \varepsilon_f^n)^T$ and $T^{n+1} (0, b^n)^T = (\varepsilon_b^n, 0, \dots, 0, 1)^T$, and the stated combinations give $e_1$ and $e_{n+1}$.
Similarly $T^{n+1} (x^n, 0)^T = (y_1, \dots, y_n, \varepsilon_x^n)^T$, and adding $(y_{n+1} - \varepsilon_x^n) b^{n+1}$ fixes the last entry.
If $1 - \varepsilon_f^n \varepsilon_b^n$ were $0$, the nonzero vector $(f^n, 0)^T - \varepsilon_f^n (0, b^n)^T$ would lie in the kernel of $T^{n+1}$.
This vector is nonzero because its last entry is $-\varepsilon_f^n b^n_n$, with $\varepsilon_f^n \ne 0$ and $b^n_n = \det T^{n-1} / \det T^n \ne 0$ by Cramer's rule.
Each step costs $O(n)$ operations, which gives the total $O(N^2)$, against $O(N^3)$ for Gaussian elimination.
The hypothesis on all leading [[minors|0BT9BYWVRY]] is needed: for $T = \begin{pmatrix} 0 & 1 \\ 1 & 0 \end{pmatrix}$ the matrix is invertible but $t_0 = 0$, and the recursion cannot start.
For symmetric positive definite $T$ every leading submatrix is invertible, and the special case of the [[Yule–Walker equations|GA46NC0CJZ]] is the Levinson–Durbin recursion.

## Explanations

### L1 human

A Toeplitz matrix is constant along each diagonal, so it is described by only $2N - 1$ numbers.
The Levinson recursion uses this structure to solve a Toeplitz system by growing the solution one size at a time.
Each growth step reuses the previous answer and costs only a few vector operations.

### L2 human

Toeplitz systems arise from stationary time series, in linear prediction, and in signal processing, where $T$ is a matrix of autocovariances.
The recursion solves them in $O(N^2)$ time and $O(N)$ memory, which made it a standard tool in speech coding.
It can be unstable when some leading submatrix is nearly singular, even if $T$ itself is well conditioned; superfast $O(N \log^2 N)$ algorithms also exist.
