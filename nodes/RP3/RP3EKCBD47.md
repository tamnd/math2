---
tag: RP3EKCBD47
kind: proof
name: Proof of the existence and uniqueness of the principal value of the argument
msc: [30A99]
proves: 0SQSQP748R
uses: [0ZZRSX91QR, 0KW2X0TFBX, 0WB57D9488, 0RDP2HEFEW, 03H7WZ4T3K, 028XEQCE88, 0P4NQD746K, 05V7J4WD1C]
sources:
  - url: https://en.wikipedia.org/wiki/Argument_(complex_analysis)
    locator: Principal value
---

## Proof

We first build an argument in $(-\pi, \pi]$, then show that there is only one.
Here $\sin$ and $\cos$ are the real functions given by their [[power series|0WB57D9488]].

1. Let $z \neq 0$ and let $r = |z|$ be its [[modulus|0KW2X0TFBX]]. Since $\operatorname{Re} z \neq 0$ or $\operatorname{Im} z \neq 0$, we have $r > 0$.
2. Let $a = \operatorname{Re} z / r$ and $b = \operatorname{Im} z / r$. Then $a^2 + b^2 = r^2 / r^2 = 1$. So $a^2 \le 1$, that is, $-1 \le a \le 1$.
3. The function $\cos$ is even and $\sin$ is odd: $\cos(-x) = \cos x$ and $\sin(-x) = -\sin x$ for real $x$.
Indeed, $(-x)^{2n} = x^{2n}$ and $(-x)^{2n+1} = -x^{2n+1}$ in each term of the power series.
4. Let $\theta_0 = \arccos a$, the [[arccosine|0RDP2HEFEW]] of $a$. Then $0 \le \theta_0 \le \pi$ and $\cos \theta_0 = a$.
5. By the [[Pythagorean identity|03H7WZ4T3K]], $\sin^2 \theta_0 = 1 - a^2 = b^2$. So $\sin \theta_0 = b$ or $\sin \theta_0 = -b$.
6. If $\sin \theta_0 = b$, let $\theta_1 = \theta_0$. Otherwise let $\theta_1 = -\theta_0$.
By step 3, in both cases $\cos \theta_1 = a$, $\sin \theta_1 = b$ and $-\pi \le \theta_1 \le \pi$.
7. If $\theta_1 = -\pi$, let $\theta = \theta_1 + 2 \pi = \pi$. Otherwise let $\theta = \theta_1$.
By [[periodicity|0P4NQD746K]], $\cos \theta = a$ and $\sin \theta = b$, and now $-\pi < \theta \le \pi$.
8. Then $r (\cos \theta + i \sin \theta) = r a + r b \, i = \operatorname{Re} z + (\operatorname{Im} z) i = z$.
So $\theta$ is an [[argument|0ZZRSX91QR]] of $z$ in $(-\pi, \pi]$.
9. For uniqueness, we first prove a claim. Let $t$ be real with $\cos t = 1$, $\sin t = 0$ and $-2\pi < t < 2\pi$. Then $t = 0$.
10. Proof of the claim. By the [[angle addition formulas|028XEQCE88]], $\sin(x + t) = \sin x \cos t + \cos x \sin t = \sin x$ for all real $x$.
Also, using step 3, $\sin(x - t) = \sin x \cos t - \cos x \sin t = \sin x$.
11. If $t > 0$, step 10 makes $t$ a positive period of $\sin$ smaller than $2\pi$. If $t < 0$, step 10 makes $-t$ such a period.
Both are impossible, because $2\pi$ is the smallest positive period of $\sin$, by [[periodicity|0P4NQD746K]]. So $t = 0$.
12. Now let $\theta$ and $\varphi$ be arguments of $z$, both in $(-\pi, \pi]$.
Then $r(\cos \theta + i \sin \theta) = r(\cos \varphi + i \sin \varphi)$.
13. Divide by the real number $r > 0$ and compare parts, by [[equality of complex numbers|05V7J4WD1C]]. This gives $\cos \theta = \cos \varphi$ and $\sin \theta = \sin \varphi$.
14. Let $t = \theta - \varphi$. By the angle addition formulas and step 3, $\cos t = \cos \theta \cos \varphi + \sin \theta \sin \varphi$.
By step 13, this is $\cos^2 \varphi + \sin^2 \varphi = 1$.
15. In the same way, $\sin t = \sin \theta \cos \varphi - \cos \theta \sin \varphi = \sin \varphi \cos \varphi - \cos \varphi \sin \varphi = 0$.
16. Both $\theta$ and $\varphi$ lie in $(-\pi, \pi]$, so $-2\pi < t < 2\pi$. By the claim in step 9, $t = 0$, that is, $\theta = \varphi$.
17. So $z$ has exactly one argument in $(-\pi, \pi]$.

## Idea

The point $z / |z|$ lies on the unit circle, and the arccosine gives an angle with the right cosine.
Flipping the sign of the angle fixes the sine if needed.
Two angles with the same cosine and sine differ by a period of $\sin$, and an interval of length $2\pi$ is too short to hold two of them.
