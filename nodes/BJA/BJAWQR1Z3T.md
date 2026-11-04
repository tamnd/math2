---
tag: BJAWQR1Z3T
kind: proof
name: Proof that uniform limits commute with integration
msc: [40A30, 26A42]
proves: 0BWGW68B66
uses: [08FPABDQ4C, 0N1JQXZXHC, 0QM4TXT3DR, 0HBY48G8G1, 069P20KYQT, 04GM4NYXJB, 0QRQVH0CRW, 0BTMQ04556, 04KFTA34C5, 017DH8WXTE, 080RWVVSB6, 0Q3HYFT9RQ, 0NR82KMYKD, 0MBWQKM8QR]
sources:
  - url: https://www.jirka.org/ra/html/sec_liminter.html
    locator: Theorem 6.2.4
---

## Proof

We prove integrability of $f$ with Riemann's criterion, and then estimate the difference of the integrals.

*Step A: integrable functions and $f$ are bounded.*

1. Let $a < b$, let each $f_n \colon [a, b] \to \R$ be [[Riemann integrable|0N1JQXZXHC]], and let $f_n \to f$ [[uniformly|08FPABDQ4C]] on $[a, b]$.
2. First let $g \colon [a, b] \to \R$ be any Riemann integrable function with integral $I$. Take $\varepsilon = 1$ in the definition, and let $\delta > 0$ be the corresponding number.
3. Fix a [[partition|069P20KYQT]] $P = (x_0, \dots, x_m)$ of $[a, b]$ into equal pieces, with [[mesh|04GM4NYXJB]] less than $\delta$.
4. Suppose that $g$ is unbounded on $[a, b]$. Then $g$ is unbounded on some piece $[x_{j-1}, x_j]$, since a finite union of bounded sets is bounded.
5. Fix tags $t_i \in [x_{i-1}, x_i]$ for $i \ne j$, and let $A = \sum_{i \ne j} g(t_i)(x_i - x_{i-1})$. For each $t \in [x_{j-1}, x_j]$, the [[Riemann sum|0HBY48G8G1]] with tag $t$ on the $j$-th piece is $A + g(t)(x_j - x_{j-1})$.
6. By step 2, this sum lies within $1$ of $I$. So $|g(t)| \le \frac{|I| + 1 + |A|}{x_j - x_{j-1}}$ for all $t \in [x_{j-1}, x_j]$. This contradicts step 4, so $g$ is bounded.
7. By uniform convergence, there is $N_1$ with $|f_{N_1}(x) - f(x)| < 1$ for all $x \in [a, b]$. By step 6, there is $K$ with $|f_{N_1}| \le K$. So $|f| \le K + 1$, and $f$ is bounded.

*Step B: $f$ is integrable.*

8. Let $\varepsilon > 0$, and put $\eta = \frac{\varepsilon}{4(b - a)}$. By uniform convergence, there is $N$ with $|f_n(x) - f(x)| < \eta$ for all $n \ge N$ and all $x \in [a, b]$.
9. The function $f_N$ is integrable and bounded. By [[Riemann's criterion|017DH8WXTE]], there is a partition $P = (x_0, \dots, x_m)$ with $U(f_N, P) - L(f_N, P) < \frac{\varepsilon}{2}$. Here $U$ and $L$ are the [[upper and lower Darboux sums|0QRQVH0CRW]].
10. Fix $i$, and let $J = [x_{i-1}, x_i]$. For $x \in J$, step 8 gives $f(x) < f_N(x) + \eta \le \sup f_N(J) + \eta$. So $\sup f(J) \le \sup f_N(J) + \eta$, by the definition of the [[supremum|0BTMQ04556]].
11. In the same way, $f(x) > f_N(x) - \eta \ge \inf f_N(J) - \eta$ for $x \in J$. So $\inf f(J) \ge \inf f_N(J) - \eta$, by the definition of the [[infimum|04KFTA34C5]].
12. Multiply steps 10 and 11 by $x_i - x_{i-1}$ and sum over $i$. Since the lengths add up to $b - a$,
$$U(f, P) - L(f, P) \le U(f_N, P) - L(f_N, P) + 2 \eta (b - a) < \frac{\varepsilon}{2} + \frac{\varepsilon}{2} = \varepsilon.$$
13. Since $\varepsilon > 0$ was arbitrary and $f$ is bounded by step 7, Riemann's criterion shows that $f$ is Riemann integrable on $[a, b]$.

*Step C: the integrals converge.*

14. Let $\varepsilon > 0$, put $\eta = \frac{\varepsilon}{2(b - a)}$, and let $N$ be as in step 8 for this $\eta$. Fix $n \ge N$.
15. By step 13 and [[linearity of the integral|080RWVVSB6]], $f_n - f$ is integrable, and $\int_a^b f_n - \int_a^b f = \int_a^b (f_n - f)$.
16. By the [[triangle inequality for integrals|0NR82KMYKD]], $|f_n - f|$ is integrable and $\big| \int_a^b (f_n - f) \big| \le \int_a^b |f_n - f|$.
17. The constant function $\eta$ has integral $\eta (b - a)$, by the [[integral of a power|0Q3HYFT9RQ]] with exponent $0$ and linearity. Since $|f_n - f| \le \eta$, [[monotonicity of the integral|0MBWQKM8QR]] gives $\int_a^b |f_n - f| \le \eta (b - a) = \frac{\varepsilon}{2}$.
18. By steps 15 to 17, $\big| \int_a^b f_n - \int_a^b f \big| \le \frac{\varepsilon}{2} < \varepsilon$ for all $n \ge N$.
19. So $\lim_{n \to \infty} \int_a^b f_n(x) \, dx = \int_a^b f(x) \, dx$, where the right side is the [[Riemann integral|0QM4TXT3DR]] of $f$.

## Idea

Uniform convergence traps the graph of $f$ in a thin band of width $2\eta$ around the graph of $f_N$. The upper and lower sums of $f$ can then differ by at most $2\eta(b - a)$ more than those of $f_N$. The same band bounds the difference of the integrals by $\eta(b - a)$.
