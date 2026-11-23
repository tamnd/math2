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

We find a [[disjunctive normal form|06S4WGSEQA]] of the [[biconditional|0S6GMNJ62Y]] $p \leftrightarrow q$ in two ways, and we see that they agree.

The first way uses the [[truth table|05RSK4Q657]].
The formula $p \leftrightarrow q$ is true when $p$ and $q$ have the same value, that is, at the rows $(0, 0)$ and $(1, 1)$.
The row $(0, 0)$ gives the minterm $\neg p \land \neg q$, and the row $(1, 1)$ gives the minterm $p \land q$, so
$$p \leftrightarrow q \;\equiv\; (p \land q) \lor (\neg p \land \neg q).$$
This is the full DNF over $p$ and $q$.

The second way uses the laws of logic.

1. Replace the biconditional by two implications, and each implication with $\alpha \to \beta \equiv \neg\alpha \lor \beta$:
$$p \leftrightarrow q \equiv (p \to q) \land (q \to p) \equiv (\neg p \lor q) \land (\neg q \lor p).$$
   This is already a CNF.
2. Distribute $\land$ over $\lor$, which pairs each literal of the first clause with each literal of the second:
$$p \leftrightarrow q \equiv (\neg p \land \neg q) \lor (\neg p \land p) \lor (q \land \neg q) \lor (q \land p).$$
3. The terms $\neg p \land p$ and $q \land \neg q$ contain a complementary pair, so they are false at every row.
   A false disjunct can be dropped, by the law $\alpha \lor \bot \equiv \alpha$.
4. What remains is $(\neg p \land \neg q) \lor (p \land q)$, the same DNF as before, up to order.

Check: at $(0, 0)$ the term $\neg p \land \neg q$ is true, at $(1, 1)$ the term $p \land q$ is true, and at $(0, 1)$ and $(1, 0)$ each term has a false literal.

## Remarks

The two methods agree, as the uniqueness of the full DNF predicts, because both results are full over $p$ and $q$ and are [[logically equivalent|0JMR2HM2N2]].
In general the method with the laws gives a DNF that need not be full, and it may produce unsatisfiable terms such as $\neg p \land p$.
You may drop them as long as at least one term remains.

Step 1 also shows a short CNF of $p \leftrightarrow q$, so this formula is short in both normal forms.
That changes when more variables are added: for the exclusive or $p_1 \oplus \cdots \oplus p_n$, every DNF has at least $2^{n-1}$ terms, by the dual of the argument in [[the exclusive or example|1CGFB0YM6F]].

## Explanations

### L1 human

"$p$ if and only if $q$" means that $p$ and $q$ have the same truth value.
There are two ways for this to happen: both are true, or both are false.
So the formula is "($p$ and $q$) or (not $p$ and not $q$)".

### L2 human

This example shows the usual cleanup after distribution.
A CNF with two clauses of two literals each distributes into $2 \cdot 2 = 4$ terms.
Terms with a complementary pair are always false, so we drop them.
Terms that repeat another term can also be dropped, by $\alpha \lor \alpha \equiv \alpha$.
Watch out: drop a term only by a law such as these two, not because it looks redundant.
For example, in $(p \land q) \lor (p \land \neg q)$ neither term can be dropped, although the two merge into $p$.
