---
tag: 1A4G6ANVZ1
kind: proof
name: Proof of integration by parts
msc: [26A42]
proves: 08Y1BBQTK9
uses: [06SKCHDQT5, 0HXEX0DPRA, 07ZMX4ANJS, 0VGMHCF4SC, 0V9A43H7WV, 06SESV7GQY, 080RWVVSB6, 0XYAFCN0PT]
sources:
  - url: https://www.math.ucdavis.edu/~hunter/m125b/ch1.pdf
    locator: Theorem 1.53
---

## Proof

We apply the second fundamental theorem to the product $u v$.

1. Let $a < b$ and let $u, v$ be [[continuously differentiable|06SKCHDQT5]] on $[a, b]$. On a closed interval we read this in the usual way.
   So $u$ and $v$ are differentiable on $(a, b)$, have [[one-sided derivatives|0HXEX0DPRA]] at $a$ and $b$, and $u'$ and $v'$ are continuous on $[a, b]$.
2. The functions $u$ and $v$ are continuous on $[a, b]$. Inside, this holds because [[differentiable functions are continuous|07ZMX4ANJS]].
   At $a$, write $u(a + h) - u(a) = h \cdot \frac{u(a + h) - u(a)}{h}$. As $h \to 0^+$ the quotient tends to $u'(a)$ and $h$ tends to $0$, so $u(a + h) \to u(a)$. The point $b$ and the function $v$ are the same.
3. Let $w = u v$. Then $w$ is continuous on $[a, b]$, as a [[product of continuous functions|0VGMHCF4SC]].
4. By the [[product rule|0V9A43H7WV]], $w$ is differentiable on $(a, b)$ with $w' = u' v + u v'$.
5. The functions $u' v$ and $u v'$ are products of continuous functions on $[a, b]$, so they are continuous. Since [[continuous functions are Riemann integrable|06SESV7GQY]], both are integrable on $[a, b]$.
6. By the [[linearity of the integral|080RWVVSB6]], $g = u' v + u v'$ is integrable on $[a, b]$, and
   $$\int_a^b g(x) \, dx = \int_a^b u'(x) v(x) \, dx + \int_a^b u(x) v'(x) \, dx.$$
7. The function $g$ is integrable on $[a, b]$ and equals $w'$ on $(a, b)$. By the [[second fundamental theorem of calculus|0XYAFCN0PT]], $\int_a^b g(x) \, dx = w(b) - w(a) = u(b) v(b) - u(a) v(a)$.
8. Combining steps 6 and 7 and moving the integral of $u' v$ to the other side gives
   $$\int_a^b u(x) v'(x) \, dx = u(b) v(b) - u(a) v(a) - \int_a^b u'(x) v(x) \, dx.$$

## Idea

The product rule says that $u v$ is an antiderivative of $u' v + u v'$. Integrating this sum with the fundamental theorem gives the boundary term $u v$ at $b$ minus at $a$. Splitting the integral of the sum moves the derivative from one factor to the other.
