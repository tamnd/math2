---
tag: MVVTVYB0PK
kind: proof
name: Proof of the formula for the characteristic function of the normal distribution
msc: ["60E10"]
proves: 0NS0TDA4E2
uses: [0MYDNRT7PP, 07RXBVTVZB, 027JF1FBB0, 04YG690N5V, 01ZWX875AT, 0D37QFPEZE, 08Y1BBQTK9, 0H5ZAZCX2T, 06JZGMYTYD, 0FR1BDKK10, 039JAF7ZAN, 0MBWQKM8QR, 028XEQCE88, 04R3CY41VJ, 0RXX2PT1MQ, 0EX9GFJ0B3, 0VCTBJMEJF, 0WM7DJCM6G]
sources:
  - url: https://en.wikipedia.org/wiki/Normal_distribution
    locator: Fourier transform and characteristic function
---

## Proof

We compute the moments of the standard normal law and expand the cosine in its Taylor polynomials.

1. Let $\mu \in \R$, $\sigma^2 > 0$, and $\sigma = \sqrt{\sigma^2} > 0$. Let $X \sim \mathcal{N}(\mu, \sigma^2)$ be [[normal|07RXBVTVZB]], and fix $t \in \R$.
2. Let $f = \varphi_{\mu, \sigma^2}$ and $\varphi = \varphi_{0,1}$ be the [[normal densities|027JF1FBB0]]. By definition, $f$ is a [[probability density function|04YG690N5V]] of $X$, and $\int_\R \varphi = 1$.
3. By definition, the [[characteristic function|0MYDNRT7PP]] is $\varphi_X(t) = E[\cos(tX)] + i \, E[\sin(tX)]$. Both expectations exist, since the variables are bounded.
4. By the [[law of the unconscious statistician|01ZWX875AT]], $E[g(X)] = \int_\R g(x) f(x) \, dx$ for each bounded continuous $g$. These integrals converge absolutely as [[improper integrals|0VCTBJMEJF]].
5. For all real $z$, $\sigma f(\mu + \sigma z) = \varphi(z)$. With [[substitution|0D37QFPEZE]] $x = \mu + \sigma z$ on bounded intervals, step 4 gives $E[g(X)] = \int_\R g(\mu + \sigma z) \varphi(z) \, dz$.

First, the integrals $\int_\R \abs{z}^k \varphi(z) \, dz$ converge.

6. Let $k \ge 0$ be an integer. By the [[exponential series|06JZGMYTYD]], $e^{z^2/4} \ge (z^2/4)^k / k!$. So $\abs{z}^k e^{-z^2/4} \le k! \, 4^k$ for $\abs{z} \ge 1$, and it is at most $1$ for $\abs{z} < 1$.
7. Since $(\abs{z}/2 - 1)^2 \ge 0$, we have $z^2/4 \ge \abs{z} - 1$. So $e^{-z^2/4} \le e \cdot e^{-\abs{z}}$.
8. By steps 6 and 7, $\abs{z}^k \varphi(z) \le C_k e^{-\abs{z}}$ with $C_k = k! \, 4^k e$. By the [[comparison test|0FR1BDKK10]] and the [[integral of $e^{-x}$|039JAF7ZAN]], $\int_\R \abs{z}^k \varphi(z) \, dz$ converges.
9. Step 8 with $k + 1$ in place of $k$ gives $\abs{z}^k \varphi(z) \le C_{k+1} e^{-\abs{z}}/\abs{z}$ for $z \ne 0$. So $\abs{z}^k \varphi(z) \to 0$ as $\abs{z} \to \infty$.

Next, the even moments.

