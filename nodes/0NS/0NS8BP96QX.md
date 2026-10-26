---
tag: 0NS8BP96QX
kind: definition
name: Local minimum
aliases: [relative-minimum]
msc: [26A24]
defines: 09WRNGPTMV
uses: [00999TYPXB]
sources:
  - url: https://en.wikipedia.org/wiki/Maximum_and_minimum
    locator: Definition
---

## Definition

Let $D \subseteq \mathbb{R}$, let $f \colon D \to \mathbb{R}$, and let $a \in D$.
The function $f$ has a local minimum at $a$ if there is $\delta > 0$ with $f(x) \ge f(a)$ for all $x \in D$ with $|x - a| < \delta$.
It is a strict local minimum if $f(x) > f(a)$ for all such $x \ne a$.

## Remarks

So $f$ has a local minimum at $a$ exactly when $-f$ has a [[local maximum|00999TYPXB]] at $a$.
For example, $x^2$ has a strict local minimum at $0$.
Mathlib defines it as `IsLocalMin`.

## Explanations

### L1 human

A local minimum is the bottom of a valley of the graph.
Nearby values are not lower.
