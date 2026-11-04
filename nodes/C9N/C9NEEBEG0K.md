---
tag: C9NEEBEG0K
kind: proof
name: Proof of Taylor's theorem with the Cauchy remainder by the mean value theorem
msc: [41A80]
proves: 005Q84BMAD
uses: [0HFSFVMWQB, 0BARQY52N5, 084NGSTWM7, 0HXEX0DPRA, 07ZMX4ANJS, 0V9A43H7WV, 0JZGW75C5Z, 0RXX2PT1MQ]
sources:
  - url: https://en.wikipedia.org/wiki/Taylor%27s_theorem
    locator: Derivation for the mean value forms of the remainder
---

## Proof

We expand $f(x)$ around a moving point $t$ and apply the mean value theorem in $t$.

1. Let $\alpha < \beta$ be the endpoints of $J$, so $\set{\alpha, \beta} = \set{a, x}$. The hypothesis means that $f, f', \dots, f^{(k)}$ exist on $J$, with [[one-sided derivatives|0HXEX0DPRA]] at $\alpha$ and $\beta$.
2. For $t \in J$ define $F(t) = \sum_{j=0}^{k} \dfrac{f^{(j)}(t)}{j!} (x - t)^j$.
3. For $j < k$, $f^{(j)}$ is differentiable on $J$, so it is continuous on $J$. Inside $J$ this is [[differentiability implies continuity|07ZMX4ANJS]].
4. At an endpoint, write $f^{(j)}(s) - f^{(j)}(\alpha) = (s - \alpha) \cdot \dfrac{f^{(j)}(s) - f^{(j)}(\alpha)}{s - \alpha}$. The quotient has a finite limit, so the product tends to $0$. The endpoint $\beta$ is similar.
5. Also $f^{(k)}$ is continuous on $J$ by hypothesis. So $F$ is continuous on $J$, as a sum of products of continuous functions.
6. By the [[power rule|0JZGW75C5Z]] and the [[chain rule|0RXX2PT1MQ]], $\dfrac{d}{dt} \dfrac{(x - t)^j}{j!} = -\dfrac{(x - t)^{j-1}}{(j-1)!}$ for $j \ge 1$.
7. For $0 \le j \le k$ and $t \in (\alpha, \beta)$ let $A_j(t) = \dfrac{f^{(j+1)}(t)}{j!} (x - t)^j$. This uses the hypothesis that [[$f^{(k+1)}$|084NGSTWM7]] exists on $(\alpha, \beta)$.
8. By the [[product rule|0V9A43H7WV]] and step 6, the $j$-th term of $F$ has derivative $A_j - A_{j-1}$ for $j \ge 1$. The term with $j = 0$ is $f$, with derivative $A_0$.
9. Adding, the sum telescopes: $F'(t) = A_0 + \sum_{j=1}^{k} (A_j - A_{j-1}) = A_k = \dfrac{f^{(k+1)}(t)}{k!} (x - t)^k$ on $(\alpha, \beta)$.
10. By the [[mean value theorem|0BARQY52N5]], there is $\xi \in (\alpha, \beta)$ with $F(\beta) - F(\alpha) = F'(\xi)(\beta - \alpha)$.
11. Exchanging $\alpha$ and $\beta$ multiplies both sides by $-1$. So $F(x) - F(a) = F'(\xi)(x - a)$, and $\xi$ lies strictly between $a$ and $x$.
12. At $t = x$, every term of $F$ with $j \ge 1$ vanishes, so $F(x) = f(x)$. At $t = a$, $F(a) = P_k(x)$, the value at $x$ of the [[Taylor polynomial|0HFSFVMWQB]] of $f$ at $a$.
13. Substituting steps 9 and 12 into step 11 gives $f(x) = P_k(x) + \dfrac{f^{(k+1)}(\xi)}{k!} (x - \xi)^k (x - a)$.

## Idea

The function $F(t)$ is the Taylor polynomial of degree $k$ at $t$, evaluated at $x$. It moves from $P_k(x)$ at $t = a$ to $f(x)$ at $t = x$, and its derivative telescopes to a single term. The plain mean value theorem applied to $F$ then gives the Cauchy form directly.
