---
tag: NK8394NHRC
kind: proof
name: Proof of Lebesgue's criterion for Riemann integrability
msc: [26A42]
proves: 0565EGK6XP
uses: [0N1JQXZXHC, 017DH8WXTE, 0QRQVH0CRW, 069P20KYQT, 0EEE2CZB2A, 0W8YHHGCJG, 0BTMQ04556, 04KFTA34C5, 0A3GWZ86AY, 07PFYV65MB, 0P6PMJB4MA, 0G5AV9Q4RR, 0Z8FM54P86, 5XW4N8KY3Y]
sources:
  - url: https://en.wikipedia.org/wiki/Riemann_integral
    locator: Integrability
---

## Proof

We use the oscillation of $f$ and Riemann's criterion, and compactness for the converse.
Let $a < b$ and let $f \colon [a, b] \to \mathbb{R}$ be bounded. Fix $K > 0$ with $|f(x)| \le K$ for all $x \in [a, b]$.
A set $E \subseteq \mathbb{R}$ has measure zero if for each $\varepsilon > 0$ it is covered by countably many open intervals of total length less than $\varepsilon$.
Write $U(P)$ and $L(P)$ for the upper and lower [[Darboux sums|0QRQVH0CRW]] of $f$ for a [[partition|069P20KYQT]] $P$, with $M_i$ and $m_i$ as in their definition.

1. For a nonempty set $A \subseteq [a, b]$, let $\omega(A) = \sup f(A) - \inf f(A)$, using the [[supremum|0BTMQ04556]] and the [[infimum|04KFTA34C5]]. If $A \subseteq B$, then $\omega(A) \le \omega(B)$.
   For $x, y \in A$ we have $|f(x) - f(y)| \le \omega(A)$.
2. For $x \in [a, b]$ and $r > 0$, let $A_r(x) = (x - r, x + r) \cap [a, b]$. The [[oscillation|5XW4N8KY3Y]] of $f$ at $x$ is $\omega(x) = \inf_{r > 0} \omega(A_r(x)) \ge 0$.
3. We claim that $f$ is [[continuous at|0EEE2CZB2A]] $x$ if and only if $\omega(x) = 0$. Suppose first that $f$ is continuous at $x$, and let $\varepsilon > 0$.
   By the [[epsilon-delta form of continuity|0W8YHHGCJG]], there is $r > 0$ with $|f(y) - f(x)| < \varepsilon / 2$ for $y \in A_r(x)$. So $f(A_r(x)) \subseteq [f(x) - \varepsilon/2, f(x) + \varepsilon/2]$ and $\omega(x) \le \omega(A_r(x)) \le \varepsilon$. Hence $\omega(x) = 0$.
4. Conversely, let $\omega(x) = 0$ and $\varepsilon > 0$. There is $r > 0$ with $\omega(A_r(x)) < \varepsilon$. By step 1, $|f(y) - f(x)| < \varepsilon$ for all $y \in A_r(x)$. So $f$ is continuous at $x$.
5. For $\alpha > 0$, let $D_\alpha = \{x \in [a, b] : \omega(x) \ge \alpha\}$, and let $D$ be the set of points where $f$ is not continuous.
   By steps 3 and 4 and the [[Archimedean property|0A3GWZ86AY]], $x \in D$ if and only if $\omega(x) \ge 1/k$ for some integer $k \ge 1$. So $D = \bigcup_{k \ge 1} D_{1/k}$, and $D_\alpha \subseteq D$ for each $\alpha > 0$.
6. We claim that $D_\alpha$ is [[closed|0G5AV9Q4RR]]. Let $x \in [a, b] \setminus D_\alpha$. Then there is $r > 0$ with $\omega(A_r(x)) < \alpha$.
   For $y \in A_r(x)$, let $s = r - |y - x| > 0$. Then $A_s(y) \subseteq A_r(x)$, so $\omega(y) \le \omega(A_s(y)) \le \omega(A_r(x)) < \alpha$. Thus $(x - r, x + r)$ does not meet $D_\alpha$.
7. Each point outside $[a, b]$ also has an open interval around it that misses $[a, b] \supseteq D_\alpha$. So the complement of $D_\alpha$ in $\mathbb{R}$ is open, and $D_\alpha$ is closed. It is bounded, so it is compact by the [[Heine–Borel theorem|07PFYV65MB]].

First assume that $f$ is [[Riemann integrable|0N1JQXZXHC]].

