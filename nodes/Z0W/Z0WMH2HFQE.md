---
tag: Z0WMH2HFQE
kind: proof
name: Niven's proof of the irrationality of pi
msc: [11J72]
proves: 0QHZX1PK8V
uses: [080T2TXVQV, 0C1VYVNV2N, 0WB57D9488, 01A8JGR4JM, 028XEQCE88, 03H7WZ4T3K, 0XE690QF65, 00R4MWW532, 0V2DV29EGT, 07ZMX4ANJS, 00KAFBR32E, 07J5X2T1ZX, 0EHWPWGHB2, 0MH1WK89PP, 084NGSTWM7, 0RXX2PT1MQ, 0V9A43H7WV, 0M0TKFRX2A, 0C5TP6RYSV, 0VGMHCF4SC, 06SESV7GQY, 0NHGY0N0JB, 0MBWQKM8QR, 05RCDKHZM6, 0QNY6ZBXPN, 0VVY4H92G2]
sources:
  - url: https://en.wikipedia.org/wiki/Proof_that_pi_is_irrational
    locator: Niven's proof
---

## Proof

We argue by contradiction. Assume that $\pi$ is not [[irrational|080T2TXVQV]].

1. By the [[definition of $\pi$|0C1VYVNV2N]], $\pi/2$ is the only zero of $\cos$ in $[0, 2]$. From the [[defining series|0WB57D9488]], $\cos 0 = 1$, so $\pi > 0$.
2. So $\pi = a/b$ for some positive integers $a$ and $b$. In particular $b \pi = a$.
3. From the defining series, $\sin 0 = 0$, and $\sin$ is [[odd|0XE690QF65]] because its series has only odd powers. By [[this result|01A8JGR4JM]], $\sin \pi = 0$ and $\cos \pi = -1$.
4. By the [[derivatives of sine|00R4MWW532]] and [[of cosine|0V2DV29EGT]], both are differentiable, hence [[continuous|07ZMX4ANJS]]. If $\cos x \le 0$ for some $0 < x < \pi/2$, the [[intermediate value theorem|00KAFBR32E]] gives a zero of $\cos$ in $[0, x]$.
5. That zero would be at most $x < \pi/2 \le 2$, a second zero of $\cos$ in $[0, 2]$. So $\cos > 0$ on $[0, \pi/2)$.
6. By [[this result|07J5X2T1ZX]], $\sin$ is strictly increasing on $[0, \pi/2]$. So $\sin x > 0$ for $0 < x \le \pi/2$, and $\sin x \ge \sin(\pi/4) > 0$ for $\pi/4 \le x \le \pi/2$.
7. By the [[addition formula|028XEQCE88]] and oddness, $\sin(\pi - u) = \sin \pi \cos(-u) + \cos \pi \sin(-u) = \sin u$. With step 6, $\sin x > 0$ for $0 < x < \pi$.
8. So $\sin x \ge 0$ on $[0, \pi]$. Also $\sin x \le 1$, since $\sin^2 x = 1 - \cos^2 x \le 1$ by the [[Pythagorean identity|03H7WZ4T3K]].
9. Now fix a positive integer $n$, and let $f(x) = \frac{x^n (a - b x)^n}{n!}$. By the [[binomial theorem|0EHWPWGHB2]], $n! \, f(x) = \sum_{k=n}^{2n} c_k x^k$ with integers $c_k$.
10. By the [[derivative of a polynomial|0MH1WK89PP]], applied $j$ times, the [[$j$-th derivative|084NGSTWM7]] is $f^{(j)}(x) = \sum_{k \ge j} \frac{c_k}{n!} \frac{k!}{(k-j)!} x^{k-j}$. In particular $f^{(j)} = 0$ for $j > 2n$.
11. At $x = 0$ only the term $k = j$ survives. So $f^{(j)}(0) = 0$ if $j < n$ or $j > 2n$, and $f^{(j)}(0) = c_j \frac{j!}{n!}$ if $n \le j \le 2n$.
12. For $j \ge n$, the number $\frac{j!}{n!} = (n+1)(n+2) \cdots j$ is an integer. So $f^{(j)}(0)$ is an integer for every $j \ge 0$.
13. By step 2, $a - b(\pi - x) = b x$ and $\pi - x = \frac{a - b x}{b}$. So $f(\pi - x) = \frac{(a - b x)^n (b x)^n}{b^n \, n!} = f(x)$ for all real $x$.
14. Differentiating $j$ times with the [[chain rule|0RXX2PT1MQ]] gives $(-1)^j f^{(j)}(\pi - x) = f^{(j)}(x)$. At $x = 0$, $f^{(j)}(\pi) = (-1)^j f^{(j)}(0)$, an integer.
15. Let $F = \sum_{i=0}^{n} (-1)^i f^{(2i)}$. By steps 12 and 14, $F(0)$ and $F(\pi)$ are integers.
16. By [[linearity of the derivative|0M0TKFRX2A]], $F'' = \sum_{i=0}^{n} (-1)^i f^{(2i+2)} = -\sum_{i=1}^{n+1} (-1)^i f^{(2i)}$. Since $f^{(2n+2)} = 0$, this gives $F + F'' = f^{(0)} = f$.
17. Let $G(x) = F'(x) \sin x - F(x) \cos x$. By the [[product rule|0V9A43H7WV]], $G' = F'' \sin + F' \cos - F' \cos + F \sin = (F'' + F) \sin = f \sin$.
18. Let $g(x) = f(x) \sin x$. It is [[continuous|0VGMHCF4SC]], since [[polynomials are continuous|0C5TP6RYSV]]. So $g$ is [[Riemann integrable|06SESV7GQY]] on every closed interval.
19. By the [[fundamental theorem of calculus|0NHGY0N0JB]], $J = \int_0^{\pi} g(x) \, dx = G(\pi) - G(0)$.
20. By steps 1 and 3, $G(\pi) = F'(\pi) \cdot 0 - F(\pi) \cdot (-1) = F(\pi)$ and $G(0) = -F(0)$. So $J = F(\pi) + F(0)$ is an integer.
21. Let $0 \le x \le \pi$. Then $0 \le x^n \le \pi^n$, and $0 \le a - b x = b(\pi - x) \le a$. So $0 \le f(x) \le \frac{\pi^n a^n}{n!}$.
22. By step 8, $0 \le g(x) \le \frac{(\pi a)^n}{n!}$ on $[0, \pi]$. A constant $C$ has $\int_\alpha^\beta C \, dx = C(\beta - \alpha)$, by the fundamental theorem with $G(x) = C x$.
23. By [[monotonicity of the integral|0MBWQKM8QR]], $J \le \pi \frac{(\pi a)^n}{n!}$.
24. Let $\pi/4 \le x \le \pi/2$. Then $x \ge \pi/4$, $a - b x = b(\pi - x) \ge b \pi / 2$, and $\sin x \ge \sin(\pi/4) > 0$ by step 6.
25. So $g(x) \ge m$ on $[\pi/4, \pi/2]$, where $m = \frac{(\pi/4)^n (b \pi / 2)^n}{n!} \sin(\pi/4) > 0$.
26. By [[additivity over intervals|05RCDKHZM6]], $J$ is the sum of the integrals of $g$ over $[0, \pi/4]$, $[\pi/4, \pi/2]$ and $[\pi/2, \pi]$.
27. Since $g \ge 0$, monotonicity makes the first and last integrals at least $0$, and the middle one at least $m \pi / 4 > 0$. So $J > 0$, and $J \ge 1$ as an integer.
28. Let $C = \pi a$ and $t_n = \frac{C^n}{n!} > 0$. Then $\frac{t_{n+1}}{t_n} = \frac{C}{n+1} \to 0$. By the [[ratio test|0QNY6ZBXPN]], $\sum t_n$ converges.
29. By the [[term test|0VVY4H92G2]], $t_n \to 0$. So there is a positive integer $n$ with $\pi t_n < 1$.
30. For this $n$, steps 23 and 27 give $1 \le J \le \pi t_n < 1$, a contradiction. So $\pi$ is irrational.

## Idea

If $\pi = a/b$, Niven builds a polynomial $f$ whose derivatives at $0$ and $\pi$ are all integers. Two integrations by parts, packed into the function $G$, turn $\int_0^\pi f(x) \sin x \, dx$ into an integer. This integral is positive but tends to $0$ as $n$ grows, since $n!$ beats $(\pi a)^n$, and no integer lies strictly between $0$ and $1$.
