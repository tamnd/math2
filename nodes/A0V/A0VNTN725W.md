---
tag: A0VNTN725W
kind: concept
name: Isolated type
aliases: [principal-type]
msc: ["03C07", "03C15"]
topics: [Z772KEC9BY]
audience: grad
uses: [9V71Q3SD1G, VDY4PG5WHN, 0A1YXSKB48, 655K8Y7VS8]
sources:
  - url: https://en.wikipedia.org/wiki/Type_(model_theory)
    locator: Omitting types theorem
  - url: https://en.wikipedia.org/wiki/Atomic_model_(mathematical_logic)
    locator: lead section
  - book: isbn:9780387987606
    locator: Chapter 4
---

## Summary

Let $T$ be an $L$-theory and let $p(\bar{x})$ be an $n$-[[type|9V71Q3SD1G]] of $T$.
A formula $\varphi(\bar{x})$ *isolates* $p$ when $T \cup \set{\varphi}$ is satisfiable and $T \models \forall \bar{x} \, (\varphi(\bar{x}) \to \psi(\bar{x}))$ for every $\psi \in p$.
The type $p$ is *isolated*, or *principal*, when some formula isolates it, and *non-isolated* or *non-principal* otherwise.
For types over a set $A$ in a structure $\mathcal{M}$, take $T = \operatorname{Th}_A(\mathcal{M})$ and $L_A$-formulas.
A complete type is isolated exactly when it is an [[isolated point|0A1YXSKB48]] of the [[Stone space|VDY4PG5WHN]] $S_n(T)$.
Isolated types of a [[complete theory|655K8Y7VS8]] are realized in every model, and the non-isolated types are the ones that a model can avoid.

## Motivation

Some types are forced on every model of a complete theory, and some are not.
In the field $\C$ the type of $\sqrt{2}$ over $\emptyset$ is forced, because $x \cdot x = 1 + 1$ has a solution in every model and every solution has this type.
The type of $\pi$ is not forced, since the algebraic numbers form a model without transcendental elements.
The difference is whether one formula carries the whole type.
This leads to the [[omitting types theorem|7MFGBVDVG9]] and to atomic and [[prime models|S8W40PYNHX]], the models that realize only isolated types.

## Notation

The words isolated and principal are synonyms; principal comes from the principal ultrafilters of the Lindenbaum algebra.
The isolating formula is sometimes called a generator or a complete formula when $p$ is complete.

## Remarks

### Examples

- In $\mathrm{ACF}_0$ the type of a root of an irreducible $g \in \Z[x]$ is isolated by $g(x) = 0$; see [[the type space of algebraically closed fields|6DP6ESTNYR]].
- For dense linear orders every complete $2$-type over $\emptyset$ is isolated by an atomic formula; see [[the 2-types of dense linear orders|3GD87G9ARX]].
- The type of an element of a structure $\mathcal{M}$ over a set $A$ that contains it is isolated by $x = a$.
- For $T = \operatorname{Th}(\N, 0, 1, +, \cdot, <)$ the type of the number $5$ is isolated by $x = \underline{5}$.

### Non-examples

- The [[type of an infinite natural number|Q0H5CJGCAY]] is not isolated, since any consistent formula has a standard witness.
- The transcendental type of $\mathrm{ACF}_0$ is not isolated: each formula in it holds at infinitely many algebraic numbers.
- In $(\R, <)$ the type of $\sqrt{2}$ over $\Q$ is not isolated, since every formula in it holds on an interval with other irrationals.

### Basic properties

- If $p$ is complete and $\varphi$ isolates it, then $\varphi \in p$: otherwise $\neg \varphi \in p$, so $T \models \varphi \to \neg \varphi$, against the consistency of $\varphi$.
- A complete $p$ is isolated by $\varphi$ exactly when $[\varphi] = \set{p}$, since a complete type that contains $\varphi$ contains every consequence of $\varphi$.
- If $T$ is complete and $\varphi$ isolates $p$, then $T \models \exists \bar{x} \, \varphi$, and a witness of $\varphi$ in any model realizes $p$.
- If $S_n(T)$ is countable, then the isolated types are dense in $S_n(T)$, by the Baire category theorem applied to each nonempty open set.
- A countable complete theory is $\aleph_0$-categorical exactly when every type over $\emptyset$ is isolated, by the [[Ryll-Nardzewski theorem|1513J40TKA]].

### History

The notion of isolated type appears in the omitting types theorem and in Vaught's study of prime and atomic models around 1960.

### Common errors

- Forgetting that $T$ must be complete for realization: in the theory of fields, $x \cdot x = 1 + 1$ isolates a type, and $\Q$ omits it.
- Confusing "isolated" with "realized": in $(\R, <)$ the type of $\sqrt{2}$ over $\Q$ is realized and not isolated.
- Checking only that $\varphi \in p$: the formula must imply every member of $p$ modulo $T$.

## Explanations

### L1 human

A type is isolated when one property already says everything that the type says.
The number $\sqrt{2}$ is pinned down, among complex numbers, by the single equation $x^2 = 2$, up to its sign.
A transcendental number such as $\pi$ is not pinned down by any single property.
So every model of the theory must contain an element like $\sqrt{2}$, but a model can avoid elements like $\pi$.

### L2 human

We show that the type $p$ of $\sqrt{2}$ over $\emptyset$ in the field $\C$ is isolated.

1. Let $\varphi(x)$ be $x \cdot x = 1 + 1$, and let $\psi(x) \in p$.
2. By quantifier elimination, $\psi$ is a Boolean combination of equations $f(x) = 0$ with $f \in \Z[x]$.
3. Both roots $\pm\sqrt{2}$ of $\varphi$ satisfy the same equations, since $f(\sqrt{2}) = 0$ exactly when $x^2 - 2$ divides $f$, and then $f(-\sqrt{2}) = 0$.
4. So $\psi$ holds at every root of $\varphi$ in every algebraically closed field of characteristic $0$, and $\varphi$ isolates $p$.

The typical use is to show that a type must be realized in every model.
The trap is to think that $x \ne 0$ isolates the type of $\pi$: it also holds at $\sqrt{2}$.

### L3 human

Under Stone duality an isolated type is an atom of the Lindenbaum algebra of the theory, and a theory whose algebras are atomic has a prime model in the countable case.
The isolated points of a compact space are the points of Cantor-Bendixson rank $0$, and higher ranks measure how far a type is from being isolated; this is the start of [[Morley rank|WN43DRPNBX]].
In the [[omitting types theorem|7MFGBVDVG9]], the closed set $[p]$ of a non-isolated type has empty interior, so it is nowhere dense, and a generic model avoids it.
