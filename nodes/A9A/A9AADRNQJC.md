---
tag: A9AADRNQJC
kind: proof
name: Proof of differentiation under the integral sign
msc: ["26B15"]
proves: 0AR06W1E1B
uses: [05AXG3QRKR, 0S9EK5MQPE, 07PFYV65MB, 06B8BNJCD6, 0BARQY52N5, 0N91N98EG5, 063H5KJC69, 06SESV7GQY]
sources:
  - url: https://en.wikipedia.org/wiki/Leibniz_integral_rule
    locator: Proofs
---

## Proof

We use the mean value theorem and the uniform continuity of $\partial f / \partial t$.

1. Write $f_t = \partial f / \partial t$ for the [[partial derivative|05AXG3QRKR]] in the second variable. Let $K = [a, b] \times [t_0, t_1]$.
2. The set $K$ is closed and bounded, so it is compact by the [[Heine–Borel theorem|07PFYV65MB]]. By the [[Heine–Cantor theorem|06B8BNJCD6]], $f_t$ is uniformly continuous on $K$.
3. Fix $\varepsilon > 0$. By step 2 there is $\delta > 0$ such that $\abs{f_t(x, s) - f_t(x, s')} < \varepsilon$ for all $x \in [a, b]$ and all $s, s' \in [t_0, t_1]$ with $\abs{s - s'} < \delta$.
4. For each fixed $t$, the functions $x \mapsto f(x, t)$ and $x \mapsto f_t(x, t)$ are [[continuous|0S9EK5MQPE]] on $[a, b]$. So they are [[Riemann integrable|06SESV7GQY]], and $F(t) = \int_a^b f(x, t) \, dx$ is defined.
5. Fix $t \in [t_0, t_1]$ and $h \ne 0$ with $\abs{h} < \delta$ and $t + h \in [t_0, t_1]$. For each $x$, the function $s \mapsto f(x, s)$ is differentiable on $[t_0, t_1]$ with derivative $f_t(x, s)$.
6. By the [[mean value theorem|0BARQY52N5]], for each $x$ there is $\theta$ strictly between $t$ and $t + h$ with $f(x, t + h) - f(x, t) = h \, f_t(x, \theta)$.
7. Since $\abs{\theta - t} < \delta$, step 3 gives $\abs{\frac{f(x, t + h) - f(x, t)}{h} - f_t(x, t)} < \varepsilon$ for every $x \in [a, b]$.
8. Integrate this bound over $[a, b]$: $\abs{\frac{F(t + h) - F(t)}{h} - \int_a^b f_t(x, t) \, dx} \le \varepsilon (b - a)$.
9. Since $\varepsilon$ is arbitrary, $F'(t)$ exists and equals $\int_a^b f_t(x, t) \, dx$. At $t = t_0$ and $t = t_1$ the derivative is one-sided.
10. For $s, t \in [t_0, t_1]$ with $\abs{s - t} < \delta$, step 3 gives $\abs{F'(s) - F'(t)} \le \int_a^b \abs{f_t(x, s) - f_t(x, t)} \, dx \le \varepsilon (b - a)$. So $F'$ is continuous, and $F$ is continuously differentiable.
11. Now let $\alpha, \beta \colon [t_0, t_1] \to [a, b]$ be continuously differentiable, and let $H(t) = \int_{\alpha(t)}^{\beta(t)} f(x, t) \, dx$. Here $\int_u^v = -\int_v^u$ when $v < u$.
12. Fix $t$ and $h$ as in step 5. Then $H(t + h) - H(t) = A_h + B_h$, with $A_h = \int_{\alpha(t+h)}^{\beta(t+h)} \big( f(x, t + h) - f(x, t) \big) \, dx$ and $B_h = \int_{\alpha(t+h)}^{\beta(t+h)} f(x, t) \, dx - \int_{\alpha(t)}^{\beta(t)} f(x, t) \, dx$.
13. The interval between $\alpha(t + h)$ and $\beta(t + h)$ lies in $[a, b]$. So step 7 gives $\abs{\frac{A_h}{h} - \int_{\alpha(t+h)}^{\beta(t+h)} f_t(x, t) \, dx} \le \varepsilon (b - a)$.
14. Let $G(u) = \int_a^u f_t(x, t) \, dx$ for $u \in [a, b]$. By the [[first fundamental theorem of calculus|063H5KJC69]], $G$ is continuous on $[a, b]$.
15. The integral in step 13 is $G(\beta(t + h)) - G(\alpha(t + h))$. As $h \to 0$ it tends to $G(\beta(t)) - G(\alpha(t)) = \int_{\alpha(t)}^{\beta(t)} f_t(x, t) \, dx$, since $\alpha$, $\beta$ and $G$ are continuous.
16. With step 13 and $\varepsilon$ arbitrary, $A_h / h \to \int_{\alpha(t)}^{\beta(t)} f_t(x, t) \, dx$ as $h \to 0$.
17. Next, $B_h = \int_{\beta(t)}^{\beta(t+h)} f(x, t) \, dx - \int_{\alpha(t)}^{\alpha(t+h)} f(x, t) \, dx$, by additivity of the integral over intervals.
18. By the [[mean value theorem for integrals|0N91N98EG5]], there is $\xi_h$ between $\beta(t)$ and $\beta(t + h)$ with $\int_{\beta(t)}^{\beta(t+h)} f(x, t) \, dx = \big( \beta(t + h) - \beta(t) \big) f(\xi_h, t)$. If $\beta(t + h) = \beta(t)$, take $\xi_h = \beta(t)$.
19. As $h \to 0$, $\abs{\xi_h - \beta(t)} \le \abs{\beta(t + h) - \beta(t)} \to 0$. Since $f$ is continuous, $f(\xi_h, t) \to f(\beta(t), t)$.
20. So the first term of $B_h$, divided by $h$, tends to $\beta'(t) \, f(\beta(t), t)$. In the same way, the second term divided by $h$ tends to $\alpha'(t) \, f(\alpha(t), t)$.
21. Adding steps 16 and 20, $H'(t) = \int_{\alpha(t)}^{\beta(t)} f_t(x, t) \, dx + f(\beta(t), t) \, \beta'(t) - f(\alpha(t), t) \, \alpha'(t)$. This is the second formula.

## Idea

The difference quotient of $f$ in $t$ is a value of $\partial f / \partial t$ at a nearby point, by the mean value theorem. Uniform continuity on the compact rectangle makes this approximation good for all $x$ at once, so the limit passes under the integral. When the limits move, the thin strips near the ends add the boundary terms.
