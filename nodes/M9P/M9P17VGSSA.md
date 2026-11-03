---
tag: M9P17VGSSA
kind: statement
role: theorem
name: Slutsky equation
msc: [91B42, 91B16]
uses: [EQPEPJ7QQZ, ZFX4T69SST, N9S29DKCY8, T968JGCJHC, 09EGC6F8PT]
about: [EQPEPJ7QQZ, ZFX4T69SST]
sources:
  - url: https://en.wikipedia.org/wiki/Slutsky_equation
same_as:
  wikidata: Q431721
  wikipedia: Slutsky equation
---

## Statement

Let $u \colon \R^n_{\ge 0} \to \R$ be a continuous, locally nonsatiated and strictly quasiconcave utility function.
Let $x(p, w)$ be its [[Marshallian demand|EQPEPJ7QQZ]], $h(p, \bar{u})$ its [[Hicksian demand|ZFX4T69SST]] and $v(p, w)$ its [[indirect utility|N9S29DKCY8]].
Let $p \in \R^n$ have all entries positive, let $w > 0$, and set $\bar{u} = v(p, w)$.
Assume that $x$ is differentiable at $(p, w)$ and that $h$ is differentiable at $(p, \bar{u})$.
Then, for all goods $\ell, k \in \set{1, \dots, n}$,
$$\frac{\partial h_\ell}{\partial p_k}(p, \bar{u}) = \frac{\partial x_\ell}{\partial p_k}(p, w) + \frac{\partial x_\ell}{\partial w}(p, w)\, x_k(p, w).$$

## Remarks

The proof differentiates the identity $h_\ell(p, \bar{u}) = x_\ell(p, e(p, \bar{u}))$, where $e$ is the expenditure function, with respect to $p_k$ by the chain rule.
[[Shephard's lemma|T968JGCJHC]] gives $\partial e / \partial p_k = h_k(p, \bar{u}) = x_k(p, w)$, and $e(p, \bar{u}) = w$.
Example: for $u = \sqrt{x_1 x_2}$, $x_1 = w / (2p_1)$, so the right side for $\ell = k = 1$ is $-w/(2p_1^2) + w/(4p_1^2) = -w/(4p_1^2)$.
On the left, $h_1 = \bar{u}\sqrt{p_2/p_1}$ gives $\partial h_1 / \partial p_1 = -\tfrac12 \bar{u} \sqrt{p_2}\, p_1^{-3/2}$, which equals $-w/(4p_1^2)$ for $\bar{u} = w/(2\sqrt{p_1 p_2})$.
The matrix of the left sides, the Slutsky matrix, is symmetric and negative semidefinite, and it has $p$ in its kernel.

## Explanations

### L1 human

When a price rises, a consumer changes what they buy for two reasons.
The good is now dearer relative to others, which is the substitution effect, and the consumer is poorer, which is the income effect.
The Slutsky equation splits the total change into these two parts exactly.

### L2 human

Rearranged, it reads $\partial x_\ell / \partial p_k = \partial h_\ell / \partial p_k - x_k\, \partial x_\ell / \partial w$: total effect equals substitution effect minus income effect.
The own substitution effect $\partial h_\ell / \partial p_\ell$ is never positive.
So a good whose demand rises with its own price, a Giffen good, must be an inferior good with a large income effect.
The symmetry and negative semidefiniteness of the Slutsky matrix are the testable restrictions of utility maximization on a demand function.
