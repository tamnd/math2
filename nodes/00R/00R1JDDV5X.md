---
tag: 00R1JDDV5X
kind: definition
name: Arc length parametrisation
msc: [53A04]
defines: 0Q4CJ5NAT1
uses: [06JMR2XWXW, 0D98771SM0, 0C28RT5BG7]
sources:
  - url: https://en.wikipedia.org/wiki/Differentiable_curve
    locator: Length and natural parametrization
  - url: https://en.wikipedia.org/wiki/Arc_length
    locator: Finding arc lengths by integration
---

## Definition

Let $\gamma \colon [a, b] \to \mathbb{R}^n$ be a [[regular|06JMR2XWXW]] $C^1$ curve.
Its arc length function is
$$s(t) = \int_a^t \|\gamma'(u)\| \, du, \qquad t \in [a, b],$$
and its length is $\ell = s(b)$.
Since $s'(t) = \|\gamma'(t)\| > 0$, the function $s \colon [a, b] \to [0, \ell]$ is a strictly increasing $C^1$ bijection with a $C^1$ inverse $t(s)$.
The arc length parametrisation of $\gamma$ is the curve $\tilde\gamma \colon [0, \ell] \to \mathbb{R}^n$, $\tilde\gamma(s) = \gamma(t(s))$.

## Remarks

The curve $\tilde\gamma$ has the same image and direction as $\gamma$, and $\|\tilde\gamma'(s)\| = 1$ for each $s$. So $\tilde\gamma'(s)$ is the unit [[tangent vector|0D98771SM0]].
The length of $\tilde\gamma$ from $\tilde\gamma(s_0)$ to $\tilde\gamma(s_1)$ is $s_1 - s_0$.
For the helix $\gamma(t) = (\cos t, \sin t, t)$, $\|\gamma'(t)\| = \sqrt{2}$, so $s = \sqrt{2}\, t$ and $\tilde\gamma(s) = (\cos(s / \sqrt{2}), \sin(s / \sqrt{2}), s / \sqrt{2})$.
The arc length parametrisation is unique up to a shift of the parameter. It simplifies the formulas for curvature.

## Explanations

### L1 human

Reparametrise the curve so that the parameter is the distance travelled from the start.
Then the point moves at constant speed $1$, and only the shape of the curve remains.
