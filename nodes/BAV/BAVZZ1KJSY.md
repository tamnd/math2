---
tag: BAVZZ1KJSY
kind: proof
name: Proof of the Weierstrass approximation theorem
msc: [41A10]
proves: 0JQE130DHW
uses: [0NRQPQX3VA, 0ATVXC3NCC, 0W0TZDRF9C, 0A3CK6DVVB, 0C4VWBFY73, 0EHWPWGHB2, 033KTKKRV6, 03HF5PMY5T, 0A74SX55QP]
sources:
  - url: https://en.wikipedia.org/wiki/Bernstein_polynomial
    locator: Approximating continuous functions, Elementary proof
---

## Proof

We move the problem to $[0, 1]$ and show that the Bernstein polynomials of the moved function approximate it uniformly.

*Part 1: reduction to $[0, 1]$.*

1. Let $a < b$, let $f \colon [a, b] \to \R$ be continuous, and let $\varepsilon > 0$. Put $L = b - a > 0$.
2. For $t \in [0, 1]$, let $g(t) = f(a + tL)$. The map $t \mapsto a + tL$ is continuous and sends $[0, 1]$ into $[a, b]$.
3. So $g \colon [0, 1] \to \R$ is continuous, since a [[composition of continuous functions is continuous|0NRQPQX3VA]].
4. By the [[boundedness theorem|0ATVXC3NCC]], there is $M > 0$ with $\abs{g(t)} \le M$ for all $t \in [0, 1]$.
5. Continuous functions on a closed bounded interval are [[uniformly continuous|0W0TZDRF9C]]. By the definition of [[uniform continuity|0A3CK6DVVB]], there is $\delta > 0$ with this property.
$$s, t \in [0, 1], \ \abs{s - t} < \delta \implies \abs{g(s) - g(t)} < \frac{\varepsilon}{2}.$$

*Part 2: three identities.*

6. Fix an integer $n \ge 1$ and $x \in [0, 1]$. For $0 \le k \le n$, let $b_k = \binom{n}{k} x^k (1 - x)^{n-k}$, the [[Bernstein basis polynomials|0C4VWBFY73]] at $x$. Each $b_k \ge 0$.
7. By the [[binomial theorem|0EHWPWGHB2]], $\sum_{k=0}^{n} b_k = (x + (1 - x))^n = 1$.
8. For $1 \le k \le n$, the [[factorial formula|033KTKKRV6]] gives $k \binom{n}{k} = \frac{n!}{(k-1)! \, (n-k)!} = n \binom{n-1}{k-1}$.
9. The term with $k = 0$ vanishes. So by step 8, with $j = k - 1$ and the binomial theorem,
$$\sum_{k=0}^{n} k b_k = n x \sum_{j=0}^{n-1} \binom{n-1}{j} x^j (1 - x)^{n-1-j} = n x.$$
10. Similarly, for $2 \le k \le n$, the factorial formula gives $k (k - 1) \binom{n}{k} = n (n - 1) \binom{n-2}{k-2}$.
11. The terms with $k = 0$ and $k = 1$ vanish. If $n \ge 2$, step 10 and the binomial theorem give $\sum_{k=0}^{n} k (k - 1) b_k = n (n - 1) x^2$.
12. If $n = 1$, both sides of this identity are $0$. So it holds for all $n \ge 1$.
13. Write $(k - nx)^2 = k (k - 1) + k - 2nx \, k + n^2 x^2$. By steps 7, 9 and 11,
$$\sum_{k=0}^{n} (k - nx)^2 b_k = n(n-1) x^2 + nx - 2 n^2 x^2 + n^2 x^2 = n x (1 - x).$$
14. Since $\frac{1}{4} - x + x^2 = (x - \frac{1}{2})^2 \ge 0$, we have $x (1 - x) \le \frac{1}{4}$. Dividing step 13 by $n^2$ gives
$$\sum_{k=0}^{n} \Big( \frac{k}{n} - x \Big)^2 b_k \le \frac{1}{4n}.$$

*Part 3: the estimate.*

15. The [[Bernstein polynomial|0C4VWBFY73]] of $g$ is $B_n(g)(x) = \sum_{k=0}^{n} g(\frac{k}{n}) b_k$. By step 7, $g(x) = \sum_{k=0}^{n} g(x) b_k$.
16. Subtracting, and using the [[triangle inequality|03HF5PMY5T]] with $b_k \ge 0$,
$$\abs{g(x) - B_n(g)(x)} \le \sum_{k=0}^{n} \Big| g(x) - g\Big(\frac{k}{n}\Big) \Big| \, b_k.$$
17. Let $K_1$ be the set of $k$ with $\abs{\frac{k}{n} - x} < \delta$. Let $K_2$ be the set of the remaining $k \in \set{0, \dots, n}$.
18. For $k \in K_1$, step 5 gives $\abs{g(x) - g(\frac{k}{n})} < \frac{\varepsilon}{2}$. So by step 7, the sum over $K_1$ is at most $\frac{\varepsilon}{2} \sum_{k} b_k = \frac{\varepsilon}{2}$.
19. For $k \in K_2$, step 4 gives $\abs{g(x) - g(\frac{k}{n})} \le 2M$. Also $1 \le (\frac{k}{n} - x)^2 / \delta^2$.
20. So by step 14, the sum over $K_2$ is at most
$$\frac{2M}{\delta^2} \sum_{k \in K_2} \Big( \frac{k}{n} - x \Big)^2 b_k \le \frac{2M}{\delta^2} \cdot \frac{1}{4n} = \frac{M}{2 n \delta^2}.$$
21. By the [[Archimedean property|0A74SX55QP]], choose an integer $n \ge 1$ with $n > \frac{M}{\varepsilon \delta^2}$. Then $\frac{M}{2 n \delta^2} < \frac{\varepsilon}{2}$.
22. For this $n$, steps 16 to 21 give $\abs{g(x) - B_n(g)(x)} < \frac{\varepsilon}{2} + \frac{\varepsilon}{2} = \varepsilon$. This holds for every $x \in [0, 1]$, since $n$ does not depend on $x$.

*Part 4: back to $[a, b]$.*

23. Let $q = B_n(g)$, a polynomial in one variable. Define $p(x) = q\big( \frac{x - a}{L} \big)$ for real $x$.
24. Each power $\big( \frac{x - a}{L} \big)^j$ expands into a polynomial in $x$, by the binomial theorem. So $p$ is a polynomial.
25. Let $x \in [a, b]$, and put $t = \frac{x - a}{L}$. Then $t \in [0, 1]$, $a + tL = x$, and so $g(t) = f(x)$.
26. By step 22, $\abs{f(x) - p(x)} = \abs{g(t) - q(t)} < \varepsilon$. This proves the theorem.

## Idea

The Bernstein polynomial $B_n(g)(x)$ is a weighted average of the values $g(k/n)$. The weights $b_k(x)$ concentrate near $k/n = x$, because their variance about $x$ is at most $1/(4n)$. Uniform continuity controls the nearby terms, and the variance bound makes the distant terms small.
