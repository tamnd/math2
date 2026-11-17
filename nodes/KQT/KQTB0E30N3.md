---
tag: KQTB0E30N3
kind: example
name: Disjunctive normal form of p ↔ q
msc: ["03B05"]
topics: [JDK63589SA]
audience: ug1
instance_of: [0GVDFAY4KW]
uses: [06S4WGSEQA, 0S6GMNJ62Y, 05RSK4Q657, 0JMR2HM2N2]
sources:
  - url: https://en.wikipedia.org/wiki/Disjunctive_normal_form
    locator: Conversion to DNF
---

## Example

We find a [[disjunctive normal form|06S4WGSEQA]] of the [[biconditional|0S6GMNJ62Y]] $p \leftrightarrow q$ in two ways.

**From the truth table.**

1. The formula $p \leftrightarrow q$ is true when $p$ and $q$ have the same value, that is, at the rows $(p, q) = (0,0)$ and $(1,1)$.
2. The row $(0,0)$ gives the minterm $\neg p \land \neg q$, and the row $(1,1)$ gives the minterm $p \land q$.
3. So $p \leftrightarrow q \equiv (p \land q) \lor (\neg p \land \neg q)$. This is the full DNF over $p, q$.

**With the laws of logic.**

4. Replace the biconditional: $p \leftrightarrow q \equiv (p \to q) \land (q \to p)$.
5. Replace each implication with $\alpha \to \beta \equiv \neg\alpha \lor \beta$: $p \leftrightarrow q \equiv (\neg p \lor q) \land (\neg q \lor p)$. This is a CNF.
6. Distribute $\land$ over $\lor$: the result is $(\neg p \land \neg q) \lor (\neg p \land p) \lor (q \land \neg q) \lor (q \land p)$.
7. The terms $\neg p \land p$ and $q \land \neg q$ contain a complementary pair, so they are false under every assignment. A false disjunct can be dropped, by $\alpha \lor \bot \equiv \alpha$.
8. So $p \leftrightarrow q \equiv (\neg p \land \neg q) \lor (p \land q)$, the same DNF as in step 3, up to order.

**Check.**

9. At $(0,0)$ the first term is true; at $(1,1)$ the second term is true; at $(0,1)$ and $(1,0)$ each term has a false literal. So the DNF has the [[truth table|05RSK4Q657]] of $p \leftrightarrow q$.

## Remarks

The two methods give the same result, as the uniqueness of the full DNF predicts: both DNFs are full over $p, q$ and [[logically equivalent|0JMR2HM2N2]].
In general the method with the laws gives a DNF that need not be full, and it may contain unsatisfiable terms such as $\neg p \land p$, which can be dropped as long as another term remains.
Step 5 shows a CNF of $p \leftrightarrow q$, so this formula has short forms of both kinds.
For the exclusive or $p_1 \oplus \cdots \oplus p_n$, every DNF has $2^{n-1}$ terms or more, by the dual of the argument in [[the exclusive or example|1CGFB0YM6F]].

## Explanations

### L1 human

"$p$ if and only if $q$" means that $p$ and $q$ have the same truth value.
There are two ways for this to happen: both are true, or both are false.
So the formula is "($p$ and $q$) or (not $p$ and not $q$)".

### L2 human

This example shows the typical cleanup after distribution.

1. Distribution of a CNF with two clauses of two literals gives $2 \cdot 2 = 4$ terms.
2. Terms with a complementary pair are always false, so we drop them.
3. Terms that repeat another term can also be dropped, by $\alpha \lor \alpha \equiv \alpha$.

A trap: do not drop a term only because it looks "redundant" to the eye; drop it only by a law, such as the two laws above.
