---
tag: QZ9FRRH7Y1
kind: example
name: Strong Kleene logic is not first-degree entailment
msc: ["03B50"]
topics: [WZP584JQ06]
audience: research
instance_of: [SZHA10A9X7]
not_instance_of:
  - target: KXTP4P3GHT
    note: explosion is valid in K3 but not in FDE
uses: [74R8A41V6M, AWEG5PR3GF]
sources:
  - url: https://plato.stanford.edu/entries/logic-manyvalued/
    locator: 2.3 True, False, Neither, and Both
---

## Example

[[Strong Kleene logic|74R8A41V6M]] is the restriction of the [[Belnap-Dunn matrix|AWEG5PR3GF]] to $\set{\mathbf{T}, \mathbf{F}, \mathbf{N}}$, with $\mathbf{N}$ in the role of $\tfrac12$ and designated set $\set{\mathbf{T}}$.
We show that the two logics differ.

1. $\set{\mathbf{T}, \mathbf{F}, \mathbf{N}}$ is closed under $\neg$, $\land$, $\lor$: the clauses never add both $T$ and $F$ when no input contains both.
2. In $\mathsf{K}_3$, $p \land \neg p \models q$: the premise has value $\min(x, 1 - x) \le \tfrac12$, so it is never designated.
3. In $\mathsf{FDE}$, $p \land \neg p \not\models q$, by $p = \mathbf{B}$ and $q = \mathbf{F}$.
4. So $\mathsf{K}_3$ validates an inference that $\mathsf{FDE}$ does not.

## Remarks

1. The other direction holds: every $\mathsf{FDE}$-valid inference is $\mathsf{K}_3$-valid, because $\mathsf{K}_3$ valuations are $\mathsf{FDE}$ valuations with values in a submatrix.
2. In the same way $\mathsf{LP}$, the restriction to $\set{\mathbf{T}, \mathbf{F}, \mathbf{B}}$, validates $p \models q \lor \neg q$, which fails in $\mathsf{FDE}$.
3. So $\mathsf{FDE}$ lies below both $\mathsf{K}_3$ and $\mathsf{LP}$, and they are incomparable.

## Explanations

### L1 human

Strong Kleene logic has a value for "no information" but none for "conflicting information".
Without conflicts, a contradiction can never be accepted, so it proves everything.
First-degree entailment has the conflict value, so it does not.

### L2 human

1. Note that $\mathsf{K}_3$ is the part of $\mathsf{FDE}$ without $\mathbf{B}$.
2. Find an $\mathsf{FDE}$ counter-model that needs $\mathbf{B}$.
3. Check that no $\mathsf{K}_3$ valuation can replace it.

The typical use is to compare sublogics of $\mathsf{FDE}$ by the values they keep.
A trap: the $\mathsf{K}_3$ matrix is a submatrix of the $\mathsf{FDE}$ matrix, so $\mathsf{K}_3$ has more valid inferences, not fewer.
