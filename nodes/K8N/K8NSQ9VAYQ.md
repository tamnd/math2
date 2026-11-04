---
tag: K8NSQ9VAYQ
kind: proof
name: Proof of the volume of a ball in R^n by slicing
msc: ["28A75"]
proves: 00YH28R457
uses: [2Z2QVWZ262, 067SYD2J4B, XVEWR93EMV, 0V3FZMVB4K, 0FDCW77H44, 0DFT1GP1JP, 0D37QFPEZE, 08Y1BBQTK9, 0XPR1E85W0]
sources:
  - url: https://en.wikipedia.org/wiki/Volume_of_an_n-ball
    locator: The one-dimension recursion formula
---

## Proof

We argue by induction on $n$, slicing the ball by hyperplanes.

1. Here $\operatorname{vol}$ is [[Lebesgue measure|2Z2QVWZ262]] $\lambda^n$ on [[Euclidean space|0XPR1E85W0]] $\R^n$. For $\rho \ge 0$ let $B_n(\rho) = \set{x \in \R^n : \norm{x} \le \rho}$ and $V_n(\rho) = \lambda^n(B_n(\rho))$. Each $B_n(\rho)$ is closed, so it is a Borel set and Lebesgue measurable.
2. Let $c_n = \pi^{n/2} / \Gamma(n/2 + 1)$, with $\Gamma$ the [[gamma function|0V3FZMVB4K]]. We prove by induction on $n \ge 1$ the claim $P(n)$: $V_n(\rho) = c_n \rho^n$ for every $\rho \ge 0$. This contains the statement.
3. First, $\Gamma(1/2) = \sqrt{\pi}$. For $0 < \varepsilon < M$, [[substitution|0D37QFPEZE]] with $t = u^2$, $dt = 2u \, du$ gives $\int_\varepsilon^M t^{-1/2} e^{-t} \, dt = 2 \int_{\sqrt{\varepsilon}}^{\sqrt{M}} e^{-u^2} \, du$.
4. Let $\varepsilon \to 0$ and $M \to \infty$. Since $e^{-u^2}$ is even, the [[Gaussian integral|0DFT1GP1JP]] gives $\Gamma(1/2) = 2 \int_0^\infty e^{-u^2} \, du = \int_{-\infty}^{\infty} e^{-u^2} \, du = \sqrt{\pi}$.
5. By the [[functional equation|0FDCW77H44]] $\Gamma(s + 1) = s \, \Gamma(s)$, we get $\Gamma(3/2) = \sqrt{\pi}/2$, and $\Gamma(1) = 0! = 1$.
6. The case $\rho = 0$ holds for every $n$. Indeed $B_n(0) = \set{0}$ is the box $[0, 0]^n$ of volume $0$, so $\lambda^n(B_n(0)) = 0 = c_n \cdot 0^n$.
7. Base case $n = 1$, $\rho > 0$. Here $B_1(\rho) = [-\rho, \rho]$. On a bounded interval the [[Lebesgue integral|XVEWR93EMV]] of a Riemann integrable function equals its Riemann integral. So $V_1(\rho) = \int_{-\rho}^{\rho} 1 \, dx = 2\rho$.
8. By step 5, $c_1 = \sqrt{\pi} / \Gamma(3/2) = 2$. So $P(1)$ holds.
9. For an integer $m \ge 0$ let $J_m = \int_{-1}^{1} (1 - u^2)^{m/2} \, du$. We claim that $J_m = \sqrt{\pi} \, \Gamma(m/2 + 1) / \Gamma(m/2 + 3/2)$.
10. For $m = 0$: $J_0 = 2$, and the right side is $\sqrt{\pi} \, \Gamma(1) / \Gamma(3/2) = 2$ by step 5.
11. For $m = 1$: substitute $u = \sin \theta$ with $\theta \in [-\pi/2, \pi/2]$. Then $\sqrt{1 - u^2} = \cos \theta$ and $J_1 = \int_{-\pi/2}^{\pi/2} \cos^2 \theta \, d\theta = \int_{-\pi/2}^{\pi/2} \tfrac{1}{2}(1 + \cos 2\theta) \, d\theta = \pi/2$.
12. The right side for $m = 1$ is $\sqrt{\pi} \, \Gamma(3/2) / \Gamma(2) = \sqrt{\pi} \cdot (\sqrt{\pi}/2) / 1 = \pi/2$. So the claim holds for $m = 1$.
13. Let $m \ge 2$. The function $w(u) = (1 - u^2)^{m/2}$ is continuously differentiable on $[-1, 1]$, with $w'(u) = -m u (1 - u^2)^{m/2 - 1}$, since $m/2 - 1 \ge 0$.
14. [[Integration by parts|08Y1BBQTK9]] with the factors $w$ and $u$ gives $J_m = [u \, w(u)]_{-1}^{1} - \int_{-1}^1 u \, w'(u) \, du = m \int_{-1}^1 u^2 (1 - u^2)^{m/2 - 1} \, du$, because $w(\pm 1) = 0$.
15. Write $u^2 = 1 - (1 - u^2)$. Then step 14 reads $J_m = m (J_{m-2} - J_m)$, so $J_m = \frac{m}{m+1} J_{m-2}$.
16. Assume the claim of step 9 for $m - 2$. By step 5's functional equation, $\Gamma(m/2 + 1) = \tfrac{m}{2} \Gamma(m/2)$ and $\Gamma(m/2 + 3/2) = \tfrac{m+1}{2} \Gamma(m/2 + 1/2)$.
17. Hence $\sqrt{\pi} \, \Gamma(m/2 + 1) / \Gamma(m/2 + 3/2) = \frac{m}{m+1} \sqrt{\pi} \, \Gamma(m/2) / \Gamma(m/2 + 1/2) = \frac{m}{m+1} J_{m-2} = J_m$. By induction on $m$, the claim of step 9 holds for all $m \ge 0$.
18. Inductive step. Let $n \ge 2$ and assume $P(n - 1)$. Fix $R > 0$. Write a point of $\R^n$ as $(s, y)$ with $s \in \R$ and $y \in \R^{n-1}$, so that $\norm{(s, y)}^2 = s^2 + \norm{y}^2$.
19. For $\abs{s} \le R$, the slice $\set{y : (s, y) \in B_n(R)}$ is $B_{n-1}(\sqrt{R^2 - s^2})$. For $\abs{s} > R$ the slice is empty.
20. Apply [[Tonelli's theorem|067SYD2J4B]] to the indicator function of $B_n(R)$ on $\R \times \R^{n-1}$. With step 19 and $P(n - 1)$, $V_n(R) = \int_{\R} g(s) \, ds$, where $g(s) = c_{n-1} (R^2 - s^2)^{(n-1)/2}$ for $\abs{s} \le R$ and $g(s) = 0$ otherwise.
21. The function $g$ is continuous on $[-R, R]$ and zero outside. So, as in step 7, its Lebesgue integral is the Riemann integral $c_{n-1} \int_{-R}^{R} (R^2 - s^2)^{(n-1)/2} \, ds$.
22. The substitution $s = R u$ turns this into $c_{n-1} R^n J_{n-1}$, since $(R^2 - R^2 u^2)^{(n-1)/2} \cdot R = R^n (1 - u^2)^{(n-1)/2}$.
23. By step 9 with $m = n - 1$, $c_{n-1} J_{n-1} = \frac{\pi^{(n-1)/2}}{\Gamma((n+1)/2)} \cdot \frac{\sqrt{\pi} \, \Gamma((n+1)/2)}{\Gamma(n/2 + 1)} = \frac{\pi^{n/2}}{\Gamma(n/2 + 1)} = c_n$.
24. So $V_n(R) = c_n R^n$ for $R > 0$, and step 6 covers $R = 0$. This proves $P(n)$.
25. By induction, $\operatorname{vol}(B_n(R)) = \frac{\pi^{n/2}}{\Gamma(n/2 + 1)} R^n$ for all $n \ge 1$ and $R > 0$.

## Idea

Cut the $n$-ball into slices perpendicular to one axis. Each slice is an $(n-1)$-ball, so its volume is known by induction, and the volume of the $n$-ball becomes a one-variable integral. Integration by parts gives a recursion for that integral, and the recursion matches the functional equation of the gamma function.
