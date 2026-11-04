---
tag: 8Z4R1MEPAN
kind: proof
name: Proof of Abel's theorem by summation by parts
msc: [40A30]
proves: 0S4EMDQS2F
uses: [0CVVKY7GY2, 0VP56B4EMX, 0909PWZR62, 0NB643K60Q, 0S4JF619V7, 01X5CVV1Q5, 0Q7K4AXE53, 04Z5G0THN6, 0Y123X48GA, 0RAM4E07NR, 0734RSVF2V, 09G6KHS6GY, 03HF5PMY5T]
sources:
  - url: https://en.wikipedia.org/wiki/Abel%27s_theorem
    locator: Outline of proof
---

## Proof

We rewrite $G$ with the partial sums by summation by parts.

1. Let $s_n = \sum_{k=0}^{n} a_k$ be the [[partial sums|0NB643K60Q]], and let $s = \lim s_n$, which exists by hypothesis. Put $s_{-1} = 0$, so that $a_n = s_n - s_{n-1}$ for all $n \ge 0$.
2. The sequence $(s_n)$ converges, so it is [[bounded|0S4JF619V7]]: there is $K$ with $\abs{s_n} \le K$ for all $n$. Then $\abs{a_n} \le 2K$ by the [[triangle inequality|03HF5PMY5T]].
3. Fix $x$ with $0 \le x < 1$. Then $\abs{a_n x^n} \le 2K x^n$ and $\abs{s_n x^n} \le K x^n$. The [[geometric series|01X5CVV1Q5]] $\sum x^n$ converges.
4. By the [[comparison test|04Z5G0THN6]], $\sum a_n x^n$ and $\sum s_n x^n$ converge absolutely. So both [[converge|0Y123X48GA]].
5. For each $N$,
$$\sum_{n=0}^{N} a_n x^n = \sum_{n=0}^{N} s_n x^n - \sum_{n=1}^{N} s_{n-1} x^n = (1 - x) \sum_{n=0}^{N} s_n x^n + s_N x^{N+1}.$$
6. We have $\abs{s_N x^{N+1}} \le K x^{N+1}$, and [[$x^{N+1} \to 0$|0Q7K4AXE53]]. So $s_N x^{N+1} \to 0$.
7. Let $N \to \infty$ in step 5. The [[sum rule|0RAM4E07NR]] and the [[product rule|0734RSVF2V]] for limits give $G(x) = (1 - x) \sum_{n=0}^{\infty} s_n x^n$.
8. The geometric series gives $(1 - x) \sum_{n=0}^{\infty} x^n = 1$. So $s = (1 - x) \sum_{n=0}^{\infty} s x^n$.
9. Subtract step 8 from step 7, using the limit rules on partial sums: $G(x) - s = (1 - x) \sum_{n=0}^{\infty} (s_n - s) x^n$.
10. Let $\varepsilon > 0$. By the [[epsilon-N form|09G6KHS6GY]], there is $N$ with $\abs{s_n - s} < \varepsilon / 2$ for all $n \ge N$. Let $C = \sum_{n=0}^{N-1} \abs{s_n - s}$.
11. Split the series of step 9 into the terms with $n < N$ and the tail with $n \ge N$. Since $x^n \le 1$, the first part has absolute value at most $C$.
12. The tail has terms of absolute value at most $(\varepsilon/2) x^n$. By the [[bound for absolutely convergent series|0Y123X48GA]] and the comparison test, its absolute value is at most $(\varepsilon/2) \sum_{n \ge N} x^n$.
13. The geometric series gives $(1 - x) \sum_{n \ge N} x^n = x^N \le 1$. With steps 9, 11 and 12, $\abs{G(x) - s} \le (1 - x) C + \varepsilon/2$.
14. Let $\delta = \min(1, \varepsilon / (2C + 1))$. If $1 - \delta < x < 1$, then $0 \le x < 1$, and $(1 - x) C \le \delta C \le C \varepsilon / (2C + 1) < \varepsilon / 2$.
15. So $\abs{G(x) - s} < \varepsilon$ for all $x$ with $1 - \delta < x < 1$. By the definition of the [[left limit|0909PWZR62]], $G(x) \to s = \sum_{n=0}^{\infty} a_n$ as $x \to 1$ from the left.

## Idea

Summation by parts writes $G(x) - s$ as $(1 - x) \sum (s_n - s) x^n$. The factor $1 - x$ kills the finitely many early terms as $x \to 1$. The later terms have small coefficients $s_n - s$, and $(1 - x) \sum x^n \le 1$ keeps their total small.
