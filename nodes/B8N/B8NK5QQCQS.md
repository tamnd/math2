---
tag: B8NK5QQCQS
kind: proof
name: Proof of Jordan's lemma by Jordan's inequality
msc: ["30E20"]
proves: 0PNPG2PP9H
uses: [00FWNP9TXY, 054VXHMCA3, 0WM7DJCM6G, 04R3CY41VJ, 03H7WZ4T3K, 0HYNZE940T, 0MBWQKM8QR, 0D37QFPEZE, 0BARQY52N5, 026BJBQNGJ, 0KN2V7840E]
sources:
  - url: https://en.wikipedia.org/wiki/Jordan%27s_lemma
    locator: Proof of Jordan's lemma
---

## Proof

1. Let $a$, $R$, $C_R$, $g$, $f$ and $M_R$ be as in the statement. By the definition of the [[contour integral|00FWNP9TXY]], $$\int_{C_R} f(z) \, dz = \int_0^\pi e^{iaRe^{i\theta}} \, g(Re^{i\theta}) \, iRe^{i\theta} \, d\theta.$$
2. For real $t$, $\abs{e^{it}} = \abs{\cos t + i \sin t} = 1$, by [[Euler's formula|04R3CY41VJ]] and the [[Pythagorean identity|03H7WZ4T3K]].
3. We have $iaRe^{i\theta} = -aR\sin\theta + iaR\cos\theta$. By the [[product of exponentials|0WM7DJCM6G]], step 2 and the [[multiplicativity of the modulus|0HYNZE940T]], $\abs{e^{iaRe^{i\theta}}} = e^{-aR\sin\theta}$.
4. So the modulus of the integrand in step 1 is at most $e^{-aR\sin\theta} M_R R$, since $\abs{iRe^{i\theta}} = R$.
5. For a continuous complex function $k$ on $[0, \pi]$, write $\int_0^\pi k = \abs{\int_0^\pi k} \, e^{i\alpha}$ with $\alpha$ real. Then $\abs{\int_0^\pi k} = \int_0^\pi \operatorname{Re}(e^{-i\alpha} k) \le \int_0^\pi \abs{k}$, by [[monotonicity of the integral|0MBWQKM8QR]].
6. By steps 4 and 5, $\abs{\int_{C_R} f(z) \, dz} \le R M_R \int_0^\pi e^{-aR\sin\theta} \, d\theta$.
7. The [[substitution|0D37QFPEZE]] $\theta \mapsto \pi - \theta$ and $\sin(\pi - \theta) = \sin\theta$ give $\int_{\pi/2}^{\pi} e^{-aR\sin\theta} \, d\theta = \int_0^{\pi/2} e^{-aR\sin\theta} \, d\theta$. So the integral in step 6 is $2 \int_0^{\pi/2} e^{-aR\sin\theta} \, d\theta$.
8. Jordan's inequality: $\sin\theta \ge 2\theta/\pi$ for $\theta \in [0, \pi/2]$. Let $h(\theta) = \sin\theta - 2\theta/\pi$. Then $h(0) = h(\pi/2) = 0$, and $h'(\theta) = \cos\theta - 2/\pi$ is strictly decreasing on $[0, \pi/2]$.
9. By the [[mean value theorem|0BARQY52N5]] there is $\xi \in (0, \pi/2)$ with $h'(\xi) = 0$. So $h' \ge 0$ on $[0, \xi]$ and $h' \le 0$ on $[\xi, \pi/2]$.
10. By [[nonnegative derivative implies increasing|026BJBQNGJ]], applied to $h$ on $[0, \xi]$ and to $-h$ on $[\xi, \pi/2]$, we get $h \ge h(0) = 0$ and $h \ge h(\pi/2) = 0$. This proves Jordan's inequality.
11. Since $a R > 0$ and the [[exponential function is increasing|0KN2V7840E]], step 10 gives $e^{-aR\sin\theta} \le e^{-2aR\theta/\pi}$ on $[0, \pi/2]$.
12. By monotonicity of the integral, $\int_0^{\pi/2} e^{-aR\sin\theta} \, d\theta \le \int_0^{\pi/2} e^{-2aR\theta/\pi} \, d\theta = \frac{\pi}{2aR} \bigl( 1 - e^{-aR} \bigr) \le \frac{\pi}{2aR}$.
13. Combining steps 6, 7 and 12, $\abs{\int_{C_R} f(z) \, dz} \le R M_R \cdot 2 \cdot \frac{\pi}{2aR} = \frac{\pi}{a} M_R$.

## Idea

On the upper semicircle, $\abs{e^{iaz}} = e^{-aR\sin\theta}$ is very small except near the two ends, where $\sin\theta$ is close to $0$. Jordan's inequality $\sin\theta \ge 2\theta/\pi$ bounds this factor by an exponential that integrates to about $\pi/(2aR)$. This factor $1/R$ cancels the length $\pi R$ of the semicircle.
