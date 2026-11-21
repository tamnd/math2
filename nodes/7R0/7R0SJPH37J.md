---
tag: 7R0SJPH37J
kind: concept
name: Interpretation
aliases: [interpretation-model-theory, interpretable-structure, interpretation-of-a-structure]
msc: ["03C07"]
topics: [SZRM3N6BXW]
audience: grad
uses: [983GZBQYT4, HYJ10AF6RT, CY1TXHF6KQ, 0G8VEZ3WTK, 0011MTQMR6, WDVVEYD6AT]
sources:
  - url: https://en.wikipedia.org/wiki/Interpretation_(model_theory)
    locator: Definition
  - url: https://en.wikipedia.org/wiki/Interpretation_(model_theory)
    locator: Example
  - book: isbn:9780387987606
    locator: Section 1.3
  - book: isbn:9780521587136
---

## Summary

Let $M$ be an $L$-[[structure|983GZBQYT4]], let $N$ be an $L'$-structure, and let $A \subseteq M$.
An *$n$-dimensional interpretation* of $N$ in $M$ over $A$ consists of an $L_A$-[[formula|HYJ10AF6RT]] $\partial(\bar x)$ in an $n$-tuple $\bar x$, an $L_A$-formula $\varepsilon(\bar x, \bar y)$, an $L_A$-formula $\varphi_S$ for each symbol $S$ of $L'$, and a surjective *coordinate map* $f : \partial(M^n) \to N$.
The conditions are: $f(\bar a) = f(\bar b)$ exactly when $M \models \varepsilon(\bar a, \bar b)$, and each relation, function graph or constant of $N$ holds at $f(\bar a_1), \dots, f(\bar a_k)$ exactly when $\varphi_S(\bar a_1, \dots, \bar a_k)$ holds in $M$.
So $N$ is a copy of a [[definable set|CY1TXHF6KQ]] modulo a definable [[equivalence relation|0G8VEZ3WTK]], with definable structure on the [[quotient|0011MTQMR6]]; the exact page is [[this definition|C5BWHPHAGA]].
Interpretations let one structure live inside another, so that every first-order fact about the inner structure becomes a first-order fact about the outer one.

## Motivation

Many constructions of algebra build a new structure from tuples and classes of an old one.
The rational numbers are pairs of integers modulo cross-multiplication, and the complex numbers are pairs of reals.
In each case the new elements, the new equality and the new operations are given by formulas of the old structure.
An interpretation records exactly these formulas.
Then a question about the new structure translates into a question about the old one, so decidability, stability and similar properties pass from the old structure to the new one.
The idea also explains why a structure "contains" a field or a group that is not a subset of it, as in the group of affine maps of a line.

## Notation

One writes $\Gamma$ for an interpretation, $\partial_\Gamma$ for its domain formula and $f_\Gamma$ for its coordinate map.
Hodges's books include the coordinate map in the interpretation, so an interpretation is a pair of formulas and a map.
Other books, such as Marker's, give only the formulas, and say that $N$ is interpretable in $M$ when $N$ is isomorphic to the quotient structure that the formulas define.
When $\varepsilon$ is equality, $N$ is *definable* in $M$, and when $A = \emptyset$, the interpretation is *without parameters*, or a $\emptyset$-interpretation.

## Remarks

### Examples

- The field $\Q$ is $2$-dimensionally interpretable in the ring $\Z$ without parameters: pairs $(a, b)$ with $b \neq 0$, modulo $a d = c b$; see [[this example|T2TBP1SA2T]].
- The field $\C$ is $2$-dimensionally definable in the field $\R$ without parameters, as pairs $(a, b)$ for $a + b i$; see [[this example|E355PSA9SW]].
- In the group $G$ of maps $x \mapsto a x + b$ of a field $K$, the field $K$ is definable with one parameter; see [[this example|C8NGHRR1ND]]. For $K$ algebraically closed, $G$ is a group of [[Morley rank|WN43DRPNBX]] $2$, and this is the model case of Zilber's field theorem.
- Every [[reduct|EY20BF96SJ]] of $M$ is $1$-dimensionally definable in $M$, with $\partial$ the formula $x = x$ and $\varepsilon$ equality.
- For a $\emptyset$-definable equivalence relation $E$ on $M^n$, the set $M^n / E$ is interpretable in $M$; these quotients are the sorts of the [[imaginary elements|Q0HM88QQKN]].

### Non-examples

