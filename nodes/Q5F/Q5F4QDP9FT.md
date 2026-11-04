---
tag: Q5F4QDP9FT
kind: proof
name: Proof of the power series of arctangent by integrating a finite geometric sum
msc: [30B10, 33B10]
proves: 0T32ME0A6H
uses: [065XW2V6C3, 06T0HS14PP, 0WB57D9488, 05P4B4Q22V, 05APWSX53S, 0C5TP6RYSV, 0GR2APWTAC, 06SESV7GQY, 0NHGY0N0JB, 07ZMX4ANJS, 080RWVVSB6, 0Q3HYFT9RQ, 0MBWQKM8QR, 0WH916TJNY, 0K0H5E3Z5N]
sources:
  - url: https://en.wikipedia.org/wiki/Leibniz_formula_for_%CF%80
    locator: Proofs
---

## Proof

We integrate a finite geometric sum with an explicit remainder, and show that the remainder tends to $0$. This handles $|x| < 1$ and $x = \pm 1$ at once.

1. Fix an integer $n \ge 0$ and a real $t$. Put $r = -t^2$. Then $r \le 0$, so $r \ne 1$ and $1 - r = 1 + t^2$.
2. By the [[sum of a finite geometric series|05APWSX53S]], $\sum_{k=0}^{n} r^k = \frac{1 - r^{n+1}}{1 + t^2}$. Rearranging gives
$$\frac{1}{1 + t^2} = \sum_{k=0}^{n} (-1)^k t^{2k} + (-1)^{n+1} \frac{t^{2n+2}}{1 + t^2}.$$
3. Let $0 < x \le 1$. The functions $t \mapsto \frac{1}{1 + t^2}$, $t \mapsto t^{2k}$ and $t \mapsto \frac{t^{2n+2}}{1 + t^2}$ are continuous on $[0, x]$. This holds since [[polynomials are continuous|0C5TP6RYSV]] and [[quotients of continuous functions are continuous|0GR2APWTAC]] where the denominator is nonzero.
4. So these functions are Riemann integrable on $[0, x]$, since [[continuous functions are Riemann integrable|06SESV7GQY]].
5. By the [[derivative of arctangent|05P4B4Q22V]], $\arctan$ is differentiable on $\R$ with derivative $\frac{1}{1 + t^2}$. So it is continuous on $[0, x]$, since [[differentiable functions are continuous|07ZMX4ANJS]].
6. Since $\tan 0 = 0$ and $0 \in (-\pi/2, \pi/2)$, the definition of the [[arctangent|065XW2V6C3]] gives $\arctan 0 = 0$.
7. By the [[fundamental theorem of calculus|0NHGY0N0JB]] and steps 5 and 6, $\int_0^x \frac{dt}{1 + t^2} = \arctan x - \arctan 0 = \arctan x$.
8. By the [[integral of a power|0Q3HYFT9RQ]], $\int_0^x t^{2k} \, dt = \frac{x^{2k+1}}{2k + 1}$ for each $k \ge 0$.
9. Let $S_n(x) = \sum_{k=0}^{n} \frac{(-1)^k x^{2k+1}}{2k + 1}$ and $R_n(x) = \int_0^x \frac{t^{2n+2}}{1 + t^2} \, dt$.
10. Integrate the identity of step 2 over $[0, x]$. By [[linearity of the integral|080RWVVSB6]] and steps 7 and 8, $\arctan x = S_n(x) + (-1)^{n+1} R_n(x)$.
11. For $t \in [0, x]$, we have $0 \le \frac{t^{2n+2}}{1 + t^2} \le t^{2n+2}$, since $1 + t^2 \ge 1$.
12. By [[monotonicity of the integral|0MBWQKM8QR]], step 11 and step 8, $0 \le R_n(x) \le \frac{x^{2n+3}}{2n + 3} \le \frac{1}{2n + 3}$. The last bound uses $0 < x \le 1$.
13. By steps 10 and 12, $|\arctan x - S_n(x)| \le \frac{1}{2n + 3} < \frac{1}{n}$ for each $n \ge 1$.
14. Let $\varepsilon > 0$. There is $N \ge 1$ with $\frac{1}{N} < \varepsilon$, by the [[Archimedean property|0WH916TJNY]]. For $n \ge N$, step 13 gives $|\arctan x - S_n(x)| < \frac{1}{n} \le \frac{1}{N} < \varepsilon$.
15. So the partial sums $S_n(x)$ tend to $\arctan x$. By the definition of the [[sum of a series|0K0H5E3Z5N]], the series converges and its sum is $\arctan x$, for $0 < x \le 1$.
16. For $x = 0$, every term of the series is $0$, and $\arctan 0 = 0$ by step 6. So the formula holds.
17. Let $-1 \le x < 0$, and put $w = -x \in (0, 1]$ and $y = \arctan w \in (-\pi/2, \pi/2)$.
18. The series defining [[sine and cosine|0WB57D9488]] contain only odd and only even powers. So $\sin(-y) = -\sin y$ and $\cos(-y) = \cos y$.
19. By step 18 and the definition of the [[tangent|06T0HS14PP]], $\tan(-y) = -\tan y = -w = x$. Also $-y \in (-\pi/2, \pi/2)$.
20. By the uniqueness in the definition of the arctangent, $\arctan x = -y = -\arctan w$.
21. Each term of $S_n$ is an odd power of its argument times a constant. So $S_n(x) = -S_n(w)$ for each $n$.
22. By step 15, $S_n(w) \to \arctan w$. So $S_n(x) = -S_n(w) \to -\arctan w = \arctan x$ by step 20.
23. Steps 15, 16 and 22 give $\arctan x = \sum_{n=0}^{\infty} \frac{(-1)^n x^{2n+1}}{2n + 1}$ for every real $x$ with $|x| \le 1$.

## Idea

The derivative $\frac{1}{1 + t^2}$ is a geometric sum in $-t^2$ plus a small remainder. Integrating term by term over $[0, x]$ gives the partial sums of the series, plus an error at most $\frac{|x|^{2n+3}}{2n+3}$. This error tends to $0$ even at $|x| = 1$, so no separate argument with Abel's theorem is needed.
