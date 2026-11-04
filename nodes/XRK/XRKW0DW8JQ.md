---
tag: XRKW0DW8JQ
kind: proof
name: Proof of the fundamental theorem of calculus
msc: [26A42]
proves: 0NHGY0N0JB
uses: [06SESV7GQY, 063H5KJC69, 0XYAFCN0PT]
sources:
  - url: https://www.math.ucdavis.edu/~hunter/m125b/ch1.pdf
    locator: Theorems 1.45 and 1.50
---

## Proof

We combine the two parts of the theorem.

1. Let $a < b$ and let $f \colon [a, b] \to \mathbb{R}$ be continuous. Since [[continuous functions are Riemann integrable|06SESV7GQY]], $f$ is Riemann integrable on $[a, b]$.
2. For $a < x \le b$, $f$ is continuous on $[a, x]$, hence integrable there. So $F(x) = \int_a^x f(t) \, dt$ is defined on $[a, b]$, with $F(a) = 0$. Let $c \in (a, b)$. The function $f$ is continuous at $c$.
3. By the [[first fundamental theorem of calculus|063H5KJC69]], $F$ is differentiable at $c$ with $F'(c) = f(c)$. So $F$ is differentiable on $(a, b)$ with $F' = f$.
4. Now let $G$ be continuous on $[a, b]$ with $G' = f$ on $(a, b)$. Then $G$ is differentiable on $(a, b)$, and $f$ is a Riemann integrable function on $[a, b]$ that extends $G'$, by step 1.
5. By the [[second fundamental theorem of calculus|0XYAFCN0PT]], $\int_a^b f(x) \, dx = G(b) - G(a)$.

## Idea

A continuous function is integrable and continuous at every point. So both halves of the theorem apply to it directly: the integral up to $x$ has derivative $f$, and any antiderivative computes the integral.
