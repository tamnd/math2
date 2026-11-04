---
tag: BVVQ49AYSB
kind: proof
name: Proof of the integral equation form of an initial value problem
msc: [34A12]
proves: 015KK993C5
uses: [0NRQPQX3VA, 0NHGY0N0JB, 0NC2A3HWGT]
sources:
  - url: https://en.wikipedia.org/wiki/Picard%E2%80%93Lindel%C3%B6f_theorem
    locator: Proof sketch
---

## Proof

Integrals and derivatives of maps into $\R^n$ are taken componentwise. We assume that $J$ has more than one point, since otherwise no derivative on $J$ is defined.

1. Let $g(s) = f(s, \gamma(s))$ for $s \in J$. The map $s \mapsto (s, \gamma(s))$ is continuous from $J$ to $J \times U$, and $f$ is continuous. So $g$ is [[continuous|0NRQPQX3VA]] on $J$.
2. First direction. Assume $\gamma$ is differentiable on $J$ with $\gamma' = g$ and $\gamma(t_0) = x_0$. Let $t \in J$ with $t \ne t_0$, and let $[c, d]$ be the closed interval with endpoints $t_0$ and $t$. It lies in $J$.
3. Each component $\gamma_i$ is continuous on $[c, d]$ and differentiable on $(c, d)$ with derivative $g_i$, which is continuous. By the [[fundamental theorem of calculus|0NHGY0N0JB]], $\int_c^d g_i(s)\, ds = \gamma_i(d) - \gamma_i(c)$.
4. In both orders of $t_0$ and $t$ this means $\gamma(t) - \gamma(t_0) = \int_{t_0}^{t} g(s)\, ds$. With $\gamma(t_0) = x_0$, this is the integral equation at $t$. At $t = t_0$ it reads $\gamma(t_0) = x_0$, which holds.
5. Second direction. Assume the integral equation holds on $J$. At $t = t_0$ the integral is $0$, so $\gamma(t_0) = x_0$.
6. Let $\hat J$ be the open interval obtained from $J$ by adding $(e - 1, e]$ at a left endpoint $e \in J$, and $[e, e + 1)$ at a right endpoint $e \in J$.
7. Let $\hat g = g$ on $J$, and let $\hat g$ be constant, equal to $g(e)$, on each added piece beyond an endpoint $e$. The pieces agree at $e$, so $\hat g$ is continuous on $\hat J$.
8. By [[the antiderivative theorem|0NC2A3HWGT]], applied to each component, $G(t) = \int_{t_0}^{t} \hat g(s)\, ds$ is differentiable on $\hat J$ with $G' = \hat g$.
9. On $J$ we have $\gamma = x_0 + G$, since $\hat g = g$ on $J$. At an interior point $t$ of $J$, this gives $\gamma'(t) = \hat g(t) = g(t)$.
10. At an endpoint $e \in J$, the one-sided derivative of $\gamma$ is the one-sided derivative of $G$, which equals $G'(e) = \hat g(e) = g(e)$.
11. So $\gamma$ is differentiable on $J$, with $\gamma'(t) = f(t, \gamma(t))$ for each $t \in J$, and $\gamma(t_0) = x_0$.

## Idea

Both directions are the fundamental theorem of calculus. Integrating the equation gives the integral form, and differentiating the integral form gives back the equation. Continuity of $f$ and $\gamma$ makes the integrand continuous, which is what both parts of the theorem need.
