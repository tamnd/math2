---
tag: WYJ1D6HPJ5
kind: example
name: Global truth in a model is not a normal modal logic
msc: ["03B45"]
topics: [SPQVNPZDTB]
audience: research
not_instance_of:
  - target: EZ011FT3GT
    note: the formulas true in one model are not closed under uniform substitution, so they do not form a normal modal logic
uses: [EZ011FT3GT, DE0GD8BM4M, G989VP2NGP, NGHWZ9Y7ZV]
sources:
  - url: https://en.wikipedia.org/wiki/Normal_modal_logic
    locator: Common normal modal logics
  - url: https://en.wikipedia.org/wiki/Kripke_semantics
    locator: Correspondence and completeness
---

## Example

Let $\mathfrak{M}$ be the [[Kripke model|NGHWZ9Y7ZV]] with one world $a$, the relation $\{(a, a)\}$, and $p$ true at $a$.
Let $\mathrm{Th}(\mathfrak{M})$ be the set of formulas true at every world of $\mathfrak{M}$.
We show that $\mathrm{Th}(\mathfrak{M})$ passes every test for a normal modal logic except one, so it is not an element of the [[lattice of normal modal logics|EZ011FT3GT]].

1. Tautologies and the axiom K: the formulas $\square(p \to q) \to (\square p \to \square q)$ and all tautologies are true at every world of every model, so they lie in $\mathrm{Th}(\mathfrak{M})$.
2. Modus ponens: if $\varphi$ and $\varphi \to \psi$ are true at $a$, then $\psi$ is true at $a$.
3. [[Necessitation|G989VP2NGP]]: if $\varphi$ is true at every world, then $\square \varphi$ is true at every world, because every successor is a world.
4. The formula $p$ lies in $\mathrm{Th}(\mathfrak{M})$, since $p$ is true at $a$.
5. [[Uniform substitution|DE0GD8BM4M]] fails: substituting $\bot$ for $p$ turns $p$ into $\bot$, which is false at $a$.
6. So $\mathrm{Th}(\mathfrak{M})$ is closed under modus ponens and necessitation, but not under substitution, and it is not a normal modal logic.

## Remarks

The example shows why logics are defined by validity on frames, which ranges over all valuations, and not by truth in one model.
The formulas valid on the frame $(\{a\}, \{(a, a)\})$ form the normal logic $\mathrm{Log}(\circ)$, and $p$ is not among them.
Every maximal consistent set fails substitution in the same way, since it contains $p$ or $\neg p$, and substituting $\bot$ or $\top$ for $p$ gives $\bot$ or $\neg \top$.
In algebraic terms, a model fixes one element of a modal algebra for each variable, while a logic must hold for every choice of elements.

Watch out: closure under necessitation holds for truth at every world of a model, but it fails for truth at one world.
In a model where $a$ sees a world $b$ with $p$ false, $p$ can hold at $a$ while $\square p$ fails there.
So "true in the model" and "true at a world" are two different notions, and neither gives a logic.

## Explanations

### L1 human

A model fixes which basic statements are true; here it says "$p$ is true".
A logic may only contain laws that hold whatever the basic statements say.
"$p$ is true" holds in this model, but it is not a law, because replacing $p$ by a false statement breaks it.
So the truths of one model are not a logic.

### L2 human

We push the substitution test further.
In $\mathfrak{M}$, the three formulas $p$, $\square p$ and $\lozenge p$ are all true at $a$.
Substitute $\neg p$ for $p$ in each, to get $\neg p$, $\square \neg p$ and $\lozenge \neg p$.
At $a$ we have $p$, and $a$ sees only $a$, so all three new formulas are false.
On the frame of $\mathfrak{M}$, with every valuation, the formula $\square p \leftrightarrow p$ is valid, and it does survive every substitution.
The typical use of the example is to separate the notion of a theory, the truths of one structure, from the notion of a logic.
