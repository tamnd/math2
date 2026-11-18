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

Let $\mathfrak{M}$ be the Kripke model with one world $a$, the relation $\set{(a, a)}$, and $p$ true at $a$.
Let $\mathrm{Th}(\mathfrak{M})$ be the set of formulas true at every world of $\mathfrak{M}$.
We show that $\mathrm{Th}(\mathfrak{M})$ is not an element of the [[lattice of normal modal logics|EZ011FT3GT]].

1. $\mathrm{Th}(\mathfrak{M})$ contains all tautologies and the axiom $\square(p \to q) \to (\square p \to \square q)$, since these are true at every world of every model.
2. It is closed under modus ponens, since truth at a world respects $\to$.
3. It is closed under [[necessitation|G989VP2NGP]]: if $\varphi$ is true at every world, then $\square \varphi$ is true at every world.
4. It contains $p$, since $p$ is true at $a$.
5. The [[uniform substitution|DE0GD8BM4M]] of $\bot$ for $p$ sends $p$ to $\bot$, and $\bot$ is false at $a$. So $\mathrm{Th}(\mathfrak{M})$ is not closed under uniform substitution.
6. So $\mathrm{Th}(\mathfrak{M})$ satisfies every condition of a normal modal logic except closure under substitution, and it is not a normal modal logic.

## Remarks

The example shows why logics are defined by validity on frames, which quantifies over all valuations, and not by truth in a model.
The set of formulas valid on the frame $(\set{a}, \set{(a, a)})$ is the normal logic $\mathrm{Log}(\circ)$, and it does not contain $p$.
Every maximal consistent set of a consistent logic also fails closure under substitution, since it contains $p$ or $\neg p$.
In algebraic terms, a model fixes elements of a modal algebra for the variables, while a logic must hold for every choice of elements.

## Explanations

### L1 human

A model fixes which basic statements are true, here "$p$ is true".
A logic must contain only laws that hold whatever the basic statements say.
"$p$ is true" holds in this model but is not a law, because replacing $p$ by a false statement breaks it.
So the truths of one model are not a logic.

### L2 human

1. In $\mathfrak{M}$, the formulas $p$, $\square p$ and $\lozenge p$ are true.
2. Substituting $\neg p$ for $p$ gives $\neg p$, $\square \neg p$ and $\lozenge \neg p$, which are all false at $a$.
3. On the frame of $\mathfrak{M}$ with all valuations, $\square p \leftrightarrow p$ is valid, and it is in $\mathrm{Log}(\circ)$.

The typical use of the example is to separate the notions of theory and logic.
A trap: closure under necessitation holds for global truth in a model but fails for truth at one world, so the two notions of truth also differ.
