---
tag: PGZSNWS5VN
kind: definition
name: Universal Horn class
msc: ["03C52", "08C15"]
defines: 9A4CYWXPEA
uses: [QR92EZDTKF, WDVVEYD6AT, 983GZBQYT4, DKFGQTRYZE]
sources:
  - url: https://en.wikipedia.org/wiki/Horn_clause
---

## Definition

Let $\sigma$ be a first-order [[signature|WDVVEYD6AT]].
A *universal Horn sentence* of $\sigma$ is a [[sentence|DKFGQTRYZE]] $\forall x_1 \cdots \forall x_m \, \varphi$ in which $\varphi$ is a [[Horn clause|QR92EZDTKF]].
The atoms of $\varphi$ are atomic $\sigma$-formulas, possibly equations, in the variables $x_1, \ldots, x_m$.
Let $K$ be a class of [[$\sigma$-structures|983GZBQYT4]].
Then $K$ is a *universal Horn class* if there is a set $\Sigma$ of universal Horn sentences of $\sigma$ with the following property.
A $\sigma$-structure is in $K$ exactly when it satisfies every sentence of $\Sigma$.

## Remarks

Equivalently, each axiom has one of the forms $\forall \bar x \, (\alpha_1 \wedge \cdots \wedge \alpha_n \rightarrow \beta)$ or $\forall \bar x \, \neg (\alpha_1 \wedge \cdots \wedge \alpha_n)$ with atomic $\alpha_i$ and $\beta$.
Universal Horn sentences are preserved by substructures and by direct products of nonempty families, so every universal Horn class is closed under these constructions.

Example: [[partial orders|0QV2JS9RJ3]], in the signature with one binary relation $\le$, form a universal Horn class.
Its axioms $\forall x \, (x \le x)$, $\forall x \forall y \, (x \le y \wedge y \le x \rightarrow x = y)$ and $\forall x \forall y \forall z \, (x \le y \wedge y \le z \rightarrow x \le z)$ are universal Horn sentences.

Non-example: [[total orders|0FRXBVVR03]] do not form a universal Horn class.
The product of the 2-element chain $\set{0 < 1}$ with itself, ordered coordinatewise, is a partial order in which $(0, 1)$ and $(1, 0)$ are incomparable, so the class is not closed under products.

When $\sigma$ has only function symbols, the universal Horn sentences of the first form are exactly the [[quasi-identities|94GVY3APPQ]], so the corresponding classes are the [[quasivarieties|WRXEKT4NQS]].
