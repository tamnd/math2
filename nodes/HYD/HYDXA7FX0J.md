---
tag: HYDXA7FX0J
kind: proof
name: Proof of the quotient rule from the product and reciprocal rules
msc: [26A24]
proves: 0BS0NJPKVE
uses: [0V9A43H7WV, 0QD4E5JYPT, 07ZMX4ANJS, 0W8YHHGCJG, 0C9S13WKMF, 0F1WR9C83K, 07EGCNHAVW, 000MXHEY22]
sources:
  - url: https://en.wikipedia.org/wiki/Reciprocal_rule
    locator: Application to a proof of the quotient rule
---

## Proof

We write $f/g = f \cdot (1/g)$ near $a$ and use the [[product rule|0V9A43H7WV]] and the [[reciprocal rule|0QD4E5JYPT]].

1. Since $g$ is differentiable at $a$, it is continuous at $a$ by [[differentiable functions are continuous|07ZMX4ANJS]]. By the [[epsilon-delta form of continuity|0W8YHHGCJG]] with $\varepsilon = \abs{g(a)}$, there is $\delta_0 > 0$ with $\abs{g(x) - g(a)} < \abs{g(a)}$ for $x \in I$ with $\abs{x - a} < \delta_0$.
2. For such $x$, the [[reverse triangle inequality|0C9S13WKMF]] gives $\abs{g(x)} \ge \abs{g(a)} - \abs{g(x) - g(a)} > 0$.
3. Let $I_0 = I \cap (a - \delta_0, a + \delta_0)$. It is an open interval containing $a$, and $g$ has no zero on $I_0$. So $f/g$ is defined on $I_0$.
4. Claim: if $u \colon I \to \R$ is differentiable at $a$, then its restriction to $I_0$ is differentiable at $a$ with the same [[derivative|0F1WR9C83K]].
5. Proof of the claim. Let $H = \set{h \ne 0 : a + h \in I}$ and $H_0 = \set{h \ne 0 : a + h \in I_0}$. Then $H_0 \subseteq H$, and $0$ is a [[limit point|07EGCNHAVW]] of $H_0$.
6. Every sequence in $H_0$ tending to $0$ is a sequence in $H$. By the [[sequential characterization of limits|000MXHEY22]], the difference quotients of $u$ along it tend to $u'(a)$. These are also the difference quotients of the restriction. By the sequential characterization again, the claim follows.
7. By step 4, $f$ and $g$ restricted to $I_0$ are differentiable at $a$. Since $g(a) \ne 0$, the reciprocal rule on $I_0$ shows that $1/g$ is differentiable at $a$ with $(1/g)'(a) = -\frac{g'(a)}{g(a)^2}$.
8. On $I_0$ we have $\frac{f}{g} = f \cdot \frac{1}{g}$. The product rule on $I_0$ shows that $f/g$ is differentiable at $a$, with
$$\left( \frac{f}{g} \right)'(a) = f'(a) \cdot \frac{1}{g(a)} + f(a) \cdot \left( -\frac{g'(a)}{g(a)^2} \right).$$
9. Over the common denominator $g(a)^2$, this equals $\frac{f'(a) g(a) - f(a) g'(a)}{g(a)^2}$.

## Idea

Division by $g$ is multiplication by $1/g$. The product rule handles the multiplication, and the reciprocal rule gives the derivative of $1/g$. The only extra care is to work on an interval around $a$ where $g$ has no zero.
