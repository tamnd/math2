---
tag: C30ABKJ9F6
kind: proof
name: Proof that the integral of a continuous function is an antiderivative
msc: [26A36]
proves: 0NC2A3HWGT
uses: [06SESV7GQY, 021WEM680W, 05RCDKHZM6, 063H5KJC69, 0F1WR9C83K, 0BW9N5CDSB]
sources:
  - url: https://www.math.ucdavis.edu/~hunter/m125b/ch1.pdf
    locator: Theorem 1.50 and Definition 1.34
---

## Proof

We reduce to the first fundamental theorem on a closed interval around each point.

1. Let $I$ be an open interval, let $f \colon I \to \mathbb{R}$ be continuous, and let $a \in I$. For $x \in I$, the restriction of $f$ to the closed interval between $a$ and $x$ is continuous.
   Since [[continuous functions are Riemann integrable|06SESV7GQY]], the [[definite integral|021WEM680W]] $F(x) = \int_a^x f(t) \, dt$ is defined.
2. Fix $x_0 \in I$. Since $I$ is open, there are $p, q \in I$ with $p < \min(a, x_0)$ and $q > \max(a, x_0)$. Then $[p, q] \subseteq I$, and $f$ is continuous on $[p, q]$.
3. Define $G(x) = \int_p^x f(t) \, dt$ for $x \in [p, q]$. We claim that $F(x) = G(x) - G(a)$ for all $x \in (p, q)$.
4. If $x > a$, the [[additivity of the integral|05RCDKHZM6]] on $[p, x]$ split at $a$ gives $G(x) = G(a) + \int_a^x f(t) \, dt = G(a) + F(x)$.
5. If $x = a$, then $F(a) = 0 = G(a) - G(a)$ by the convention for the definite integral.
6. If $x < a$, additivity on $[p, a]$ split at $x$ gives $G(a) = G(x) + \int_x^a f(t) \, dt$. By the sign convention, $\int_x^a f(t) \, dt = -F(x)$. So $F(x) = G(x) - G(a)$.
7. The function $f$ is continuous at $x_0 \in (p, q)$. By the [[first fundamental theorem of calculus|063H5KJC69]] on $[p, q]$, $G$ is differentiable at $x_0$ with $G'(x_0) = f(x_0)$.
8. For $0 < |h|$ small enough, $x_0 + h \in (p, q)$. Then step 3 gives $\frac{F(x_0 + h) - F(x_0)}{h} = \frac{G(x_0 + h) - G(x_0)}{h}$.
9. So the two difference quotients have the same limit as $h \to 0$. By the definition of the [[derivative|0F1WR9C83K]], $F$ is differentiable at $x_0$ with $F'(x_0) = f(x_0)$.
10. Since $x_0 \in I$ was arbitrary, $F$ is differentiable on $I$ with $F' = f$. So $F$ is an [[antiderivative|0BW9N5CDSB]] of $f$ on $I$.

## Idea

Differentiability is a local property. Near any point $x_0$ we can place a closed interval $[p, q]$ inside $I$. There $F$ differs from $\int_p^x f$ only by a constant, and the first fundamental theorem gives the derivative.
