---
tag: PGZSNWS5VN
kind: definition
name: Universal Horn class
aliases: [universal-horn-sentence]
msc: ["03C52", "08C15"]
topics: [JYJHB4YBAH]
audience: grad
defines: 9A4CYWXPEA
uses: [QR92EZDTKF, WDVVEYD6AT, 983GZBQYT4, DKFGQTRYZE, MCZRXR3SVB]
sources:
  - url: https://en.wikipedia.org/wiki/Horn_clause
    locator: Definition
  - book: isbn:9780521587136
---

## Definition

Let $\sigma$ be a first-order [[signature|WDVVEYD6AT]].
A *universal Horn sentence* of $\sigma$ is a [[sentence|DKFGQTRYZE]] $\forall x_1 \cdots \forall x_m \, \varphi$ in which $\varphi$ is a [[Horn clause|QR92EZDTKF]].
This means that $\varphi$ is a finite disjunction of [[atomic $\sigma$-formulas|MCZRXR3SVB]] and negated atomic $\sigma$-formulas, at most one of them unnegated.
The atoms may be equations between terms, and their variables are among $x_1, \ldots, x_m$.
Let $K$ be a class of [[$\sigma$-structures|983GZBQYT4]].
Then $K$ is a *universal Horn class* if there is a set $\Sigma$ of universal Horn sentences of $\sigma$ with the following property.
A $\sigma$-structure is in $K$ exactly when it satisfies every sentence of $\Sigma$.

## Notation

Up to logical equivalence, each axiom has one of the forms

$$\forall \bar x \, (\alpha_1 \wedge \cdots \wedge \alpha_n \rightarrow \beta), \qquad \forall \bar x \, \neg (\alpha_1 \wedge \cdots \wedge \alpha_n),$$

with atomic $\alpha_i$ and $\beta$.
Axioms of the first form are *strict* universal Horn sentences, and for $n = 0$ the first form reads $\forall \bar x \, \beta$.
In the second form $n \ge 1$.

## Remarks

- Universal Horn sentences are preserved by substructures and by reduced products of nonempty families, so every universal Horn class is closed under these constructions.
- [[Partial orders|0QV2JS9RJ3]] in the signature $\set{\le}$ form a universal Horn class, since reflexivity, antisymmetry and transitivity are strict universal Horn sentences.
- [[Total orders|0FRXBVVR03]] do not. The square of the chain $\set{0 < 1}$, ordered coordinatewise, has the incomparable elements $(0, 1)$ and $(1, 0)$, so the class is not closed under products.
- When $\sigma$ has only function and constant symbols, the strict universal Horn sentences are the [[quasi-identities|94GVY3APPQ]], and the classes they axiomatize are the [[quasivarieties|WRXEKT4NQS]].
- Structures here have nonempty domains, as is usual in first-order logic.

## Explanations

### L1 human

A universal Horn rule is a rule of the form "whenever these basic facts hold, this other basic fact holds", for all choices of elements.
It may also be a ban: "these basic facts never hold together".
A universal Horn class is everything that obeys a given list of such rules.

### L2 human

We sort the axioms of groups with the signature $\set{\cdot, {}^{-1}, e}$.

1. Associativity $\forall x \forall y \forall z \, ((xy)z = x(yz))$ is a strict universal Horn sentence with $n = 0$.
2. The laws $xe = x$ and $x x^{-1} = e$, quantified universally, are of the same kind.
3. Cancellation $\forall x \forall y \forall z \, (xz = yz \rightarrow x = y)$ is strict with $n = 1$.
4. So groups form a universal Horn class, and in fact a variety.

A trap is to write a group axiom as $\forall x \, \exists y \, (xy = e)$; with that axiom the signature lacks ${}^{-1}$, and the class of groups in the signature $\set{\cdot, e}$ is not universal, since $(\mathbb{N}, +, 0)$ is a substructure of $(\mathbb{Z}, +, 0)$.
