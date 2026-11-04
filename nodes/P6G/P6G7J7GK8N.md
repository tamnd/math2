---
tag: P6G7J7GK8N
kind: proof
name: Proof of the formula for the Laplace transform of a derivative by integration by parts
msc: [44A10]
proves: 0K090GVHVN
uses: [05XT5AVJBK, 0WM7DJCM6G, F6PH4JEGS5, 019H1Z6419, 0V9A43H7WV, 0XYAFCN0PT, 06SESV7GQY, 06D0EWR2DV, 0FR1BDKK10, 0D37QFPEZE]
sources:
  - url: https://en.wikipedia.org/wiki/Laplace_transform
    locator: Transform of a function's derivative
---

## Proof

We integrate by parts on $[0, T]$ and let $T \to \infty$.

1. Fix $s \in \mathbb{C}$ with $\sigma = \operatorname{Re} s > a$, and write $s = \sigma + i \omega$ with $\omega$ real. Let $E(t) = e^{-st}$ for $t \ge 0$. Note that $M \ge \abs{f(0)} \ge 0$.
2. By the [[product of exponentials|0WM7DJCM6G]], $E(t) = e^{-\sigma t} e^{-i \omega t}$. By [[Euler's formula|F6PH4JEGS5]], $\abs{e^{-i\omega t}} = \abs{\cos(\omega t) - i \sin(\omega t)} = 1$. So $\abs{E(t)} = e^{-\sigma t}$.
3. For real $h \ne 0$, $\dfrac{E(t + h) - E(t)}{h} = E(t)\, \dfrac{e^{-sh} - 1}{h}$, by the product of exponentials. If $s \ne 0$, this quotient tends to $-s E(t)$ as $h \to 0$, by the [[derivative of the complex exponential|019H1Z6419]] at $0$. If $s = 0$, it is $0$. So $E'(t) = -s E(t)$.
4. Let $g(t) = M e^{-(\sigma - a) t}$. By step 2, $\abs{f(t) E(t)} \le M e^{at} e^{-\sigma t} = g(t)$ for $t \ge 0$.
5. By the [[integral of the exponential function|06D0EWR2DV]] and [[integration by substitution|0D37QFPEZE]] with $x = -(\sigma - a) t$, $\int_0^T g(t)\, dt = \frac{M}{\sigma - a}\left( 1 - e^{-(\sigma - a) T} \right)$. This tends to $\frac{M}{\sigma - a}$ as $T \to \infty$, since $\sigma - a > 0$.
6. Let $p$ be the real part of $t \mapsto f(t) E(t)$. It is continuous, and $0 \le p(t) + g(t) \le 2 g(t)$ by step 4.
7. By the [[comparison test for improper integrals|0FR1BDKK10]] and step 5, $\int_0^\infty (p + g)$ converges. So $\int_0^T p = \int_0^T (p + g) - \int_0^T g$ has a limit as $T \to \infty$.
8. The same argument applies to the imaginary part. So the limit $F(s) = \lim_{T \to \infty} \int_0^T f(t) E(t)\, dt$ exists.
9. The function $f'$ is continuous, so it is [[Riemann integrable|06SESV7GQY]] on each $[0, T]$. Thus its [[Laplace transform|05XT5AVJBK]] is defined as a limit, where the limit exists.
10. By the [[product rule|0V9A43H7WV]], applied to real and imaginary parts, and step 3, $(f E)' = f' E - s f E$. This derivative is continuous on $[0, \infty)$.
11. By the [[second fundamental theorem of calculus|0XYAFCN0PT]], applied to the real and imaginary parts of $f E$ on $[0, T]$, we get $f(T) E(T) - f(0) = \int_0^T f'(t) E(t)\, dt - s \int_0^T f(t) E(t)\, dt$.
12. So $\int_0^T f'(t) e^{-st}\, dt = f(T) e^{-sT} - f(0) + s \int_0^T f(t) e^{-st}\, dt$ for each $T > 0$.
13. By step 4, $\abs{f(T) e^{-sT}} \le M e^{-(\sigma - a) T}$, and this tends to $0$ as $T \to \infty$.
14. By steps 8 and 13, the right side of step 12 tends to $0 - f(0) + s F(s)$ as $T \to \infty$.
15. Hence the Laplace transform of $f'$ converges at $s$, and $\mathcal{L}\{f'\}(s) = s F(s) - f(0)$.

## Idea

Integration by parts moves the derivative from $f$ onto $e^{-st}$, and differentiating $e^{-st}$ only multiplies it by $-s$. The boundary term at $0$ gives $-f(0)$. The boundary term at $T$ vanishes in the limit because $f$ grows at most like $e^{at}$, while $e^{-st}$ decays like $e^{-\operatorname{Re}(s) t}$.
