---
tag: EHMRNDEFAV
kind: example
name: One-point phase space and classical truth tables
msc: ["03F52"]
topics: [98QF5J4W16]
audience: research
instance_of: [64MHHQQ6G6]
uses: [5M4Z5EE88F, 14Z5D0JX98]
sources:
  - doi: 10.1016/0304-3975(87)90045-4
    locator: pages 1-101
    note: Girard, Linear logic, Theoretical Computer Science 50 (1987)
  - url: https://plato.stanford.edu/entries/logic-linear/
    locator: 3.1 Semantics of provability
    note: Di Cosmo and Miller, Linear Logic, Stanford Encyclopedia of Philosophy, revision of 2023-09-16
---

## Example

Let $M = \set{e}$ be the one-point monoid, and let $\bot = \emptyset$.
This [[phase space|5M4Z5EE88F]] gives the classical two-valued truth tables.

1. $\emptyset^{\perp} = M$, and $\set{e}^{\perp} = \emptyset$, since $e e = e \notin \bot$.
2. So the facts are $\emptyset$ and $M$.
   We read $\emptyset$ as "false" and $M$ as "true".
3. Negation $X \mapsto X^{\perp}$ exchanges false and true.
4. $X Y$ is $M$ if $X = Y = M$, and $\emptyset$ otherwise.
   So $\otimes$ is "and", and $\mathbin{\&}$, the intersection, is also "and".
5. $(A \mathbin{\wp} B)^* = ((A^*)^{\perp} (B^*)^{\perp})^{\perp}$ is "not (not $A$ and not $B$)", that is, "or".
   The closure of a union, $\oplus$, is also "or".
6. $1^* = \set{e}^{\perp\perp} = M$ and $\top^* = M$ are true; $\bot^* = \emptyset$ and $0^* = M^{\perp} = \emptyset$ are false.
7. $V(\Gamma) \subseteq \emptyset$ if and only if some factor $(A^*)^{\perp}$ is empty, that is, some $A$ in $\Gamma$ is true.

So a sequent $\vdash \Gamma$ is valid in this model under a valuation if and only if the classical disjunction of $\Gamma$ is true under it.
By [[soundness|14Z5D0JX98]], every sequent derivable in MALL is a classical tautology under this reading.

## Remarks

The converse fails: $\vdash p^{\perp}, p \otimes p$ is a classical tautology, read as "not $p$ or ($p$ and $p$)", but it is [[not derivable|V444A285N3]].
The sequent $\vdash p \otimes p^{\perp}$ is false under both valuations, so it is not derivable.
With $\bot = M$ instead, $X^{\perp} = M$ for every $X$, the only fact is $M$, and every sequent is valid.

## Explanations

### L1 human

A one-point model cannot count resources, since one point plus one point is still one point.
So it forgets the difference between the two "and" connectives and between the two "or" connectives.
What is left is the usual truth table of classical logic.

### L2 human

We evaluate $\vdash p^{\perp} \mathbin{\wp} q^{\perp}, q \otimes p$ under the valuation $p^* = M$, $q^* = \emptyset$.

1. $(p^{\perp})^* = \emptyset$ and $(q^{\perp})^* = M$, so $(p^{\perp} \mathbin{\wp} q^{\perp})^*$ is "false or true", that is, $M$.
2. $(q \otimes p)^*$ is "false and true", that is, $\emptyset$.
3. One formula is true, so the sequent is valid under this valuation.
4. The other three valuations also make one formula true, as a check of the truth table shows.

The typical use of this model is to show that a sequent is not derivable because it is not even a classical tautology.
A trap: a classical tautology need not be derivable in linear logic, so this model cannot prove derivability.
