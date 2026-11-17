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

The majority function $\operatorname{maj}(p, q, r)$ of three variables is true when at least two of $p, q, r$ are true.
We find its full [[disjunctive normal form|06S4WGSEQA]] from its [[truth table|05RSK4Q657]].

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

1. The function is true at the four rows $(0,1,1)$, $(1,0,1)$, $(1,1,0)$ and $(1,1,1)$, the rows with at least two ones.
2. Each true row gives a minterm: take $p$ if $p = 1$ in the row and $\neg p$ if $p = 0$, and the same for $q$ and $r$.
3. The four minterms are $\neg p \land q \land r$, $p \land \neg q \land r$, $p \land q \land \neg r$ and $p \land q \land r$.
4. Each minterm is true at its own row only, so their disjunction is true exactly at the four true rows.
5. So the full DNF is
$$\operatorname{maj}(p,q,r) \equiv (p \land q \land r) \lor (p \land q \land \neg r) \lor (p \land \neg q \land r) \lor (\neg p \land q \land r).$$
6. By uniqueness of the full DNF, every full DNF of the majority function over $p, q, r$ has these four terms, in some order.

## Remarks

A shorter DNF is $(p \land q) \lor (p \land r) \lor (q \land r)$.
It is true exactly when some pair of the variables is true, that is, when at least two are true.
It is obtained from the full DNF by the law $(\alpha \land \beta) \lor (\alpha \land \neg\beta) \equiv \alpha$: the first two terms combine to $p \land q$, and $p \land q \land r$ also combines with each of the last two terms.
Since $\alpha \equiv \alpha \lor \alpha$, the term $p \land q \land r$ may be used in all three combinations.
The majority function preserves $0$ and $1$, and it is monotone and self-dual, so it lies in four of the five classes of [[Post's functional completeness theorem|WGBR7JHBV4]].
It is not affine, because its algebraic normal form $pq \oplus pr \oplus qr$ has terms of degree $2$.

## Explanations

### L1 human

Three friends vote yes or no, and the group says yes when at least two friends say yes.
There are four ways to get a yes: all three say yes, or exactly one friend says no.
Each way gives one part of the formula, such as "$p$ and $q$ and not $r$".
The formula is the "or" of these four parts.

### L2 human

The majority function is the basic gate of fault-tolerant circuits: three copies of a circuit vote, and one faulty copy is outvoted.
The full DNF has $4$ terms with $3$ literals each, and the short DNF has $3$ terms with $2$ literals each.
A trap is to forget the row $(1,1,1)$: "at least two" includes "all three".
Without the term $p \land q \land r$, the full DNF would describe "exactly two".
