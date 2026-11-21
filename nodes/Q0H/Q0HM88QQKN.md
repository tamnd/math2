---
tag: Q0HM88QQKN
kind: concept
name: Imaginary elements
aliases: [imaginary-elements, imaginary-element, m-eq, t-eq, canonical-parameter]
msc: ["03C07", "03C45"]
topics: [SZRM3N6BXW]
audience: grad
uses: [7R0SJPH37J, 7TDHDN8P96, 0G8VEZ3WTK, CY1TXHF6KQ, 0011MTQMR6, DSQ17TNW1C, 92SWXST1ZM]
sources:
  - url: https://en.wikipedia.org/wiki/Imaginary_element
    locator: Definitions
  - url: https://en.wikipedia.org/wiki/Imaginary_element
    locator: Examples
  - book: isbn:9780521763240
  - book: isbn:9780387987606
---

## Summary

Let $T$ be a complete [[theory|92SWXST1ZM]] and let $M \models T$.
For each formula $E(\bar x, \bar y)$ that $T$ proves to be an [[equivalence relation|0G8VEZ3WTK]] on $n$-tuples, add a new sort for the [[quotient|0011MTQMR6]] $M^n / E$ and a map $\pi_E$ from $M^n$ onto it.
The resulting [[many-sorted|7TDHDN8P96]] structure is $M^{\mathrm{eq}}$, its theory is $T^{\mathrm{eq}}$, and the elements of the new sorts are the *imaginary elements* of $M$.
For a [[definable set|CY1TXHF6KQ]] $X = \varphi(M, \bar b)$, the *canonical parameter* $\ulcorner X \urcorner$ is the class of $\bar b$ under "defines the same set"; the exact page is [[this definition|120S3V3975]].
Imaginaries turn definable sets, cosets and classes into elements, so that every [[interpretation|7R0SJPH37J]] becomes a definable set in one structure.

## Motivation

Many objects that a structure "knows about" are not elements of it.
A line in the plane $K^2$ is a set of points, a coset of a definable subgroup is a set of group elements, and a class of a definable equivalence relation is a set of tuples.
Automorphisms act on these objects, and one wants to speak of their fixed points, their orbits and the sets defined over them.
$M^{\mathrm{eq}}$ adds all of them at once as elements, in a way that does not change the definable sets of $M$ itself.
Then "the set $X$ is defined over $A$" becomes "the element $\ulcorner X \urcorner$ is in the definable closure of $A$", which is the language of Galois theory.

## Notation

$S_E$ is the sort of $E$-classes, and the home sort $S_=$ is the sort of real elements.
One writes $\operatorname{dcl}^{\mathrm{eq}}$ and $\operatorname{acl}^{\mathrm{eq}}$ for closure in $M^{\mathrm{eq}}$.
The notation $M^{\mathrm{eq}}$ and $T^{\mathrm{eq}}$ is Shelah's.
Some books add only the sorts that a given problem needs, or add finitely many sorts as a disjoint union.

## Remarks

### Examples

- In the theory of an equivalence relation with infinitely many infinite classes, each class is an imaginary that no real tuple codes; see [[this example|ZRJHD4RSXG]].
- A line in $K^2$, for a field $K$, has a canonical parameter, which is interdefinable with a real triple of normalized coefficients; see [[this example|AJFN2F6GKH]].
- An unordered pair $\set{a, b}$ is the class of $(a, b)$ under $(x_1 = y_1 \wedge x_2 = y_2) \vee (x_1 = y_2 \wedge x_2 = y_1)$. In a field it is coded by the real pair $(a + b, a b)$, by the roots of $X^2 - (a + b) X + a b$.
- For a $\emptyset$-definable subgroup $H$ of a group $G$, the cosets $g H$ form a sort of $G^{\mathrm{eq}}$.
- The field $\mathbb{Q}$ in the ring $\mathbb{Z}$ is a $\emptyset$-definable set in a sort of $\mathbb{Z}^{\mathrm{eq}}$, by its [[interpretation|T2TBP1SA2T]].

### Non-examples

