---
tag: SE8YGSNANQ
kind: proof
name: Proof of Stirling's formula by a monotone sequence and the Wallis product
msc: [41A60, 05A10]
proves: 0KC0F51T6A
uses: [0044CPHJBV, 0K2FNY6DYV, 0J7PHRBNNS, 0V948DE5KA, 07X1QA6BRW, 0RXX2PT1MQ, 0M0TKFRX2A, 0GR2APWTAC, 0NHGY0N0JB, 0MBWQKM8QR, 0Q3HYFT9RQ, 080RWVVSB6, 0KN22AAW5R, 0FM6N4R0VB, 0E8HNVBCSP, 0EX9GFJ0B3, 07ZMX4ANJS, 0PAQM3H57X, 0P9BNBW2W3, 0734RSVF2V, 03S6GWWKEZ, 0RAM4E07NR, 08QAX4H1PF, 0XCYA4YERS, 04TSHB9H8D, 00SB5EA3VW]
sources:
  - url: https://en.wikipedia.org/wiki/Stirling%27s_approximation
    locator: Equation for discrete cases
---

## Proof

We show that $\ln n! - (n + \frac{1}{2}) \ln n + n$ converges, by bounding its successive differences. Then the [[Wallis product|0XCYA4YERS]] identifies the limit.

*Part 1: a convergent sequence.*

1. For each integer $n \ge 1$, let $d_n = \ln(n!) - (n + \tfrac{1}{2}) \ln n + n$. Here $\ln$ is the [[natural logarithm|0044CPHJBV]].
2. By the [[logarithm of a product|0K2FNY6DYV]], $\ln((n + 1)!) = \ln(n!) + \ln(n + 1)$. Substituting this into $d_n - d_{n+1}$ and collecting terms gives
$$d_n - d_{n+1} = (n + \tfrac{1}{2}) \big( \ln(n + 1) - \ln n \big) - 1.$$
3. For $-1 < t < 1$, let $\varphi(t) = \ln(1 + t) - \ln(1 - t)$. By the [[derivative of the logarithm|07X1QA6BRW]], the [[chain rule|0RXX2PT1MQ]] and [[linearity of differentiation|0M0TKFRX2A]], $\varphi'(t) = \frac{1}{1 + t} + \frac{1}{1 - t} = \frac{2}{1 - t^2}$.
4. Let $0 < x < 1$. The function $t \mapsto \frac{2}{1 - t^2}$ is continuous on $[0, x]$, by [[continuity of quotients|0GR2APWTAC]]. Also $\varphi(0) = 0$.
5. By the [[fundamental theorem of calculus|0NHGY0N0JB]] and steps 3 and 4, $\varphi(x) = \int_0^x \frac{2}{1 - t^2} \, dt$.
6. Let $0 \le t \le x$. Since $(1 - t^2)(1 + t^2) = 1 - t^4 \le 1$, we get $\frac{2}{1 - t^2} \ge 2 + 2t^2$.
7. Also $\frac{2}{1 - t^2} = 2 + \frac{2t^2}{1 - t^2} \le 2 + \frac{2t^2}{1 - x^2}$, since $1 - t^2 \ge 1 - x^2 > 0$.
8. By [[monotonicity of the integral|0MBWQKM8QR]], the [[integral of a power|0Q3HYFT9RQ]] and [[linearity of the integral|080RWVVSB6]], steps 5 to 7 give
$$2x + \frac{2x^3}{3} \le \varphi(x) \le 2x + \frac{2x^3}{3(1 - x^2)}.$$
9. Fix $n \ge 1$ and put $x = \frac{1}{2n + 1}$. Then $\frac{1 + x}{1 - x} = \frac{n + 1}{n}$ and $n + \frac{1}{2} = \frac{1}{2x}$.
10. By the [[logarithm of a quotient|0J7PHRBNNS]], $\varphi(x) = \ln \frac{1 + x}{1 - x} = \ln(n + 1) - \ln n$. So step 2 gives $d_n - d_{n+1} = \frac{\varphi(x)}{2x} - 1$.
11. Dividing step 8 by $2x$ gives $\frac{x^2}{3} \le d_n - d_{n+1} \le \frac{x^2}{3(1 - x^2)}$.
12. With $x = \frac{1}{2n+1}$, we have $\frac{x^2}{1 - x^2} = \frac{1}{(2n + 1)^2 - 1} = \frac{1}{4n(n + 1)}$. So step 11 gives
$$0 < d_n - d_{n+1} \le \frac{1}{12 n (n + 1)} = \frac{1}{12} \Big( \frac{1}{n} - \frac{1}{n + 1} \Big).$$
13. By step 12, $(d_n)$ is [[decreasing|0KN22AAW5R]].
14. Let $e_n = d_n - \frac{1}{12 n}$. By step 12, $e_n - e_{n+1} = (d_n - d_{n+1}) - \frac{1}{12}(\frac{1}{n} - \frac{1}{n+1}) \le 0$. So $(e_n)$ is increasing.
15. Since $\ln 1 = 0$, we get $d_1 = 1$. By step 14, $d_n \ge e_n \ge e_1 = \frac{11}{12}$ for all $n$.
16. The sequence $(-d_n)$ is increasing and bounded above by $-\frac{11}{12}$. By the [[monotone convergence theorem|0FM6N4R0VB]], it converges. So $d_n \to C$ for some real number $C$.

