---
tag: 74YHTDPEKW
kind: example
name: The formula ((A → B) → B) → A in abelian logic
msc: ["03B47"]
topics: [98QF5J4W16]
audience: research
instance_of: [W3CPQAFQJ3]
uses: [49QSARV4BA]
sources:
  - url: https://plato.stanford.edu/entries/logic-manyvalued/
    locator: 2.4 A continuum of truth values
    note: Marcos, Přenosil and Egré, Many-Valued Logic, Stanford Encyclopedia of Philosophy, revision of 2026-09-29
  - url: https://en.wikipedia.org/wiki/Glossary_of_logic
    locator: section A, Abelian logic
---

## Example

For all formulas $A$ and $B$, the formula $((A \to B) \to B) \to A$ is valid in [[abelian logic|49QSARV4BA]].
Fix a valuation $v$, and write $a = v(A)$ and $b = v(B)$.

1. $v(A \to B) = b - a$, by the clause for $\to$.
2. $v((A \to B) \to B) = b - (b - a) = a$, by the same clause.
3. $v(((A \to B) \to B) \to A) = a - a = 0$, by the same clause.
4. $0 \geq 0$, so the formula is valid.

## Remarks

The SEP entry on many-valued logic gives $((p \to q) \to q) \to p$ as a theorem of abelian logic that classical logic does not prove.
The converse formula $A \to ((A \to B) \to B)$ also has the value $a - a = 0$, so $A$ and $(A \to B) \to B$ imply each other.
The Wikipedia glossary describes abelian logic as a logic that accepts this formula.

## Explanations

### L1 human

The value of $A \to B$ is the step from $A$ to $B$.
Taking that step back from $B$ returns the value of $A$, so the whole formula has the value $0$.

### L2 human

We check one valuation with numbers: $v(p) = 3$ and $v(q) = -5$.

1. $v(p \to q) = -5 - 3 = -8$.
2. $v((p \to q) \to q) = -5 - (-8) = 3$.
3. $v(((p \to q) \to q) \to p) = 3 - 3 = 0$.

The typical use of this formula is to show that abelian logic proves a formula that classical logic does not prove.
A trap: in [[classical logic|JG17B0XHTB]] the same formula fails at $p$ false and $q$ true.
