---
tag: HBH31BEN54
kind: proof
name: Proof of Darboux's theorem from the extreme value theorem
msc: [26A24]
proves: 0Q5A47J48D
uses: [0WS1A8E2P9, 0PCVBRV9VJ, 0HXEX0DPRA, 0909PWZR62, 07ZMX4ANJS, 0P27W9RW0G, 0NS8BP96QX]
sources:
  - url: https://en.wikipedia.org/wiki/Darboux%27s_theorem_(analysis)
    locator: Proof from the extreme value theorem
---

## Proof

We first treat the case $f'(a) < y < f'(b)$, and find an interior minimum of a shifted function.

1. Assume $f'(a) < y < f'(b)$. Here $f'(a)$ is the right derivative and $f'(b)$ is the left derivative, as [[one-sided derivatives|0HXEX0DPRA]].
2. Define $g \colon [a, b] \to \R$ by $g(x) = f(x) - y x$. Then $g$ is differentiable on $(a, b)$ with $g'(x) = f'(x) - y$.
3. In the same way, $g$ has right derivative $g'(a) = f'(a) - y < 0$ and left derivative $g'(b) = f'(b) - y > 0$.
4. The function $g$ is [[continuous|07ZMX4ANJS]] at each point of $(a, b)$, since it is differentiable there.
5. For $a < t \le b$ write $g(t) - g(a) = (t - a) q(t)$, where $q(t) = (g(t) - g(a))/(t - a)$. As $t \to a^+$, $q(t) \to g'(a)$ and $t - a \to 0$. So $g(t) \to g(a)$.
6. In the same way $g(t) \to g(b)$ as $t \to b^-$. With step 4, $g$ is [[continuous|0P27W9RW0G]] on $[a, b]$.
7. By the [[extreme value theorem|0WS1A8E2P9]], there is $c \in [a, b]$ with $g(c) \le g(t)$ for all $t \in [a, b]$.
8. Since $q(t) \to g'(a) < 0$ as $t \to a^+$, the definition of the [[right limit|0909PWZR62]] gives $\delta > 0$ with $q(t) < 0$ for $a < t < a + \delta$, $t \le b$.
9. For such $t$, $g(t) - g(a) = (t - a) q(t) < 0$. So $g(t) < g(a)$, and $c \ne a$.
10. Likewise, the quotient $(g(t) - g(b))/(t - b)$ tends to $g'(b) > 0$ as $t \to b^-$. So it is positive for $t < b$ close to $b$.
11. For such $t$ we have $t - b < 0$, so $g(t) - g(b) < 0$. Thus $g(t) < g(b)$, and $c \ne b$.
12. So $c \in (a, b)$. The restriction of $g$ to the open interval $(a, b)$ has a [[local minimum|0NS8BP96QX]] at $c$, and it is differentiable at $c$.
13. By [[Fermat's theorem|0PCVBRV9VJ]], $g'(c) = 0$. So $f'(c) = y$.
14. Now assume $f'(a) > y > f'(b)$. The function $-f$ satisfies the hypotheses, with $(-f)'(a) < -y < (-f)'(b)$.
15. By steps 1 to 13 applied to $-f$ and $-y$, there is $c \in (a, b)$ with $-f'(c) = -y$. So $f'(c) = y$.

## Idea

Subtracting the line $y x$ turns the problem into finding a zero of a derivative. The signs of $g'$ at the ends give values of $g$ below $g(a)$ just right of $a$. They also give values below $g(b)$ just left of $b$. So the minimum of $g$ is inside, and Fermat's theorem makes the derivative zero there.
