---
tag: 8ZRGJ9W5QN
kind: proof
name: Proof that continuous functions on a closed bounded interval are uniformly continuous
msc: [26A15]
proves: 0W0TZDRF9C
uses: [0A3CK6DVVB, 0P27W9RW0G, 0W8YHHGCJG, 0KDJD249DT, 0R8J3ZQMJS, 0N32V0E3XJ, 09G6KHS6GY, 0WH916TJNY, 03HF5PMY5T]
sources:
  - url: https://www.jirka.org/ra/html/sec_unifcont.html
    locator: Theorem 3.4.4
---

## Proof

We argue by contradiction.

1. Suppose that $f$ is not [[uniformly continuous|0A3CK6DVVB]] on $[a, b]$. Then there is $\varepsilon > 0$ with the following property. For each $\delta > 0$ there are $x, y \in [a, b]$ with $\abs{x - y} < \delta$ and $\abs{f(x) - f(y)} \ge \varepsilon$.
2. For each $n \in \N$, apply step 1 with $\delta = \frac{1}{n+1}$. This gives $x_n, y_n \in [a, b]$ with $\abs{x_n - y_n} < \frac{1}{n+1}$ and $\abs{f(x_n) - f(y_n)} \ge \varepsilon$.
3. The sequence $(x_n)$ lies in $[a, b]$, so it is bounded. By the [[Bolzano–Weierstrass theorem|0KDJD249DT]], a [[subsequence|0R8J3ZQMJS]] $(x_{n_k})$ converges to some real $c$.
4. Since $a \le x_{n_k} \le b$ for all $k$, [[limits preserve non-strict inequalities|0N32V0E3XJ]] gives $a \le c \le b$.
5. The indices satisfy $n_0 < n_1 < \cdots$, so induction gives $n_k \ge k$. Hence $\abs{x_{n_k} - y_{n_k}} < \frac{1}{n_k+1} \le \frac{1}{k+1}$.
6. The function $f$ is [[continuous|0P27W9RW0G]] at $c$. By the [[epsilon-delta form of continuity|0W8YHHGCJG]], there is $\delta > 0$ with $\abs{f(x) - f(c)} < \frac{\varepsilon}{2}$ for all $x \in [a, b]$ with $\abs{x - c} < \delta$.
7. By the [[epsilon-N form of limits|09G6KHS6GY]], there is $K_1$ with $\abs{x_{n_k} - c} < \frac{\delta}{2}$ for all $k \ge K_1$. By [[this lemma|0WH916TJNY]], there is $K_2 \ge 1$ with $\frac{1}{K_2} < \frac{\delta}{2}$.
8. Let $k = \max(K_1, K_2)$. Step 5 gives $\abs{x_{n_k} - y_{n_k}} < \frac{1}{k+1} < \frac{1}{K_2} < \frac{\delta}{2}$. By the [[triangle inequality|03HF5PMY5T]] and steps 5 and 7, $\abs{y_{n_k} - c} \le \abs{y_{n_k} - x_{n_k}} + \abs{x_{n_k} - c} < \frac{\delta}{2} + \frac{\delta}{2} = \delta$.
9. Also $\abs{x_{n_k} - c} < \delta$. So step 6 gives $\abs{f(x_{n_k}) - f(c)} < \frac{\varepsilon}{2}$ and $\abs{f(y_{n_k}) - f(c)} < \frac{\varepsilon}{2}$.
10. By the triangle inequality, $\abs{f(x_{n_k}) - f(y_{n_k})} < \varepsilon$. This contradicts step 2.
11. So the assumption of step 1 is false, and $f$ is uniformly continuous on $[a, b]$.

## Idea

If uniform continuity fails, there are pairs of points closer and closer together whose values stay $\varepsilon$ apart. The Bolzano–Weierstrass theorem makes both points of these pairs converge to one point $c$ of the interval. Continuity at $c$ then forces the values together, which is a contradiction.
