---
tag: RXHJPVMPJH
kind: definition
name: Heyting arithmetic
msc: ["03F55", "03F30", "03F50"]
defines: CK8ZQRN183
uses: [0QFT7Z76N5, Q11N8X99FK, 0RYYK8PG4S]
sources:
  - url: https://en.wikipedia.org/wiki/Heyting_arithmetic
---

## Definition

*Heyting arithmetic*, written HA, is the first-order theory in the language $0, S, +, \cdot, =$ with these parts.

1. Its logic is first-order [[intuitionistic logic|Q11N8X99FK]] with equality.
2. Its axioms are those of first-order [[Peano arithmetic|0QFT7Z76N5]]. They are $S x \ne 0$, $S x = S y \to x = y$, and $x + 0 = x$, $x + S y = S(x + y)$, $x \cdot 0 = 0$, $x \cdot S y = x \cdot y + x$. They also include the induction scheme $A(0) \wedge \forall x\, (A(x) \to A(S x)) \to \forall x\, A(x)$ for every formula $A$.

Thus HA has the same axioms as Peano arithmetic PA.
The theory PA is HA together with the [[law of excluded middle|0RYYK8PG4S]] $A \vee \neg A$ for all formulas $A$.

## Remarks

Example: HA proves $\forall x\, \forall y\, (x = y \vee \neg x = y)$, by induction on $x$ and $y$.
So excluded middle holds in HA for equations, and, by induction on formulas, for all formulas without unbounded quantifiers.
Non-example: HA does not prove $\forall x\, (\exists y\, T(x, x, y) \vee \neg \exists y\, T(x, x, y))$, where $T$ is Kleene's predicate for "program $x$ on input $x$ halts within $y$ steps".
This formula is provable in PA, so the two theories differ.
HA has the disjunction property: if HA proves a closed formula $A \vee B$, then it proves $A$ or it proves $B$.
It has the existence property: if HA proves a closed formula $\exists x\, A(x)$, then it proves $A(\overline{n})$ for some numeral $\overline{n}$.
