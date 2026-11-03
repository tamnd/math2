---
tag: NTS9ZF3PHJ
kind: definition
name: Linear type system
msc: [68N15, 03B47, 68N18]
defines: DJGYZTS0YC
uses: [2DP940895E, AVVQEG0MRJ, 2P2184B6HE]
sources:
  - url: https://en.wikipedia.org/wiki/Substructural_type_system
---

## Definition

Take the types $\tau ::= b \mid \tau \multimap \tau \mid \tau \otimes \tau$ and the terms of the [[simply typed lambda calculus|2DP940895E]] with pairs $(t, u)$ and the destructor $\mathsf{let}\ (x, y) = t\ \mathsf{in}\ u$.
A context $\Gamma$ is a finite list of distinct typed variables, and $\Gamma, \Delta$ denotes the union of two contexts with no common variable.
The *linear type system* is the least relation $\Gamma \vdash t : \tau$ closed under these rules.

1. Variable: $x : \tau \vdash x : \tau$, with exactly one variable in the context.
2. Abstraction: if $\Gamma, x : \sigma \vdash t : \tau$, then $\Gamma \vdash \lambda x.\, t : \sigma \multimap \tau$.
3. Application: if $\Gamma \vdash t : \sigma \multimap \tau$ and $\Delta \vdash u : \sigma$, then $\Gamma, \Delta \vdash t\, u : \tau$.
4. Pairing: if $\Gamma \vdash t : \sigma$ and $\Delta \vdash u : \tau$, then $\Gamma, \Delta \vdash (t, u) : \sigma \otimes \tau$.
5. Unpairing: if $\Gamma \vdash t : \sigma \otimes \rho$ and $\Delta, x : \sigma, y : \rho \vdash u : \tau$, then $\Gamma, \Delta \vdash \mathsf{let}\ (x, y) = t\ \mathsf{in}\ u : \tau$.
6. Exchange: the order of variables in a context does not matter.

The context is split between subterms, and the variable rule allows no extra variables.
So every variable of $\Gamma$ occurs exactly once in $t$ whenever $\Gamma \vdash t : \tau$.

## Remarks

Example: $\vdash \lambda p.\, \mathsf{let}\ (x, y) = p\ \mathsf{in}\ (y, x) : \sigma \otimes \rho \multimap \rho \otimes \sigma$.
The check: rule 4 with the contexts $y : \rho$ and $x : \sigma$ gives $(y, x)$ its type, rule 5 with $\Gamma = p : \sigma \otimes \rho$ consumes $p$, and rule 2 abstracts $p$.

Non-example: $\lambda x.\, (x, x)$ has no type.
Rule 4 needs disjoint contexts for the two components, but both need $x$; this is contraction, which the system lacks.
Likewise $\lambda x.\, \lambda y.\, x$ has no type, since $y$ would stay unused at the variable rule; this is weakening.

The connectives $\multimap$ and $\otimes$ are linear implication and the multiplicative conjunction of [[linear logic|2P2184B6HE]].
Adding weakening gives affine types, adding contraction gives relevant types, and adding both gives back the ordinary [[type system|AVVQEG0MRJ]] of the simply typed calculus.