8. Fix an integer $k \ge 1$ and let $\varepsilon > 0$. By [[Riemann's criterion|017DH8WXTE]], there is a partition $P = (x_0, \dots, x_n)$ with $U(P) - L(P) < \frac{\varepsilon}{2k}$.
9. Let $B$ be the set of indices $i$ such that the open interval $(x_{i-1}, x_i)$ contains a point $y$ of $D_{1/k}$. For such $i$ and $y$, some $A_r(y)$ lies in $[x_{i-1}, x_i]$.
   So $M_i - m_i = \omega([x_{i-1}, x_i]) \ge \omega(A_r(y)) \ge \omega(y) \ge 1/k$.
10. Every term $(M_i - m_i)(x_i - x_{i-1})$ of $U(P) - L(P)$ is at least $0$. So step 9 gives $\frac{1}{k} \sum_{i \in B} (x_i - x_{i-1}) \le U(P) - L(P) < \frac{\varepsilon}{2k}$. Hence $\sum_{i \in B} (x_i - x_{i-1}) < \frac{\varepsilon}{2}$.
11. Each point of $D_{1/k}$ lies in some $(x_{i-1}, x_i)$ with $i \in B$, or is a point $x_j$ of $P$. Let $\eta = \frac{\varepsilon}{4(n + 1)}$.
    The intervals $(x_{i-1}, x_i)$ for $i \in B$ and $(x_j - \eta, x_j + \eta)$ for $j = 0, \dots, n$ cover $D_{1/k}$. Their total length is less than $\frac{\varepsilon}{2} + 2(n + 1)\eta = \varepsilon$. So $D_{1/k}$ has measure zero.
12. Now let $\varepsilon > 0$. For each $k \ge 1$, step 11 gives countably many open intervals that cover $D_{1/k}$ with total length less than $\varepsilon / 2^{k + 1}$.
13. Together these intervals cover $D$ by step 5. They form a countable family, since a [[countable union of countable sets is countable|0Z8FM54P86]].
14. Any finitely many of them lie in the families for $k \le N$, for some $N$. So their total length is less than $\sum_{k = 1}^{N} \varepsilon / 2^{k + 1} < \varepsilon / 2$.
    Hence the total length of the whole family is at most $\varepsilon / 2 < \varepsilon$. So $D$ has measure zero.

Now assume that $D$ has measure zero.

15. Let $\varepsilon > 0$, and let $\alpha = \frac{\varepsilon}{4(b - a)}$. By step 5, $D_\alpha \subseteq D$. So countably many open intervals of total length less than $\frac{\varepsilon}{4K}$ cover $D_\alpha$.
16. By step 7 and [[compactness via open covers|0P6PMJB4MA]], finitely many of them, say $G_1, \dots, G_N$, already cover $D_\alpha$. Their total length is still less than $\frac{\varepsilon}{4K}$. If $D_\alpha$ is empty, take $N = 0$.
17. Let $z \in [a, b]$ lie in none of the $G_j$. Then $z \notin D_\alpha$, so $\omega(z) < \alpha$. Choose $r_z > 0$ with $\omega(A_{r_z}(z)) < \alpha$, and let $H_z = (z - r_z / 2, z + r_z / 2)$.
18. The open intervals $G_1, \dots, G_N$ and $H_z$ cover $[a, b]$. By the Heine–Borel theorem $[a, b]$ is compact, so finitely many $H_{z_1}, \dots, H_{z_m}$ together with $G_1, \dots, G_N$ cover $[a, b]$.
19. Let $P = (x_0, \dots, x_n)$ be the partition whose points are $a$, $b$ and all endpoints of these $N + m$ intervals that lie in $(a, b)$.
20. Fix $i$, and let $c$ be the midpoint of $[x_{i-1}, x_i]$. Choose an interval $V$ of the finite cover that contains $c$, and take $V = G_j$ for some $j$ when this is possible.
21. We claim $(x_{i-1}, x_i) \subseteq V$. Suppose that $y \in (x_{i-1}, x_i)$ is not in $V$. Since $V$ is an interval containing $c$, one endpoint of $V$ lies between $c$ and $y$.
    That endpoint lies in $(x_{i-1}, x_i)$, so it is a point of $P$ strictly inside a subinterval of $P$. This is impossible. So $[x_{i-1}, x_i]$ lies in the closure of $V$.
22. Call $i$ of type 1 if $V = G_j$, and of type 2 if $V = H_z$. For type 2, $[x_{i-1}, x_i] \subseteq [z - r_z/2, z + r_z/2] \cap [a, b] \subseteq A_{r_z}(z)$. So $M_i - m_i \le \omega(A_{r_z}(z)) < \alpha$ by step 1.
23. For type 1, $M_i - m_i \le 2K$. The type 1 subintervals with $V = G_j$ do not overlap and lie in the closure of $G_j$. So their total length is at most the length of $G_j$.
24. Adding over $j$, the type 1 subintervals have total length less than $\frac{\varepsilon}{4K}$. The type 2 subintervals have total length at most $b - a$.
25. Hence
    $$U(P) - L(P) = \sum_{i = 1}^{n} (M_i - m_i)(x_i - x_{i-1}) \le 2K \cdot \frac{\varepsilon}{4K} + \alpha (b - a) = \frac{3 \varepsilon}{4} < \varepsilon.$$
26. Such a partition exists for each $\varepsilon > 0$. By [[Riemann's criterion|017DH8WXTE]], $f$ is Riemann integrable on $[a, b]$.

Steps 14 and 26 prove both directions.

## Idea

The oscillation $\omega(x)$ measures how much $f$ jumps near $x$, and $f$ is discontinuous exactly where it is positive. If $f$ is integrable, the subintervals where $f$ jumps by at least $1/k$ must have small total length, so each set $D_{1/k}$ is small. Conversely, the points with large oscillation form a compact set, so finitely many short intervals cover them. Elsewhere $f$ varies little, and the upper and lower sums come close together.
