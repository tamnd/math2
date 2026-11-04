---
tag: 6TNJQKXA3G
kind: proof
name: Proof of the Heine–Borel theorem by sequential compactness
msc: ["54E45"]
proves: 07PFYV65MB
uses: [0E1MMCAY5B, 00R0X1WGPX, 0G5AV9Q4RR, 0P953MG05E, 0R7BTEWCJ2, 0P9DCDES73, 0MYFJVMN7M, 0CARW59WD2, 0K8SGQSV7G, 0KDJD249DT, 05FQ3VGAR9, 0R8J3ZQMJS, 0VHAVXW08V, 09GQ3ZTQJ9, 06JYPJ4WHH]
sources:
  - url: https://en.wikipedia.org/wiki/Bolzano%E2%80%93Weierstrass_theorem
    locator: Sequential compactness in Euclidean spaces
  - url: https://proofwiki.org/wiki/Heine-Borel_Theorem/Euclidean_Space
---

## Proof

The direct part uses general facts on metric spaces. For the converse, we show that $K$ is sequentially compact, coordinate by coordinate.

1. Let $n \ge 1$, and let $d_2$ be the [[Euclidean metric|0E1MMCAY5B]] on $\R^n$. Let $K \subseteq \R^n$.
2. Assume $K$ is [[compact|00R0X1WGPX]]. Since [[compact subsets of a metric space are bounded|0R7BTEWCJ2]], $K$ is [[bounded|0P953MG05E]].
3. [[Metric spaces are Hausdorff|0P9DCDES73]], and [[compact subsets of a Hausdorff space are closed|0MYFJVMN7M]]. So $K$ is [[closed|0G5AV9Q4RR]].
4. Now assume $K$ is closed and bounded. If $K = \emptyset$, it is compact. So assume $K \ne \emptyset$, fix $a \in K$, and let $M$ be real with $d_2(x, y) \le M$ for $x, y \in K$.
5. For $x \in K$ and each coordinate $i$, $\abs{x_i - a_i} \le d_2(x, a) \le M$, since one term of a sum of squares is at most the sum. So $\abs{x_i} \le \abs{a_i} + M$.
6. Let $(p^{(m)})_{m \ge 1}$ be a sequence in $K$. By step 5, each coordinate sequence $(p^{(m)}_i)_m$ is a [[bounded real sequence|05FQ3VGAR9]], also along any subsequence.
7. By the [[Bolzano–Weierstrass theorem|0KDJD249DT]], the first coordinates have a convergent [[subsequence|0R8J3ZQMJS]]. Pass to it.
8. Repeat for coordinates $2, \ldots, n$: at step $j$, apply Bolzano–Weierstrass to the $j$-th coordinates along the current subsequence, and pass to a further subsequence.
9. A subsequence of a subsequence is a subsequence. [[Subsequences of a convergent sequence converge to the same limit|0VHAVXW08V]], so coordinates that converged earlier still converge.
10. After $n$ steps we get indices $m_1 < m_2 < \cdots$ and reals $c_1, \ldots, c_n$ with $p^{(m_k)}_i \to c_i$ for each $i$. Let $c = (c_1, \ldots, c_n)$.
11. For reals $t_1, \ldots, t_n$, expanding the square gives $(\sum_i \abs{t_i})^2 \ge \sum_i t_i^2$, since the cross terms are $\ge 0$. So $\sqrt{\sum_i t_i^2} \le \sum_i \abs{t_i}$.
12. By step 11, $d_2(p^{(m_k)}, c) \le \sum_{i=1}^n \abs{p^{(m_k)}_i - c_i}$.
13. Let $\varepsilon > 0$. For each $i$, there is $L_i$ with $\abs{p^{(m_k)}_i - c_i} < \varepsilon / n$ for $k \ge L_i$. For $k \ge \max_i L_i$, step 12 gives $d_2(p^{(m_k)}, c) < \varepsilon$.
14. So $p^{(m_k)} \to c$ in $(\R^n, d_2)$, in the sense of [[convergence|06JYPJ4WHH]].
15. All $p^{(m_k)}$ lie in $K$, and $K$ is closed. Since [[closed sets contain their limits|09GQ3ZTQJ9]], $c \in K$.
16. So every sequence in $K$ has a subsequence that converges to a point of $K$. Thus $K$ is [[sequentially compact|0CARW59WD2]].
17. Since [[compactness and sequential compactness agree in metric spaces|0K8SGQSV7G]], $K$ is compact.

## Idea

Compact sets in any metric space are closed and bounded, so the work is in the converse.
A bounded sequence in $\R^n$ has bounded coordinates. Bolzano–Weierstrass, applied once per coordinate, gives a convergent subsequence, and closedness keeps its limit in $K$.
