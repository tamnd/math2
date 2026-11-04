---
tag: R4HZTBV9VJ
kind: proof
name: Proof of the fundamental theorem of contour integration
msc: ["30E20"]
proves: 0YQ458D7PF
uses: [00FWNP9TXY, 0DG0Z72CQD, 0D1C9Y1EXA, 0NHGY0N0JB, 05RCDKHZM6]
sources:
  - url: https://en.wikipedia.org/wiki/Cauchy%27s_integral_theorem
    locator: Fundamental theorem for complex line integrals
---

## Proof

We show that $t \mapsto F(\gamma(t))$ has derivative $f(\gamma(t)) \gamma'(t)$ and apply the real fundamental theorem of calculus on each piece.

1. Choose $a = t_0 < t_1 < \dots < t_m = b$ such that $\gamma$ is continuously differentiable on each $[t_{j-1}, t_j]$, with one-sided derivatives at the end points.
2. Let $p \in U$. Define $E(w) = \frac{F(w) - F(p)}{w - p} - F'(p)$ for $w \in U$, $w \ne p$, and $E(p) = 0$. Since $F$ is [[complex differentiable|0D1C9Y1EXA]] at $p$, $E$ is continuous at $p$.
3. For every $w \in U$, $F(w) - F(p) = (F'(p) + E(w)) (w - p)$.
4. Fix $j$, put $\varphi(t) = F(\gamma(t))$ for $t \in [t_{j-1}, t_j]$, and fix $t$ there. Put $p = \gamma(t)$. By step 3, for $s \ne 0$ with $t + s \in [t_{j-1}, t_j]$, $\frac{\varphi(t+s) - \varphi(t)}{s} = (F'(p) + E(\gamma(t+s))) \frac{\gamma(t+s) - \gamma(t)}{s}$.
5. As $s \to 0$, $\gamma(t+s) \to p$ because $\gamma$ is continuous. So $E(\gamma(t+s)) \to 0$ by step 2. Also the last factor tends to $\gamma'(t)$.
6. Hence $\varphi'(t) = F'(\gamma(t)) \gamma'(t) = f(\gamma(t)) \gamma'(t)$, one-sided at the end points. This is continuous in $t$, since $f$, $\gamma$ and $\gamma'$ are continuous on the piece.
7. Apply the [[fundamental theorem of calculus|0NHGY0N0JB]] to $\operatorname{Re} \varphi$ and $\operatorname{Im} \varphi$ on $[t_{j-1}, t_j]$. It gives $\int_{t_{j-1}}^{t_j} f(\gamma(t)) \gamma'(t) \, dt = F(\gamma(t_j)) - F(\gamma(t_{j-1}))$.
8. By the [[definition of the contour integral|00FWNP9TXY]] and [[additivity over intervals|05RCDKHZM6]], $\int_\gamma f(z) \, dz$ is the sum over $j$ of the integrals in step 7.
9. The sum telescopes: $\int_\gamma f(z) \, dz = F(\gamma(t_m)) - F(\gamma(t_0)) = F(\gamma(b)) - F(\gamma(a))$.
10. If $\gamma$ is closed, then $\gamma(b) = \gamma(a)$, so $\int_\gamma f(z) \, dz = 0$.

## Idea

Along the path, $F(\gamma(t))$ is an ordinary function of the real variable $t$. The chain rule says its derivative is the integrand $f(\gamma(t)) \gamma'(t)$, so the real fundamental theorem of calculus applies.
