---
tag: RRBCGTD2SB
kind: proof
name: Proof of continuous dependence on initial data by Grönwall's inequality
msc: [34A12]
proves: 0G3DBXRRQJ
uses: [04SW7WECS8, 055VVSN00V, 0XYAFCN0PT, 080RWVVSB6, 0RFWW56Y22, 0MBWQKM8QR, 0FJZMBX0ZZ, 07EJHQYR9A]
sources:
  - url: https://en.wikipedia.org/wiki/Gr%C3%B6nwall%27s_inequality
    locator: Integral form for continuous functions
---

## Proof

We write the solutions as integrals and apply the integral form of Grönwall's inequality. Here $\|\cdot\|$ is the Euclidean norm on $\mathbb{R}^n$.

1. As [[solutions|04SW7WECS8]] on $[a, b]$, the curves $\gamma_1, \gamma_2$ are differentiable, hence continuous, on $[a, b]$. For $t \in (a, b)$ they satisfy $\gamma_i'(t) = f(t, \gamma_i(t))$. Only these facts are used.
2. For $i = 1, 2$ let $g_i(s) = f(s, \gamma_i(s))$ for $s \in [a, b]$. As a composition of continuous maps, $g_i$ is continuous on $[a, b]$.
3. Fix $t \in (a, b]$. Apply the [[second fundamental theorem of calculus|0XYAFCN0PT]] to each coordinate of $\gamma_i$ on $[a, t]$. The derivative extends to the continuous function $g_i$, so $\gamma_i(t) = \gamma_i(a) + \int_a^t g_i(s)\, ds$, with coordinatewise integrals.
4. Let $e(t) = \gamma_1(t) - \gamma_2(t)$. By step 3 and [[linearity of the integral|080RWVVSB6]], $e(t) = e(a) + \int_a^t \left( g_1(s) - g_2(s) \right) ds$.
5. Let $v : [a, t] \to \mathbb{R}^n$ be continuous and let $w = \int_a^t v(s)\, ds$. We show $\|w\| \le \int_a^t \|v(s)\|\, ds$.
6. By linearity, $\|w\|^2 = \sum_{j} w_j \int_a^t v_j(s)\, ds = \int_a^t w \cdot v(s)\, ds$.
7. By the [[Cauchy–Schwarz inequality|0RFWW56Y22]], $w \cdot v(s) \le \|w\|\, \|v(s)\|$. By [[monotonicity of the integral|0MBWQKM8QR]], $\|w\|^2 \le \|w\| \int_a^t \|v(s)\|\, ds$.
8. If $w = 0$, then $\|w\| = 0$, and the integral of the non-negative function $\|v\|$ is non-negative. Otherwise divide by $\|w\| > 0$.
9. By the [[Lipschitz condition|055VVSN00V]] in the hypothesis, $\|g_1(s) - g_2(s)\| \le K \|e(s)\|$ for $s \in [a, b]$.
10. Let $u(s) = \|e(s)\|$, a continuous function on $[a, b]$. By step 4, the [[triangle inequality|0FJZMBX0ZZ]], step 5 and step 9, $u(t) \le u(a) + \int_a^t K\, u(s)\, ds$.
11. This also holds for $t = a$, where the integral is $0$. So it holds for each $t \in [a, b]$.
12. Apply the integral form of [[Grönwall's inequality|07EJHQYR9A]] on $I = [a, b]$ with $\beta = K \ge 0$ and the constant, hence non-decreasing, function $\alpha = u(a)$.
13. It gives $u(t) \le u(a) \exp\left( \int_a^t K\, ds \right) = u(a)\, e^{K(t - a)}$. This is $\|\gamma_1(t) - \gamma_2(t)\| \le \|\gamma_1(a) - \gamma_2(a)\|\, e^{K(t - a)}$ for each $t \in [a, b]$.

## Idea

The difference of two solutions changes at a rate bounded by $K$ times its own size, because of the Lipschitz condition. In integral form this is exactly the hypothesis of Grönwall's inequality, which bounds the size by exponential growth with rate $K$.
