---
tag: M7D1HEJQVH
kind: object
name: Rathjen's psi function
msc: ["03F15", "03E55"]
topics: [XTTKZTYDSD]
audience: research
uses: [8S6CT4TMB7, E7WEFRMQTB, CJFEPPP9KA, 13ZV2F8JAR, 6FDYJVG1CK, JQFAE9S2F4, C5E5TG8PGP]
sources:
  - url: https://en.wikipedia.org/wiki/Rathjen%27s_psi_function
    locator: lead section
  - url: https://en.wikipedia.org/wiki/Rathjen%27s_psi_function
    locator: Explanation
  - url: https://en.wikipedia.org/wiki/Ordinal_collapsing_function
    locator: Collapsing large cardinals
---

## Description

Take the map $\kappa \mapsto \kappa^+$ that sends a cardinal to the next cardinal.
Its closure points, the cardinals $\lambda$ with $\kappa^+ < \lambda$ for all $\kappa < \lambda$, are the limit cardinals, and they form a closed unbounded class.
Below a weakly Mahlo cardinal $M$ one of these closure points is [[regular|13ZV2F8JAR]], so it is a weakly inaccessible cardinal, and the same holds for every normal function on $M$.
Rathjen's $\psi$ function turns this reflection property into names for countable ordinals.

A cardinal $M$ is weakly [[Mahlo|CJFEPPP9KA]] when it is regular and the regular cardinals below $M$ form a [[stationary set|6FDYJVG1CK]] in $M$.
Rathjen's system is a family of [[ordinal collapsing functions|8S6CT4TMB7]] built on such an $M$, and it has three kinds of function.

- Collapsing functions $\psi_\kappa$, one for each regular $\kappa < M$ that the system can name, and a function $\psi_\Omega$ with countable values. Each $\psi_\kappa(\alpha)$ is the least ordinal not in a closure set, as in [[Buchholz's system|E7WEFRMQTB]].
- Functions $\chi_\alpha$ that list the regular cardinals $\kappa < M$ which reflect the term $\alpha$, in the sense that the construction of $\alpha$ from names below $\kappa$ adds no ordinal between $\kappa$ and $M$.
- Addition and the [[Veblen function|JQFAE9S2F4]], which handle the predicative part.

So $M$ is collapsed in two steps: $\chi$ produces regular cardinals below $M$ from terms above $M$, and $\psi_\kappa$ collapses each such $\kappa$ further.
The countable values $\psi_\Omega(\alpha)$ form an ordinal notation system strong enough for the set theory $\mathrm{KPM}$.
This theory is Kripke-Platek set theory with one more scheme: for each $\Delta_0$-formula $H(x, y)$, if $\forall x \, \exists y \, H(x, y)$, then some admissible set $z$ satisfies $\forall x \in z \, \exists y \in z \, H(x, y)$.

## Remarks

### Which $\psi$ this is

The letter $\psi$ has a third meaning here.
In the Wikipedia system of [[collapsing functions|8S6CT4TMB7]], $\psi$ has one argument and the names $0, 1, \omega, \Omega$.
In Buchholz's system, $\psi_\nu$ is indexed by the numbers $\nu \le \omega$.
In Rathjen's system, $\psi_\kappa$ is indexed by regular cardinals below a Mahlo cardinal, and $\psi_\Omega$ is the countable collapse.
The values depend on fine details of the closure sets, which differ between presentations, so we describe the structure and give no explicit values.

### Why a Mahlo cardinal

The axiom of $\mathrm{KPM}$ says that every total $\Delta_0$ relation is already total on some admissible set.
Its natural models $L_\mu$ in the constructible hierarchy have a recursively Mahlo height $\mu$, the recursive analogue of a Mahlo cardinal.
The weakly Mahlo $M$ is the large cardinal image of $\mu$: every normal function on $M$ has a regular closure point below $M$, because the regular cardinals are stationary and the closure points form a club.
The functions $\chi_\alpha$ make this reflection explicit inside the notation, just as the opening example finds a weakly inaccessible closure point of $\kappa \mapsto \kappa^+$.

### Where it sits

Each step up in the large ordinal of the notation matches a step up in the strength of the theory.
One uncountable $\Omega$ gives the [[Bachmann-Howard ordinal|QH3ENXFRSV]], the ordinal of Kripke-Platek set theory.
The tower $\Omega_1, \Omega_2, \dots, \Omega_\omega$ of Buchholz gives the [[Takeuti-Feferman-Buchholz ordinal|NZWRK062WQ]].
A weakly Mahlo $M$ gives the ordinal of $\mathrm{KPM}$, far beyond both.

### Watch out

Do not read Rathjen's $\psi_\Omega$ as Buchholz's $\psi_0$.
Both collapse to countable ordinals, but the closure operations differ, since Rathjen's sets contain the Veblen function and the $\chi$ functions.
So the same written term can denote different ordinals in the two systems.

### History

Rathjen published the analysis of $\mathrm{KPM}$ in "Proof-theoretic analysis of KPM", Archive for Mathematical Logic, 1991.
He gave the well-ordering proof in "Collapsing functions based on recursively large ordinals: a well-ordering proof for KPM", Archive for Mathematical Logic, 1994.
He later used a weakly compact cardinal in the same way to analyze Kripke-Platek set theory with $\Pi_3$-reflection.

## Explanations

### L1 human

Collapsing functions name small infinite ordinals with the help of much larger ones.
Buchholz used a ladder of larger and larger infinities for this.
Rathjen used a single, much larger infinity $M$, a Mahlo cardinal, that contains many ladders below itself.
A helper function picks the rungs of these ladders, and a collapse turns each expression into a countable ordinal.
The result names ordinals far beyond Buchholz's system.

### L2 human

Why does $M$ contain a weakly inaccessible cardinal?
The limit cardinals below $M$ form a closed unbounded set, since a limit of limit cardinals is a limit cardinal and above each $\kappa < M$ there is the limit cardinal $\aleph_{\kappa + \omega}$, which is below $M$ because $M$ is a regular limit cardinal.
A stationary set meets every closed unbounded set, so some regular cardinal below $M$ is a limit cardinal, and that is a weakly inaccessible.
The same argument, applied to the closure points of any normal function on $M$, gives the reflection that the $\chi$ functions use.

In [[ordinal analysis|C5E5TG8PGP]] this argument is the template for the reflection axiom of $\mathrm{KPM}$: a property of the whole universe is reflected down to an admissible set.
Watch out: this works only because the regular cardinals are stationary, and the least weakly inaccessible cardinal does not have that property.

### L3 human

The pattern continues beyond Mahlo cardinals.
Weakly compact cardinals give the notation for $\Pi_3$-reflection, and stronger reflection principles need stronger cardinals or their recursive analogues.
In each case the large cardinal is only a guide for the construction: the notation system itself is a primitive recursive set of terms, and the cardinal can be replaced by a recursively large ordinal in the well-ordering proof.
