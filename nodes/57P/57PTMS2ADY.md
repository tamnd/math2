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

An ordinal analysis of a theory is a set of three results that together compute its proof-theoretic ordinal.

Let $T$ be a recursively axiomatized theory that contains elementary arithmetic.
For a primitive recursive order $\lhd$, let $\operatorname{TI}(\lhd, X)$ be the statement of [[transfinite induction|0ZHQMQ2C1N]] along $\lhd$ for a set variable $X$; for a first-order $T$, it is the schema for all formulas.
We use the $\Pi^1_1$ [[proof-theoretic ordinal|C19Z3B6V4P]], the supremum of the order types of the primitive recursive well-orders $\lhd$ with $T \vdash \operatorname{TI}(\lhd, X)$.
An *ordinal analysis* of $T$ with ordinal $\alpha$ consists of the following.

1. A notation system: a natural primitive recursive [[ordinal notation system|3CNSYYX2HF]] $(A, \prec)$ of order type $\alpha$.
2. A lower bound: for each $a \in A$, $T$ proves $\operatorname{TI}(\prec_a, X)$, where $\prec_a$ is the restriction of $\prec$ to $\{ b : b \prec a \}$.
3. An upper bound: if $\lhd$ is a primitive recursive well-order and $T \vdash \operatorname{TI}(\lhd, X)$, then the order type of $\lhd$ is less than $\alpha$.

When the three results hold, $\lvert T \rvert = \alpha$, and we say that $T$ *has ordinal* $\alpha$.

## Notation

We write $\lvert T \rvert = \alpha$, or $\lvert T \rvert_{\Pi^1_1} = \alpha$ when other ordinals of $T$ are also in use.
The phrase "$T$ proves the well-foundedness of $\alpha$" is short for result 2 along a fixed notation system.

## Remarks

Why three results?
Result 2 alone shows that $\lvert T \rvert \ge \alpha$, since the initial segments $\prec_a$ have order types that reach every ordinal below $\alpha$.
Result 3 alone shows that $\lvert T \rvert \le \alpha$.
Together they fix the supremum, and result 1 makes the ordinal concrete enough to state the bounds.

The two bounds have different shapes, and this is where students slip.
Result 3 speaks about every primitive recursive well-order, so it does not depend on the chosen notation system.
Result 2 speaks about one system, and it is only convincing when the system is natural; see [[ordinal notation system|7MBX59Y7N9]].
Result 3 also shows that $T$ does not prove $\operatorname{TI}(\prec, X)$ for the whole order $\prec$, because that order has type $\alpha$, which is not less than $\alpha$.

For an example, Gentzen's analysis of [[Peano arithmetic|0QFT7Z76N5]] uses the Cantor normal forms below [[epsilon nought|KT50SMH3EC]] and gives $\lvert \mathrm{PA} \rvert = \varepsilon_0$.
A bare consistency proof of $T$ fails the definition, because it gives none of the three results.
In practice result 3 is proved in a weak base theory together with induction along $\prec$, and the same argument then proves the consistency of $T$.

## Explanations

### L1 human

To measure a theory, we need three things.
First, a list of names for ordinals that a computer can compare.
Second, a proof inside the theory that each part of the list below a given name has no endless way down.
Third, a proof that the theory can never do this for a longer list.
The length of the list is then the ordinal of the theory.

### L2 human

We check the three results for PA with $\alpha = \varepsilon_0$.
The notation system is the [[Cantor normal form notation|R3BJR7TM2Z]], whose comparison is primitive recursive.
The lower bound is the first part of [[transfinite induction in arithmetic|ZE54ABPMJ0]]: PA proves induction up to each notation, such as $\omega^{\omega^\omega}$.
The upper bound comes from cut elimination for PA with the [[ω-rule|XAMKAB1BZM]].
A PA proof of $\operatorname{TI}(\lhd, X)$ gives a cut-free infinitary derivation of height below $\varepsilon_0$, and this height bounds the order type of $\lhd$.
The typical use is to place a new theory on the scale of known ordinals.

### L3 human

The lower bound is a well-ordering proof, and it shows what the theory can do.
The upper bound is a proof-theoretic reduction, and it shows what the theory cannot do.
In modern analyses, the upper bound comes from operator-controlled infinitary derivations or from [[collapsing functions|8S6CT4TMB7]].
The notation system is designed so that both halves meet at the same ordinal.
