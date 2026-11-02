---
tag: WQ1ZE255SF
kind: statement
role: theorem
name: Gödel's completeness theorem
msc: [03B10, 03C07]
uses: [DKFGQTRYZE, 1HK0VYWTV7, 1MGMQX43B8, MVCH6N9SNW]
about: [1HK0VYWTV7, 086QKPF0A6]
sources:
  - url: https://en.wikipedia.org/wiki/Gödel's_completeness_theorem
same_as:
  wikidata: Q902052
  wikipedia: Gödel's completeness theorem
---

## Statement

Let $\sigma$ be a signature, let $\Gamma$ be a set of first-order [[sentences|DKFGQTRYZE]] over $\sigma$, and let $\varphi$ be a sentence over $\sigma$.
Let $\vdash$ be derivability in a standard [[Hilbert system|1MGMQX43B8]] for first-order logic with equality.
If $\Gamma \models \varphi$, as a [[logical consequence|1HK0VYWTV7]], then $\Gamma \vdash \varphi$.

## Remarks

Together with [[soundness|4A84VHDTHV]], the theorem gives that $\Gamma \vdash \varphi$ if and only if $\Gamma \models \varphi$.
An equivalent form: every consistent set of sentences has a [[model|MVCH6N9SNW]].
The usual proof is Henkin's.
Extend a consistent $\Gamma$ to a maximal consistent set with witnesses: for each sentence $\exists x \, \chi$ in it, a constant $c$ with $\chi(c)$.
The closed terms, modulo provable equality, then form a model.
Since derivations are finite, the theorem implies the [[compactness theorem|1NR3HAWG9D]].
For example, every sentence true in all groups is derivable from the group axioms.
The theorem is about first-order logic; full second-order logic has no sound and complete proof system of this kind.
Kurt Gödel proved the theorem in his doctoral thesis of 1929.

## Explanations

### L1 human

The theorem says that the rules of first-order proof are strong enough.
Whatever follows from some axioms, in the sense that it is true in every situation where the axioms are true, can actually be proved from them.
So "true in all models" and "provable" mean the same thing.

### L2 human

The completeness theorem links syntax with semantics.
To show that something is unprovable, it is enough to build a model where the axioms hold and the statement fails.
This is how independence results, such as those in set theory, are proved.
It should not be confused with the [[incompleteness theorems|X9WYNYE29C]]: these say that some theories are incomplete, meaning that they neither prove nor refute some sentence.
Both results hold at once, since such a sentence is true in some models of the theory and false in others.
