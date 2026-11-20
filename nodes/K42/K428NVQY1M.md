---
tag: K428NVQY1M
kind: example
name: Controlled weakening in linear logic
msc: ["03F52", "03B47"]
topics: [98QF5J4W16]
audience: research
instance_of: [VHRXX0T5XT]
uses: [H408H4WHBA, JNYY1WD8SR]
sources:
  - url: https://en.wikipedia.org/wiki/Linear_logic
    locator: Exponentials
  - url: https://plato.stanford.edu/entries/logic-linear/
    locator: 2.1 Sequent calculus
    note: Di Cosmo and Miller, Linear Logic, Stanford Encyclopedia of Philosophy, revision of 2023-09-16
---

## Example

Let $A$ and $B$ be formulas of [[linear logic|H408H4WHBA]].
The formula $A \multimap (!B \multimap A)$ is derivable in the one-sided calculus, by one use of the weakening rule $?W$.

1. By the definition of $\multimap$ and of linear negation, $!B \multimap A = (!B)^{\perp} \mathbin{\wp} A = ?B^{\perp} \mathbin{\wp} A$.
2. So the formula is $A^{\perp} \mathbin{\wp} (?B^{\perp} \mathbin{\wp} A)$.
3. $\vdash A^{\perp}, A$ is an axiom.
4. The rule $?W$ adds a formula of the form $?C$.
   With $C = B^{\perp}$ it gives $\vdash A^{\perp}, A, ?B^{\perp}$.
5. The rule ${\mathbin{\wp}}$ on $?B^{\perp}$ and $A$ gives $\vdash A^{\perp}, ?B^{\perp} \mathbin{\wp} A$.
6. The rule ${\mathbin{\wp}}$ on the two remaining formulas gives $\vdash A^{\perp} \mathbin{\wp} (?B^{\perp} \mathbin{\wp} A)$.

## Remarks

Step 4 is an instance of [[weakening|JNYY1WD8SR]], restricted to a formula with the exponential $?$.
In two-sided notation, the formula $!B$ on the left can be discarded, since $(!B)^{\perp} = ?B^{\perp}$ on the right of a one-sided sequent.
If we replace $!B$ by $B$, the formula $A \multimap (B \multimap A)$ is [[not derivable|V1ZRAX3GBM]].
So the exponential marks exactly the hypotheses that may be ignored.

## Explanations

### L1 human

In linear logic, every hypothesis must be used, unless it carries the mark "!".
The mark says "there is an unlimited stock of this".
An unlimited stock can be left unused, so the hypothesis $!B$ can be thrown away.

### L2 human

We check that step 4 is the only place where weakening is used.

1. Step 3 is an axiom with the two formulas $A^{\perp}$ and $A$.
2. Step 4 adds $?B^{\perp}$, which comes from no premise.
3. Steps 5 and 6 are par rules, which keep all formulas and join two of them.

The typical use of $?W$ is to discard a hypothesis that was marked as reusable.
A trap: $?W$ adds $?C$ in one-sided notation, which corresponds to discarding $!C^{\perp}$ on the left in two-sided notation.
