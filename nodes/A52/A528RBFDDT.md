---
tag: A528RBFDDT
kind: proof
name: Proof of the extreme value theorem by the Bolzano–Weierstrass theorem
msc: [26A15]
proves: 0WS1A8E2P9
uses: [0ATVXC3NCC, 0AXWET80YW, 0BTMQ04556, 0KDJD249DT, 0R8J3ZQMJS, 0N32V0E3XJ, 0PAQM3H57X, 0XMF00T4XQ, 0RAM4E07NR, 0WH916TJNY, 09G6KHS6GY, 0ZXJ2455NJ, 0W8YHHGCJG, 0P27W9RW0G]
sources:
  - url: https://en.wikipedia.org/wiki/Extreme_value_theorem
---

## Proof

We first find a point $d$ where $f$ is largest, then apply this to $-f$.

1. Let $S = f([a, b]) = \set{f(x) : a \le x \le b}$. It is nonempty, since $a \in [a, b]$.
2. By the [[boundedness theorem|0ATVXC3NCC]], $S$ is bounded above. By the [[completeness axiom|0AXWET80YW]], $S$ has a [[supremum|0BTMQ04556]] $M$.
3. Let $n \in \N$. The number $M - \frac{1}{n+1}$ is less than $M$, so it is not an upper bound of $S$. Choose $d_n \in [a, b]$ with $f(d_n) > M - \frac{1}{n+1}$.
4. The sequence $(d_n)$ satisfies $a \le d_n \le b$, so it is bounded. By the [[Bolzano–Weierstrass theorem|0KDJD249DT]], it has a [[subsequence|0R8J3ZQMJS]] $(d_{n_k})$ converging to some real $d$.
5. Apply [[limits preserve non-strict inequalities|0N32V0E3XJ]] to $a \le d_{n_k}$ and $d_{n_k} \le b$, with constant sequences $a$ and $b$. This gives $a \le d \le b$.
6. The function $f$ is [[continuous|0P27W9RW0G]] on $[a, b]$. By [[continuity is equivalent to sequential continuity|0PAQM3H57X]], $f(d_{n_k}) \to f(d)$.
7. Since $n_0 < n_1 < \cdots$ are natural numbers, induction gives $n_k \ge k$. So $M - \frac{1}{k+1} \le M - \frac{1}{n_k+1} < f(d_{n_k}) \le M$ for all $k$.
8. Let $\varepsilon > 0$. By [[this lemma|0WH916TJNY]], there is $N \ge 1$ with $\frac{1}{N} < \varepsilon$. For $k \ge N$ we get $0 < \frac{1}{k+1} < \varepsilon$. So $\frac{1}{k+1} \to 0$ and $-\frac{1}{k+1} \to 0$ by the [[epsilon-N form of limits|09G6KHS6GY]].
9. By the [[limit of a sum of sequences|0RAM4E07NR]], $M - \frac{1}{k+1} \to M$. By step 7 and the [[squeeze theorem|0XMF00T4XQ]], $f(d_{n_k}) \to M$.
10. By [[uniqueness of limits|0ZXJ2455NJ]], steps 6 and 9 give $f(d) = M$. Since $M$ is an upper bound of $S$, $f(x) \le f(d)$ for all $x \in [a, b]$.
11. Now let $g = -f$ on $[a, b]$. For all $x, y$ we have $\abs{g(x) - g(y)} = \abs{f(x) - f(y)}$. So the [[epsilon-delta form of continuity|0W8YHHGCJG]] shows that $g$ is continuous.
12. Steps 1 to 10 applied to $g$ give $c \in [a, b]$ with $-f(x) \le -f(c)$ for all $x \in [a, b]$. That is, $f(c) \le f(x)$.
13. Together, $f(c) \le f(x) \le f(d)$ for all $x \in [a, b]$, with $c, d \in [a, b]$.

## Idea

Pick points where $f$ comes within $\frac{1}{n+1}$ of its supremum. The Bolzano–Weierstrass theorem gives a convergent subsequence of these points, and its limit stays in the closed interval. Continuity carries the values to the limit point, so the supremum is attained there.