10. For $k \ge 0$, let $m_{2k} = \int_\R z^{2k} \varphi(z) \, dz$. Then $m_0 = 1$ by step 2.
11. By the [[chain rule|0RXX2PT1MQ]] and [[the derivative of the exponential|0EX9GFJ0B3]], $\varphi'(z) = -z \varphi(z)$.
12. [[Integration by parts|08Y1BBQTK9]] with $u(z) = z^{2k+1}$ and $v(z) = -\varphi(z)$ gives, for $R > 0$,
$$\int_{-R}^{R} z^{2k+2} \varphi(z) \, dz = -2R^{2k+1} \varphi(R) + (2k + 1) \int_{-R}^{R} z^{2k} \varphi(z) \, dz.$$
13. Let $R \to \infty$. By step 9, the boundary term tends to $0$. So $m_{2k+2} = (2k + 1) \, m_{2k}$.
14. By induction on $k$, $m_{2k} = (2k)!/(2^k k!)$. Indeed, $(2k+1) (2k)!/(2^k k!) = (2k+2)!/(2^{k+1} (k+1)!)$, since $(2k+2)/(2(k+1)) = 1$.

Now the standard normal case.

15. For real $s$, let $S(s) = \int_\R \sin(sz) \varphi(z) \, dz$ and $C(s) = \int_\R \cos(sz) \varphi(z) \, dz$. Both converge absolutely by step 8 with $k = 0$.
16. The function $\sin(sz) \varphi(z)$ is odd in $z$. Substituting $z = -u$ on $(-\infty, 0]$ shows that $S(s) = 0$.
17. Fix $N \ge 0$. By [[Taylor's theorem with the Lagrange remainder|0H5ZAZCX2T]] for $\cos$ at $0$, of degree $2N + 1$, we get for real $y$
$$\abs{\cos y - \sum_{k=0}^{N} \frac{(-1)^k y^{2k}}{(2k)!}} \le \frac{y^{2N+2}}{(2N+2)!}.$$
Here we used that all derivatives of $\cos$ are $\pm\sin$ or $\pm\cos$, so they are bounded by $1$.
18. Put $y = sz$, multiply by $\varphi(z) > 0$, and integrate. By [[monotonicity of the integral|0MBWQKM8QR]] on bounded intervals and a limit, step 14 gives
$$\abs{C(s) - \sum_{k=0}^{N} \frac{(-1)^k s^{2k} m_{2k}}{(2k)!}} \le \frac{s^{2N+2} m_{2N+2}}{(2N+2)!} = \frac{(s^2/2)^{N+1}}{(N+1)!}.$$
19. By step 14, the sum in step 18 equals $\sum_{k=0}^{N} (-s^2/2)^k / k!$. By the [[exponential series|06JZGMYTYD]], it tends to $e^{-s^2/2}$ as $N \to \infty$.
20. The right side of step 18 is a term of the convergent series for $e^{s^2/2}$. So it tends to $0$ as $N \to \infty$.
21. By steps 18 to 20, $C(s) = e^{-s^2/2}$ for all real $s$.

Finally, the general case.

22. By step 5 and the [[angle addition formulas|028XEQCE88]], $E[\cos(tX)] = \cos(\mu t) \, C(\sigma t) - \sin(\mu t) \, S(\sigma t)$.
23. In the same way, $E[\sin(tX)] = \sin(\mu t) \, C(\sigma t) + \cos(\mu t) \, S(\sigma t)$.
24. By steps 16 and 21, $E[\cos(tX)] = \cos(\mu t) \, e^{-\sigma^2 t^2/2}$ and $E[\sin(tX)] = \sin(\mu t) \, e^{-\sigma^2 t^2/2}$.
25. By step 3 and [[Euler's formula|04R3CY41VJ]], $\varphi_X(t) = (\cos(\mu t) + i \sin(\mu t)) \, e^{-\sigma^2 t^2/2} = e^{i\mu t} e^{-\sigma^2 t^2/2}$.
26. By the [[product of exponentials|0WM7DJCM6G]], $e^{w} e^{w'} = e^{w + w'}$ for complex $w$ and $w'$. So $\varphi_X(t) = \exp\left(i\mu t - \tfrac{1}{2}\sigma^2 t^2\right)$.
27. For $\mu = 0$ and $\sigma^2 = 1$, this gives $\varphi(t) = e^{-t^2/2}$ for the standard normal distribution.

## Idea

The sine part vanishes because the standard normal density is symmetric. For the cosine part, expand $\cos(sz)$ in its Taylor polynomials and integrate term by term. The even moments $(2k)!/(2^k k!)$ turn the cosine series into the series of $e^{-s^2/2}$, and the Taylor remainder controls the error.