*Part 2: the limit is $\ln \sqrt{2\pi}$.*

17. For $n \ge 1$, let $a_n = \frac{n! \, e^n}{n^n \sqrt{n}}$.
18. By the [[exponential of a sum|0E8HNVBCSP]] and induction on $n$, $e^n = \exp(1)^n = \exp(n)$. So $\ln(e^n) = n$, by the definition of $\ln$.
19. By the [[logarithm of a power|0V948DE5KA]], $\ln(n^n) = n \ln n$ and $2 \ln \sqrt{n} = \ln n$.
20. By steps 18 and 19, and the logarithm of a product and of a quotient, $\ln a_n = \ln(n!) + n - n \ln n - \frac{1}{2} \ln n = d_n$. So $a_n = \exp(d_n)$.
21. The exponential function is differentiable by [[$\exp' = \exp$|0EX9GFJ0B3]]. So it is continuous, since [[differentiable functions are continuous|07ZMX4ANJS]].
22. By step 21 and [[sequential continuity|0PAQM3H57X]], $a_n = \exp(d_n) \to \exp(C)$. Put $\alpha = \exp(C)$. Then $\alpha > 0$, since [[the exponential function is positive|0P9BNBW2W3]].
23. For each $N$, $n \ge N$ implies $2n \ge N$. So also $a_{2n} \to \alpha$.
24. Let $q_n = \frac{a_n^2}{a_{2n}}$. By the limit rules for [[products|0734RSVF2V]] and [[quotients|03S6GWWKEZ]], and $\alpha \ne 0$, we get $q_n \to \frac{\alpha^2}{\alpha} = \alpha$.
25. Substituting the definition of $a_n$ and $a_{2n}$, the factors $e^{2n}$ and $n^{2n}$ cancel. Using $\sqrt{2n} = \sqrt{2} \sqrt{n}$, this gives
$$q_n = \frac{(n!)^2 \, 2^{2n} \sqrt{2}}{(2n)! \, \sqrt{n}}, \qquad q_n^2 = \frac{2 \cdot 2^{4n} (n!)^4}{((2n)!)^2 \, n}.$$
26. Let $P_n = \prod_{k=1}^{n} \frac{4k^2}{4k^2 - 1}$ be the partial products of the Wallis product. The numerators multiply to $\prod_{k=1}^n (2k)^2 = 2^{2n} (n!)^2$.
27. Write $4k^2 - 1 = (2k - 1)(2k + 1)$. Since $(2n)!$ is the product of the even numbers $2k$ and the odd numbers $2k - 1$ for $k \le n$, we get $\prod_{k=1}^{n} (2k - 1) = \frac{(2n)!}{2^n n!}$.
28. Shifting the index, $\prod_{k=1}^{n} (2k + 1) = (2n + 1) \prod_{k=1}^{n} (2k - 1)$. With steps 26 and 27,
$$P_n = \frac{2^{4n} (n!)^4}{(2n + 1) \, ((2n)!)^2}.$$
29. Comparing steps 25 and 28, $q_n^2 = P_n \cdot \frac{2(2n + 1)}{n} = P_n \big( 4 + \frac{2}{n} \big)$.
30. By the [[Wallis product|0XCYA4YERS]], $P_n \to \frac{\pi}{2}$. Since [[$1/n \to 0$|08QAX4H1PF]], the [[sum rule|0RAM4E07NR]] gives $4 + \frac{2}{n} \to 4$. By the product rule, $q_n^2 \to 2\pi$.
31. By step 24 and the product rule, also $q_n^2 \to \alpha^2$. A sequence has at most one limit, so $\alpha^2 = 2\pi$. Since $\alpha > 0$, $\alpha = \sqrt{2\pi}$.

*Part 3: conclusion.*

32. For $n \ge 1$, let $s_n = \sqrt{2\pi n} \, (n/e)^n$ and $\rho_n = \frac{n!}{s_n}$. Then $\rho_n = \frac{n! \, e^n}{\sqrt{2\pi} \sqrt{n} \, n^n} = \frac{a_n}{\sqrt{2\pi}}$.
33. By steps 22 and 31, $\rho_n \to \frac{\alpha}{\sqrt{2\pi}} = 1$. This is the ratio form of the statement.
34. Let $\varepsilon > 0$. By step 33, there is $N$ with $|\rho_n - 1| \le \varepsilon$ for all $n \ge N$. Then $|n! - s_n| = |\rho_n - 1| \, s_n \le \varepsilon s_n$ for $n \ge N$.
35. By the definition of [[little o notation|04TSHB9H8D]], step 34 says $n! - s_n = o(s_n)$. So $n! \sim \sqrt{2\pi n} \, (n/e)^n$, by the definition of [[asymptotic equivalence|00SB5EA3VW]].

## Idea

The quantity $d_n = \ln n! - (n + \frac{1}{2}) \ln n + n$ changes by at most $\frac{1}{12n(n+1)}$ per step, and these changes have a finite total. So $n!$ is asymptotic to $\alpha \sqrt{n} (n/e)^n$ for some constant $\alpha > 0$. Comparing $n!$ with $(2n)!$ turns the constant into the Wallis product, which forces $\alpha = \sqrt{2\pi}$.
