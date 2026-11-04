---
tag: N698HXMWTV
kind: proof
name: Proof of integration by substitution
msc: [26A42]
proves: 0D37QFPEZE
uses: [06SKCHDQT5, 0HXEX0DPRA, 07ZMX4ANJS, 0WS1A8E2P9, 0C9S13WKMF, 0QNVQ4VD9T, 0K1EWAR6AF, 0NRQPQX3VA, 0VGMHCF4SC, 0NC2A3HWGT, 0RXX2PT1MQ, 06SESV7GQY, 0XYAFCN0PT, 021WEM680W, 0HBY48G8G1]
sources:
  - url: https://www.math.ucdavis.edu/~hunter/m125b/ch1.pdf
    locator: Theorem 1.55
---

## Proof

We find an antiderivative $F$ of $f$ and apply the second fundamental theorem to $F \circ g$.

1. Let $a < b$. We read [[continuously differentiable|06SKCHDQT5]] on the closed interval $[a, b]$ in the usual way.
   So $g$ is differentiable on $(a, b)$, has [[one-sided derivatives|0HXEX0DPRA]] at $a$ and $b$, and $g'$ is continuous on $[a, b]$.
2. The function $g$ is continuous on $[a, b]$. Inside, [[differentiable functions are continuous|07ZMX4ANJS]]. At $a$, $g(a + h) - g(a) = h \cdot \frac{g(a + h) - g(a)}{h}$ tends to $0 \cdot g'(a) = 0$ as $h \to 0^+$, and $b$ is the same.
3. By the [[extreme value theorem|0WS1A8E2P9]], $g$ has a minimum $m$ and a maximum $M$ on $[a, b]$. Let $J$ be the interval on which $f$ is continuous. It contains $m$ and $M$, so it contains $[m, M] \supseteq g([a, b])$.
4. Let $k(u) = \min(\max(u, m), M)$ for $u \in \mathbb{R}$. Then $k(u) \in [m, M]$, and $k(u) = u$ for $u \in [m, M]$.
5. We have $\max(u, m) = \frac{u + m + |u - m|}{2}$. With the [[reverse triangle inequality|0C9S13WKMF]], $|\max(u, m) - \max(v, m)| \le |u - v|$. In the same way $|\min(u, M) - \min(v, M)| \le |u - v|$.
   So $|k(u) - k(v)| \le |u - v|$, and $k$ is [[Lipschitz|0QNVQ4VD9T]]. Hence [[$k$ is continuous|0K1EWAR6AF]].
6. Let $\tilde f = f \circ k$ on $\mathbb{R}$. It is continuous, as a [[composition of continuous functions|0NRQPQX3VA]], and $\tilde f = f$ on $[m, M]$.
7. Let $F(y) = \int_0^y \tilde f(s) \, ds$ for $y \in \mathbb{R}$. By the theorem that [[the integral of a continuous function is an antiderivative|0NC2A3HWGT]], $F$ is differentiable on $\mathbb{R}$ with $F' = \tilde f$.
8. Let $H = F \circ g$ on $[a, b]$. It is continuous by steps 2 and 7, since differentiable functions are continuous and compositions of continuous functions are continuous.
9. For $x \in (a, b)$, the [[chain rule|0RXX2PT1MQ]] gives $H'(x) = F'(g(x)) g'(x) = \tilde f(g(x)) g'(x) = f(g(x)) g'(x)$, since $g(x) \in [m, M]$.
10. The function $x \mapsto f(g(x)) g'(x) = \tilde f(g(x)) g'(x)$ is continuous on $[a, b]$, by [[products of continuous functions|0VGMHCF4SC]]. So it is [[Riemann integrable|06SESV7GQY]], and it extends $H'$.
11. By the [[second fundamental theorem of calculus|0XYAFCN0PT]], $\int_a^b f(g(x)) g'(x) \, dx = H(b) - H(a) = F(g(b)) - F(g(a))$.
12. Let $\alpha = g(a)$ and $\beta = g(b)$. Both lie in $[m, M]$, so $f = \tilde f$ on the closed interval between them. Their [[Riemann sums|0HBY48G8G1]] there agree, so their integrals agree.
13. If $\alpha < \beta$, apply the second fundamental theorem to $F$ on $[\alpha, \beta]$. $F$ is continuous and differentiable with $F' = \tilde f$, and $\tilde f$ is continuous, hence integrable. So $\int_\alpha^\beta f(u) \, du = F(\beta) - F(\alpha)$.
14. If $\alpha > \beta$, the same argument on $[\beta, \alpha]$ and the sign convention for the [[definite integral|021WEM680W]] give $\int_\alpha^\beta f(u) \, du = -(F(\alpha) - F(\beta)) = F(\beta) - F(\alpha)$.
    If $\alpha = \beta$, both sides are $0$.
15. By steps 11 to 14, $\int_a^b f(g(x)) \, g'(x) \, dx = F(g(b)) - F(g(a)) = \int_{g(a)}^{g(b)} f(u) \, du$.

## Idea

If $F$ is an antiderivative of $f$, the chain rule makes $F \circ g$ an antiderivative of $(f \circ g) \, g'$. So both integrals equal $F(g(b)) - F(g(a))$. The extension $\tilde f$ only makes sure that $F$ is defined and differentiable on an open set around all values of $g$.
