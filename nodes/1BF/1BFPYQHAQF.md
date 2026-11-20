---
tag: 1BFPYQHAQF
kind: example
name: Classical logic is not connexive
msc: ["03B60", "03B05"]
topics: [NJB94B39QK]
audience: ug2
not_instance_of:
  - target: NQFYY76BSM
    note: classical propositional logic proves none of Aristotle's and Boethius' theses
uses: [NQFYY76BSM, 05RSK4Q657, 4KTD8GB5PV, 22K4GWJ0WM]
sources:
  - url: https://plato.stanford.edu/entries/logic-connexive/
    locator: Connexive Logic (SEP entry), section 1
---

## Example

We show with [[truth tables|05RSK4Q657]] that classical propositional logic proves none of the connexive theses.
Write $\neg$ for classical negation and $\to$ for the material conditional.

[[Aristotle's thesis|4KTD8GB5PV]] AT: $\neg(\neg p \to p)$.

1. Let $p$ be true.
2. Then $\neg p \to p$ is true, since its consequent is true.
3. So $\neg(\neg p \to p)$ is false.

AT′: $\neg(p \to \neg p)$.

4. Let $p$ be false.
5. Then $p \to \neg p$ is true, since its antecedent is false.
6. So $\neg(p \to \neg p)$ is false.

[[Boethius' thesis|22K4GWJ0WM]] BT: $(p \to q) \to \neg(p \to \neg q)$.

7. Let $p$ be false and $q$ be arbitrary.
8. Then $p \to q$ and $p \to \neg q$ are both true, since their antecedent is false.
9. So $\neg(p \to \neg q)$ is false, and BT is false.

BT′: $(p \to \neg q) \to \neg(p \to q)$ fails at the same row, by the same argument.

So classical logic is not a [[connexive logic|NQFYY76BSM]].

## Remarks

Classical logic also cannot be extended to a connexive logic.
The table shows that $\neg(\neg p \to p)$ has the same value as $\neg p$.
If we add all instances of AT, we get $\neg C$ for every formula $C$.
With $C := q \to q$, we get $\neg(q \to q)$, and with the theorem $q \to q$ every formula follows.
The same argument works for any non-tautology, because classical propositional logic is Post complete.

## Explanations

### L1 human

Classically, "if not $p$, then $p$" is true whenever $p$ is true.
So "it is not the case that if not $p$ then $p$" is false in that case.
Connexive logic wants this sentence to be always true, so it cannot be classical.

### L2 human

Each thesis fails in a single row: AT when $p$ is true, AT′ and both Boethius theses when $p$ is false.
These rows come from the paradoxes of material implication: a true consequent or a false antecedent makes a conditional true.
A trap is to repair this by adding AT as an axiom; that makes every formula a theorem.
