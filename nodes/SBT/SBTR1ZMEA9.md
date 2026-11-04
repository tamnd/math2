---
tag: SBTR1ZMEA9
kind: proof
name: Proof of the existence and uniqueness of Laurent expansions on an annulus
msc: [30B10]
proves: 06WHRARZKY
uses: [0AJ0YVK743, 0X3XD2ATB0, 0DG0Z72CQD, 0D1C9Y1EXA, 0T7ABX4CWE, 0QEBN8DGVE, 0AR06W1E1B, 0NHGY0N0JB, 0BARQY52N5, 0826SGV3R0, 0YMP521ZR5, 045EWAXY9P, 0DG10TVYPN, 02AC7JR6G6, 0YQ458D7PF, 05APWSX53S, 0DJMGPN8K9, 0V4DET59NW, 0NX5NWAFC9, 02P2PYH3X3]
sources:
  - url: https://proofwiki.org/wiki/Existence_of_Laurent_Series
  - url: https://en.wikipedia.org/wiki/Laurent_series
    locator: Uniqueness
---

## Proof

Let $c$, $r$, $R$, $A$ and $f$ be as in the statement. For $r < \rho < R$, let $C_\rho$ be the circle $\abs{w - c} = \rho$. All integrals over $C_\rho$ are [[circle integrals|0T7ABX4CWE]].
For $n \in \Z$ and $r < \rho < R$, let $I_n(\rho) = \frac{1}{2\pi i} \oint_{C_\rho} \frac{f(w)}{(w - c)^{n+1}} \, dw$.

*Lemma: integrals over circles do not depend on the radius.*

1. Let $\varphi$ be [[holomorphic|0DG0Z72CQD]] on the [[annulus|0AJ0YVK743]] $A$, and let $J(\rho) = \oint_{C_\rho} \varphi(w) \, dw = \int_0^{2\pi} \varphi(c + \rho e^{i\theta}) \, i \rho e^{i\theta} \, d\theta$.
2. By the definition of [[complex differentiability|0D1C9Y1EXA]], as in the real chain rule, $\partial_\rho \varphi(c + \rho e^{i\theta}) = \varphi'(c + \rho e^{i\theta}) e^{i\theta}$ and $\partial_\theta \varphi(c + \rho e^{i\theta}) = \varphi'(c + \rho e^{i\theta}) i \rho e^{i\theta}$.
3. Let $\Phi(\rho, \theta) = \varphi(c + \rho e^{i\theta}) i \rho e^{i\theta}$ and $G_\rho(\theta) = \varphi(c + \rho e^{i\theta}) \rho e^{i\theta}$. By step 2, $\rho \, \partial_\rho \Phi = \partial_\theta G_\rho$. Both sides equal $i \varphi' \rho^2 e^{2i\theta} + i \varphi \rho e^{i\theta}$.
4. By [[holomorphic functions are infinitely differentiable|0QEBN8DGVE]], $\varphi'$ is holomorphic, hence continuous. So $\partial_\rho \Phi$ is continuous on $[\rho_a, \rho_b] \times [0, 2\pi]$ for each $r < \rho_a < \rho_b < R$.
5. By [[differentiation under the integral sign|0AR06W1E1B]] for the real and imaginary parts, and by the [[fundamental theorem of calculus|0NHGY0N0JB]], $J'(\rho) = \frac{1}{\rho} \bigl( G_\rho(2\pi) - G_\rho(0) \bigr) = 0$.
6. By the [[mean value theorem|0BARQY52N5]] for the real and imaginary parts of $J$, $J$ is constant on $(r, R)$.
7. Apply this to $\varphi(w) = f(w)/(w - c)^{n+1}$, which is holomorphic on $A$ since $c \notin A$. So $I_n(\rho)$ does not depend on $\rho$. Write $a_n = I_n(\rho)$.

*Existence.*

