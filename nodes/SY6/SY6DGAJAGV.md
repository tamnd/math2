---
tag: SY6DGAJAGV
kind: proof
name: Proof of the additivity of the integral over intervals
msc: [26A42]
proves: 05RCDKHZM6
uses: [0N1JQXZXHC, 0HBY48G8G1, 0QRQVH0CRW, 09FQT057T7, 069P20KYQT, 0A3GWZ86AY, 0BTMQ04556, 04KFTA34C5, 017DH8WXTE, 021XJAQVDC]
sources:
  - url: https://www.math.ucdavis.edu/~hunter/m125b/ch1.pdf
    locator: Theorem 1.33
---

## Proof

We use Riemann's criterion and split partitions at $c$.
Write $U(g, P)$ and $L(g, P)$ for the upper and lower [[Darboux sums|0QRQVH0CRW]] of a bounded function $g$ for a partition $P$.

1. First a lemma: a function $g$ that is [[Riemann integrable|0N1JQXZXHC]] on an interval $[r, s]$ is bounded there. Let $I$ be its integral. Take $\delta > 0$ such that each tagged partition of mesh less than $\delta$ has [[Riemann sum|0HBY48G8G1]] within $1$ of $I$.
2. By the [[Archimedean property|0A3GWZ86AY]], fix a partition $P = (x_0, \dots, x_n)$ of $[r, s]$ with all subintervals shorter than $\delta$, and fix tags $t$.
3. Fix $i$ and $x \in [x_{i-1}, x_i]$. Let $t'$ be the tags $t$ with $t_i$ replaced by $x$. Both sums are within $1$ of $I$, so $|S(g, P, t') - S(g, P, t)| < 2$.
   This difference is $(g(x) - g(t_i))(x_i - x_{i-1})$. So $|g(x)| < |g(t_i)| + \frac{2}{x_i - x_{i-1}}$.
4. So $g$ is bounded on each of the $n$ subintervals. The largest of these $n$ bounds bounds $g$ on $[r, s]$. This proves the lemma.
5. Now let $a < c < b$ and $f \colon [a, b] \to \mathbb{R}$. For a [[partition|069P20KYQT]] $P_1$ of $[a, c]$ and a partition $P_2$ of $[c, b]$, let $P_1 \oplus P_2$ be the partition of $[a, b]$ with the points of both.
   Its subintervals are those of $P_1$ and those of $P_2$. So $U(f, P_1 \oplus P_2) = U(f, P_1) + U(f, P_2)$, and the same holds for $L$.
6. Each partition of $[a, b]$ that contains $c$ has this form $P_1 \oplus P_2$.
7. Let $P$ be a partition of $[a, b]$ and let $P'$ be $P$ with the point $c$ added. We claim $U(f, P') \le U(f, P)$ and $L(f, P') \ge L(f, P)$.
   If $c$ is a point of $P$, then $P' = P$. Otherwise $c$ lies inside one subinterval $[x_{j-1}, x_j]$. Its term $M_j (x_j - x_{j-1})$ is replaced by $M' (c - x_{j-1}) + M'' (x_j - c)$.
8. Here $M'$ and $M''$ are [[suprema|0BTMQ04556]] over subsets of $[x_{j-1}, x_j]$, so $M', M'' \le M_j$. This gives $U(f, P') \le U(f, P)$. The same argument with [[infima|04KFTA34C5]] gives $L(f, P') \ge L(f, P)$.
9. Assume that $f$ is integrable on $[a, b]$. By the lemma, $f$ is bounded. Let $\varepsilon > 0$. By [[Riemann's criterion|017DH8WXTE]], there is $P$ with $U(f, P) - L(f, P) < \varepsilon$.
10. Write $P' = P_1 \oplus P_2$ as in steps 6 and 7. Since $U(f, P_2) \ge L(f, P_2)$, steps 5 and 8 give
    $$U(f, P_1) - L(f, P_1) \le U(f, P') - L(f, P') \le U(f, P) - L(f, P) < \varepsilon.$$
11. By Riemann's criterion, $f$ is integrable on $[a, c]$. The same argument with $P_1$ and $P_2$ exchanged shows that $f$ is integrable on $[c, b]$.
12. Conversely, assume that $f$ is integrable on $[a, c]$ and on $[c, b]$. By the lemma, $f$ is bounded on each of them, so on $[a, b]$.
13. Let $\varepsilon > 0$. By Riemann's criterion, there are partitions $P_1$ of $[a, c]$ and $P_2$ of $[c, b]$ with $U(f, P_i) - L(f, P_i) < \varepsilon/2$ for $i = 1, 2$.
14. Let $P = P_1 \oplus P_2$. By step 5, $U(f, P) - L(f, P) < \varepsilon$. By Riemann's criterion, $f$ is integrable on $[a, b]$.
15. Now let $f$ be integrable on all three intervals. Let $I$, $I_1$ and $I_2$ be its integrals over $[a, b]$, $[a, c]$ and $[c, b]$.
16. Take a bounded integrable function and any partition $Q$ of its interval. Then $L(Q)$ is at most the lower [[Darboux integral|09FQT057T7]] and $U(Q)$ is at least the upper one.
    Both equal the integral, since [[Darboux and Riemann integrals agree|021XJAQVDC]]. So $L(Q)$ is at most the integral, and $U(Q)$ is at least the integral.
17. Let $\varepsilon > 0$, and take $P_1$, $P_2$ and $P = P_1 \oplus P_2$ as in steps 13 and 14. By step 16 on each piece, $L(f, P_1) + L(f, P_2) \le I_1 + I_2 \le U(f, P_1) + U(f, P_2)$.
18. By step 5, this says $L(f, P) \le I_1 + I_2 \le U(f, P)$. By step 16 on $[a, b]$, also $L(f, P) \le I \le U(f, P)$.
19. So $|I - (I_1 + I_2)| \le U(f, P) - L(f, P) < \varepsilon$. This holds for each $\varepsilon > 0$, so $\int_a^b f(x) \, dx = \int_a^c f(x) \, dx + \int_c^b f(x) \, dx$.

## Idea

Adding the point $c$ to a partition only brings the upper and lower sums closer. A partition containing $c$ is two partitions side by side, and its Darboux sums are the sums of the two pieces. So small gaps on $[a, b]$ give small gaps on both halves, and conversely, and the integrals are trapped in the same small interval.
