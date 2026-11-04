---
tag: KAN26HZ6F2
kind: proof
name: Proof of the variation of constants formula for linear systems
msc: [34A30]
proves: 0S1KG0XE40
uses: [0A6QZ367GX, 0MQ24RBG93, 016PE4VZ8Q, 03Q7RE2HXR, 0ENVM493VK, 0NC2A3HWGT, 0V9A43H7WV, 0M0TKFRX2A, 0WS1A8E2P9, 0RFWW56Y22, 055VVSN00V, 025PKW8AMR]
sources:
  - url: https://en.wikipedia.org/wiki/Matrix_exponential
    locator: 'Inhomogeneous case generalization: variation of parameters'
---

## Proof

1. The [[fundamental matrix|0MQ24RBG93]] $\Phi$ is differentiable, so its entries are continuous on $I$. By the [[Leibniz formula|016PE4VZ8Q]], $\det \Phi(s)$ is a polynomial in these entries, so it is continuous in $s$.
2. Each $\Phi(s)$ is invertible, so [[$\det \Phi(s) \ne 0$|03Q7RE2HXR]]. Let $\Psi(s) = \Phi(s)^{-1}$.
3. For $n = 1$, $\Psi = 1/\Phi$ is continuous. For $n \ge 2$, $\Psi(s) = \operatorname{adj} \Phi(s) / \det \Phi(s)$ by [[the adjugate formula|0ENVM493VK]]. The entries of the adjugate are signed minors, which are polynomials in the entries of $\Phi$. So $\Psi$ is continuous on $I$.
4. Let $g(s) = \Psi(s) b(s)$, a continuous map $I \to \R^n$. Let $c(t) = \Psi(t_0) x_0 + \int_{t_0}^{t} g(s)\, ds$, componentwise.
5. By [[the antiderivative theorem|0NC2A3HWGT]], applied to each component, $c$ is differentiable on $I$ with $c' = g$.
6. Let $x(t) = \Phi(t) c(t)$. This is the formula of the statement.
7. By the entrywise [[product rule|0V9A43H7WV]] and [[linearity of differentiation|0M0TKFRX2A]], $x' = \Phi' c + \Phi c' = A \Phi c + \Phi \Psi b = A x + b$ on $I$.
8. Also $x(t_0) = \Phi(t_0) \Psi(t_0) x_0 + 0 = x_0$. So $x$ solves the [[linear system|0A6QZ367GX]] $x' = A(t) x + b(t)$ on $I$ with $x(t_0) = x_0$.
9. Uniqueness. Let $F(t, x) = A(t) x + b(t)$ on the open set $D = I \times \R^n$. It is continuous.
10. Let $(t_1, x_1) \in D$. Choose $[c, d] \subseteq I$ with $c < t_1 < d$. By the [[extreme value theorem|0WS1A8E2P9]], the continuous function $t \mapsto \left(\sum_{i, j} A_{ij}(t)^2\right)^{1/2}$ has a maximum $K$ on $[c, d]$.
11. For $t \in [c, d]$ and $v \in \R^n$, the [[Cauchy–Schwarz inequality|0RFWW56Y22]] on each row gives $\norm{A(t) v} \le K \norm{v}$. So $\norm{F(t, x) - F(t, y)} \le K \norm{x - y}$ on $(c, d) \times \R^n$.
12. Thus $F$ is locally [[Lipschitz|055VVSN00V]] in $x$. By [[uniqueness of solutions for Lipschitz vector fields|025PKW8AMR]], any solution on $I$ with value $x_0$ at $t_0$ equals $x$.

## Idea

Try $x = \Phi c$ with a varying vector $c$. Since $\Phi' = A \Phi$, the equation reduces to $\Phi c' = b$, so $c' = \Phi^{-1} b$. Integrating $c'$ from $t_0$ gives the formula, and uniqueness holds because the right side is locally Lipschitz in $x$.
