---
tag: MTM92ND7HE
kind: definition
name: Mikusiński operational calculus
msc: [44A40]
defines: TD5XK5AHNV
uses: [82YAXZMMQ1, FCKX8KFVGN, 0QQRP17Z7S]
sources:
  - url: https://en.wikipedia.org/wiki/Operational_calculus
---

## Definition

Let $\mathcal{M}$ be the [[Mikusiński field of operators|82YAXZMMQ1]].
It contains the complex numbers and the continuous functions on $[0, \infty)$, with the [[convolution on the half-line|FCKX8KFVGN]] as product.
Let $l$ be the constant function $1$ and $s = 1/l \in \mathcal{M}$.
The *Mikusiński operational calculus* is the method of solving linear problems in $\mathcal{M}$ with the following rules.

1. For every $n \ge 1$ and every $n$ times continuously differentiable $f$ on $[0, \infty)$, $f^{(n)} = s^n f - s^{n-1} f(0) - s^{n-2} f'(0) - \dots - f^{(n-1)}(0)$ in $\mathcal{M}$.
2. For every complex $\alpha$, the operator $1/(s - \alpha)$ is the function $e^{\alpha t}$, and more generally $1/(s - \alpha)^{k}$ is the function $t^{k-1} e^{\alpha t}/(k-1)!$ for $k \ge 1$.
3. A [[linear differential equation|0QQRP17Z7S]] with constant coefficients and given initial values is rewritten by rule 1 as a linear equation for $y \in \mathcal{M}$. This equation is solved in the field $\mathcal{M}$, and the solution is identified as a function by rule 2 and partial fractions.

## Remarks

Rule 1 follows by induction from $s f = f' + f(0)$, which is the identity $l * f' = f - f(0) l$ divided by $l$.
Rule 2 for $k = 1$ follows from rule 1: for $f = e^{\alpha t}$, $s f - 1 = \alpha f$, so $(s - \alpha) f = 1$.
The solution found in step 3 is the unique solution, because $\mathcal{M}$ is a field and the embedding of continuous functions is injective.
The rules agree with those of the Laplace transform method, with $s$ in the role of the transform variable, but they apply to all continuous functions, without growth conditions.

Example: $y'' + y = 0$, $y(0) = 1$, $y'(0) = 0$.
Rule 1 gives $s^2 y - s + y = 0$, so $y = s/(s^2 + 1) = \frac{1}{2}\left(\frac{1}{s - i} + \frac{1}{s + i}\right)$.
By rule 2, $y = \frac{1}{2}(e^{it} + e^{-it}) = \cos t$.

Non-example: the operator $s$ itself is not a continuous function, so rule 2 has no analogue for $s$.
If $s = g$ for a continuous $g$, then $l * g = l \cdot s = 1$, so $l * g * l = l$ as functions.
The left side is a convolution of continuous functions, so it vanishes at $t = 0$, while $l(0) = 1$.
