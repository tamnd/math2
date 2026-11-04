---
tag: QBE5S7KN2B
kind: proof
name: Proof that harmonic numbers grow like log n
msc: [11B83, 26A12]
proves: 05S2GSPMGA
uses: [0D2Y6G4C4S, 0044CPHJBV, 0K1N1Y4EGZ, 0J7PHRBNNS, 0GR2APWTAC, 06SESV7GQY, 0Q3HYFT9RQ, 080RWVVSB6, 0MBWQKM8QR, 0KN22AAW5R, 0FM6N4R0VB, 0N32V0E3XJ, 0A74SX55QP, 0KN2V7840E, 04TSHB9H8D, 00SB5EA3VW]
sources:
  - url: https://en.wikipedia.org/wiki/Euler%27s_constant
    locator: Introduction
---

## Proof

We compare each term $\frac{1}{k}$ with the integral of $\frac{1}{t}$ over $[k, k + 1]$, and use the monotone convergence theorem.

1. For each integer $n \ge 1$, let $H_n$ be the $n$-th [[harmonic number|0D2Y6G4C4S]], and let $a_n = H_n - \ln n$. Here $\ln$ is the [[natural logarithm|0044CPHJBV]].
2. Let $k \ge 1$ be an integer. By the [[integral of 1/x|0K1N1Y4EGZ]] and the [[logarithm of a quotient|0J7PHRBNNS]], $\int_k^{k+1} \frac{dt}{t} = \ln \frac{k+1}{k} = \ln(k + 1) - \ln k$.
3. The function $t \mapsto \frac{1}{t}$ is continuous on $[k, k + 1]$, by [[continuity of quotients|0GR2APWTAC]]. So it is Riemann integrable there, since [[continuous functions are Riemann integrable|06SESV7GQY]].
4. For a constant $c$, the [[integral of a power|0Q3HYFT9RQ]] with exponent $0$ and [[linearity of the integral|080RWVVSB6]] give $\int_k^{k+1} c \, dt = c$.
5. For $t \in [k, k + 1]$, we have $\frac{1}{k + 1} \le \frac{1}{t} \le \frac{1}{k}$.
6. By [[monotonicity of the integral|0MBWQKM8QR]] and steps 2 to 5,
$$\frac{1}{k + 1} \le \ln(k + 1) - \ln k \le \frac{1}{k}.$$
7. For $n \ge 1$, $a_{n+1} - a_n = \frac{1}{n + 1} - (\ln(n + 1) - \ln n)$. This is $\le 0$ by the left inequality of step 6 with $k = n$. So $(a_n)$ is [[decreasing|0KN22AAW5R]].
8. Since $e^0 = 1$, the definition of $\ln$ gives $\ln 1 = 0$.
9. Summing the right inequality of step 6 over $k = 1, \dots, n$ gives a telescoping sum: $\ln(n + 1) - \ln 1 \le H_n$. By step 8, $\ln(n + 1) \le H_n$.
10. By step 9 and step 6 with $k = n$, $a_n \ge \ln(n + 1) - \ln n \ge \frac{1}{n + 1} > 0$. So $(a_n)$ is bounded below by $0$.
11. The sequence $(-a_n)$ is increasing by step 7, and bounded above by $0$ by step 10.
12. By the [[monotone convergence theorem|0FM6N4R0VB]], $(-a_n)$ converges. So $(a_n)$ converges to some real number $\gamma$.
13. By step 8, $a_1 = 1 - \ln 1 = 1$. By steps 7 and 10, $0 \le a_n \le 1$ for all $n \ge 1$.
14. Since [[limits preserve non-strict inequalities|0N32V0E3XJ]], step 13 gives $0 \le \gamma \le 1$. So the limit exists and lies in $[0, 1]$.
15. It remains to show $H_n \sim \ln n$. Let $\varepsilon > 0$. By the [[Archimedean property|0A74SX55QP]], there is an integer $N \ge 2$ with $N > e^{1/\varepsilon}$.
16. Let $n \ge N$. Suppose that $\ln n < \frac{1}{\varepsilon}$. Since the [[exponential function is strictly increasing|0KN2V7840E]], $n = e^{\ln n} < e^{1/\varepsilon} < N$. This contradicts $n \ge N$.
17. So $\ln n \ge \frac{1}{\varepsilon} > 0$ for all $n \ge N$. With step 13, $|H_n - \ln n| = a_n \le 1 \le \varepsilon \ln n$ for all $n \ge N$.
18. By the definition of [[little o notation|04TSHB9H8D]], step 17 says $H_n - \ln n = o(\ln n)$. This is the definition of [[asymptotic equivalence|00SB5EA3VW]], so $H_n \sim \ln n$.

## Idea

The integral $\int_k^{k+1} \frac{dt}{t}$ lies between $\frac{1}{k+1}$ and $\frac{1}{k}$. So the gap $H_n - \ln n$ loses a little at each step, but it never drops below $0$. A decreasing sequence that is bounded below converges. Since the gap stays bounded while $\ln n \to \infty$, the two sequences are asymptotically equal.
