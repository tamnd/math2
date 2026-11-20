---
tag: W3CPQAFQJ3
kind: concept
name: Abelian logic
msc: ["03B47", "06F20"]
topics: [98QF5J4W16]
audience: research
uses: [ZZKTJY5J4T, 082GHNPJ53, J0DHYQ0MDE]
sources:
  - wikipedia: en:76765067@r1368301704
    locator: Glossary of logic, section A
    note: adopted
    mention: wikipedia://en/76765067#AE1L
    sections: [Summary]
  - url: https://plato.stanford.edu/entries/logic-manyvalued/
    locator: 2.4 A continuum of truth values
    note: Marcos, Přenosil and Egré, Many-Valued Logic, Stanford Encyclopedia of Philosophy, revision of 2026-09-29
  - url: https://en.wikipedia.org/wiki/Residuated_lattice
    locator: Examples
  - doi: 10.2307/j.ctv2x8v8c7.12
    locator: pages 245-288
    note: Meyer and Slaney, Abelian Logic (from A to Z), in Paraconsistent Logic, Essays on the Inconsistent (1989)
  - doi: 10.1145/1071596.1071600
    locator: abstract; pages 578-613
    note: Metcalfe, Olivetti and Gabbay, Sequent and hypersequent calculi for abelian and Łukasiewicz logics, ACM Transactions on Computational Logic 6 (2005)
inventory: [DS26MBK56Q]
---

## Summary

*Abelian logic* is the logic of the ordered additive group of real numbers, with implication $a \to b = b - a$.
Its designated values are the non-negative numbers; see [[the definition|49QSARV4BA]].
It is a [[substructural logic|ZZKTJY5J4T]] with neither weakening nor contraction.
It proves $((A \to B) \to B) \to A$, which is not a classical tautology.
The abstract of Metcalfe, Olivetti and Gabbay calls it the logic of [[lattice-ordered|J0DHYQ0MDE]] [[abelian groups|082GHNPJ53]].

## Motivation

The Wikipedia article on residuated lattices states that the integers with $\min$, $\max$, $+$, $0$ and subtraction form a commutative residuated lattice.
In this structure, subtraction is a true inverse of addition, not only a residual.
Abelian logic reads the laws of this group as laws of logic.
The SEP entry on many-valued logic uses it as an example of a substructural logic that is not contained in classical logic.

## Notation

A valuation $v$ gives each atom a real number.
It extends to all formulas by $v(A \wedge B) = \min(v(A), v(B))$, $v(A \vee B) = \max(v(A), v(B))$ and $v(A \to B) = v(B) - v(A)$.
A formula $A$ is *valid* if $v(A) \geq 0$ for every valuation $v$.

## Remarks

### Examples

1. [[The formula $((A \to B) \to B) \to A$|74YHTDPEKW]] has the value $0$ under every valuation, so it is valid.
2. The identity $A \to A$ has the value $v(A) - v(A) = 0$, so it is valid.
3. Prefixing $(A \to B) \to ((C \to A) \to (C \to B))$ has the value $(b - a) - (b - a) = 0$, where $a, b$ are the values of $A, B$.
4. Permutation $(A \to (B \to C)) \to (B \to (A \to C))$ has the value $(c - a - b) - (c - b - a) = 0$.

### Non-examples

1. [[Contraction|K16VJQASTK]] $(A \to (A \to B)) \to (A \to B)$ has the value $v(A)$, so it fails when $v(A) < 0$.
2. [[Weakening|VHRXX0T5XT]] in the form $p \to (q \to p)$ has the value $-v(q)$, so it fails when $v(q) > 0$.
3. Classical logic does not contain abelian logic, since [[$((p \to q) \to q) \to p$ is not a classical tautology|JG17B0XHTB]].

### Basic properties

1. The integers, the rationals and the reals give the same valid formulas; [[the definition|49QSARV4BA]] proves this.
2. A formula built from atoms with $\to$ alone has the value $\sum_i n_i v(p_i)$ for integers $n_i$.
   It is valid if and only if every $n_i$ is $0$; the definition proves this.
3. So the valid formulas with $\to$ alone are decidable: count, for each atom, its signed number of occurrences.
4. The formulas $(A \to B) \to B$ and $A$ always have the same value.

### History

The SEP entry and the paper cited here name Meyer and Slaney (1989) as the source of abelian logic.
The abstract of Metcalfe, Olivetti and Gabbay (2005) gives two embeddings of Łukasiewicz logic into abelian logic and new proof systems for it.

### Common errors

The Wikipedia glossary calls abelian logic a type of relevance logic.
It does not have the variable sharing property of [[relevance logic|KXTCZ2FY5M]]: $(p \to p) \to (q \to q)$ has the value $0 - 0 = 0$, so it is valid.
Its antecedent and its consequent have no atom in common.

## Explanations

### L1 human

In abelian logic, a formula is a number, and a formula is true when its number is at least $0$.
"$A$ implies $B$" is the gain from $A$ to $B$, that is, $B$ minus $A$.

### L2 human

We compute the value of $(p \to q) \to (q \to p)$.

1. $v(p \to q) = v(q) - v(p)$.
2. $v(q \to p) = v(p) - v(q)$.
3. So the value is $(v(p) - v(q)) - (v(q) - v(p)) = 2v(p) - 2v(q)$.
4. With $v(p) = 0$ and $v(q) = 1$, the value is $-2$, so the formula is not valid.

The typical use of the value is to decide validity by algebra in place of a search for proofs.
A trap: a formula can have value $0$ for every valuation and still contain each atom many times, as prefixing does with $A = B = C = p$.

### L3 human

Abelian logic is an extreme case of a substructural logic: implication is subtraction in a group, so each value has an inverse.
This makes it contraclassical, since it proves formulas that classical logic rejects.
