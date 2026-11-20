---
tag: AX9Q86GB8M
kind: concept
name: Ultraproduct
aliases: [ultraproduct-of-structures]
msc: ["03C20"]
topics: [HZG1YP26AB]
audience: ug2
uses: [983GZBQYT4, WDVVEYD6AT, J64Y3JC0RE, F4WRD396PB, 09CEDJYBKP]
sources:
  - url: https://en.wikipedia.org/wiki/Ultraproduct
    locator: lead section
  - book: isbn:9780387987606
  - book: isbn:9780521587136
same_as:
  wikidata: Q1535225
  wikipedia: Ultraproduct
---

## Summary

Let $L$ be a [[signature|WDVVEYD6AT]], let $\mathcal{U}$ be an [[ultrafilter|J64Y3JC0RE]] on a nonempty set $I$, and let $(\mathcal{M}_i)_{i \in I}$ be $L$-[[structures|983GZBQYT4]] with nonempty domains $M_i$.
The *ultraproduct* $\prod_{i \in I} \mathcal{M}_i / \mathcal{U}$ is the [[reduced product|F4WRD396PB]] of the $\mathcal{M}_i$ modulo $\mathcal{U}$.
Its elements are the classes $[a]$ of elements $a$ of the [[Cartesian product|09CEDJYBKP]] $\prod_{i \in I} M_i$, where $a$ and $b$ are identified when $\set{i : a(i) = b(i)} \in \mathcal{U}$.
Functions act coordinatewise, and a relation holds of $[a_1], \dots, [a_n]$ when it holds coordinatewise on a set of indices in $\mathcal{U}$.
By [[Łoś's theorem|AGYBSTD7BG]], every first-order formula holds in the ultraproduct exactly when it holds in the factors for a set of indices in $\mathcal{U}$.
So an ultraproduct is a first-order "average" of its factors, and it is the main algebraic tool to build models without syntax.

## Motivation

Many arguments need a structure that has every first-order property shared by "most" members of a family.
The direct product does not work: $\Q \times \Q$ is not a field, because "or" and "not" do not pass to products.
A reduced product modulo a filter keeps more, but a filter may contain neither a set nor its complement, and then negation fails.
An ultrafilter decides every set of indices: for each $X \subseteq I$, either $X$ or $I \setminus X$ is in $\mathcal{U}$.
With this choice, truth in the quotient is truth on a large set of factors, for every formula.
Ultraproducts thus give the [[compactness theorem|1NR3HAWG9D]], nonstandard models such as the [[hyperreal numbers|421QMTFG9T]], and a link between finite structures and infinite ones.

## Notation

We write $\prod_{i \in I} \mathcal{M}_i / \mathcal{U}$, $\prod_{\mathcal{U}} \mathcal{M}_i$ or $\prod \mathcal{M}_i / \mathcal{U}$, and $[a]$ or $[a]_{\mathcal{U}}$ for the class of $a$.
When all factors equal $\mathcal{M}$, the ultraproduct is the [[ultrapower|~93a646cd]] $\mathcal{M}^I / \mathcal{U}$.
Chang and Keisler write $D$ for the ultrafilter, and some texts write $\mathcal{F}$.
The truth set of a formula $\varphi$ at $a_1, \dots, a_n$ is $[\![ \varphi(a_1, \dots, a_n) ]\!] = \set{i \in I : \mathcal{M}_i \models \varphi(a_1(i), \dots, a_n(i))}$.
In Mathlib, ultraproducts of first-order structures are in the namespace `FirstOrder.Language.Ultraproduct`.
The formal construction, with the check that it is well defined, is the [[definition of the ultraproduct|VFPGADHJYA]].

## Remarks

### Examples

- For a nonprincipal ultrafilter $\mathcal{U}$ on $\N$, the ultrapower $\R^{\N} / \mathcal{U}$ of the ordered field $\R$ is a field of [[hyperreal numbers|421QMTFG9T]]; the class of $(1, 1/2, 1/3, \dots)$ is a positive infinitesimal.
- For a nonprincipal ultrafilter on the set of primes, the ultraproduct of the prime fields $\F_p$ is a field of characteristic $0$; see [[this example|~e99f36f5]].
- For a principal ultrafilter at $i_0$, the ultraproduct is isomorphic to $\mathcal{M}_{i_0}$; see [[this example|~7d5e0b68]].
- For a nonprincipal ultrafilter on $\N$, the ultrapower of $(\N, +, \cdot, 0, 1, <)$ is a nonstandard model of arithmetic; see [[this example|~3c3d87d7]].
- An ultraproduct of finite sets of unbounded size over a nonprincipal ultrafilter on $\N$ is infinite; see [[this example|~19a24785]].

### Non-examples

- The reduced power $\R^{\N} / F$ for the [[Fréchet filter|QN98V7NMCD]] $F$ is not an ultraproduct, since $F$ is not an ultrafilter; it is a ring with zero divisors. See [[this non-example|~d563b9b4]].
- An ultraproduct of finite sets is infinite, so the property "finite", which is not first-order, is not kept; see [[this non-example|~08410ca2]].
- If one factor has an empty domain, the Cartesian product is empty, and the construction gives no structure; this is why domains are nonempty.

### Basic properties

- [[Łoś's theorem|AGYBSTD7BG]]: $\prod_{\mathcal{U}} \mathcal{M}_i \models \varphi([a_1], \dots, [a_n])$ if and only if $[\![ \varphi(a_1, \dots, a_n) ]\!] \in \mathcal{U}$.
- If each $\mathcal{M}_i$ is a model of a theory $T$, so is the ultraproduct; for example, ultraproducts of groups are groups and ultraproducts of fields are fields.
- If $\mathcal{U}$ is principal at $i_0$, then $\prod_{\mathcal{U}} \mathcal{M}_i \cong \mathcal{M}_{i_0}$.
- If $\mathcal{U}$ is nonprincipal on a countable set $I$ and the language is countable, the ultraproduct is $\aleph_1$-saturated; see [[saturation of ultraproducts|~bf3451a3]].
- An ultraproduct of a countably infinite family over a nonprincipal ultrafilter on $\N$ is finite or has at least $2^{\aleph_0}$ elements.

### History

Jerzy Łoś defined ultraproducts of general structures and proved his theorem in 1955.
In the early 1960s Frayne, Morel, Scott and Keisler developed the theory, and Keisler and later Shelah described elementary equivalence through ultrapowers.
Abraham Robinson's [[nonstandard analysis|WM62GKCBWN]] of the 1960s can be built on an ultrapower of the real field.

### Common errors

- To expect something new from a principal ultrafilter: it gives back one factor.
- To believe that Łoś's theorem holds for all properties. It holds for first-order formulas, and it fails for "finite", "well ordered" or "complete as an ordered field".
- To forget the axiom of choice: nonprincipal ultrafilters need the [[ultrafilter lemma|3MKZST79MK]], and the proof of Łoś's theorem chooses witnesses.

## Explanations

### L1 human

Take infinitely many copies of the real numbers, one for each natural number.
An element of the new structure is an infinite list of reals, one from each copy.
An ultrafilter is a rule that says, for each set of positions, whether it counts as "most" positions.
Two lists count as equal when they agree at most positions.
The list $1, 2, 3, \dots$ is then larger than every ordinary number $r$, because it is larger than $r$ at all but finitely many positions.
So the new structure contains infinitely large numbers.

### L2 human

Let $\mathcal{U}$ be a nonprincipal ultrafilter on $\N$, and let $\mathcal{H} = \R^{\N} / \mathcal{U}$ be the ultrapower of the ordered field $\R$.
We show that $\mathcal{H}$ is linearly ordered and has an element above every real.

1. Let $[a], [b] \in \mathcal{H}$, and let $X = \set{n : a(n) \le b(n)}$.
2. Its complement is $\set{n : b(n) < a(n)}$, and one of the two sets is in $\mathcal{U}$.
3. In the first case $[a] \le [b]$, and in the second case $[b] \le [a]$. So the order is linear.
4. Let $\omega = [(0, 1, 2, \dots)]$ and $r \in \R$. The set $\set{n : n > r}$ is cofinite.
5. A nonprincipal ultrafilter contains every cofinite set, so $\omega > r$ in $\mathcal{H}$, where $r$ stands for the class of the constant sequence.

The typical use is to read a property of the ultraproduct from the factors by Łoś's theorem.
The trap is step 2 with a filter that is not an ultrafilter: then neither set may be large, and linearity fails.

### L3 human

An ultraproduct is a filtered colimit of products, and the ultrafilter makes the colimit preserve all first-order logic, not only Horn formulas.
In categorical logic, Makkai and later Lurie studied categories of models together with their ultraproducts, called ultracategories, to recover a theory from its models.
In analysis, the [[ultralimit|3R9GQGFHP5]] of a bounded sequence along $\mathcal{U}$ and ultraproducts of Banach spaces follow the same pattern with a norm instead of equality.
In algebra, ultraproducts of finite fields are pseudofinite fields, and they connect statements about all large primes with characteristic $0$.
Ultrapowers lead to [[saturation|~bf3451a3]], the [[Keisler-Shelah theorem|~4f3e3ffa]] and [[Keisler's order|~889bca65]], and in set theory to measurable cardinals.