8. Fix $z \in A$ and choose $\rho_1, \rho_2$ with $r < \rho_1 < \abs{z - c} < \rho_2 < R$.
9. Let $q(w) = \frac{f(w) - f(z)}{w - z}$ for $w \in A$, $w \ne z$, and $q(z) = f'(z)$. It is holomorphic on $A \setminus \set{z}$ as a quotient.
10. Near $z$: on a disc around $z$ inside $A$, $f(w) = \sum_{k \ge 0} b_k (w - z)^k$ by [[holomorphic functions are analytic|0826SGV3R0]], with $b_0 = f(z)$ and $b_1 = f'(z)$ by [[term-by-term differentiation|0YMP521ZR5]].
11. So $q(w) = \sum_{k \ge 1} b_k (w - z)^{k-1}$ on that disc. This series converges at each point of the disc, so its [[radius of convergence|045EWAXY9P]] is at least the radius of the disc.
12. Indeed, a power series that converges at a point has bounded terms there. By step 11 and [[power series are holomorphic|0YMP521ZR5]], $q$ is holomorphic near $z$, hence on $A$.
13. By the lemma, $\oint_{C_{\rho_2}} q = \oint_{C_{\rho_1}} q$.
14. By [[Cauchy's integral formula|0DG10TVYPN]] for the constant function $1$, $\oint_{C_{\rho_2}} \frac{dw}{w - z} = 2\pi i$, since $\abs{z - c} < \rho_2$.
15. The function $w \mapsto 1/(w - z)$ is holomorphic on the disc $\abs{w - c} < \abs{z - c}$, which contains $C_{\rho_1}$. By [[primitives on a disc|02AC7JR6G6]] and the [[fundamental theorem of contour integration|0YQ458D7PF]], $\oint_{C_{\rho_1}} \frac{dw}{w - z} = 0$.
16. Writing $q$ out in step 13 and using steps 14 and 15 gives $$f(z) = \frac{1}{2\pi i} \oint_{C_{\rho_2}} \frac{f(w)}{w - z} \, dw - \frac{1}{2\pi i} \oint_{C_{\rho_1}} \frac{f(w)}{w - z} \, dw.$$
17. Let $w \in C_{\rho_2}$ and $t = (z - c)/(w - c)$, so $\abs{t} = q_2 = \abs{z - c}/\rho_2 < 1$. By the [[finite geometric sum|05APWSX53S]], $\frac{1}{w - z} - \sum_{n=0}^{N} \frac{(z - c)^n}{(w - c)^{n+1}} = \frac{t^{N+1}}{w - z}$.
18. Let $M_2$ be the maximum of $\abs{f}$ on $C_{\rho_2}$, which exists by [[attainment of bounds|0V4DET59NW]]. Also $\abs{w - z} \ge \rho_2 - \abs{z - c}$ on $C_{\rho_2}$.
19. By the [[estimation lemma|0DJMGPN8K9]] and step 17, $\abs{\frac{1}{2\pi i} \oint_{C_{\rho_2}} \frac{f(w)}{w - z} \, dw - \sum_{n=0}^{N} a_n (z - c)^n} \le \frac{\rho_2 M_2 \, q_2^{N+1}}{\rho_2 - \abs{z - c}}$. Here we used step 7 to write $I_n(\rho_2) = a_n$.
20. As $N \to \infty$ the bound tends to $0$. So the first integral in step 16 equals $\sum_{n \ge 0} a_n (z - c)^n$.
21. Let $w \in C_{\rho_1}$ and $s = (w - c)/(z - c)$, so $\abs{s} = q_1 = \rho_1/\abs{z - c} < 1$. Then $-\frac{1}{w - z} - \sum_{m=0}^{N} \frac{(w - c)^m}{(z - c)^{m+1}} = \frac{s^{N+1}}{z - w}$, and $\abs{z - w} \ge \abs{z - c} - \rho_1$.
22. As in steps 18 to 20, $-\frac{1}{2\pi i} \oint_{C_{\rho_1}} \frac{f(w)}{w - z} \, dw = \sum_{m \ge 0} I_{-m-1}(\rho_1) (z - c)^{-m-1} = \sum_{n \ge 1} a_{-n} (z - c)^{-n}$.
23. By steps 16, 20 and 22, both parts of the [[Laurent series|0X3XD2ATB0]] $\sum_{n \in \Z} a_n (z - c)^n$ converge, and its sum is $f(z)$. The coefficients are $a_n = I_n(\rho)$ for any $\rho \in (r, R)$, by step 7.

*Absolute and uniform convergence.*

24. For $r < \rho < R$, let $M(\rho)$ be the maximum of $\abs{f}$ on $C_\rho$. By the estimation lemma, $\abs{a_n} \le \frac{1}{2\pi} \cdot 2\pi\rho \cdot M(\rho) \rho^{-n-1} = M(\rho) \rho^{-n}$ for each $n \in \Z$.
25. Let $r < \sigma_1 \le \sigma_2 < R$, and choose $s_1 \in (r, \sigma_1)$ and $s_2 \in (\sigma_2, R)$. Let $\sigma_1 \le \abs{z - c} \le \sigma_2$.
26. By step 24, $\abs{a_n (z - c)^n} \le M(s_2) (\sigma_2/s_2)^n$ for $n \ge 0$, and $\abs{a_{-n} (z - c)^{-n}} \le M(s_1) (s_1/\sigma_1)^n$ for $n \ge 1$.
27. Both bounds are terms of convergent geometric series. By the [[Weierstrass M-test|0NX5NWAFC9]], applied to real and imaginary parts, both parts converge absolutely and uniformly on the closed annulus.
28. Each $z \in A$ lies in such a closed annulus, with $\sigma_1 = \sigma_2 = \abs{z - c}$. So the series converges absolutely on $A$.

*Uniqueness.*

29. Let $\sum_{n \in \Z} b_n (z - c)^n$ be a Laurent series that converges to $f(z)$ at each $z \in A$. Fix $\rho \in (r, R)$, $s_1 \in (r, \rho)$ and $s_2 \in (\rho, R)$.
30. Convergence at points with $\abs{z - c} = s_2$ and $\abs{z - c} = s_1$ makes the terms bounded there: $\abs{b_n} s_2^n \le B_2$ for $n \ge 0$ and $\abs{b_{-n}} s_1^{-n} \le B_1$ for $n \ge 1$.
31. On $C_\rho$, this gives $\abs{b_n (z - c)^n} \le B_2 (\rho/s_2)^n$ and $\abs{b_{-n} (z - c)^{-n}} \le B_1 (s_1/\rho)^n$. As in step 27, both parts converge uniformly on $C_\rho$.
32. Fix $k \in \Z$. Multiplying by $(z - c)^{-k-1}$, which has modulus $\rho^{-k-1}$ on $C_\rho$, keeps the convergence uniform. By the estimation lemma applied to the tails, we may integrate term by term: $$a_k = \frac{1}{2\pi i} \oint_{C_\rho} \frac{f(z)}{(z - c)^{k+1}} \, dz = \sum_{n \in \Z} b_n \frac{1}{2\pi i} \oint_{C_\rho} (z - c)^{n - k - 1} \, dz.$$
33. For $m \in \Z$, $\oint_{C_\rho} (z - c)^m \, dz = i \rho^{m+1} \int_0^{2\pi} e^{i(m+1)\theta} \, d\theta$. This is $2\pi i$ if $m = -1$.
34. If $m \ne -1$, the integrand has the primitive $e^{i(m+1)\theta}/(i(m+1))$, which takes equal values at $0$ and $2\pi$ by [[periodicity|02P2PYH3X3]]. So the integral is $0$.
35. By steps 32 to 34, only the term $n = k$ survives, and $a_k = b_k$. So the coefficients are unique.

## Idea

Cauchy's integral formula on the region between two circles writes $f(z)$ as an integral over the outer circle minus an integral over the inner circle. On the outer circle $1/(w - z)$ expands in powers of $z - c$, and on the inner circle in powers of $1/(z - c)$. Integrating term by term gives the two halves of the Laurent series. Integrating a Laurent series against $(z - c)^{-k-1}$ over a circle picks out the single coefficient $a_k$, which gives uniqueness.
