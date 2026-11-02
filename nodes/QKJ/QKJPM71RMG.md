---
tag: QKJPM71RMG
kind: definition
name: Model category
msc: [18N40, 55U35]
defines: SDTZVZ6B4Q
uses: [A2DE66937D, CHS5AFJGWE, BJS1CGTKQ5, E2870TEDG7, AZK4RD8XV0, DXJH3DGXBC]
sources:
  - url: https://en.wikipedia.org/wiki/Model_category
    locator: Definition
---

## Definition

A *model category* is a [[category|A2DE66937D]] $\mathcal{M}$ with all small [[limits|CHS5AFJGWE]] and [[colimits|BJS1CGTKQ5]], together with three classes of morphisms.
They are the [[weak equivalences|E2870TEDG7]] $W$, the *fibrations* $\mathrm{Fib}$ and the *cofibrations* $\mathrm{Cof}$.
Each class contains the identities and is closed under composition.
A morphism in $\mathrm{Fib} \cap W$ is a *trivial fibration*, and a morphism in $\mathrm{Cof} \cap W$ is a *trivial cofibration*.
The classes satisfy the following axioms.

1. (two out of three) If $f$ and $g$ are composable and two of $f$, $g$, $g \circ f$ are in $W$, then so is the third.
2. (retracts) Each of $W$, $\mathrm{Fib}$ and $\mathrm{Cof}$ is closed under [[retracts|DXJH3DGXBC]] in the category of arrows of $\mathcal{M}$.
3. (lifting) Cofibrations have the left [[lifting property|AZK4RD8XV0]] with respect to trivial fibrations, and trivial cofibrations have the left lifting property with respect to fibrations.
4. (factorization) Every morphism $f$ factors as $f = p \circ i$ with $i$ a trivial cofibration and $p$ a fibration. It also factors as $f = q \circ j$ with $j$ a cofibration and $q$ a trivial fibration.

## Remarks

Some authors ask only for finite limits and colimits, as Quillen did, and some ask the factorizations in axiom 4 to be functorial.

Example: let $\mathcal{C}$ be any category with all small limits and colimits, let $W$ be the isomorphisms, and let $\mathrm{Fib}$ and $\mathrm{Cof}$ be all morphisms.
Isomorphisms satisfy two out of three and are closed under retracts.
Every square lifts against an isomorphism, which settles axiom 3, and $f = f \circ \id = \id \circ f$ gives axiom 4.

Non-example: in the category of sets, let all three classes be all maps.
Then the map $i \colon \set{0, 1} \to \set{0}$ is a cofibration and a trivial fibration.
Consider the commutative square with $i$ on both vertical sides, $\id$ on $\set{0, 1}$ on top and $\id$ on $\set{0}$ below.
A lift would be a map $h \colon \set{0} \to \set{0, 1}$ with $h \circ i = \id$, which does not exist, so axiom 3 fails.

The main example is the Quillen model structure on topological spaces: weak equivalences are weak homotopy equivalences, fibrations are Serre fibrations, and cofibrations are retracts of relative cell complexes.
An object $X$ is *fibrant* if $X \to \ast$ is a fibration and *cofibrant* if $\emptyset \to X$ is a cofibration.
