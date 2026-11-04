---
tag: 855HEQHXC5
kind: proof
name: Proof that a monotone function has countably many discontinuities
msc: [26A48]
proves: 0WYTM4C9QG
uses: [0KJXHN0TW0, 0TK8Y3J5RW, 0W8YHHGCJG, 0909PWZR62, 0STX0WRDNG, 0DS9KWFDK2, 0ZG61TFBES, 0PVG1CRAJN, 01FPXMTBX1]
sources:
  - url: https://www.jirka.org/ra/html/sec_monotonefunc.html
    locator: Corollary 3.6.4
---

## Proof

We assign a different rational number to each discontinuity that is not an endpoint of $I$.

1. First let $f$ be increasing: $x \le y$ implies $f(x) \le f(y)$. Let $D$ be the set of points of $I$ where $f$ is not continuous.
2. Call $c \in I$ an inner point if $I$ has a point $p < c$ and a point $q > c$. Then $(p, q) \subseteq I$, since $I$ is an [[interval|0TK8Y3J5RW]].
3. Let $c$ be an inner point. Apply the [[existence of one-sided limits|0KJXHN0TW0]] to $f$ restricted to $(p, q)$. Write $c^-$ and $c^+$ for its left and right limits at $c$.
4. That result gives $c^- = \sup_{p < x < c} f(x) \le f(c) \le \inf_{c < x < q} f(x) = c^+$.
5. Claim: $c^+ \le f(t)$ for each $t \in I$ with $t > c$. Choose $s$ with $c < s < \min(t, q)$. Then $c^+ \le f(s) \le f(t)$ by step 4 and monotonicity.
6. In the same way, $f(t) \le c^-$ for each $t \in I$ with $t < c$.
7. Claim: if $c$ is an inner point in $D$, then $c^- < c^+$. Suppose instead $c^- = c^+$. Then step 4 gives $c^- = f(c) = c^+$.
8. Let $\varepsilon > 0$. By the definition of [[one-sided limits|0909PWZR62]], there are $\delta_1, \delta_2 > 0$ with these properties. We have $\abs{f(x) - f(c)} < \varepsilon$ for $x \in (p, q)$ with $c - \delta_1 < x < c$, and also for $x \in (p, q)$ with $c < x < c + \delta_2$.
9. Let $\delta = \min(\delta_1, \delta_2, c - p, q - c)$. Each $x \in I$ with $\abs{x - c} < \delta$ lies in $(p, q)$, so $\abs{f(x) - f(c)} < \varepsilon$ by step 8.
10. By the [[epsilon-delta form of continuity|0W8YHHGCJG]], $f$ is continuous at $c$. This contradicts $c \in D$, which proves the claim of step 7.
11. Let $D_0$ be the set of inner points in $D$. For $c \in D_0$, the [[density of the rationals|0STX0WRDNG]] gives a rational $r(c)$ with $c^- < r(c) < c^+$.
12. Let $c < e$ be two points of $D_0$. Put $t = \frac{c + e}{2}$, so $t \in I$ and $c < t < e$. Steps 5 and 6 give $c^+ \le f(t) \le e^-$.
13. So $r(c) < c^+ \le e^- < r(e)$. Hence $r \colon D_0 \to \Q$ is [[injective|0PVG1CRAJN]].
14. By [[the rationals are countable|0DS9KWFDK2]], there is a bijection $\N \to \Q$. Its inverse $j \colon \Q \to \N$ is injective. By [[composition of injections|01FPXMTBX1]], $\varphi = j \circ r \colon D_0 \to \N$ is injective.
15. A point of $D$ that is not inner is the least element or the greatest element of $I$. So $D \setminus D_0$ has at most two points.
16. Define $\psi \colon D \to \N$ by $\psi(c) = \varphi(c) + 2$ for $c \in D_0$. Send the least element of $I$ to $0$, if it lies in $D$. Send the greatest element to $1$, if it lies in $D$ and differs from the least.
17. The map $\psi$ is injective, since $\varphi$ is injective and its shifted values are at least $2$. So $D$ is [[countable|0ZG61TFBES]].
18. Now let $f$ be decreasing, and put $g = -f$. Then $g$ is increasing. Also $\abs{g(x) - g(c)} = \abs{f(x) - f(c)}$, so $f$ and $g$ have the same points of continuity.
19. By steps 1 to 17 applied to $g$, the set of discontinuities of $f$ is countable.

## Idea

At each discontinuity inside $I$, an increasing function jumps over an open gap between its left and right limits. Gaps at different points do not overlap, because $f$ increases between them. Picking a rational in each gap gives an injection into $\Q$, and the two endpoints of $I$ add at most two more points.
