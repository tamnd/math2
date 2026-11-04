---
tag: HQFEP4AXHN
kind: proof
name: Proof of the derivative of arcsine by the inverse function rule
msc: [33B10, 26A24]
proves: 0GA6G43EA9
uses: [0B89D93YA1, 0WB57D9488, 0C1VYVNV2N, 0XE690QF65, 00R4MWW532, 0V2DV29EGT, 07ZMX4ANJS, 00KAFBR32E, 07J5X2T1ZX, 03H7WZ4T3K, 0M0RZ3HSB0]
sources:
  - url: https://en.wikipedia.org/wiki/Differentiation_of_trigonometric_functions
    locator: Differentiating the inverse sine function
---

## Proof

1. From the [[defining series|0WB57D9488]], $\sin 0 = 0$ and $\cos 0 = 1$. The sine series has only odd powers and the cosine series only even powers.
2. So replacing $x$ by $-x$ gives $\sin(-x) = -\sin x$ and $\cos(-x) = \cos x$. That is, $\sin$ is [[odd and $\cos$ is even|0XE690QF65]].
3. By the [[derivative of sine|00R4MWW532]] and the [[derivative of cosine|0V2DV29EGT]], both functions are differentiable on $\mathbb{R}$, hence [[continuous|07ZMX4ANJS]].
4. By the [[definition of $\pi$|0C1VYVNV2N]], $\pi/2$ is the only zero of $\cos$ in $[0, 2]$. Since $\cos 0 = 1$, we get $0 < \pi/2 \le 2$.
5. We claim $\cos x > 0$ for $0 \le x < \pi/2$. Suppose $\cos x \le 0$ for such an $x$. Then $x \ne 0$, and the [[intermediate value theorem|00KAFBR32E]] on $[0, x]$ gives $c \in [0, x]$ with $\cos c = 0$.
6. Then $c < \pi/2 \le 2$, so $c$ is a second zero of $\cos$ in $[0, 2]$, a contradiction. This proves the claim.
7. Since $\cos$ is even, $\cos y > 0$ for every $y$ in $I = (-\pi/2, \pi/2)$.
8. On $[-\pi/2, \pi/2]$, $\sin$ is continuous with $\sin' = \cos > 0$ at interior points. By [[this result|07J5X2T1ZX]], $\sin$ is strictly increasing on $[-\pi/2, \pi/2]$.
9. So $\sin(\pi/2) > \sin 0 = 0$. By the [[Pythagorean identity|03H7WZ4T3K]], $\sin^2(\pi/2) = 1 - \cos^2(\pi/2) = 1$. So $\sin(\pi/2) = 1$, and $\sin(-\pi/2) = -1$ by oddness.
10. By steps 8 and 9, $\sin$ maps $I$ into $(-1, 1)$. Let $f \colon I \to \mathbb{R}$ be the restriction of $\sin$ to the open interval $I$.
11. Let $-1 < x < 1$, and let $y = \arcsin x$. By the [[definition of arcsine|0B89D93YA1]], $y \in [-\pi/2, \pi/2]$ and $\sin y = x$.
12. Since $\sin(\pm \pi/2) = \pm 1 \ne x$, we have $y \in I$. So $f(I) = (-1, 1)$, and the inverse $f^{-1} \colon (-1, 1) \to I$ equals $\arcsin$ on $(-1, 1)$.
13. The function $f$ is continuous and strictly monotone on $I$. It is differentiable at $y$ with $f'(y) = \cos y > 0$ by step 7.
14. By the [[inverse function rule|0M0RZ3HSB0]], $\arcsin$ is differentiable at $x = f(y)$, and $\arcsin'(x) = \frac{1}{\cos y}$.
15. By the Pythagorean identity, $\cos^2 y = 1 - \sin^2 y = 1 - x^2$. Since $\cos y > 0$, we get $\cos y = \sqrt{1 - x^2}$.
16. So $\arcsin$ is differentiable on $(-1, 1)$, and $\frac{d}{dx} \arcsin x = \frac{1}{\sqrt{1 - x^2}}$ for $-1 < x < 1$.

## Idea

On $(-\pi/2, \pi/2)$ sine is strictly increasing with derivative $\cos y > 0$, so its inverse has derivative $\frac{1}{\cos y}$. Since $\sin y = x$ and $\cos y > 0$ there, the Pythagorean identity rewrites $\cos y$ as $\sqrt{1 - x^2}$.
