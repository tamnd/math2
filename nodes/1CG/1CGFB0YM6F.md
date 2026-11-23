---
tag: 1CGFB0YM6F
kind: example
name: Conjunctive normal form of exclusive or from the truth table
msc: ["03B05"]
topics: [JDK63589SA]
audience: ug1
instance_of: [0B3D4C8YF2]
uses: [07C4A8Y18K, 05RSK4Q657]
sources:
  - url: https://en.wikipedia.org/wiki/Conjunctive_normal_form
    locator: Conversion by semantic means
---

## Example

Exclusive or, $p \oplus q$, is true when exactly one of $p$ and $q$ is true.
We read a [[conjunctive normal form|07C4A8Y18K]] of it off its [[truth table|05RSK4Q657]]:

| $p$ | $q$ | $p \oplus q$ |
|---|---|---|
| 0 | 0 | 0 |
| 0 | 1 | 1 |
| 1 | 0 | 1 |
| 1 | 1 | 0 |

1. The formula is false at the two rows $(0, 0)$ and $(1, 1)$, and the CNF needs one clause for each of them.
2. Each clause must be false at its own row and true at every other row.
   So each literal must be false at that row: take the variable when its value is $0$, and its negation when its value is $1$.
3. The row $(0, 0)$ gives the clause $p \lor q$, which is false only when $p = 0$ and $q = 0$.
4. The row $(1, 1)$ gives the clause $\neg p \lor \neg q$, which is false only when $p = 1$ and $q = 1$.
5. The conjunction is false exactly where one of its clauses is false, so
$$p \oplus q \;\equiv\; (p \lor q) \land (\neg p \lor \neg q).$$

Check at the row $(0, 1)$: the first clause is true because $q = 1$, and the second is true because $\neg p = 1$, so the CNF is true, as $p \oplus q$ is.

## Remarks

The result is the full CNF of $p \oplus q$, because each clause contains each variable once.
The same method applied to $p \leftrightarrow q$, the negation of $p \oplus q$, uses the false rows $(0, 1)$ and $(1, 0)$ and gives $(p \lor \neg q) \land (\neg p \lor q)$.

For the exclusive or of $n$ variables, $p_1 \oplus \cdots \oplus p_n$, the function is false at the rows with an even number of ones.
There are $2^{n-1}$ such rows, so the method gives $2^{n-1}$ clauses.
No CNF of this function is shorter.
Drop from the CNF every clause with a complementary pair, since such a clause is always true.
Suppose a remaining clause $C$ does not mention some variable $p_i$.
Then $C$ is false at some row, and also at the row that differs from it only in $p_i$.
The function is true at one of these two rows, because flipping one variable changes the parity, but the CNF is false at both.
This is impossible, so each remaining clause mentions all $n$ variables, is false at one row only, and each false row needs its own clause.

## Explanations

### L1 human

"Exactly one of $p$ and $q$ is true" says two things.
At least one of them is true, which is $p \lor q$.
At least one of them is false, which is $\neg p \lor \neg q$.
Both things together give the formula $(p \lor q) \land (\neg p \lor \neg q)$.

### L2 human

The truth-table method works for each formula that is false at some row.
List the rows where the formula is false.
For each such row write one clause, with $p$ when $p = 0$ in the row and $\neg p$ when $p = 1$.
Then join the clauses with $\land$.
Watch out for the rule in the middle step: students often swap it, but the clause must be false at its row, so each literal must be false there.
The dual method takes the true rows and the opposite rule, and it gives the [[disjunctive normal form|0GVDFAY4KW]] $(\neg p \land q) \lor (p \land \neg q)$.
