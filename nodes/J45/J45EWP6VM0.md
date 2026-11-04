---
tag: J45EWP6VM0
kind: proof
name: Proof of the first fundamental theorem of calculus
msc: [26A42]
proves: 063H5KJC69
uses: [0N1JQXZXHC, 0HBY48G8G1, 0A3GWZ86AY, 021WEM680W, 05RCDKHZM6, 080RWVVSB6, 0MBWQKM8QR, 0W8YHHGCJG, 0F1WR9C83K, 0GBZDAFPX8]
sources:
  - url: https://www.math.ucdavis.edu/~hunter/m125b/ch1.pdf
    locator: Theorems 1.48 and 1.50
---

## Proof

We write the difference quotient of $F$ as an average of $f$.

1. Let $a < b$ and let $f \colon [a, b] \to \mathbb{R}$ be [[Riemann integrable|0N1JQXZXHC]] with integral $I$. We first show that $f$ is bounded.
   Take $\delta > 0$ such that each tagged partition of mesh less than $\delta$ has [[Riemann sum|0HBY48G8G1]] within $1$ of $I$.
2. By the [[Archimedean property|0A3GWZ86AY]], fix a partition $(x_0, \dots, x_n)$ of $[a, b]$ with all subintervals shorter than $\delta$, and fix tags $t$.
   For $x \in [x_{i-1}, x_i]$, replace $t_i$ by $x$. The two Riemann sums differ by $(f(x) - f(t_i))(x_i - x_{i-1})$, which has absolute value less than $2$.
3. So $|f(x)| < |f(t_i)| + \frac{2}{x_i - x_{i-1}}$ on the $i$-th subinterval. Let $K > 0$ be larger than all these $n$ bounds. Then $|f(x)| \le K$ on $[a, b]$.
4. Now we check that $F$ is well defined. $F(a) = 0$ by the convention for the [[definite integral|021WEM680W]]. For $a < x < b$, $f$ is integrable on $[a, x]$ by the [[additivity of the integral|05RCDKHZM6]].
5. Let $a \le x < y \le b$. We claim that $f$ is integrable on $[x, y]$ and $F(y) - F(x) = \int_x^y f(t) \, dt$.
   For $x = a$ this is the definition of $F$. For $x > a$, apply additivity to $[a, y]$ split at $x$. This gives $F(y) = F(x) + \int_x^y f(t) \, dt$.
6. Each Riemann sum of a constant $k$ over $[x, y]$ equals $k (y - x)$. So the constant $k$ is integrable over $[x, y]$ with integral $k (y - x)$.
   Since $-K \le f \le K$, the [[monotonicity of the integral|0MBWQKM8QR]] gives $|F(y) - F(x)| \le K (y - x)$.
7. Let $\varepsilon > 0$ and $\delta' = \varepsilon / K$. If $x, y \in [a, b]$ and $|x - y| < \delta'$, then $|F(x) - F(y)| < \varepsilon$ by step 6. By the [[epsilon-delta form of continuity|0W8YHHGCJG]], $F$ is continuous on $[a, b]$.
8. Now let $c \in (a, b)$, and let $f$ be continuous at $c$. Let $\varepsilon > 0$. By the epsilon-delta form, there is $\eta > 0$ with $|f(t) - f(c)| < \varepsilon$ for $t \in [a, b]$ with $|t - c| < \eta$.
   Making $\eta$ smaller, we may assume $(c - \eta, c + \eta) \subseteq (a, b)$.
9. Let $0 < h < \eta$. By step 5, by step 6 for the constant $f(c)$, and by the [[linearity of the integral|080RWVVSB6]],
   $$F(c + h) - F(c) - f(c) h = \int_c^{c + h} \big(f(t) - f(c)\big) \, dt.$$
10. On $[c, c + h]$ the integrand lies in $[-\varepsilon, \varepsilon]$. By monotonicity and step 6, the right side of step 9 has absolute value at most $\varepsilon h$. Dividing by $h$ gives $\big| \frac{F(c + h) - F(c)}{h} - f(c) \big| \le \varepsilon$.
11. Let $-\eta < h < 0$. In the same way, $F(c) - F(c + h) - f(c)(-h) = \int_{c + h}^{c} \big(f(t) - f(c)\big) \, dt$, and its absolute value is at most $\varepsilon |h|$.
    Dividing by $-h > 0$ gives again $\big| \frac{F(c + h) - F(c)}{h} - f(c) \big| \le \varepsilon$.
12. So for each $\varepsilon > 0$ there is $\eta > 0$ with $\big| \frac{F(c + h) - F(c)}{h} - f(c) \big| \le \varepsilon$ whenever $0 < |h| < \eta$.
    By the [[epsilon-delta form of limits|0GBZDAFPX8]], the difference quotient tends to $f(c)$ as $h \to 0$.
13. By the definition of the [[derivative|0F1WR9C83K]], applied to $F$ on the open interval $(a, b)$, $F$ is differentiable at $c$ and $F'(c) = f(c)$.

## Idea

The difference $F(c + h) - F(c)$ is the integral of $f$ over a short interval, so the difference quotient is the average of $f$ there. A bounded $f$ makes $F$ change at most linearly, so $F$ is continuous. If $f$ is continuous at $c$, its averages over shrinking intervals at $c$ tend to $f(c)$.
