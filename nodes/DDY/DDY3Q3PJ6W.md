---
tag: DDY3Q3PJ6W
kind: example
name: Real closed field
msc: [12D15, 03C10, 03C64]
illustrates: [7FDDXV3JK7, YR6HCMABTE]
uses: [0P3VCBDEE2, 04C5ZBG1WT, FSJ9NGRRPA, 08J2M1JYAG, 0NCJ5WXN6Z, 655K8Y7VS8]
sources:
  - url: https://en.wikipedia.org/wiki/Real_closed_field
same_as:
  wikidata: Q2068227
  wikipedia: Real closed field
---

## Example

A *real closed field* is an [[ordered field|0P3VCBDEE2]] $(R, <)$ with two properties.
Every positive element has a square root in $R$.
Every polynomial of odd degree with coefficients in $R$ has a root in $R$.
The [[real numbers|08J2M1JYAG]] form a real closed field.
A positive real number has a real square root.
A real polynomial of odd degree takes values of both signs, so it has a root by the intermediate value theorem.
The real algebraic numbers also form a real closed field, and it is countable.

The [[rational numbers|0NCJ5WXN6Z]] do not form a real closed field: $2 > 0$ has no rational square root.

## Remarks

The theory $\mathrm{RCF}$ of real closed fields in the signature $\set{+, -, \cdot, 0, 1, <}$ has [[quantifier elimination|FSJ9NGRRPA]].
So it is model complete, it is [[complete|655K8Y7VS8]], and it is decidable.
Every real closed field therefore satisfies the same first-order sentences as $\R$.
In the signature of rings without $<$, the theory is still model complete, but it no longer has quantifier elimination, since the order $x \ge 0$ is defined by $\exists y \, (x = y^2)$.

A field $R$ is real closed, for some ordering, exactly when $-1$ is not a sum of squares in $R$ and $R(\sqrt{-1})$ is algebraically closed.
The ordering is then unique: the positive elements are the nonzero squares.

## Explanations

### L1 human

Real closed fields are the fields that behave like the real numbers for all algebraic purposes.
Every positive number has a square root and odd-degree polynomials always have a root.
Take any statement written with $+$, $\cdot$, $<$ and quantifiers over the elements of the field.
Model theory shows that it is true in a real closed field exactly when it is true in $\R$.
