---
tag: CWQV9PTCB3
kind: definition
name: Model
msc: ["03C07"]
topics: [NJDME6F845]
audience: ug2
defines: MVCH6N9SNW
uses: [92SWXST1ZM, 983GZBQYT4, DKFGQTRYZE, ~58a589d1]
formal:
  - system: lean4
    library: mathlib
    decl: FirstOrder.Language.Theory.Model
    match: exact
sources:
  - url: https://en.wikipedia.org/wiki/Structure_(mathematical_logic)
  - book: isbn:9780122384523
    locator: Section 2.2
  - url: https://builds.openlogicproject.org/
    locator: Theories and Their Models
---

## Definition

Let $L$ be a signature and let $T$ be a set of $L$-[[sentences|DKFGQTRYZE]], for example an $L$-[[theory|92SWXST1ZM]].
An $L$-[[structure|983GZBQYT4]] $\mathcal{M}$ is a model of $T$ when $\mathcal{M} \models \sigma$ for every sentence $\sigma \in T$.
Here $\mathcal{M} \models \sigma$ means that $\sigma$ is [[true in $\mathcal{M}$|~58a589d1]].
The set $T$ is satisfiable when it has a model.

## Notation

The notation is $\mathcal{M} \models T$.
The class of all models of $T$ is written $\operatorname{Mod}(T)$.
In Mathlib, `M ⊨ T` is the class `FirstOrder.Language.Theory.Model`.

## Remarks

Example: let $T$ be the set of group axioms in the signature $\set{\cdot, e, {}^{-1}}$.
The structure $(\Z, +, 0, -)$, with $\cdot$ read as $+$, $e$ as $0$ and ${}^{-1}$ as $-$, is a model of $T$.
Indeed addition of integers is associative, $0$ is neutral and $-x$ is an inverse of $x$.

Non-example: the structure $(\N, +, 0, \id)$, with ${}^{-1}$ read as the identity map, is not a model of $T$.
The sentence $\forall x \, (x \cdot x^{-1} = e)$ fails at $x = 1$, because $1 + 1 \neq 0$.

The empty set of sentences has every $L$-structure as a model.
The concept page [[model|MVCH6N9SNW]] lists the basic properties of $\operatorname{Mod}(T)$.

## Explanations

### L1 human

To check that a structure is a model of a set of axioms, you check each axiom in the structure.
Every group is a model of the group axioms, and every model of the group axioms is a group.

### L2 human

We check the definition on $T = \set{\forall x \, \forall y \, (x \cdot y = y \cdot x)}$ and two structures.

1. In $(\Z, +)$, for all integers $a$ and $b$ we have $a + b = b + a$, so every assignment satisfies $x \cdot y = y \cdot x$, and $(\Z, +) \models T$.
2. In the symmetric group $S_3$, the transpositions $a = (1 \, 2)$ and $b = (2 \, 3)$ give $ab \neq ba$.
3. So the assignment $x \mapsto a$, $y \mapsto b$ does not satisfy $x \cdot y = y \cdot x$, and $S_3$ is not a model of $T$.

The typical use is to sort structures by the axioms that they satisfy: here, abelian groups are the groups that are models of $T$.
A trap is to forget that a model of $T$ must satisfy every sentence of $T$, including the axioms that look harmless.
