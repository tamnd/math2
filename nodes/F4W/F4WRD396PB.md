---
tag: F4WRD396PB
kind: concept
name: Reduced product
aliases: [reduced-power, reduced-direct-product]
msc: ["03C20", "08B25"]
topics: [HZG1YP26AB]
audience: grad
uses: [983GZBQYT4, WDVVEYD6AT, 15PF73BKY6, 09CEDJYBKP, WJ73XYBNE4]
sources:
  - url: https://en.wikipedia.org/wiki/Reduced_product
    locator: lead section
  - book: isbn:9780521587136
same_as:
  wikidata: Q7306336
  wikipedia: Reduced product
---

## Summary

Let $L$ be a [[signature|WDVVEYD6AT]], let $I$ be a nonempty set, let $F$ be a [[filter|15PF73BKY6]] on $I$, and let $(\mathcal{M}_i)_{i \in I}$ be $L$-[[structures|983GZBQYT4]] with nonempty domains $M_i$.
On the [[Cartesian product|09CEDJYBKP]] $\prod_{i \in I} M_i$ put $a \sim_F b$ when $\set{i \in I : a(i) = b(i)} \in F$.
The *reduced product* $\prod_{i \in I} \mathcal{M}_i / F$ has the classes $[a]_F$ as its elements.
Functions and constants act coordinatewise on representatives.
A relation $R$ holds of $([a_1]_F, \dots, [a_n]_F)$ when the set of indices $i$ with $(a_1(i), \dots, a_n(i)) \in R^{\mathcal{M}_i}$ lies in $F$.
For $F = \set{I}$ this is the [[direct product|WJ73XYBNE4]], and for an [[ultrafilter|J64Y3JC0RE]] it is the [[ultraproduct|AX9Q86GB8M]].
Reduced products keep every Horn sentence of the factors, and they are the common frame for direct products and ultraproducts.

## Motivation

