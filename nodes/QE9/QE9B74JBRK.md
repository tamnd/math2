---
tag: QE9B74JBRK
kind: proof
name: Proof that sine and cosine are 2π-periodic with smallest period 2π
msc: [33B10]
proves: 0P4NQD746K
uses: [0WB57D9488, 0C1VYVNV2N, 01A8JGR4JM, 028XEQCE88, 089KWVYD69, 0XE690QF65, 0V2DV29EGT, 00R4MWW532, 07ZMX4ANJS, 00KAFBR32E, 07J5X2T1ZX, 03H7WZ4T3K, 0RXX2PT1MQ]
sources:
  - url: https://proofwiki.org/wiki/Sine_and_Cosine_are_Periodic_on_Reals
---

## Proof

First we show that $2\pi$ is a period. Then we locate the zeros of $\sin$ in $(0, 2\pi)$ and rule out smaller periods.

1. From the [[defining series|0WB57D9488]], $\sin 0 = 0$ and $\cos 0 = 1$. By [[this result|01A8JGR4JM]], $\cos \pi = -1$ and $\sin \pi = 0$.
2. By the [[addition formulas|028XEQCE88]] with $x = y = \pi$, $\cos 2\pi = \cos^2 \pi - \sin^2 \pi = 1$ and $\sin 2\pi = 2 \sin \pi \cos \pi = 0$.
3. By the addition formulas with $y = 2\pi$, $\sin(x + 2\pi) = \sin x \cdot 1 + \cos x \cdot 0 = \sin x$ and $\cos(x + 2\pi) = \cos x \cdot 1 - \sin x \cdot 0 = \cos x$.
4. By the [[definition of $\pi$|0C1VYVNV2N]], $\pi/2 \in [0, 2]$ and $\cos(\pi/2) = 0$. Since $\cos 0 = 1$, we get $0 < \pi/2 \le 2$. So $2\pi > 0$ is a [[period|089KWVYD69]] of $\sin$ and of $\cos$.
5. The sine series has only odd powers of $x$. Replacing $x$ by $-x$ changes the sign of every term, so $\sin(-u) = -\sin u$. Thus $\sin$ is [[odd|0XE690QF65]].
6. By the addition formulas and step 1, $\sin(x + \pi) = \sin x \cos \pi + \cos x \sin \pi = -\sin x$ for all real $x$.
7. Also $\sin(\pi - u) = \sin \pi \cos(-u) + \cos \pi \sin(-u) = -\sin(-u) = \sin u$ for all real $u$.
8. The functions $\sin$ and $\cos$ are differentiable, by the [[derivative of sine|00R4MWW532]] and the [[derivative of cosine|0V2DV29EGT]]. So they are [[continuous|07ZMX4ANJS]].
9. We claim $\cos x > 0$ for $0 \le x < \pi/2$. Suppose $\cos x \le 0$ for such an $x$. Then $x \ne 0$, and the [[intermediate value theorem|00KAFBR32E]] on $[0, x]$ gives $c \in [0, x]$ with $\cos c = 0$.
10. Then $c < \pi/2 \le 2$, so $c$ is a second zero of $\cos$ in $[0, 2]$. This contradicts the definition of $\pi$, and proves the claim.
11. So $\sin' = \cos > 0$ on $(0, \pi/2)$. By [[this result|07J5X2T1ZX]], $\sin$ is strictly increasing on $[0, \pi/2]$. So $\sin x > \sin 0 = 0$ for $0 < x \le \pi/2$.
12. By the [[Pythagorean identity|03H7WZ4T3K]], $\sin^2(\pi/2) = 1 - \cos^2(\pi/2) = 1$. By step 11, $\sin(\pi/2) = 1$.
13. Let $\pi/2 < x < \pi$, and let $u = \pi - x$. Then $0 < u < \pi/2$, and by steps 7 and 11, $\sin x = \sin u > 0$. So $\sin > 0$ on $(0, \pi)$.
14. Let $\pi < x < 2\pi$, and let $u = x - \pi \in (0, \pi)$. By steps 6 and 13, $\sin x = \sin(u + \pi) = -\sin u < 0$.
15. So the only zero of $\sin$ in the open interval $(0, 2\pi)$ is $\pi$.
16. Suppose that $p$ is a period of $\sin$ with $0 < p < 2\pi$. Then $\sin p = \sin(0 + p) = \sin 0 = 0$. By step 15, $p = \pi$.
17. But by steps 6 and 12, $\sin(\pi/2 + \pi) = -\sin(\pi/2) = -1 \ne 1 = \sin(\pi/2)$. So $\pi$ is not a period of $\sin$, a contradiction.
18. Suppose that $p$ is a period of $\cos$ with $0 < p < 2\pi$. Then $\cos(x + p) = \cos x$ for all real $x$.
19. Differentiating both sides with the [[chain rule|0RXX2PT1MQ]] gives $-\sin(x + p) = -\sin x$ for all real $x$. So $p$ is a period of $\sin$, which contradicts steps 16 and 17.
20. So $\sin(x + 2\pi) = \sin x$ and $\cos(x + 2\pi) = \cos x$ for all real $x$, and $2\pi$ is the smallest positive period of $\sin$ and of $\cos$.

## Idea

The values $\cos 2\pi = 1$ and $\sin 2\pi = 0$ make the addition formulas return the same values after a shift by $2\pi$. To see that no shorter shift works, note that a period $p$ of sine must be a zero of sine. Inside $(0, 2\pi)$ the only zero is $\pi$, and shifting by $\pi$ flips the sign of sine.
