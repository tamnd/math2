---
tag: 2ESE9EE9G7
kind: proof
name: Proof of Rolle's theorem
msc: [26A24]
proves: 0194DY35BG
uses: [0WS1A8E2P9, 0PCVBRV9VJ, 00999TYPXB, 0NS8BP96QX, 0F1WR9C83K, 0GBZDAFPX8]
sources:
  - url: https://en.wikipedia.org/wiki/Rolle%27s_theorem
    locator: Proof of the generalized version
---

## Proof

1. By the [[extreme value theorem|0WS1A8E2P9]], there are $c, d \in [a, b]$ with $f(c) \le f(x) \le f(d)$ for all $x \in [a, b]$.
2. Case 1: both $c$ and $d$ lie in $\set{a, b}$. Since $f(a) = f(b)$, we get $f(c) = f(d) = f(a)$. So $f(x) = f(a)$ for all $x \in [a, b]$, by step 1.
3. In Case 1, let $x_0 = \frac{a + b}{2} \in (a, b)$. For $h \ne 0$ with $x_0 + h \in (a, b)$, the difference quotient of $f$ at $x_0$ is $\frac{f(a) - f(a)}{h} = 0$.
4. By the [[epsilon-delta form of limits|0GBZDAFPX8]], these quotients tend to $0$. So $f'(x_0) = 0$ by the definition of the [[derivative|0F1WR9C83K]], and $x_0$ works.
5. Case 2: $d \in (a, b)$. Let $g$ be the restriction of $f$ to the open interval $(a, b)$. Then $g$ is differentiable at $d$, by hypothesis.
6. For all $x \in (a, b)$, $g(x) \le g(d)$ by step 1. So $g$ has a [[local maximum|00999TYPXB]] at $d$, with any $\delta > 0$.
7. By [[Fermat's theorem on stationary points|0PCVBRV9VJ]], $f'(d) = g'(d) = 0$. So $d$ works.
8. Case 3: $c \in (a, b)$. In the same way, $g(x) \ge g(c)$ for all $x \in (a, b)$, so $g$ has a [[local minimum|0NS8BP96QX]] at $c$. Fermat's theorem gives $f'(c) = 0$.
9. If Case 1 fails, then $c$ or $d$ lies in $(a, b)$, so Case 2 or Case 3 applies. In every case there is a point of $(a, b)$ where $f'$ vanishes.

## Idea

A continuous function on $[a, b]$ attains a maximum and a minimum. If both sit at the endpoints, the equal end values force $f$ to be constant. Otherwise one extremum is inside the interval, and there the derivative must be $0$.
