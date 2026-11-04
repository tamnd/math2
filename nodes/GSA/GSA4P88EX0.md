---
tag: GSA4P88EX0
kind: proof
name: Proof of Taylor's theorem with the integral remainder by the fundamental theorem of calculus
msc: [41A80]
proves: 0WJGR81HBD
uses: [0HFSFVMWQB, 0NHGY0N0JB, 0QM4TXT3DR, 084NGSTWM7, 0HXEX0DPRA, 07ZMX4ANJS, 0V9A43H7WV, 0JZGW75C5Z, 0RXX2PT1MQ]
sources:
  - url: https://en.wikipedia.org/wiki/Taylor%27s_theorem
    locator: Derivation for the integral form of the remainder
---

## Proof

We expand $f(x)$ around a moving point $t$, differentiate in $t$, and integrate back with the fundamental theorem of calculus. The source uses repeated integration by parts; this route packs those steps into one telescoping sum.

1. Let $\alpha < \beta$ be the endpoints of $J$, so $\set{\alpha, \beta} = \set{a, x}$. The hypothesis means that $f, f', \dots, f^{(k+1)}$ exist on $J$, with [[one-sided derivatives|0HXEX0DPRA]] at $\alpha$ and $\beta$.
2. For $t \in J$ define $F(t) = \sum_{j=0}^{k} \dfrac{f^{(j)}(t)}{j!} (x - t)^j$.
3. For $j \le k$, $f^{(j)}$ is differentiable on $J$, so it is continuous on $J$. Inside $J$ this is [[differentiability implies continuity|07ZMX4ANJS]].
4. At an endpoint, write $f^{(j)}(s) - f^{(j)}(\alpha) = (s - \alpha) \cdot \dfrac{f^{(j)}(s) - f^{(j)}(\alpha)}{s - \alpha}$. The quotient has a finite limit, so the product tends to $0$. The endpoint $\beta$ is similar.
5. So $F$ is continuous on $J$, as a sum of products of continuous functions.
6. By the [[power rule|0JZGW75C5Z]] and the [[chain rule|0RXX2PT1MQ]], $\dfrac{d}{dt} \dfrac{(x - t)^j}{j!} = -\dfrac{(x - t)^{j-1}}{(j-1)!}$ for $j \ge 1$.
7. For $0 \le j \le k$ and $t \in J$ let $A_j(t) = \dfrac{f^{(j+1)}(t)}{j!} (x - t)^j$. Here [[$f^{(j+1)}$|084NGSTWM7]] exists on $J$ by step 1.
8. By the [[product rule|0V9A43H7WV]] and step 6, the $j$-th term of $F$ has derivative $A_j - A_{j-1}$ on $(\alpha, \beta)$ for $j \ge 1$. The term with $j = 0$ is $f$, with derivative $A_0$.
9. Adding, the sum telescopes: $F'(t) = A_0 + \sum_{j=1}^{k} (A_j - A_{j-1}) = A_k(t)$ on $(\alpha, \beta)$.
10. The function $A_k(t) = \dfrac{f^{(k+1)}(t)}{k!} (x - t)^k$ is continuous on $J$, since $f^{(k+1)}$ is continuous on $J$ by hypothesis.
11. By the [[fundamental theorem of calculus|0NHGY0N0JB]] with steps 5, 9 and 10, $\int_\alpha^\beta A_k(t) \, dt = F(\beta) - F(\alpha)$.
12. For $x < a$ the [[integral|0QM4TXT3DR]] $\int_a^x$ means $-\int_x^a$. With this convention, step 11 gives $\int_a^x A_k(t) \, dt = F(x) - F(a)$ in both cases.
13. At $t = x$, every term of $F$ with $j \ge 1$ vanishes, so $F(x) = f(x)$. At $t = a$, $F(a) = P_k(x)$, the value at $x$ of the [[Taylor polynomial|0HFSFVMWQB]] of $f$ at $a$.
14. So $f(x) - P_k(x) = \int_a^x \dfrac{f^{(k+1)}(t)}{k!} (x - t)^k \, dt$, which is the claim.

## Idea

The function $F(t)$ is the Taylor polynomial of degree $k$ at $t$, evaluated at $x$. It equals $P_k(x)$ at $t = a$ and $f(x)$ at $t = x$. Its derivative telescopes to the integrand of the remainder, so the remainder is the integral of $F'$ from $a$ to $x$.
