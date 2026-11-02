---
tag: RPQNSM5HKC
kind: statement
role: proposition
name: Mellin transform of a power times a function
msc: [44A15]
uses: [SGZZ4Y0D36, N5PVGRJE1T, 0RNGDMHT7M]
about: [N5PVGRJE1T]
sources:
  - url: https://en.wikipedia.org/wiki/Mellin_transform
---

## Statement

Let $f \colon (0, \infty) \to \C$ be measurable, let $a \in \C$, and let $g(x) = x^{a} f(x)$ for $x > 0$, where $x^{a} = e^{a \log x}$ is the [[complex power|0RNGDMHT7M]].
Let $s \in \C$.
Then $g$ is [[Mellin convergent|SGZZ4Y0D36]] at $s$ if and only if $f$ is Mellin convergent at $s + a$.
In that case
$$\mathcal{M}g(s) = \mathcal{M}f(s + a),$$
where $\mathcal{M}$ is the [[Mellin transform|N5PVGRJE1T]].

## Remarks

The proof is the identity $x^{s-1} \cdot x^{a} = x^{(s + a) - 1}$ for $x > 0$, which holds because $\log x$ is real.
Taking absolute values gives $\abs{x^{s-1} g(x)} = x^{\operatorname{Re}(s + a) - 1} \abs{f(x)}$, hence the equivalence of convergence.
So the strip of convergence is shifted by $-\operatorname{Re} a$.
Example: $f(x) = e^{-x}$ and $a = 1$ give $\mathcal{M}[x e^{-x}](s) = \Gamma(s + 1)$ for $\operatorname{Re} s > -1$.

## Explanations

### L1 human

Multiplying a function by a power $x^{a}$ just shifts its Mellin transform by $a$ in the variable $s$.
This is the Mellin counterpart of the rule that multiplying by $e^{i\omega x}$ shifts a Fourier transform.

### L2 human

The rule shows that the choice of the exponent $s - 1$ rather than $s$ in the Mellin kernel is a convention: changing it only shifts $s$.
With the dilation rule and the power substitution rule, it gives the Mellin transforms of all functions $x^{b} f(c x^{a})$ from that of $f$.
It is also how a weight $x^{\sigma}$ is moved in and out of Plancherel-type identities for the Mellin transform.