- With all pairs $(a, b)$ of integers as domain, including $b = 0$, the cross-multiplication formula is not transitive, so it is not the kernel of any coordinate map; see [[this non-example|ZRFSPE7TCQ]].
- The ordered field $\R$ is not interpretable in the field $\C$, with or without parameters. The theory of $\C$ is [[stable|T7JW5QY6KR]], the order of $\R$ has the order property, and stability passes to interpretable structures.
- The ring $(\Z, +, \cdot)$ is not interpretable in $(\Z, +)$. The theory of $(\Z, +, 1)$ is [[decidable|HWC687ES0Q]] by [[Presburger's theorem|4W0E9G7PPV]], and the theory of the ring is not, while interpretations transfer decidability.

### Basic properties

- Reduction. For each $L'$-formula $\psi(y_1, \dots, y_k)$ there is an $L_A$-formula $\psi_\Gamma(\bar x_1, \dots, \bar x_k)$ with $N \models \psi(f \bar a_1, \dots, f \bar a_k)$ if and only if $M \models \psi_\Gamma(\bar a_1, \dots, \bar a_k)$. The proof is an induction on $\psi$: replace each symbol by its formula, $=$ by $\varepsilon$, and $\exists y$ by $\exists \bar x \, (\partial(\bar x) \wedge \cdots)$.
- Definable sets. The preimage under $f$ of a definable subset of $N^k$ is definable in $M$.
- Theories. For a $\emptyset$-interpretation, $N \models \psi$ if and only if $M \models \psi_\Gamma$ for each sentence $\psi$. So the same formulas interpret a model of $\operatorname{Th}(N)$ in every model of $\operatorname{Th}(M)$, and a decidable $\operatorname{Th}(M)$ gives a decidable $\operatorname{Th}(N)$.
- Composition. An interpretation of $P$ in $N$ and an interpretation of $N$ in $M$ compose to an interpretation of $P$ in $M$, and the dimensions multiply.
- Automorphisms. Each [[automorphism|DSQ17TNW1C]] $\sigma$ of $M$ that fixes $A$ pointwise induces the automorphism $f(\bar a) \mapsto f(\sigma \bar a)$ of $N$. This gives a group homomorphism $\operatorname{Aut}(M/A) \to \operatorname{Aut}(N)$.
- Tameness. If $\operatorname{Th}(M)$ is stable, then so is $\operatorname{Th}(N)$. An order property of $\psi$ in $N$ gives an order property of $\psi_\Gamma$ in $M$.

### History

Tarski, Mostowski and Robinson used interpretations in their 1953 book *Undecidable Theories* to transfer undecidability from one theory to another.
Interpretations of one structure in another became a standard tool of model theory with the study of groups and fields definable in stable structures.
Hodges's textbooks made the coordinate map a part of the definition.

### Common errors

- Confusing interpretations of structures with [[interpretability between theories|8H03GRMDYG]]. An interpretation of a theory $T$ in a theory $S$ only asks that $S$ prove the translated axioms of $T$. It concerns theories, not one fixed structure, and different models of $S$ can give models of $T$ that are not elementarily equivalent.
- Forgetting the parameters. The field in the affine group needs a parameter, and the transfer of decidability holds for interpretations without parameters.
- Forgetting the invariance of the formulas $\varphi_S$ under $\varepsilon$. A formula that gives different answers on two $\varepsilon$-equivalent tuples does not define a relation on the quotient.

## Explanations

### L1 human

An interpretation builds a new structure from pieces of an old one.
The new objects are lists of old objects, and two lists can stand for the same new object.
All the rules for building and comparing the lists are written in the language of the old structure.
For example, a fraction is a pair of whole numbers, like $(1, 2)$ for one half.
The pairs $(1, 2)$ and $(2, 4)$ stand for the same fraction, because $1 \cdot 4 = 2 \cdot 2$.
So every question about fractions becomes a question about whole numbers.

### L2 human

We check that the formulas for $\C$ in $\R$ give the multiplication of complex numbers.

1. The domain is $\R^2$, the formula $\varepsilon$ is equality, and $f(a, b) = a + b i$.
2. The formula $\varphi_\times(x_1, x_2, y_1, y_2, z_1, z_2)$ is $z_1 = x_1 y_1 - x_2 y_2 \wedge z_2 = x_1 y_2 + x_2 y_1$.
3. For $(x_1, x_2) = (1, 2)$ and $(y_1, y_2) = (3, -1)$ it gives $z_1 = 3 + 2 = 5$ and $z_2 = -1 + 6 = 5$.
4. In $\C$, $(1 + 2i)(3 - i) = 3 - i + 6i - 2i^2 = 5 + 5i$, which is $f(5, 5)$.

The typical use is the reduction property: a sentence about $\C$ becomes a sentence about $\R$.
A trap is to think that $\R$ is then interpretable in $\C$; the converse direction fails, as the non-examples show.

### L3 human

An interpretation of $N$ in $M$ over $A$ identifies $N$ with a definable set in one sort of $M^{\mathrm{eq}}$, with relations that are definable over $A$ there.
So the [[imaginary elements|Q0HM88QQKN]] are the universal home of all interpretations, and [[bi-interpretability|KHZ1E7RMMQ]] is the corresponding notion of equivalence of structures.
In geometric stability theory, interpretations carry the main questions: which groups and fields are interpretable in a given structure, as in Zilber's field theorem and the group configuration theorem.
In the [[reconstruction theorem|AM0523XJ9D]] of Ahlbrandt and Ziegler, interpretations without parameters between $\omega$-categorical structures correspond to continuous homomorphisms of automorphism groups.
