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

Test explosion $p \land \neg p \models q$ in two logics.
[[Strong Kleene logic|74R8A41V6M]] is the restriction of the [[Belnap-Dunn matrix|AWEG5PR3GF]] to $\{\mathbf{T}, \mathbf{F}, \mathbf{N}\}$, with $\mathbf{N}$ in the role of $\tfrac12$ and the designated set $\{\mathbf{T}\}$.
First-degree entailment uses all four values $\mathbf{T}$, $\mathbf{F}$, $\mathbf{N}$ and $\mathbf{B}$, with $\mathbf{T}$ and $\mathbf{B}$ designated.

1. The set $\{\mathbf{T}, \mathbf{F}, \mathbf{N}\}$ is closed under $\neg$, $\land$ and $\lor$, because the clauses never produce "both told true and told false" from inputs that are never told both.
2. In $\mathsf{K}_3$, explosion holds, since the premise has the value $\min(x, 1 - x) \le \tfrac12$ and is never designated.
3. In $\mathsf{FDE}$, explosion fails at $p = \mathbf{B}$ and $q = \mathbf{F}$, where $p \land \neg p = \mathbf{B}$ is designated and $q$ is not.
4. So $\mathsf{K}_3$ validates an inference that $\mathsf{FDE}$ does not.

## Remarks

The other direction holds: every $\mathsf{FDE}$-valid inference is $\mathsf{K}_3$-valid, because $\mathsf{K}_3$ valuations are $\mathsf{FDE}$ valuations with values in a submatrix.
In the same way $\mathsf{LP}$, the restriction to $\{\mathbf{T}, \mathbf{F}, \mathbf{B}\}$, validates $p \models q \lor \neg q$, which fails in $\mathsf{FDE}$ at $p = \mathbf{T}$, $q = \mathbf{N}$.
So $\mathsf{FDE}$ lies below both $\mathsf{K}_3$ and $\mathsf{LP}$, and the two three-valued logics are incomparable.

## Explanations

### L1 human

Strong Kleene logic has a value for "no information" but none for "conflicting information".
Without conflicts, a contradiction can never be accepted, so it entails everything.
First-degree entailment has the conflict value, so it does not.

### L2 human

To compare two sublogics of $\mathsf{FDE}$, find an $\mathsf{FDE}$ counter-model that needs a value the smaller matrix lacks, here $\mathbf{B}$.
Then check that no valuation of the smaller matrix can replace it.
The typical use is to compare sublogics of $\mathsf{FDE}$ by the values they keep.
Watch out: the $\mathsf{K}_3$ matrix is a submatrix of the $\mathsf{FDE}$ matrix, so $\mathsf{K}_3$ has more valid inferences, not fewer.
