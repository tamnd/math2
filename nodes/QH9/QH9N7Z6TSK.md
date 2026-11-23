---
tag: QH9N7Z6TSK
kind: example
name: Full disjunctive normal form of the majority of three variables
msc: ["03B05", "06E30"]
topics: [JDK63589SA]
audience: ug1
instance_of: [0GVDFAY4KW]
uses: [06S4WGSEQA, 05RSK4Q657, 0X05GS525E]
sources:
  - url: https://en.wikipedia.org/wiki/Disjunctive_normal_form
    locator: Conversion to DNF
  - url: https://en.wikipedia.org/wiki/Majority_function
    locator: lead section
---

## Example

The majority function $\operatorname{maj}(p, q, r)$ is true when at least two of $p$, $q$ and $r$ are true.
We find its full [[disjunctive normal form|06S4WGSEQA]] from its [[truth table|05RSK4Q657]]:

| $p$ | $q$ | $r$ | $\operatorname{maj}$ |
|---|---|---|---|
| 0 | 0 | 0 | 0 |
| 0 | 0 | 1 | 0 |
| 0 | 1 | 0 | 0 |
| 0 | 1 | 1 | 1 |
| 1 | 0 | 0 | 0 |
| 1 | 0 | 1 | 1 |
| 1 | 1 | 0 | 1 |
| 1 | 1 | 1 | 1 |

1. The function is true at the four rows with at least two ones: $(0, 1, 1)$, $(1, 0, 1)$, $(1, 1, 0)$ and $(1, 1, 1)$.
2. Each true row gives a minterm, with $p$ when $p = 1$ in the row and $\neg p$ when $p = 0$, and the same for $q$ and $r$.
   The minterms are $\neg p \land q \land r$, $p \land \neg q \land r$, $p \land q \land \neg r$ and $p \land q \land r$.
3. Each minterm is true at its own row only, so their disjunction is true exactly at the four true rows:
$$\operatorname{maj}(p, q, r) \equiv (p \land q \land r) \lor (p \land q \land \neg r) \lor (p \land \neg q \land r) \lor (\neg p \land q \land r).$$
4. The full DNF over $p, q, r$ is unique up to order, so every full DNF of the majority function has exactly these four terms.

Check at the row $(1, 0, 0)$: each term contains $q$ or $r$ as a positive literal, or contains $\neg p$, and each of these is false, so the DNF is false, as the table says.

## Remarks

The full DNF is not the shortest one.
The law $(\alpha \land \beta) \lor (\alpha \land \neg \beta) \equiv \alpha$ merges $p \land q \land r$ with $p \land q \land \neg r$ into $p \land q$.
Because $\alpha \equiv \alpha \lor \alpha$, we may reuse $p \land q \land r$ and merge it with each of the last two terms as well.
The result is
$$\operatorname{maj}(p, q, r) \equiv (p \land q) \lor (p \land r) \lor (q \land r),$$
which says that some pair of the variables is true.

The majority function is also a good test case for [[Post's functional completeness theorem|WGBR7JHBV4]].
It maps $(0, 0, 0)$ to $0$ and $(1, 1, 1)$ to $1$, it is monotone, and it is self-dual, since negating all three inputs negates the output.
It is not affine, because its algebraic normal form $pq \oplus pr \oplus qr$ has terms of degree $2$.
So it lies in four of Post's five classes.

## Explanations

### L1 human

Three friends vote yes or no, and the group says yes when at least two friends say yes.
There are four ways to get a yes: all three say yes, or exactly one friend says no.
Each way gives one part of the formula, such as "$p$ and $q$ and not $r$".
The formula is the "or" of these four parts.

### L2 human

The majority function is the voting gate of fault-tolerant circuits: three copies of a circuit vote, and one faulty copy is outvoted.
The full DNF has $4$ terms with $3$ literals each, and the short DNF has $3$ terms with $2$ literals each.
Watch out for the row $(1, 1, 1)$: "at least two" includes "all three".
Without the term $p \land q \land r$, the full DNF would describe the function "exactly two".
