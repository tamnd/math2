---
tag: CW8S9TN77Q
kind: proof
name: Proof that uniform convergence of derivatives allows term-by-term differentiation
msc: [40A30, 26A24]
proves: 0CS42KEM5C
uses: [08FPABDQ4C, 01XAY17QA3, 0F1WR9C83K, 0HXEX0DPRA, 0GBZDAFPX8, 0W8YHHGCJG, 0BARQY52N5, 0M0TKFRX2A, 0QY87R9CY3, 0ZA4AX4MW3, 0N32V0E3XJ, 03HF5PMY5T]
sources:
  - url: https://dec41.user.srcf.net/notes/IB_M/analysis_ii_thm_proof.pdf
    locator: Section 1, Uniform convergence
---

## Proof

We use the mean value theorem twice: once to show that $(f_n)$ is uniformly Cauchy, and once to control difference quotients uniformly. No continuity of the derivatives is needed.

*Setup.*

1. Let $a < b$. At an interior point, $f_n'$ is the [[derivative|0F1WR9C83K]]. At $a$ and $b$, it is the [[one-sided derivative|0HXEX0DPRA]]. So for each $y \in [a, b]$, $f_n'(y)$ is the limit of $\frac{f_n(t) - f_n(y)}{t - y}$ as $t \to y$ with $t \in [a, b]$, $t \ne y$.
2. Each $f_n$ is continuous on $[a, b]$. Indeed, fix $y$ and put $K = |f_n'(y)| + 1$. By the limit in step 1 with tolerance $1$, there is $\delta_0 > 0$ such that the quotient has absolute value at most $K$ when $0 < |t - y| < \delta_0$. So $|f_n(t) - f_n(y)| \le K |t - y|$ for these $t$. Given $\varepsilon > 0$, this is less than $\varepsilon$ when $|t - y| < \min(\delta_0, \varepsilon / K)$. By the [[epsilon-delta form|0W8YHHGCJG]], $f_n$ is continuous at $y$.
3. Let $n, m \ge 1$, put $h = f_n - f_m$, and let $s \ne t$ in $[a, b]$. By step 2, $h$ is continuous on the closed interval between $s$ and $t$. By [[linearity of differentiation|0M0TKFRX2A]], $h$ is differentiable inside it with $h' = f_n' - f_m'$.
4. By the [[mean value theorem|0BARQY52N5]], there is $\xi$ strictly between $s$ and $t$ with $h(t) - h(s) = (f_n'(\xi) - f_m'(\xi))(t - s)$.
5. Let $\eta > 0$. Since $f_n' \to g$ [[uniformly|08FPABDQ4C]], there is $N(\eta)$ with $|f_n'(x) - g(x)| < \frac{\eta}{2}$ for all $n \ge N(\eta)$ and all $x \in [a, b]$.
6. By step 5 and the [[triangle inequality|03HF5PMY5T]], $|f_n'(x) - f_m'(x)| < \eta$ for all $n, m \ge N(\eta)$ and all $x \in [a, b]$.

*The sequence $(f_n)$ converges uniformly.*

7. Let $\varepsilon > 0$. The sequence $(f_n(x_0))$ converges, so it is Cauchy, since [[convergent sequences are Cauchy|0QY87R9CY3]].
8. By steps 6 and 7, there is $N$ such that for all $n, m \ge N$, we have $|f_n(x_0) - f_m(x_0)| < \frac{\varepsilon}{2}$ and $|f_n' - f_m'| < \frac{\varepsilon}{2(b - a)}$ on $[a, b]$.
9. Let $n, m \ge N$, $h = f_n - f_m$, and $x \in [a, b]$. By step 4 with $s = x_0$ and $t = x$ (if $x \ne x_0$), and step 8,
$$|h(x)| \le |h(x) - h(x_0)| + |h(x_0)| < \frac{\varepsilon}{2(b - a)} |x - x_0| + \frac{\varepsilon}{2} \le \varepsilon.$$
10. So $(f_n)$ is [[uniformly Cauchy|01XAY17QA3]] on $[a, b]$.
11. For each $x$, the sequence $(f_n(x))$ is Cauchy by step 9. By the [[Cauchy criterion|0ZA4AX4MW3]], it converges. Let $f(x)$ be its limit.
12. Fix $n \ge N$ and $x$. Letting $m \to \infty$ in $|f_n(x) - f_m(x)| < \varepsilon$ gives $|f_n(x) - f(x)| \le \varepsilon$, since [[limits preserve non-strict inequalities|0N32V0E3XJ]].
13. Since $\varepsilon$ was arbitrary and $N$ does not depend on $x$, step 12 shows that $f_n \to f$ uniformly on $[a, b]$.

*The limit $f$ is differentiable with $f' = g$.*

14. Fix $y \in [a, b]$. For $t \in [a, b]$ with $t \ne y$, let $\varphi_n(t) = \frac{f_n(t) - f_n(y)}{t - y}$ and $\varphi(t) = \frac{f(t) - f(y)}{t - y}$. By step 11, $\varphi_n(t) \to \varphi(t)$ for each such $t$.
15. Let $\eta > 0$ and $n, m \ge N(\eta)$. By step 4 with $s = y$, and step 6, $|\varphi_n(t) - \varphi_m(t)| = |f_n'(\xi) - f_m'(\xi)| < \eta$ for each $t \ne y$.
16. Letting $m \to \infty$ in step 15 gives $|\varphi_n(t) - \varphi(t)| \le \eta$ for all $n \ge N(\eta)$ and all $t \ne y$, again since limits preserve non-strict inequalities.
17. Let $\varepsilon > 0$, put $\eta = \frac{\varepsilon}{3}$, and fix $n = N(\eta)$. By step 5, $|f_n'(y) - g(y)| < \eta$.
18. By step 1 and the [[epsilon-delta form of a limit|0GBZDAFPX8]], there is $\delta > 0$ with $|\varphi_n(t) - f_n'(y)| < \eta$ for all $t \in [a, b]$ with $0 < |t - y| < \delta$.
19. For such $t$, steps 16 to 18 and the triangle inequality give
$$|\varphi(t) - g(y)| \le |\varphi(t) - \varphi_n(t)| + |\varphi_n(t) - f_n'(y)| + |f_n'(y) - g(y)| < 3\eta = \varepsilon.$$
20. So $\varphi(t) \to g(y)$ as $t \to y$ within $[a, b]$. This means that $f$ is differentiable at $y$, one-sided if $y$ is an endpoint, with $f'(y) = g(y)$.
21. Since $y$ was arbitrary, $f_n \to f$ uniformly on $[a, b]$, $f$ is differentiable, and $f' = g$.

## Idea

The mean value theorem turns a uniform bound on $f_n' - f_m'$ into a bound on the differences of $f_n - f_m$, both between two points and in difference quotients. Convergence at one point $x_0$ anchors the functions, so they converge uniformly. The difference quotients converge uniformly too, which lets us swap the limit in $n$ with the limit $t \to y$.
