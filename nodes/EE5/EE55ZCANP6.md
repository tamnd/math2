---
tag: EE55ZCANP6
kind: proof
name: Proof of the chain rule for a composition with a curve
msc: [26B05]
proves: 0A8TJ0VHC7
uses: [0EAAS2EHDR, 0135XZZQ8M, 0G7WM8DX4P]
sources:
  - url: https://www.jirka.org/ra/realanal2.pdf
    locator: Section 8.3.3
---

## Proof

We identify the derivative of a [[curve|0G7WM8DX4P]] with a linear map on $\mathbb{R}$, and we apply the chain rule.

1. Let $I$, $U$, $\gamma$, $f$ and $t_0$ be as in the statement. The interval $I$ is an open subset of $\mathbb{R} = \mathbb{R}^1$.
2. Let $\sigma \colon I \to \mathbb{R}^p$ be any map, let $t \in I$, and let $c \in \mathbb{R}^p$. For real $s \ne 0$ with $t + s \in I$,
$$\frac{\|\sigma(t + s) - \sigma(t) - s c\|}{|s|} = \left\| \frac{\sigma(t + s) - \sigma(t)}{s} - c \right\|.$$
3. By step 2, $\sigma'(t)$ exists and equals $c$ if and only if $\sigma$ is [[differentiable|0135XZZQ8M]] at $t$ with $D\sigma(t)(s) = s c$ for $s \in \mathbb{R}$. The maps $s \mapsto s c$ are exactly the linear maps $\mathbb{R} \to \mathbb{R}^p$.
4. By step 3 with $\sigma = \gamma$, the curve $\gamma$ is differentiable at $t_0$ with $D\gamma(t_0)(s) = s \, \gamma'(t_0)$.
5. The map $\gamma$ goes from the open set $I \subseteq \mathbb{R}$ into $U$, and $f$ is differentiable at $\gamma(t_0)$. By the [[chain rule in several variables|0EAAS2EHDR]] with $n = 1$, $f \circ \gamma$ is differentiable at $t_0$.
6. The chain rule also gives, for $s \in \mathbb{R}$, $D(f \circ \gamma)(t_0)(s) = Df(\gamma(t_0))\big(s \, \gamma'(t_0)\big) = s \, Df(\gamma(t_0))\big(\gamma'(t_0)\big)$. The last equality holds since $Df(\gamma(t_0))$ is linear.
7. By step 3 with $\sigma = f \circ \gamma$ and $c = Df(\gamma(t_0))(\gamma'(t_0))$, the derivative $(f \circ \gamma)'(t_0)$ exists and equals $Df(\gamma(t_0))\big(\gamma'(t_0)\big)$.

## Idea

A curve has a velocity vector $\gamma'(t_0)$, and this is the same as a linear map $s \mapsto s \gamma'(t_0)$ from $\mathbb{R}$. With this dictionary, the result is the general chain rule with one input variable. Feeding the velocity into $Df$ gives the rate of change of $f$ along the curve.
