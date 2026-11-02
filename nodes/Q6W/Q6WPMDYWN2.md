---
tag: Q6WPMDYWN2
kind: definition
name: Equational logic
msc: [08B05, 03B10]
defines: 72S3YSQFZ7
uses: [PKD440G2XW, NCDZ969V7X, 6D3WA7N2W4]
sources:
  - url: https://en.wikipedia.org/wiki/Equational_logic
---

## Definition

Let $\sigma$ be a signature with only function symbols and let $X$ be a set of variables.
Let $\Sigma$ be a set of [[identities|PKD440G2XW]] over $\sigma$ and $X$.
The identities *derivable* from $\Sigma$ in *equational logic*, written $\Sigma \vdash s \approx t$, form the smallest set of identities that satisfies the following rules, for all [[terms|6D3WA7N2W4]] $s, t, u, s_i, t_i$:

1. (axioms) every identity in $\Sigma$ is derivable;
2. (reflexivity) $t \approx t$ is derivable;
3. (symmetry) if $s \approx t$ is derivable, so is $t \approx s$;
4. (transitivity) if $s \approx t$ and $t \approx u$ are derivable, so is $s \approx u$;
5. (replacement) if $s_i \approx t_i$ is derivable for $i = 1, \ldots, n$ and $f$ is a function symbol of arity $n$, then $f(s_1, \ldots, s_n) \approx f(t_1, \ldots, t_n)$ is derivable;
6. (substitution) if $s \approx t$ is derivable and $\theta$ is a [[substitution|NCDZ969V7X]], then $s\theta \approx t\theta$ is derivable.

## Remarks

A derivation is a finite list of identities, each one in $\Sigma$ or obtained from earlier ones by a rule.
Each rule preserves truth in every algebra, so every derivable identity holds in every algebra that satisfies $\Sigma$; Birkhoff's completeness theorem gives the converse.

Example: let $\Sigma = \set{x + 0 \approx x, \ x + y \approx y + x}$.
Rule 6 applied to the second axiom with $\theta = \set{x \mapsto 0, \ y \mapsto x}$ gives $0 + x \approx x + 0$, and rule 4 with the first axiom gives $\Sigma \vdash 0 + x \approx x$.

Non-example: $x + y \approx y$ is not derivable from $\Sigma$.
The group $(\Z, +, 0)$ satisfies $\Sigma$, and every derivable identity holds in it, but $1 + 0 \ne 0$.
