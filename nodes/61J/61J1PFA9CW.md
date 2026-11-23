---
tag: 61J1PFA9CW
kind: example
name: Łukasiewicz's three-valued logic is not strong Kleene logic
msc: ["03B50"]
topics: [WZP584JQ06]
audience: grad
instance_of: [1CE2TGM6MQ]
not_instance_of:
  - target: SZHA10A9X7
    note: its implication differs from the strong Kleene implication at the pair (1/2, 1/2)
uses: [74R8A41V6M, F9NDCFY3GS]
sources:
  - url: https://en.wikipedia.org/wiki/Three-valued_logic
    locator: Kleene and Priest logics; Łukasiewicz logic
---

## Example

Both logics use the values $0, \tfrac12, 1$, the designated set $\{1\}$, the negation $\neg x = 1 - x$, and $\min$ and $\max$ for conjunction and disjunction.
The [[strong Kleene implication|74R8A41V6M]] is $x \to_K y = \max(1 - x, y)$, and the [[Łukasiewicz implication|F9NDCFY3GS]] is $x \to_{Ł} y = \min(1, 1 - x + y)$.
We compare the nine entries of the two tables.

1. If $x = 0$, both give $1$, since $\max(1, y) = 1$ and $\min(1, 1 + y) = 1$.
2. If $x = 1$, both give $y$, since $\max(0, y) = y$ and $\min(1, y) = y$.
3. If $x = \tfrac12$ and $y = 0$, both give $\tfrac12$.
4. If $x = \tfrac12$ and $y = 1$, both give $1$.
5. If $x = y = \tfrac12$, then $\to_K$ gives $\max(\tfrac12, \tfrac12) = \tfrac12$ and $\to_{Ł}$ gives $\min(1, 1) = 1$.
6. So $p \to p$ takes the value $1$ at $p = \tfrac12$ in $\mathrm{Ł}_3$ and $\tfrac12$ in $\mathsf{K}_3$.
   It is a tautology of $\mathrm{Ł}_3$ and not of $\mathsf{K}_3$, so the two logics are different.

## Remarks

One differing entry out of nine changes the set of tautologies from empty, as in [[strong Kleene logic|SZHA10A9X7]], to infinite.
The difference is not a matter of notation either.
By [[the non-definability theorem|729J1FD1GZ]], no formula in the Kleene connectives defines $\to_{Ł}$, so $\mathrm{Ł}_3$ can say more than $\mathsf{K}_3$.

For formulas that use only $\neg$, $\land$ and $\lor$, the two logics have the same valid inferences, since those tables agree.
So the whole difference sits in the implication, and in one row of it.

## Explanations

### L1 human

Two three-valued logics can look the same and still differ.
These two disagree only on "if undecided, then undecided".
Łukasiewicz says this is true, and Kleene says it is undecided.
That one entry decides whether "if $p$ then $p$" is a law.

### L2 human

To separate two matrices on the same values, write both implication tables and compare the nine entries.
Here only the entry at $(\tfrac12, \tfrac12)$ differs.
Then find a formula that uses the differing entry, here $p \to p$ at $p = \tfrac12$.
This is the typical way to show that two matrices give different logics.
Watch out: equal tables for $\neg$, $\land$ and $\lor$ do not make two logics equal once $\to$ is primitive in one of them.
