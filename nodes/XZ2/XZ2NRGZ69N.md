---
tag: XZ2NRGZ69N
kind: example
name: One formula in Ł3, strong Kleene and weak Kleene logic
msc: ["03B50"]
topics: [WZP584JQ06]
audience: grad
instance_of: [1CE2TGM6MQ, SZHA10A9X7, BCK5QXQXA6]
uses: [F9NDCFY3GS, 74R8A41V6M, PJA9JVQ5XN]
sources:
  - url: https://en.wikipedia.org/wiki/Three-valued_logic
    locator: Kleene and Priest logics; Łukasiewicz logic
  - url: https://en.wikipedia.org/wiki/Many-valued_logic
    locator: Bochvar's internal three-valued logic
---

## Example

All three logics use the values $\set{0, \tfrac12, 1}$, the designated set $\set{1}$ and the negation $\neg x = 1 - x$.

- In [[Łukasiewicz's logic|F9NDCFY3GS]] and [[strong Kleene logic|74R8A41V6M]], $x \land y = \min(x, y)$ and $x \lor y = \max(x, y)$.
- In [[weak Kleene logic|PJA9JVQ5XN]], $\land$ and $\lor$ agree with $\min$ and $\max$ on $\set{0, 1}$, and give $\tfrac12$ when an argument is $\tfrac12$.
- The implications are $\min(1, 1 - x + y)$ in $\mathrm{Ł}_3$, and $\neg x \lor y$ in the two Kleene logics, each with its own $\lor$.

The implication tables:

| $x$ | $y$ | $\mathrm{Ł}_3$ | $\mathsf{K}_3$ | weak Kleene |
|---|---|---|---|---|
| $0$ | $0$ | $1$ | $1$ | $1$ |
| $0$ | $\tfrac12$ | $1$ | $1$ | $\tfrac12$ |
| $0$ | $1$ | $1$ | $1$ | $1$ |
| $\tfrac12$ | $0$ | $\tfrac12$ | $\tfrac12$ | $\tfrac12$ |
| $\tfrac12$ | $\tfrac12$ | $1$ | $\tfrac12$ | $\tfrac12$ |
| $\tfrac12$ | $1$ | $1$ | $1$ | $\tfrac12$ |
| $1$ | $0$ | $0$ | $0$ | $0$ |
| $1$ | $\tfrac12$ | $\tfrac12$ | $\tfrac12$ | $\tfrac12$ |
| $1$ | $1$ | $1$ | $1$ | $1$ |

We evaluate $\varphi = (p \to p) \lor q$ at $p = \tfrac12$, $q = 1$.

1. $p \to p$ at $p = \tfrac12$: $1$ in $\mathrm{Ł}_3$, by the row $(\tfrac12, \tfrac12)$; $\tfrac12$ in $\mathsf{K}_3$ and in weak Kleene logic.
2. $\mathrm{Ł}_3$: $\varphi = \max(1, 1) = 1$.
3. $\mathsf{K}_3$: $\varphi = \max(\tfrac12, 1) = 1$.
4. Weak Kleene: $\varphi = \tfrac12 \lor 1 = \tfrac12$, since an argument is $\tfrac12$.

So the subformula $p \to p$ separates $\mathrm{Ł}_3$ from $\mathsf{K}_3$, and the whole formula separates $\mathsf{K}_3$ from weak Kleene logic.

## Remarks

The three logics agree on classical arguments, so they differ only in rows that contain $\tfrac12$.
$\mathsf{K}_3$ lets a classical value decide when it can: $1 \lor \tfrac12 = 1$.
Weak Kleene logic never does: the value $\tfrac12$ spreads to the whole formula.
$\mathrm{Ł}_3$ agrees with $\mathsf{K}_3$ except at $\tfrac12 \to \tfrac12$.
With $q = 0$ instead, $\varphi$ has the values $1$, $\tfrac12$, $\tfrac12$.

## Explanations

### L1 human

Three logics use the same three values but different tables.
Take "if $p$ then $p$, or $q$", with $p$ undecided and $q$ true.
Łukasiewicz's logic says "true", because "if $p$ then $p$" is true there.
Strong Kleene logic also says "true", because $q$ is true.
Weak Kleene logic says "undecided", because one part is undecided.

### L2 human

1. Write down the tables of the three logics.
2. Evaluate the innermost subformulas first, in each logic separately.
3. Compare the final values with the designated value $1$.

The typical use is to choose the right logic for an application: computation with possible divergence, partial truth or meaninglessness.
A trap: weak Kleene logic is not "strong Kleene logic with fewer rows"; it changes the value of rows such as $1 \lor \tfrac12$.
