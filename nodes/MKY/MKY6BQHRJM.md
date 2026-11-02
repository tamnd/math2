---
tag: MKY6BQHRJM
kind: definition
name: Unification
msc: [68V15, 03B35, 08B05]
defines: RJJ9D0WF53
uses: [NCDZ969V7X, 6D3WA7N2W4]
sources:
  - url: https://en.wikipedia.org/wiki/Unification_(computer_science)
---

## Definition

Let $\sigma$ be a signature with only function symbols, let $X$ be a set of variables, and let $s, t$ be [[terms|6D3WA7N2W4]] over $\sigma$ and $X$.
A *unifier* of $s$ and $t$ is a [[substitution|NCDZ969V7X]] $\theta$ with $s\theta = t\theta$, equality meaning identical terms.
A unifier $\theta$ is a *most general unifier* if the following holds for every unifier $\eta$ of $s$ and $t$.
There is a substitution $\rho$ with $x\eta = (x\theta)\rho$ for every variable $x$.
*Unification* is the problem of deciding whether two given terms have a unifier and of finding a most general one.

## Remarks

If $s$ and $t$ have a unifier, then they have a most general unifier, unique up to renaming of variables, and Robinson's algorithm finds it.
The same notions apply to finite sets of pairs of terms, which are unified simultaneously.
In $E$-unification one asks instead for $s\theta \approx t\theta$ to follow from a set $E$ of identities.

Example: $s = f(x, b)$ and $t = f(a, y)$, with constants $a, b$, have the unifier $\theta = \set{x \mapsto a, \ y \mapsto b}$.
Indeed $s\theta = f(a, b) = t\theta$, and $\theta$ is most general because every unifier must send $x$ to $a$ and $y$ to $b$.

Non-example: $x$ and $f(x)$ have no unifier.
For every substitution $\theta$, the term $f(x)\theta = f(x\theta)$ has one more symbol than $x\theta$, so they are never identical.
