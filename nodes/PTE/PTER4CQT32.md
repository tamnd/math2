---
tag: PTER4CQT32
kind: proof
name: Proof of Dini's theorem by compactness
msc: [40A30]
proves: 0XRRYF1HPE
uses: [056FSKG32J, 08FPABDQ4C, 0N32V0E3XJ, 0VGMHCF4SC, 0W8YHHGCJG, 01ZQQDCERP, 0NVPNC12JY, 00R0X1WGPX, 07PFYV65MB]
sources:
  - url: https://proofwiki.org/wiki/Dini%27s_Theorem
    locator: Proof
---

## Proof

We cover $[a, b]$ by open sets on which the error is small, and use compactness to pick one index.

1. Let $a < b$, and let $f_n$ and $f$ be as in the statement. For each $n$, let $g_n = f - f_n$.
2. Fix $x \in [a, b]$ and $n$. For $m \ge n$, we have $f_n(x) \le f_m(x)$. Letting $m \to \infty$ gives $f_n(x) \le f(x)$, since [[limits preserve non-strict inequalities|0N32V0E3XJ]]. So $g_n(x) \ge 0$.
3. Since $f_n(x) \le f_{n+1}(x)$, we get $g_n(x) \ge g_{n+1}(x)$ for all $n$ and $x$.
4. Since $f_n \to f$ [[pointwise|056FSKG32J]], $g_n(x) \to 0$ for each $x \in [a, b]$.
5. Each $g_n = f + (-1) \cdot f_n$ is continuous on $[a, b]$, since [[sums and products of continuous functions are continuous|0VGMHCF4SC]] and constants are continuous.
6. Fix $\varepsilon > 0$. For each $n$, let $U_n$ be the union of all open intervals $V$ such that $g_n(x) < \varepsilon$ for every $x \in V \cap [a, b]$.
7. Each $U_n$ is a union of open intervals, so it is an [[open set|01ZQQDCERP]] of $\R$. By its definition, $g_n(x) < \varepsilon$ for each $x \in U_n \cap [a, b]$.
8. Let $x \in [a, b]$ with $g_n(x) < \varepsilon$. By step 5 and the [[epsilon-delta form of continuity|0W8YHHGCJG]] with tolerance $\varepsilon - g_n(x) > 0$, there is $\delta > 0$ with $g_n(t) < \varepsilon$ for all $t \in [a, b]$ with $|t - x| < \delta$. So $(x - \delta, x + \delta)$ is one of the intervals in step 6, and $x \in U_n$.
9. Let $x \in [a, b]$. By step 4, there is $n$ with $g_n(x) < \varepsilon$. By step 8, $x \in U_n$. So the family $(U_n)_{n \ge 1}$ is an [[open cover|0NVPNC12JY]] of $[a, b]$.
10. The interval $[a, b]$ is closed and bounded. By the [[Heine–Borel theorem|07PFYV65MB]], it is [[compact|00R0X1WGPX]].
11. By step 10, finitely many of the sets cover $[a, b]$, say $U_{n_1}, \dots, U_{n_k}$. Let $N = \max(n_1, \dots, n_k)$.
12. Let $x \in [a, b]$. Then $x \in U_{n_i}$ for some $i$, so $g_{n_i}(x) < \varepsilon$ by step 7.
13. Let $n \ge N$. Since $n \ge N \ge n_i$, steps 2 and 3 give $0 \le g_n(x) \le g_{n_i}(x) < \varepsilon$.
14. So $|f_n(x) - f(x)| = g_n(x) < \varepsilon$ for all $n \ge N$ and all $x \in [a, b]$. As $\varepsilon > 0$ was arbitrary, $f_n \to f$ [[uniformly|08FPABDQ4C]] on $[a, b]$.

## Idea

The set where $f - f_n < \varepsilon$ is open, by continuity, and it grows with $n$, by monotonicity. Pointwise convergence makes these sets cover $[a, b]$. Compactness reduces the cover to finitely many sets, and the largest of them is already all of $[a, b]$.
