---
tag: KCV8RKBATN
kind: definition
name: Intuitionistic type theory
msc: ["03B38", "03F55", "03F50"]
defines: ESVYD9CZ8C
uses: [42A2M9S2C1, Q11N8X99FK, HTF9E5W7EZ]
sources:
  - url: https://en.wikipedia.org/wiki/Intuitionistic_type_theory
---

## Definition

*Intuitionistic type theory*, or Martin-Löf type theory, is the dependent [[type theory|42A2M9S2C1]] with the following parts.

1. Four forms of judgment in a context $\Gamma$. They say that $A$ is a type, or that $A$ and $B$ are equal types. They also say that $a$ has type $A$, written $a : A$, or that $a$ and $b$ are equal terms of type $A$.
2. Dependent function types $\prod_{x : A} B(x)$, whose terms are functions $\lambda x.\, b(x)$ with $b(x) : B(x)$ for each $x : A$.
3. Dependent pair types $\sum_{x : A} B(x)$, whose terms are pairs $(a, b)$ with $a : A$ and $b : B(a)$.
4. Identity types $\mathrm{Id}_A(a, b)$ for $a, b : A$, with the reflexivity term $\mathrm{refl}_a : \mathrm{Id}_A(a, a)$ and an induction rule.
5. Base types: the empty type $\mathbf{0}$, the unit type $\mathbf{1}$, the type $\mathbf{2}$ of booleans and the natural numbers $\N$. Each has introduction rules and an induction rule.
6. Universes $U_0 : U_1 : \cdots$, types whose terms are codes of types.

Each type former comes with formation, introduction, elimination and computation rules.

## Remarks

Under the [[Curry–Howard correspondence|HTF9E5W7EZ]], $\prod_{x : A} B(x)$ reads as "for all $x$ in $A$, $B(x)$", $\sum_{x : A} B(x)$ as "there is $x$ in $A$ with $B(x)$", and $\mathbf{0}$ as falsity.
Example: the term $\lambda n.\, (n + 1, \mathrm{refl}_{n+1})$ has type $\prod_{n : \N} \sum_{m : \N} \mathrm{Id}_{\N}(m, n + 1)$, so it proves that every natural number has a successor.
Non-example: there is no closed term of type $\prod_{A : U_0} (A + (A \to \mathbf{0}))$, so the [[intuitionistic logic|Q11N8X99FK]] of the theory does not include excluded middle.
Martin-Löf gave several versions, with intensional or extensional identity types.
