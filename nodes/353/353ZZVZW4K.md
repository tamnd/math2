---
tag: 353ZZVZW4K
kind: definition
name: Type system
msc: [68N15, 03B38, 68Q55]
defines: AVVQEG0MRJ
uses: [Q48KGV33AH, 08EJC6Q25H]
sources:
  - url: https://en.wikipedia.org/wiki/Type_system
---

## Definition

Let $T$ be the set of terms of a programming language, with a set of variables.
A *type system* for the language consists of these data.

1. A set $\mathcal T$ of *types*.
2. *Contexts*: finite lists $\Gamma = x_1{:}\tau_1, \ldots, x_n{:}\tau_n$ of distinct variables with types $\tau_i \in \mathcal T$.
3. A set of *typing rules*, each of the form "from the judgments $\Gamma_1 \vdash t_1 : \tau_1, \ldots, \Gamma_k \vdash t_k : \tau_k$ infer $\Gamma \vdash t : \tau$".

The *typing relation* is the least [[relation|08EJC6Q25H]] $\Gamma \vdash t : \tau$ between contexts, terms and types that is closed under the typing rules.
A term $t$ is *well-typed* in $\Gamma$ if $\Gamma \vdash t : \tau$ for some type $\tau$.

## Remarks

Example: in the simply typed lambda calculus over a base type $\iota$, the types are $\iota$ and $\sigma \to \tau$.
The rules are $\Gamma \vdash x : \tau$ when $x{:}\tau$ is in $\Gamma$, the abstraction rule and the application rule.
So $\vdash \lambda x{:}\iota.\, x : \iota \to \iota$, by the abstraction rule from $x{:}\iota \vdash x : \iota$.

Non-example: in the same system the term $\lambda x{:}\iota.\, x\, x$ is not well-typed.
The application rule would need $x$ to have a type $\sigma \to \tau$, but the context gives $x$ the base type $\iota$.

A type system is *sound* for an operational semantics if well-typed closed terms never reach a stuck state.
This is usually proved from *progress* (a well-typed closed term is a value or can take a step) and *preservation* (a step keeps the type).
