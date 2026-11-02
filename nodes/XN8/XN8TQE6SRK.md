---
tag: XN8TQE6SRK
kind: definition
name: Substitution
msc: [03B10, 08B05]
defines: NCDZ969V7X
uses: [6D3WA7N2W4, WDVVEYD6AT]
sources:
  - url: https://en.wikipedia.org/wiki/Substitution_(logic)
---

## Definition

Let $\sigma$ be a [[signature|WDVVEYD6AT]] with only function symbols and let $X$ be a set of variables.
Let $T(X)$ be the set of [[terms|6D3WA7N2W4]] over $\sigma$ and $X$.
A *substitution* is a map $\theta \colon X \to T(X)$.
Its *application* to a term $t$, written $t\theta$, is defined by recursion on $t$:

1. $x\theta = \theta(x)$ for each variable $x \in X$;
2. $c\theta = c$ for each constant symbol $c$;
3. $f(t_1, \ldots, t_n)\theta = f(t_1\theta, \ldots, t_n\theta)$ for each function symbol $f$ of arity $n \ge 1$.

## Remarks

Usually $\theta(x) = x$ for all but finitely many $x$, and $\theta$ is written $\set{x_1 \mapsto s_1, \ldots, x_k \mapsto s_k}$.
A term $s$ is an *instance* of $t$ if $s = t\theta$ for some substitution $\theta$.
The substitutions are exactly the endomorphisms of the term algebra $T(X)$, restricted to the variables.
For an identity $s \approx t$, the identity $s\theta \approx t\theta$ holds in every algebra in which $s \approx t$ holds.

Example: with $\theta = \set{x \mapsto z \cdot z, \ y \mapsto 1}$, clause 3 and clause 1 give $(x + y)\theta = (z \cdot z) + 1$.

Non-example: the replacement of the first occurrence of $x$ in $x + x$ by $y$ is not a substitution.
By clauses 1 and 3, every substitution sends $x + x$ to $\theta(x) + \theta(x)$, which never equals $y + x$.
