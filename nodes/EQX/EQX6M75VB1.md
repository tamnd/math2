---
tag: EQX6M75VB1
kind: example
name: Anti-de Sitter space
msc: [83C15, 53C50, "83E05"]
instance_of: [BY4QYYS788]
illustrates: [WVKKDY9V61]
uses: [1X42JAA349, 41S2EZ0KR3, Y1YPE6PM52, 809288G50Y]
sources:
  - url: https://en.wikipedia.org/wiki/Anti-de_Sitter_space
same_as:
  wikidata: Q574780
  wikipedia: Anti-de Sitter space
---

## Example

Let $n \ge 3$ and $\alpha > 0$.
Equip $\R^{n+1}$ with coordinates $(u, v, x_1, \ldots, x_{n-1})$ and the form $\eta = -du^2 - dv^2 + dx_1^2 + \cdots + dx_{n-1}^2$ of signature $(2, n-1)$.
The *anti-de Sitter space* of radius $\alpha$ is the quadric
$$\set{-u^2 - v^2 + x_1^2 + \cdots + x_{n-1}^2 = -\alpha^2}$$
with the metric $g$ induced by $\eta$.

Check: the coordinates $u = \alpha\cosh\rho\cos\tau$, $v = \alpha\cosh\rho\sin\tau$, $x = \alpha\sinh\rho\,\omega$ with $\rho \ge 0$, $\tau$ an angle and $\omega \in S^{n-2}$ cover the quadric.
A direct substitution gives
$$g = \alpha^2\left(-\cosh^2\rho\, d\tau^2 + d\rho^2 + \sinh^2\rho\, d\Omega_{n-2}^2\right),$$
which has one negative and $n - 1$ positive directions, so $g$ is Lorentzian.

The [[sectional curvature|1X42JAA349]] is constant and equal to $-1/\alpha^2$.
So $R_{ab} = -\frac{n-1}{\alpha^2} g_{ab}$, and the space solves $G_{ab} + \Lambda g_{ab} = 0$ with negative [[cosmological constant|WVKKDY9V61]] $\Lambda = -\frac{(n-1)(n-2)}{2\alpha^2}$.
The group $O(2, n-1)$ acts by isometries, so the space is maximally symmetric.

The coordinate $\tau$ is periodic, so the curves $\rho = \text{const}$, $\omega = \text{const}$ are closed timelike curves.
One usually passes to the [[universal cover|Y1YPE6PM52]], where $\tau \in \R$; this is also called anti-de Sitter space and has no closed timelike curves.
Its slices $\tau = \text{const}$ are copies of hyperbolic space, as in the [[hyperboloid model|809288G50Y]].

## Explanations

### L1 human

Anti-de Sitter space is the Lorentzian analogue of hyperbolic space: it has constant negative curvature.
It is a universe with no matter and a negative cosmological constant, which pulls everything back towards the centre.
A thrown object always returns, and a light ray reaches the edge of the universe in finite time.
Its boundary at infinity plays a central role in the AdS/CFT correspondence of string theory.
