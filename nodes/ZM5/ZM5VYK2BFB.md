---
tag: ZM5VYK2BFB
kind: statement
role: proposition
name: Mellin transform under inversion of the variable
msc: [44A15]
uses: [SGZZ4Y0D36, N5PVGRJE1T]
about: [N5PVGRJE1T]
sources:
  - url: https://en.wikipedia.org/wiki/Mellin_transform
---

## Statement

Let $f \colon (0, \infty) \to \C$ be measurable and let $g(x) = f(1/x)$ for $x > 0$.
Let $s \in \C$.
Then $g$ is [[Mellin convergent|SGZZ4Y0D36]] at $s$ if and only if $f$ is Mellin convergent at $-s$.
In that case
$$\mathcal{M}g(s) = \mathcal{M}f(-s),$$
where $\mathcal{M}$ is the [[Mellin transform|N5PVGRJE1T]].

## Remarks

The proof is the substitution $u = 1/x$, with $dx = -u^{-2} \, du$:
$$\int_0^\infty x^{s-1} f(1/x) \, dx = \int_0^\infty u^{1-s} f(u) \, u^{-2} \, du = \int_0^\infty u^{-s-1} f(u) \, du.$$
The same computation with $\abs{f}$ gives the equivalence of convergence.
So the strip of convergence is reflected in the imaginary axis: if $f$ converges for $\alpha < \operatorname{Re} s < \beta$, then $g$ converges for $-\beta < \operatorname{Re} s < -\alpha$.
Example: $f(x) = e^{-x}$ gives $\int_0^\infty x^{s-1} e^{-1/x} \, dx = \Gamma(-s)$ for $\operatorname{Re} s < 0$.

## Explanations

### L1 human

Replacing $x$ by $1/x$ swaps the roles of $0$ and $\infty$.
On the Mellin side, this simply replaces $s$ by $-s$.

### L2 human

This rule is used with functional equations of the form $\theta(1/x) = \sqrt{x}\, \theta(x)$, where the behaviour at $0$ is read from the behaviour at $\infty$.
It also explains why the Mellin transform of a function and of its reflection have mirror strips of convergence.
Together with the rules for dilations and powers, it shows how the Mellin transform reacts to the maps $x \mapsto a x^{b}$ with $a > 0$ and $b \ne 0$.
