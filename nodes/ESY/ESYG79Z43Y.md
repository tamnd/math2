---
tag: ESYG79Z43Y
kind: proof
name: Proof that the principal logarithm is holomorphic off the branch cut
msc: [33B10]
proves: 0XVGJE7Q04
uses: [0YKY4M3KRQ, 06JYC06JHY, 0SQSQP748R, 0ZZRSX91QR, 01A8JGR4JM, 0WM7DJCM6G, 06JZGMYTYD, 0RKW2X63YR, 04R3CY41VJ, 08W5RN375X, 02KTRHQMHN, 028XEQCE88, 03H7WZ4T3K, 06T0HS14PP, 065XW2V6C3, 05P4B4Q22V, 07ZMX4ANJS, 0NRQPQX3VA, 019H1Z6419, 054VXHMCA3, 0DG0Z72CQD]
sources:
  - url: https://en.wikipedia.org/wiki/Complex_logarithm
    locator: The derivative of the complex logarithm
---

## Proof

We show that $\operatorname{Log}$ is continuous on $S$ and then invert the derivative of $\exp$.

1. The set $(-\infty, 0]$ is closed in $\C$, so the [[slit plane|06JYC06JHY]] $S$ is open. For $z \in S$, the [[principal branch|0YKY4M3KRQ]] is $\operatorname{Log} z = \ln \abs{z} + i \operatorname{Arg} z$, with $\operatorname{Arg} z \in (-\pi, \pi]$ the [[principal argument|0SQSQP748R]].
2. Let $z \in S$ and $\theta = \operatorname{Arg} z$. If $\theta = \pi$, then by the [[definition of an argument|0ZZRSX91QR]] and [[$\cos \pi = -1$, $\sin \pi = 0$|01A8JGR4JM]], $z = -\abs{z} \in (-\infty, 0]$. This is false, so $\theta \in (-\pi, \pi)$.
3. Let $z \in S$. By the [[product of exponentials|0WM7DJCM6G]], $e^{\operatorname{Log} z} = e^{\ln \abs{z}} e^{i \operatorname{Arg} z}$. Here $e^{\ln \abs{z}} = \abs{z}$, because the [[exponential series is the real exponential|06JZGMYTYD]] at real points and [[$e^{\ln t} = t$|0RKW2X63YR]].
4. By [[Euler's formula|04R3CY41VJ]], with the real [[cosine|08W5RN375X]] and [[sine|02KTRHQMHN]] at real points, $e^{i\theta} = \cos \theta + i \sin \theta$. So $e^{\operatorname{Log} z} = \abs{z} (\cos \theta + i \sin \theta) = z$.
5. Write $z = x + iy \in S$ with $x, y$ real, and let $\varphi = \theta / 2 \in (-\pi/2, \pi/2)$. By the [[angle addition formulas|028XEQCE88]] and the [[Pythagorean identity|03H7WZ4T3K]], $\sin \theta = 2 \sin \varphi \cos \varphi$ and $\cos \theta = 2 \cos^2 \varphi - 1$.
6. Since $x = \abs{z} \cos \theta$ and $y = \abs{z} \sin \theta$, step 5 gives $\abs{z} + x = 2 \abs{z} \cos^2 \varphi$ and $y = 2 \abs{z} \sin \varphi \cos \varphi$.
7. We have $\abs{z} + x > 0$ on $S$. Indeed, if $y \ne 0$ then $\abs{z} > \abs{x} \ge -x$. If $y = 0$ then $x > 0$, because $z \in S$.
8. By steps 6 and 7, $\cos \varphi \ne 0$ and $\frac{y}{\abs{z} + x} = \frac{\sin \varphi}{\cos \varphi} = \tan \varphi$, by the [[definition of the tangent|06T0HS14PP]].
9. Since $\varphi \in (-\pi/2, \pi/2)$, the [[definition of the arctangent|065XW2V6C3]] gives $\varphi = \arctan \frac{y}{\abs{z} + x}$. So $\operatorname{Arg} z = 2 \arctan \frac{y}{\abs{z} + x}$ for each $z \in S$.
10. The functions $x$, $y$ and $\abs{z}$ are continuous in $z$, and the denominator in step 9 is positive on $S$. The arctangent is [[differentiable|05P4B4Q22V]], hence [[continuous|07ZMX4ANJS]]. The function $\ln$ is [[continuous on $(0, \infty)$|0RKW2X63YR]].
11. By step 10 and the [[continuity of compositions|0NRQPQX3VA]], $\operatorname{Arg}$ and $\ln \abs{\cdot}$ are continuous on $S$. So $\operatorname{Log}$ is continuous on $S$.
12. Fix $z_0 \in S$ and put $w_0 = \operatorname{Log} z_0$. For $z \in S$ with $z \ne z_0$, put $w = \operatorname{Log} z$. By step 4, $e^w = z \ne z_0 = e^{w_0}$, so $w \ne w_0$.
13. Then $\frac{\operatorname{Log} z - \operatorname{Log} z_0}{z - z_0} = \frac{w - w_0}{e^w - e^{w_0}} = \frac{1}{Q(w)}$, where $Q(w) = \frac{e^w - e^{w_0}}{w - w_0}$ for $w \ne w_0$.
14. By the [[derivative of the complex exponential|019H1Z6419]], $Q(w) \to e^{w_0} = z_0$ as $w \to w_0$ with $w \ne w_0$.
15. Let $\varepsilon > 0$. Choose $\eta > 0$ with $\abs{Q(w) - z_0} < \varepsilon$ for $0 < \abs{w - w_0} < \eta$. By step 11, choose $\delta > 0$ with $\abs{\operatorname{Log} z - w_0} < \eta$ for $z \in S$, $\abs{z - z_0} < \delta$.
16. By steps 12 and 15, $\abs{Q(\operatorname{Log} z) - z_0} < \varepsilon$ for $z \in S$ with $0 < \abs{z - z_0} < \delta$. So $Q(\operatorname{Log} z) \to z_0$ as $z \to z_0$.
17. We have $z_0 \ne 0$. When $\abs{Q - z_0} < \abs{z_0}/2$, we get $\abs{Q} > \abs{z_0}/2$ and $\abs{1/Q - 1/z_0} = \abs{Q - z_0} / (\abs{Q} \abs{z_0}) < 2 \abs{Q - z_0} / \abs{z_0}^2$.
18. By steps 13, 16 and 17, the difference quotient of $\operatorname{Log}$ at $z_0$ tends to $1/z_0$. So $\operatorname{Log}'(z_0) = 1/z_0$.
19. This holds at each point of the open set $S$, so $\operatorname{Log}$ is [[holomorphic|0DG0Z72CQD]] on $S$ with $\operatorname{Log}'(z) = 1/z$.

## Idea

On the slit plane, the principal argument has the explicit formula $2 \arctan(y/(\abs{z} + x))$, which shows that $\operatorname{Log}$ is continuous. Since $\operatorname{Log}$ inverts the [[exponential|054VXHMCA3]], its difference quotient is the reciprocal of a difference quotient of $\exp$, which tends to $e^{w_0} = z_0$.
