---
tag: ECSW5HZGE3
kind: definition
name: Luzin N property
msc: [26A46, 26A30]
defines: WMHMGJD261
sources:
  - url: https://en.wikipedia.org/wiki/Luzin_N_property
---

## Definition

Let $a < b$ be real numbers and let $f \colon [a, b] \to \R$ be a function.
Write $\lambda$ for Lebesgue measure on $\R$.
The function $f$ has the *Luzin N property* if for every set $E \subseteq [a, b]$ with $\lambda(E) = 0$, the image $f(E)$ satisfies $\lambda(f(E)) = 0$.

## Remarks

Example: a [[Lipschitz function|0QNVQ4VD9T]] $f$ with constant $L$ has the property.
Let $\lambda(E) = 0$ and $\varepsilon > 0$, and cover $E$ by intervals $I_k$ of total length less than $\varepsilon$.
Each set $f(E \cap I_k)$ lies in an interval of length at most $L \cdot \abs{I_k}$.
So $f(E)$ is covered by intervals of total length less than $L \varepsilon$.

Non-example: the [[Cantor function|NPBYYK63FE]] maps the Cantor set $C$, which has measure $0$, onto $[0, 1]$, which has measure $1$.

The image $f(E)$ need not be measurable for a general $f$, so the condition is read with Lebesgue outer measure.
A continuous function on $[a, b]$ has the N property if and only if it maps Lebesgue measurable sets to Lebesgue measurable sets.