- The classes of "infinitely close" in a non-archimedean real closed field are not imaginaries, since the relation is only type-definable; they are [[hyperimaginaries|NQPCDVV3NB]]. See [[this example|BE6P5Y177V]].
- In the field $\mathbb{R}$, the cosets $x + \mathbb{Z}$ are not imaginaries. Each definable subset of $\mathbb{R}$ is a finite union of points and intervals, by [[Tarski's theorem|FSJ9NGRRPA]], so $\mathbb{Z}$ and the relation $x - y \in \mathbb{Z}$ are not definable.

### Basic properties

- Automorphisms. Each [[automorphism|DSQ17TNW1C]] $\sigma$ of $M$ extends uniquely to $M^{\mathrm{eq}}$, by $\sigma(\bar a / E) = \sigma(\bar a) / E$. It is well defined because $E$ is $\emptyset$-definable, and unique because $\pi_E$ is onto.
- Conservativity. Each $L^{\mathrm{eq}}$-formula whose free variables are of the home sort is equivalent in $T^{\mathrm{eq}}$ to an $L$-formula. So $M^{\mathrm{eq}}$ adds no new definable subsets of $M^n$, and $M \preceq N$ implies $M^{\mathrm{eq}} \preceq N^{\mathrm{eq}}$.
- Codes and automorphisms. For $\sigma \in \operatorname{Aut}(M)$, we have $\sigma(X) = X$ exactly when $\sigma(\ulcorner X \urcorner) = \ulcorner X \urcorner$. Both say that $\sigma \bar b$ and $\bar b$ define the same set.
- Codes and definability. $X$ is defined over $\ulcorner X \urcorner$ in $M^{\mathrm{eq}}$ by $\exists \bar y \, (\pi(\bar y) = \ulcorner X \urcorner \wedge \varphi(\bar x, \bar y))$. In the [[monster model|EYTTQZ0E1S]], $X$ is definable over $A$ exactly when $\ulcorner X \urcorner \in \operatorname{dcl}^{\mathrm{eq}}(A)$.
- Interpretations. Each $\emptyset$-interpretation of $N$ in $M$ makes $N$ a $\emptyset$-definable set of a sort of $M^{\mathrm{eq}}$, with $\emptyset$-definable relations.

### History

Shelah introduced $M^{\mathrm{eq}}$ and $T^{\mathrm{eq}}$ in his book *Classification Theory and the Number of Nonisomorphic Models* of 1978.
Poizat used imaginaries in 1983 to give a Galois theory of definable closure, and defined the [[elimination of imaginaries|6M2R0ER3KV]].
In categorical logic, adding quotients and finite disjoint unions of definable sets corresponds to the pretopos completion of the category of definable sets.

### Common errors

- Thinking that $M^{\mathrm{eq}}$ changes the model theory of $M$. By conservativity, it does not change the definable sets of real tuples, and each automorphism of $M$ extends uniquely.
- Forgetting that the canonical parameter depends on the formula. Two formulas for the same set give interdefinable codes, not equal ones.
- Confusing imaginaries with hyperimaginaries. Imaginaries come from definable equivalence relations, and hyperimaginaries from type-definable ones.

## Explanations

### L1 human

A structure has elements, and it also has groups of elements, like the lines of a plane.
Imaginary elements are names for such groups.
The line through $(0, 1)$ and $(1, 3)$ is the set of points with $y = 2 x + 1$.
It gets the name $(2, 1)$, its slope and its height at $x = 0$.
Any symmetry of the plane that keeps the line in place also keeps its name in place, and the converse holds as well.

### L2 human

We code the unordered pair $\set{2, 3}$ in the field $\mathbb{Q}$.

1. The ordered pairs $(2, 3)$ and $(3, 2)$ are equivalent under the relation "same set of two entries".
2. The imaginary $e = (2, 3) / E$ is the pair without order.
3. The sum and product, $2 + 3 = 5$ and $2 \cdot 3 = 6$, are the same for both ordered pairs.
4. Conversely, $5$ and $6$ give back $\set{2, 3}$, as the roots of $X^2 - 5 X + 6$.
5. So $e$ and the real pair $(5, 6)$ are interdefinable.

The typical use is to replace an imaginary by real elements when the theory allows it.
A trap is to expect this in every theory: in the theory of one equivalence relation with infinitely many infinite classes, no real tuple codes a class.

### L3 human

$M^{\mathrm{eq}}$ is a canonical object attached to $M$.
A $\emptyset$-[[bi-interpretation|KHZ1E7RMMQ]] between $M$ and $N$ identifies each sort of $N^{\mathrm{eq}}$ with a $\emptyset$-definable set of $M^{\mathrm{eq}}$, and conversely, so the two carry the same definable sets.
In stability theory, canonical bases of types are imaginaries, and forking calculus works in $M^{\mathrm{eq}}$ from the start; see [[stable theories|T7JW5QY6KR]].
When the theory has [[elimination of imaginaries|6M2R0ER3KV]], the imaginaries can be replaced by real tuples, as in algebraically closed fields.
Quotients by type-definable relations lead to the [[hyperimaginaries|NQPCDVV3NB]] of simple theories, and the induced structure on a sort leads to [[stably embedded sets|14WPPDDK8M]].
