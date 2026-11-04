---
tag: RCHY4KH8QD
kind: proof
name: Proof of L'Hôpital's rule from the Cauchy mean value theorem
msc: [26A24]
proves: 0JWT4PPQ7B
uses: [02SYZAWM2K, 0BARQY52N5, 0TXTSEMHR5, 07ZMX4ANJS, 0EEE2CZB2A, 0TK8Y3J5RW]
sources:
  - url: https://en.wikipedia.org/wiki/L%27H%C3%B4pital%27s_rule
    locator: General proof
---

## Proof

We extend $f$ and $g$ by $0$ at $c$ and compare $f(x)/g(x)$ with a quotient of derivatives through the Cauchy mean value theorem. Here $L$ is a real number.

1. Define $F, G \colon I \to \R$ by $F(x) = f(x)$ and $G(x) = g(x)$ for $x \ne c$, and $F(c) = G(c) = 0$.
2. For $x \ne c$, the functions $F$ and $G$ agree with $f$ and $g$ near $x$. So they are differentiable at $x$, and hence [[continuous|07ZMX4ANJS]] there.
3. At $c$, we have $F(x) \to 0 = F(c)$ and $G(x) \to 0 = G(c)$ as $x \to c$. So $F$ and $G$ are [[continuous at|0EEE2CZB2A]] $c$.
4. Fix $x \in I$ with $x \ne c$. Let $J$ be the closed interval with endpoints $c$ and $x$. Since $I$ is an [[interval|0TK8Y3J5RW]], $J \subseteq I$.
5. On $J$, $F$ and $G$ are continuous. On the interior of $J$, they are differentiable with derivatives $f'$ and $g'$.
6. By the [[mean value theorem|0BARQY52N5]] on $J$, there is $s$ strictly between $c$ and $x$ with $G(x) - G(c) = g'(s)(x - c)$. This form holds whichever endpoint is smaller.
7. So $g(x) = g'(s)(x - c)$. Both factors are nonzero, so $g(x) \ne 0$.
8. Let $\alpha < \beta$ be the endpoints of $J$. The [[Cauchy mean value theorem|02SYZAWM2K]] gives $t$ strictly between them with $(F(\beta) - F(\alpha)) G'(t) = (G(\beta) - G(\alpha)) F'(t)$.
9. Swapping $\alpha$ and $\beta$ multiplies both sides by $-1$. So $(F(x) - F(c)) g'(t) = (G(x) - G(c)) f'(t)$, that is, $f(x) g'(t) = g(x) f'(t)$.
10. Dividing by $g(x) g'(t) \ne 0$ gives $\dfrac{f(x)}{g(x)} = \dfrac{f'(t)}{g'(t)}$, where $t$ lies strictly between $c$ and $x$.
11. Now let $V$ be an open interval containing $L$. By the definition of the [[limit|0TXTSEMHR5]], there is an open interval $U$ containing $c$ with $f'(t)/g'(t) \in V$ for all $t \in U \cap I$ with $t \ne c$.
12. The set $W = U \cap I$ is an open interval containing $c$. Let $x \in W$ with $x \ne c$.
13. The point $t$ of step 10 lies between $c$ and $x$, so $t \in W$, and $t \ne c$. Hence $f(x)/g(x) = f'(t)/g'(t) \in V$.
14. So for every open interval $V$ containing $L$ there is an open interval $W$ containing $c$ with $f(x)/g(x) \in V$ for $x \in W$, $x \ne c$.
15. By the definition of the limit, $f(x)/g(x) \to L$ as $x \to c$.

## Idea

Once $f$ and $g$ are set to $0$ at $c$, the quotient $f(x)/g(x)$ is a quotient of increments over the interval from $c$ to $x$. The Cauchy mean value theorem says this equals $f'(t)/g'(t)$ at some $t$ closer to $c$ than $x$. So whatever $f'/g'$ does near $c$, $f/g$ does too.
