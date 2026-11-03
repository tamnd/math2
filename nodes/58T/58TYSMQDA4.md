---
tag: 58TYSMQDA4
kind: definition
name: Eta conversion
msc: [03B40, 68N18]
defines: 72ASX4ZM81
uses: [BD756KR8FM, Y9B9CVY6SJ]
sources:
  - url: https://en.wikipedia.org/wiki/Lambda_calculus
    locator: η-reduction
---

## Definition

Let $\Lambda$ be the set of terms of the [[lambda calculus|BD756KR8FM]], up to renaming of bound variables.
An *$\eta$-redex* is a term $\lambda x.\, M\, x$ in which the variable $x$ has no free occurrence in $M$.

*One-step $\eta$-reduction* $\to_\eta$ is the least relation on $\Lambda$ with these properties.

1. $\lambda x.\, M\, x \to_\eta M$ whenever $x$ is not free in $M$.
2. If $M \to_\eta M'$, then $M\, N \to_\eta M'\, N$, $N\, M \to_\eta N\, M'$ and $\lambda y.\, M \to_\eta \lambda y.\, M'$.

*$\eta$-conversion* $=_\eta$ is the least equivalence relation that contains $\to_\eta$.
*$\beta\eta$-conversion* $=_{\beta\eta}$ is the least equivalence relation that contains both $\to_\eta$ and the one-step [[beta reduction|Y9B9CVY6SJ]] $\to_\beta$.

## Remarks

Example: $\lambda x.\, (\lambda y.\, y)\, x \to_\eta \lambda y.\, y$, since $x$ is not free in $\lambda y.\, y$.
The same term also $\beta$-reduces to $\lambda x.\, x$, which is the same term up to renaming.

Non-example: $\lambda x.\, x\, x$ is not an $\eta$-redex.
It has the form $\lambda x.\, M\, x$ with $M = x$, but $x$ is free in $M$.

Adding $\eta$ to $\beta$ is equivalent to adding the extensionality rule: if $M\, x = N\, x$ for a variable $x$ free in neither $M$ nor $N$, then $M = N$.
So $=_{\beta\eta}$ is the least equivalence relation that contains $=_\beta$, is compatible with application and abstraction, and is closed under this rule.
