---
tag: ~dba17db1
kind: example
name: The Łukasiewicz and Gödel algebras refute cancellation
msc: ["03B52"]
topics: [WZP584JQ06]
audience: grad
not_instance_of:
  - target: ~fc3c462d
    note: the cancellation axiom has value 0.7 in both standard algebras
uses: [~9e745f02, ~1d003105]
sources:
  - url: https://plato.stanford.edu/entries/logic-fuzzy/
    locator: 1. Fuzzy connectives based on t-norms; 5. Other notable fuzzy logics
---

## Example

We evaluate the cancellation axiom $\neg \varphi \lor ((\varphi \to \varphi \otimes \psi) \to \psi)$ of [[product logic|~9e745f02]] in the standard Łukasiewicz and Gödel algebras.
The residua are those of [[the residua statement|~1d003105]].

Gödel algebra, at $x = 0.5$, $y = 0.7$:

1. $\neg 0.5 = 0$, since $0.5 > 0$.
2. $x \otimes y = \min(0.5, 0.7) = 0.5$, and $0.5 \Rightarrow 0.5 = 1$.
3. $1 \Rightarrow 0.7 = 0.7$, so the axiom has value $\max(0, 0.7) = 0.7 < 1$.

Łukasiewicz algebra, at $x = 0.3$, $y = 0.1$:

4. $\neg 0.3 = 0.7$.
5. $x \odot y = \max(0, 0.4 - 1) = 0$, and $0.3 \Rightarrow 0 = \min(1, 0.7) = 0.7$.
6. $0.7 \Rightarrow 0.1 = \min(1, 1 - 0.7 + 0.1) = 0.4$.
7. So the axiom has value $\max(0.7, 0.4) = 0.7 < 1$.

So neither standard algebra is a product algebra, and the axiom separates product logic from both.

## Remarks

1. In Gödel logic, conjunction with $x$ cuts every value above $x$ down to $x$, so the information about $y > x$ is lost.
2. In Łukasiewicz logic, conjunction with $x$ sends every $y \le 1 - x$ to $0$, so small values of $y$ are lost.
   The axiom fails exactly when $x > 0$ and $x + y < 1$.
3. Both standard algebras are BL-algebras, so the failure comes from the extra axiom, not from BL.

## Explanations

### L1 human

In product logic, "and" with a nonzero degree can be undone by division.
With the minimum or the Łukasiewicz "and", different inputs can give the same output.
Then the information cannot be recovered, and the axiom fails.

### L2 human

1. To refute cancellation, find $x > 0$ and two values of $y$ with the same value of $x \otimes y$.
2. For the minimum, take $y \ge x$ with $y < 1$; for Łukasiewicz, take $x > 0$ and $y < 1 - x$.

A trap: the Gödel failure needs $y \ge x$; for $0 < y < x$ the Gödel value is $1$.
