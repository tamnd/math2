---
tag: 8REMJJEF6T
kind: proof
name: Proof that cos pi = -1 and sin pi = 0
msc: [33B10]
proves: 01A8JGR4JM
uses: [0WB57D9488, 0C1VYVNV2N, 0V2DV29EGT, 00R4MWW532, 07ZMX4ANJS, 00KAFBR32E, 07J5X2T1ZX, 03H7WZ4T3K, 028XEQCE88]
sources:
  - url: https://proofwiki.org/wiki/Real_Cosine_Function_is_Periodic
---

## Proof

1. From the [[defining series|0WB57D9488]], $\sin 0 = 0$ and $\cos 0 = 1$. At $0$ every sine term vanishes, and only the first cosine term is nonzero.
2. By the [[definition of $\pi$|0C1VYVNV2N]], $\pi/2$ is the only zero of $\cos$ in $[0, 2]$. Since $\cos 0 = 1 \ne 0$, we get $0 < \pi/2 \le 2$.
3. By the [[derivatives of cosine|0V2DV29EGT]] and [[of sine|00R4MWW532]], both functions are differentiable on $\mathbb{R}$. So they are [[continuous|07ZMX4ANJS]].
4. We claim $\cos x > 0$ for $0 \le x < \pi/2$. Suppose instead that $\cos x \le 0$ for such an $x$. Then $x \ne 0$, since $\cos 0 = 1$.
5. The value $0$ lies between $\cos 0 = 1$ and $\cos x$. By the [[intermediate value theorem|00KAFBR32E]] on $[0, x]$, there is $c \in [0, x]$ with $\cos c = 0$.
6. Then $c \le x < \pi/2 \le 2$. So $c$ is a zero of $\cos$ in $[0, 2]$ other than $\pi/2$, a contradiction. This proves the claim.
7. On $[0, \pi/2]$, $\sin$ is continuous, and $\sin' = \cos > 0$ at each interior point. By [[this result|07J5X2T1ZX]], $\sin$ is strictly increasing on $[0, \pi/2]$.
8. So $\sin(\pi/2) > \sin 0 = 0$.
9. By the [[Pythagorean identity|03H7WZ4T3K]], $\sin^2(\pi/2) = 1 - \cos^2(\pi/2) = 1$. With step 8, $\sin(\pi/2) = 1$.
10. By the [[addition formulas|028XEQCE88]] with $x = y = \pi/2$, $\cos \pi = \cos^2(\pi/2) - \sin^2(\pi/2) = 0 - 1 = -1$.
11. In the same way, $\sin \pi = 2 \sin(\pi/2) \cos(\pi/2) = 2 \cdot 1 \cdot 0 = 0$.

## Idea

Cosine is positive before its first zero $\pi/2$, so sine increases there and $\sin(\pi/2)$ is positive. The Pythagorean identity then forces $\sin(\pi/2) = 1$. Doubling the angle with the addition formulas gives the values at $\pi$.
