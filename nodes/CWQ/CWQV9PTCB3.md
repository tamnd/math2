---
tag: CWQV9PTCB3
kind: definition
name: Model
msc: ["03C07"]
topics: [NJDME6F845]
audience: ug2
defines: MVCH6N9SNW
uses: [92SWXST1ZM, 983GZBQYT4, DKFGQTRYZE, 71X7TB3F98]
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

A model of a set of sentences is a structure in which all of the sentences are true.

Let $L$ be a signature and let $T$ be a set of $L$-[[sentences|DKFGQTRYZE]], for example an $L$-[[theory|92SWXST1ZM]].
An $L$-[[structure|983GZBQYT4]] $\mathcal{M}$ is a model of $T$ when $\mathcal{M} \models \sigma$ for every sentence $\sigma \in T$, where $\mathcal{M} \models \sigma$ means that $\sigma$ is [[true in $\mathcal{M}$|71X7TB3F98]].
The set $T$ is satisfiable when it has a model.

## Notation

The notation is $\mathcal{M} \models T$, and the class of all models of $T$ is written $\operatorname{Mod}(T)$.
In Mathlib, `M ⊨ T` is the class `FirstOrder.Language.Theory.Model`.

## Remarks

The definition has two parts, and each one matters.
The structure must be an $L$-structure, so that each sentence of $T$ can be evaluated in it.
Every sentence of $T$ must be true, so one false axiom is enough to spoil a model.
In particular, the empty set of sentences has every $L$-structure as a model.

For an example, let $T$ be the group axioms in the signature $\{\cdot, e, {}^{-1}\}$.
The structure $(\mathbb{Z}, +, 0, -)$, with $\cdot$ read as $+$, $e$ as $0$ and ${}^{-1}$ as $-$, is a model of $T$, because addition of integers is associative, $0$ is neutral, and $-a$ is an inverse of $a$.
The structure $(\mathbb{N}, +, 0, \operatorname{id})$, with ${}^{-1}$ read as the identity map, is not a model of $T$.
There the sentence $\forall x \, (x \cdot x^{-1} = e)$ fails at $x = 1$, because $1 + 1 \neq 0$.
The [[concept page on models|MVCH6N9SNW]] lists the basic properties of $\operatorname{Mod}(T)$.

## Explanations

### L1 human

To check that a structure is a model of a set of axioms, you check each axiom in the structure.
Every group is a model of the group axioms, and every model of the group axioms is a group.

### L2 human

We test the definition on $T = \{ \forall x \, \forall y \, (x \cdot y = y \cdot x) \}$ and two structures.
In $(\mathbb{Z}, +)$, for all integers $a$ and $b$ we have $a + b = b + a$, so every assignment satisfies $x \cdot y = y \cdot x$, and $(\mathbb{Z}, +) \models T$.
In the symmetric group $S_3$, the transpositions $a = (1 \, 2)$ and $b = (2 \, 3)$ give
$$ab = (1 \, 2 \, 3) \neq (1 \, 3 \, 2) = ba,$$
so the assignment $x \mapsto a$, $y \mapsto b$ fails, and $S_3$ is not a model of $T$.

The typical use is to sort structures by the axioms they satisfy, and here the abelian groups are the groups that are models of $T$.
Watch out: a model must satisfy every sentence of $T$, including the axioms that look harmless.