The direct product of two fields is not a field: in $\Q \times \Q$ the element $(1, 0)$ is not zero and has no inverse.
A product keeps equations, but it loses statements with "or" and "not", such as "every nonzero element is invertible".
A filter lets us ignore a "small" set of coordinates.
Two elements count as equal when they agree on a "large" set of indices.
The larger the filter, the more properties survive, and for a maximal filter all first-order properties survive, by [[Łoś's theorem|AGYBSTD7BG]].
Reduced products are the steps between these two extremes, and they show which sentences survive with any filter at all: the Horn sentences.

## Notation

We write $\prod_{i \in I} \mathcal{M}_i / F$ or $\prod_F \mathcal{M}_i$, and $[a]_F$ or $[a]$ for the class of $a$.
When all factors equal $\mathcal{M}$, we write $\mathcal{M}^I / F$ and speak of a *reduced power*.
Chang and Keisler write $D$ for the filter.
For a formula $\varphi(x_1, \dots, x_n)$ and $a_1, \dots, a_n \in \prod_{i \in I} M_i$, the *truth set* is
$$[\![ \varphi(a_1, \dots, a_n) ]\!] = \set{i \in I : \mathcal{M}_i \models \varphi(a_1(i), \dots, a_n(i))}.$$
The formal definition, with the check that the interpretations do not depend on the representatives, is the [[definition of the reduced product|84XXPH6XJ8]].

## Remarks

### Examples

- For $F = \set{I}$, the relation $\sim_F$ is equality, so the reduced product is the direct product; see [[this example|J2C48GYQWG]].
- For a nonempty $J \subseteq I$ and the filter $F = \set{X \subseteq I : J \subseteq X}$, the reduced product is isomorphic to $\prod_{j \in J} \mathcal{M}_j$, because only the coordinates in $J$ matter.
- For the [[Fréchet filter|QN98V7NMCD]] of cofinite subsets of $\N$, the reduced power $\R^{\N} / F$ is a commutative ring that is not a field; see [[this example|7TJPSD6H5P]].
- For the Fréchet filter $F$, the reduced power $(\N, \le)^{\N} / F$ is a partial order that is not linear; see the L2 explanation below.

### Non-examples

- The relation "agree on infinitely many indices" on $\Z^{\N}$ is not transitive, so it gives no reduced product; the infinite sets do not form a filter. See [[this non-example|W2J10Y5TC5]].
- For $I = \set{1, 2, 3}$, the family $\set{\set{1, 2}, \set{2, 3}, I}$ is not closed under intersection, and the relation it defines on $\Z^3$ is not transitive.
- If we allow the improper filter $\mathcal{P}(I)$, then any two elements are equal and every relation holds, so the quotient is a one-point structure that keeps no information. This is why filters are proper.

### Basic properties

- The relation $\sim_F$ is an equivalence relation, and the interpretations are well defined, because $F$ is closed under supersets and finite intersections.
- For an atomic formula $\alpha$, $\prod_F \mathcal{M}_i \models \alpha([a_1], \dots, [a_n])$ if and only if $[\![ \alpha(a_1, \dots, a_n) ]\!] \in F$.
- [[Reduced products preserve Horn formulas|8RRECJJM3G]]: if a Horn formula holds on a set of indices in $F$, it holds in the reduced product.
- So every class of structures axiomatized by Horn sentences, such as groups, rings, partial orders and [[universal Horn classes|9A4CYWXPEA]], is closed under reduced products.
- If $F \subseteq G$ are filters, then $\prod_G \mathcal{M}_i$ is a quotient of $\prod_F \mathcal{M}_i$, by the map $[a]_F \mapsto [a]_G$.

### History

Alfred Horn studied in 1951 the sentences that are true of direct products, and the sentences now called Horn sentences come from that paper.
Frayne, Morel and Scott studied reduced products in general in their 1962 paper "Reduced direct products".
The book of Chang and Keisler develops reduced products, Horn sentences and their preservation in detail.

### Common errors

- To expect all first-order sentences to survive. The sentence "every nonzero element has an inverse" holds in each factor $\R$ and fails in $\R^{\N} / F$ for the Fréchet filter.
- To read the relation $R$ as "holds in some factor". It must hold on a set of indices in $F$.
- To forget that the truth set depends on the chosen representatives only up to a set outside $F$; statements about $[a]$ must not depend on the representative.

## Explanations

### L1 human

Think of an element of a product as an infinite list of entries, one from each factor.
A filter says which sets of positions are "large".
In a reduced product, two lists count as the same when they agree at a large set of positions.
With the filter of all sets that miss only finitely many positions, the lists $(5, 0, 0, 0, \dots)$ and $(0, 0, 0, 0, \dots)$ count as equal.
They differ at one position only, and one position is a small set.
Addition and multiplication are still done position by position.

### L2 human

Let $F$ be the Fréchet filter on $\N$, and let $P = (\N, \le)^{\N} / F$.
So $[a] \le [b]$ holds when $a(i) \le b(i)$ for all but finitely many $i$.

1. Reflexivity: $\set{i : a(i) \le a(i)} = \N \in F$, so $[a] \le [a]$.
2. Transitivity: if $[a] \le [b]$ and $[b] \le [c]$, then $a(i) \le c(i)$ holds on the intersection of two cofinite sets, which is cofinite.
3. Antisymmetry: if $[a] \le [b]$ and $[b] \le [a]$, then $a(i) = b(i)$ on a cofinite set, so $[a] = [b]$.
4. Let $a = (0, 1, 0, 1, \dots)$ and $b = (1, 0, 1, 0, \dots)$. Then $a(i) \le b(i)$ only for even $i$, and $b(i) \le a(i)$ only for odd $i$.
5. Neither set is cofinite, so $[a]$ and $[b]$ are incomparable, and $P$ is not a linear order.

The typical use is to transfer equations and implications from the factors to a quotient.
The trap is linearity: "$x \le y$ or $y \le x$" has two positive parts, so it is not a Horn sentence, and it fails in $P$.

### L3 human

The reduced product is a filtered colimit of products.
For $X \subseteq Y$ in $F$, project $\prod_{i \in Y} \mathcal{M}_i$ onto $\prod_{i \in X} \mathcal{M}_i$; the colimit of this directed system, indexed by $F$ under reverse inclusion, is $\prod_F \mathcal{M}_i$.
In the Boolean-valued view, a formula has the truth value $[\![ \varphi ]\!]$ in the power set algebra $\mathcal{P}(I)$, and the reduced product reads it in the quotient algebra $\mathcal{P}(I) / F$.
The [[Feferman-Vaught theorem|RYMZZ2AWFT]] makes this precise for all formulas.
The converse of Horn preservation also holds: a sentence that is preserved by all reduced products is equivalent to a Horn sentence.
Reduced products also appear in algebra as subdirect constructions and in the study of [[preservation theorems|JYJHB4YBAH]].
