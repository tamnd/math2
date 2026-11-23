---
tag: 6T80N3RXDM
kind: example
name: The formula ¬(p ∨ q) ∧ r is not in conjunctive normal form
msc: ["03B05"]
topics: [JDK63589SA]
audience: ug1
instance_of: [TT7WT5HPN9]
not_instance_of:
  - target: 0B3D4C8YF2
    note: the negation applies to the compound formula p ∨ q, so ¬(p ∨ q) is not a literal and not a clause; the equivalent formula ¬p ∧ ¬q ∧ r is in CNF
uses: [07C4A8Y18K, 09PKJKA6J0]
sources:
  - url: https://en.wikipedia.org/wiki/Conjunctive_normal_form
    locator: Definition
---

## Example

Let $\varphi = \neg(p \lor q) \land r$.
We show that $\varphi$ is not in [[conjunctive normal form|07C4A8Y18K]], and we find an equivalent formula that is.

1. The top connective of $\varphi$ is $\land$, with the two parts $\neg(p \lor q)$ and $r$.
2. A CNF is a conjunction of clauses, and the parts of this conjunction that are not themselves conjunctions are $\neg(p \lor q)$ and $r$.
   So both parts would have to be clauses.
3. A clause whose top connective is $\neg$ can only be a single literal $\neg x$ with $x$ a variable.
4. Here $\neg$ is applied to $p \lor q$, which is not a variable.
   So $\neg(p \lor q)$ is not a clause, and $\varphi$ is not in CNF.
5. [[De Morgan's law|09PKJKA6J0]] gives $\neg(p \lor q) \equiv \neg p \land \neg q$, so
$$\varphi \equiv \neg p \land \neg q \land r.$$
6. This formula is a conjunction of three clauses with one literal each, so it is in CNF.

Check: both formulas are true at the row $p = 0$, $q = 0$, $r = 1$ and at no other row.

## Remarks

Being in CNF is a property of how a formula is written, not of its truth table.
So the failure here is easy to repair: an equivalent CNF always exists.
What the example shows is the rule on negation: in a CNF, $\neg$ may stand only directly in front of a variable.

The repaired formula $\neg p \land \neg q \land r$ is also in [[disjunctive normal form|0GVDFAY4KW]], as a single term.
If we change the formula to $\neg(p \land q) \land r$, De Morgan's law gives $(\neg p \lor \neg q) \land r$, which is in CNF with two clauses but is no longer in DNF.

## Explanations

### L1 human

In conjunctive normal form, the word "not" may stand only directly in front of a single letter.
The formula "not ($p$ or $q$), and $r$" breaks this rule, because "not" stands in front of "$p$ or $q$".
"Not ($p$ or $q$)" means "neither $p$ nor $q$", that is, "not $p$, and not $q$".
So the formula says "not $p$, and not $q$, and $r$", which is in conjunctive normal form.

### L2 human

To test whether a formula is in CNF, read it from the top.
First split the top-level $\land$ into its parts.
Each part must be a disjunction of literals with no $\land$ inside, and each $\neg$ must stand directly in front of a variable.
Watch out: if you stop after the first step, $\neg(p \lor q) \land r$ seems to be a conjunction of two disjunctions, but its first part is a negated disjunction.
