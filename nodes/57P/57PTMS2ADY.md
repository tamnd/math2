---
tag: 57PTMS2ADY
kind: definition
name: Ordinal analysis
msc: ["03F15", "03F05"]
topics: [XTTKZTYDSD]
audience: research
defines: C5E5TG8PGP
uses: [C19Z3B6V4P, C72RBH0CDR, 0QFT7Z76N5, KT50SMH3EC, 0ZHQMQ2C1N]
sources:
  - url: https://en.wikipedia.org/wiki/Ordinal_analysis
    locator: Definition
---

## Definition

Let $T$ be a recursively axiomatized theory that contains elementary arithmetic.
Let $\operatorname{TI}(\prec, X)$ be the statement of [[transfinite induction|0ZHQMQ2C1N]] along $\prec$ for a set variable $X$, or, for a first-order $T$, the schema for all formulas.
An *ordinal analysis* of $T$ is the determination of its [[proof-theoretic ordinal|C19Z3B6V4P]] $\abs{T}$, by three results.

1. A notation system: a natural [[ordinal notation system|~a8ed0faf]] $(A, \prec)$, primitive recursive, for an ordinal $\alpha$.
2. A lower bound: for each $a \in A$, $T$ proves $\operatorname{TI}(\prec_a, X)$, where $\prec_a$ is the restriction of $\prec$ to $\set{b : b \prec a}$.
3. An upper bound: if $\lhd$ is a primitive recursive well-order and $T$ proves $\operatorname{TI}(\lhd, X)$, then the order type of $\lhd$ is less than $\alpha$.

Then $\abs{T} = \alpha$, and we say that $T$ *has ordinal* $\alpha$.

## Notation

One writes $\abs{T} = \alpha$, or $\abs{T}_{\Pi^1_1} = \alpha$ when other ordinals of $T$ are also in use.
The phrase "$T$ proves the well-foundedness of $\alpha$" is short for result 2 along a fixed notation system.

## Remarks

- Result 3 is about all primitive recursive orders, not only $\prec$. So it is independent of the choice of notation system. Result 2 depends on the system, and this is why the system must be natural; see [[ordinal notation system|~f8083877]].
- Result 3 implies that $T$ does not prove $\operatorname{TI}(\prec, X)$ for the whole order, since that order has type $\alpha$.
- Result 3 is usually proved in a weak base theory together with transfinite induction along $\prec$. The same proof gives the consistency of $T$ in that base theory.
- Example: Gentzen's analysis of [[Peano arithmetic|0QFT7Z76N5]] uses the Cantor normal forms below [[epsilon nought|KT50SMH3EC]] and gives $\abs{\mathrm{PA}} = \varepsilon_0$.
- Non-example: a proof that $T$ is consistent, by itself, is not an ordinal analysis, because it gives no ordinal.

## Explanations

### L1 human

To analyse a theory, one needs three things.
First, a list of names for ordinals, which a computer can compare.
Second, a proof inside the theory that every proper initial part of the list has no endless way down.
Third, a proof that the theory can never do this for a longer list.
The length of the list is then the ordinal of the theory.

### L2 human

We check the three results for PA with $\alpha = \varepsilon_0$.

1. The notation system is the [[Cantor normal form notation|~abf54fbe]], which is primitive recursive.
2. The lower bound is part 1 of [[transfinite induction in arithmetic|~e065bc19]]: PA proves transfinite induction up to each notation.
3. The upper bound comes from cut elimination for PA with the [[ω-rule|~e0034cfd]]. A PA-proof of $\operatorname{TI}(\lhd, X)$ gives a cut-free infinitary derivation of height below $\varepsilon_0$. This height bounds the order type of $\lhd$.

The typical use is to place a new theory on the scale of known ordinals.
The trap: results 2 and 3 have different forms.
Result 2 is about one natural system, and result 3 is about every primitive recursive order.

### L3 human

The lower bound is a well-ordering proof, and it shows what the theory can do.
The upper bound is a proof-theoretic reduction, and it shows what the theory cannot do.
In modern analyses, the upper bound comes from operator-controlled infinitary derivations or from [[collapsing functions|~766739ea]].
The notation system is built so that both halves meet at the same ordinal.
