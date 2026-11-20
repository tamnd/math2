---
tag: K67C2N2QAH
kind: concept
name: Affine logic
msc: ["03F52", "03B47"]
topics: [98QF5J4W16]
audience: research
uses: [2P2184B6HE, H408H4WHBA, VHRXX0T5XT, ~54d8cf2f, 0HESMMSYEG]
sources:
  - wikipedia: en:76765067@r1368301704
    locator: Glossary of logic, section A
    note: adopted
    mention: wikipedia://en/76765067#DJVM
    sections: [Summary]
  - url: https://en.wikipedia.org/wiki/Affine_logic
    locator: lead
  - url: https://en.wikipedia.org/wiki/Linear_logic
    locator: Decidability/complexity of entailment; Variants
  - url: https://plato.stanford.edu/entries/logic-linear/
    locator: 1.1 Linear logic and other substructural logics; 4. Complexity
    note: Di Cosmo and Miller, Linear Logic, Stanford Encyclopedia of Philosophy, revision of 2023-09-16
  - url: https://en.wikipedia.org/wiki/BCK_algebra
    locator: lead
  - doi: 10.1006/inco.1999.2834
    locator: pages 173-198
    note: Kopylov, Decidability of linear affine logic, Information and Computation 164 (2001)
  - doi: 10.1070/IM1982v018n01ABEH001382
    locator: pages 41-59
    note: Grišin, Predicate and set-theoretic calculi based on logic without contractions, Mathematics of the USSR Izvestiya 18 (1982)
inventory: [46SEPVAV98]
---

## Summary

*Affine logic* is the substructural logic with [[weakening|VHRXX0T5XT]] but without [[contraction|~54d8cf2f]].
In its usual form it is [[linear logic|2P2184B6HE]] with the weakening rule added for all formulas, not only for formulas $?A$; the [[precise definition|~963ba4ac]] gives the rules.
In the resource reading, each hypothesis may be used at most once, where linear logic demands exactly once.
Affine logic is decidable, while full linear logic is not.

## Motivation

Contraction is the rule that lets a proof use a hypothesis twice.
The Wikipedia article states that Grishin observed that [[Russell's paradox|0HESMMSYEG]] is not derivable in a set theory without contraction, even with unrestricted [[comprehension|DMB4229W04]].
So a logic that drops contraction and keeps weakening is a natural base for such a set theory.

## Notation

We use the one-sided sequent calculus of [[linear logic|H408H4WHBA]], with $A \multimap B = A^{\perp} \mathbin{\wp} B$.
The rule of weakening is: from $\vdash \Gamma$ infer $\vdash \Gamma, A$, for any formula $A$.
Some authors call the logic *linear affine logic* or *affine linear logic*.

## Remarks

### Examples

1. [[$A \otimes B \multimap A$|~f904a999]] is derivable: discard $B$ by weakening.
2. The [[implications B, C and K|~593258d3]] are derivable; K needs weakening, and B and C are already linear.
3. In affine logic $1$ and $\top$ are equivalent, since weakening gives $\vdash 0, 1$ from $\vdash 1$, which is $\top \multimap 1$.

### Non-examples

[[$A \multimap A \otimes A$ is not derivable|~baf61dfc]] in affine logic, since affine logic has no contraction.
Linear logic is not affine: in it, $p \otimes q \multimap p$ is not derivable, as the [[example|~f904a999]] shows for MALL.

### Basic properties

1. $A \otimes B \multimap A \mathbin{\&} B$ is derivable: weakening gives $\vdash A^{\perp}, B^{\perp}, A$ and $\vdash A^{\perp}, B^{\perp}, B$, and the rule for $\mathbin{\&}$ joins them.
2. The Wikipedia article states that affine logic embeds into linear logic by sending $A \rightarrow B$ to $A \multimap B \otimes \top$.
3. The SEP entry states that linear logic with unrestricted weakening is decidable (Kopylov 1995) and hard for exponential space (Urquhart 2000).
4. Full propositional [[linear logic is undecidable|~673b5224]], so adding weakening makes the decision problem easier.

### History

The Wikipedia article states that affine logic predated linear logic and that Grishin used it in 1974, with a later paper in 1981.
It states that Girard introduced the name "affine logic", as an allusion to affine transformations in the geometry of interaction.
The decidability proof of Kopylov was first presented in 1995, as the Wikipedia article on linear logic states.

### Common errors

Affine logic is not a logic of affine transformations; the name only alludes to them.
Affine logic is an extension of linear logic, not a fragment: it proves more sequents.

## Explanations

### L1 human

Think of each hypothesis as a coin.
In linear logic you must spend every coin exactly once.
In affine logic you may also leave a coin unspent, but you still cannot spend a coin twice.

### L2 human

We derive $\top \multimap 1$, which shows that $1$ and $\top$ are equivalent in affine logic.

1. $\vdash 1$ is an axiom.
2. Weakening adds the formula $0$: $\vdash 0, 1$.
3. Since $\top^{\perp} = 0$, the sequent is $\vdash \top^{\perp}, 1$.
4. The rule $\mathbin{\wp}$ gives $\vdash \top^{\perp} \mathbin{\wp} 1$, which is $\top \multimap 1$.
5. $1 \multimap \top$ is $\vdash \bot, \top$, an instance of the axiom for $\top$.

The typical use of affine logic is to model resources that may be discarded but not copied.
A trap: affine logic keeps contraction for formulas $?A$, so $!A \multimap A \otimes A$ is still derivable.

### L3 human

The Wikipedia article states that affine logic is the foundation of [[ludics|~dbdabe57]].
The Wikipedia article on BCK algebras states that these algebras describe an implicational logic called BCK logic.
The [[formulas B, C and K|~593258d3]] are derivable in affine logic, and only K needs weakening.
