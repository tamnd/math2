---
tag: 11BXZD1EVQ
kind: proof
name: Proof of the Peano existence theorem by Euler polygons
msc: [34A12]
proves: 098YP831QY
uses: [075VBY4K4X, 0PHT6NBYPB, 0K9AAJ8G51, 06B8BNJCD6, 0MW2WXTHMC, 0381S8Z5P0, 0K8SGQSV7G, 08FPABDQ4C, 0NR82KMYKD, 0MBWQKM8QR, 080RWVVSB6, 063H5KJC69]
sources:
  - url: https://www.mat.univie.ac.at/~gerald/ftp/book-ode/ode.pdf
    locator: Section 2.7
  - url: https://en.wikipedia.org/wiki/Peano_existence_theorem
    locator: Proof
---

## Proof

We build Euler polygons, extract a uniformly convergent subsequence with the Arzelà–Ascoli theorem, and show that the limit solves the integral equation.

1. On $\mathbb{R}^n$ we use the norm $\abs{x} = \max_i \abs{x_i}$, and on $\mathbb{R} \times \mathbb{R}^n$ the norm $\max(\abs{t}, \abs{x})$. Integrals of vector functions are taken coordinatewise. For continuous $v$ on $[c, d]$, the [[triangle inequality for integrals|0NR82KMYKD]] and [[monotonicity of the integral|0MBWQKM8QR]] in each coordinate give $\abs{\int_c^d v} \le \int_c^d \abs{v}$.
2. Since $D$ is open, there are $a, b > 0$ such that $R = [t_0 - a, t_0 + a] \times \set{x : \abs{x - x_0} \le b}$ lies in $D$.
3. The set $R$ is closed and bounded, so it is compact by the [[Heine–Borel theorem|0PHT6NBYPB]]. Its image under the continuous map $\abs{f}$ is [[compact|0K9AAJ8G51]], hence bounded. Choose $M > 0$ with $\abs{f(p)} \le M$ for all $p \in R$.
4. By the [[Heine–Cantor theorem|06B8BNJCD6]], $f$ is uniformly continuous on $R$.
5. Let $h = \min(a, b/M)$ and $X = [t_0 - h, t_0 + h]$. For an integer $N \ge 1$, let $t_k = t_0 + k h / N$ for $k = -N, \dots, N$.
6. Define $x_N : X \to \mathbb{R}^n$ by $x_N(t_0) = x_0$ and, step by step outward from $t_0$, $x_N(t) = x_N(t_k) + (t - t_k)\, f(t_k, x_N(t_k))$. For $k \ge 0$ this is used for $t \in [t_k, t_{k+1}]$, and for $k \le 0$ for $t \in [t_{k-1}, t_k]$.
7. We show by induction on $\abs{k}$ that this is well defined and that $\abs{x_N(t) - x_0} \le M \abs{t - t_0}$. Assume the bound holds at $t_k$. Then $\abs{x_N(t_k) - x_0} \le M h \le b$ and $\abs{t_k - t_0} \le a$, so $(t_k, x_N(t_k)) \in R$.
8. So $f(t_k, x_N(t_k))$ is defined and has norm at most $M$. On the next piece, $\abs{x_N(t) - x_0} \le M \abs{t_k - t_0} + M \abs{t - t_k} = M \abs{t - t_0}$, since $t_k$ lies between $t_0$ and $t$. This completes the induction.
9. Each $x_N$ is continuous and piecewise linear, with slopes of norm at most $M$. Splitting $[t', t]$ at the nodes and using the triangle inequality gives $\abs{x_N(t) - x_N(t')} \le M \abs{t - t'}$ for all $t, t' \in X$.
10. By steps 8 and 9, each coordinate family $\set{x_{N, i} : N \ge 1}$ is bounded by $\abs{x_0} + b$. It is [[equicontinuous|0MW2WXTHMC]], with $\delta = \varepsilon / M$ for each $\varepsilon > 0$.
11. By the [[Arzelà–Ascoli theorem|0381S8Z5P0]], the closure of the family of first coordinates is compact in $C(X)$. By [[sequential compactness|0K8SGQSV7G]], some subsequence of $(x_{N,1})$ converges in $C(X)$, that is [[uniformly|08FPABDQ4C]].
12. Repeating step 11 for coordinates $2, \dots, n$, each time inside the previous subsequence, gives $N_1 < N_2 < \cdots$ and a continuous $z : X \to \mathbb{R}^n$ with $\sup_{t \in X} \abs{x_{N_j}(t) - z(t)} \to 0$.
13. Letting $j \to \infty$ in step 8 gives $\abs{z(t) - x_0} \le M \abs{t - t_0} \le b$. So $(t, z(t)) \in R \subseteq D$ for $t \in X$, and $z(t_0) = x_0$.
14. Let $\varepsilon > 0$. By step 4, choose $\eta > 0$ with $\abs{f(p) - f(q)} < \varepsilon$ for $p, q \in R$ with distance less than $\eta$.
15. Let $e_N(t) = x_N(t) - x_0 - \int_{t_0}^t f(s, x_N(s))\, ds$ for $t \in X$. The integrand is continuous, since $x_N$ is continuous.
16. Let $t \ge t_0$ lie in $[t_k, t_{k+1}]$. By step 6, $x_N(t) - x_0$ is the sum of the integrals of the constants $f(t_j, x_N(t_j))$ over the pieces $[t_j, t_{j+1}]$ for $j < k$ and over $[t_k, t]$.
17. So, by [[linearity of the integral|080RWVVSB6]], $e_N(t)$ is the sum over these pieces of the integrals of $f(t_j, x_N(t_j)) - f(s, x_N(s))$, with $s$ in the piece of $t_j$.
18. For $s$ in that piece, $\abs{s - t_j} \le h / N$ and, by step 9, $\abs{x_N(s) - x_N(t_j)} \le M h / N$. If $N$ is so large that $h/N < \eta$ and $Mh/N < \eta$, each integrand has norm less than $\varepsilon$.
19. By step 1 the pieces of total length $t - t_0$ then give $\abs{e_N(t)} \le \varepsilon h$. The case $t \le t_0$ is the same. So $\sup_X \abs{e_N} \to 0$ as $N \to \infty$.
20. For large $j$, $\abs{x_{N_j}(s) - z(s)} < \eta$ for all $s \in X$, so $\abs{f(s, x_{N_j}(s)) - f(s, z(s))} < \varepsilon$. By step 1, $\abs{\int_{t_0}^t \left( f(s, x_{N_j}(s)) - f(s, z(s)) \right) ds} \le \varepsilon h$ for all $t \in X$.
21. For $t \in X$, $z(t) - x_0 - \int_{t_0}^t f(s, z(s))\, ds$ equals $\left( z(t) - x_{N_j}(t) \right) + e_{N_j}(t) + \int_{t_0}^t \left( f(s, x_{N_j}(s)) - f(s, z(s)) \right) ds$.
22. By steps 12, 19 and 20, all three terms tend to $0$ as $j \to \infty$. Hence $z(t) = x_0 + \int_{t_0}^t f(s, z(s))\, ds$ for each $t \in X$.
23. The map $s \mapsto f(s, z(s))$ is continuous on $X$. Write $\int_{t_0}^t = \int_{t_0 - h}^t - \int_{t_0 - h}^{t_0}$. By the [[first fundamental theorem of calculus|063H5KJC69]] in each coordinate, $z$ is differentiable at each $t \in (t_0 - h, t_0 + h)$ with $z'(t) = f(t, z(t))$.
24. Let $I = (t_0 - h, t_0 + h)$, an open interval that contains $t_0$. By steps 13 and 23, $z$ restricted to $I$ solves the [[initial value problem|075VBY4K4X]]: $(t, z(t)) \in D$ and $z'(t) = f(t, z(t))$ for $t \in I$, and $z(t_0) = x_0$.

## Idea

Euler polygons follow the field $f$ in small straight steps, so they almost solve the equation. Their slopes are bounded by $M$, which makes the family equicontinuous, and the Arzelà–Ascoli theorem gives a uniformly convergent subsequence. Uniform continuity of $f$ on a compact box then shows that the limit solves the integral equation exactly.
