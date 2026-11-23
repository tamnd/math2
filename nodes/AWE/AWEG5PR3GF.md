---
tag: AWEG5PR3GF
kind: definition
name: First-degree entailment FDE
msc: ["03B50", "03B47"]
topics: [WZP584JQ06]
audience: research
defines: KXTP4P3GHT
uses: [66NMTCQNQV, AJEJS6TFWP, K6CVH3D7R8]
sources:
  - url: https://plato.stanford.edu/entries/logic-manyvalued/
    locator: 2.3 True, False, Neither, and Both
  - url: https://en.wikipedia.org/wiki/Four-valued_logic
    locator: Belnap
---

## Definition

First-degree entailment is the logic of a four-valued matrix whose values are the sets of reports "true" and "false" a sentence can receive, with the values that contain "true" designated.

Let $\mathbf{4} = \{\mathbf{T}, \mathbf{F}, \mathbf{B}, \mathbf{N}\}$ be the set of subsets of $\{T, F\}$, with $\mathbf{T} = \{T\}$, $\mathbf{F} = \{F\}$, $\mathbf{B} = \{T, F\}$ and $\mathbf{N} = \emptyset$.
Define the operations on $\mathbf{4}$ by the following clauses, for all $x, y \in \mathbf{4}$.

1. $T \in \neg x$ iff $F \in x$, and $F \in \neg x$ iff $T \in x$.
2. $T \in x \land y$ iff $T \in x$ and $T \in y$, and $F \in x \land y$ iff $F \in x$ or $F \in y$.
3. $T \in x \lor y$ iff $T \in x$ or $T \in y$, and $F \in x \lor y$ iff $F \in x$ and $F \in y$.

*First-degree entailment* $\mathsf{FDE}$ is the logic of the [[logical matrix|AJEJS6TFWP]] $\langle \mathbf{4}, \neg, \land, \lor, \{\mathbf{T}, \mathbf{B}\} \rangle$.
So $\Gamma \models_{\mathsf{FDE}} \varphi$ iff every valuation $v$ with $T \in v(\gamma)$ for all $\gamma \in \Gamma$ has $T \in v(\varphi)$.

The resulting tables, with the row for $x$:

| $x$ | $\neg x$ | $x \land \mathbf{N}$ | $x \land \mathbf{F}$ | $x \land \mathbf{T}$ | $x \land \mathbf{B}$ |
|---|---|---|---|---|---|
| $\mathbf{N}$ | $\mathbf{N}$ | $\mathbf{N}$ | $\mathbf{F}$ | $\mathbf{N}$ | $\mathbf{F}$ |
| $\mathbf{F}$ | $\mathbf{T}$ | $\mathbf{F}$ | $\mathbf{F}$ | $\mathbf{F}$ | $\mathbf{F}$ |
| $\mathbf{T}$ | $\mathbf{F}$ | $\mathbf{N}$ | $\mathbf{F}$ | $\mathbf{T}$ | $\mathbf{B}$ |
| $\mathbf{B}$ | $\mathbf{B}$ | $\mathbf{F}$ | $\mathbf{F}$ | $\mathbf{B}$ | $\mathbf{B}$ |

Disjunction is given by De Morgan's law $x \lor y = \neg(\neg x \land \neg y)$.

## Notation

The values are also written $\mathsf{t}$, $\mathsf{f}$, $\mathsf{b}$, $\mathsf{n}$, or as pairs of bits for "told true" and "told false".
$\mathsf{FDE}$ is also called $\mathrm{BD}$, for Belnap-Dunn.
In the truth order $\le_t$, $\mathbf{F}$ is the bottom, $\mathbf{T}$ is the top, and $\mathbf{N}$ and $\mathbf{B}$ are incomparable; $\land$ and $\lor$ are the meet and join for $\le_t$.

## Remarks

Each part of the definition has a reason.
The two halves of each clause treat truth and falsity separately, so a report of falsity never cancels a report of truth.
On $\{\mathbf{T}, \mathbf{F}\}$ the clauses are the classical tables, so every $\mathsf{FDE}$-valid inference is classically valid.
The [[designated values|K6CVH3D7R8]] are the sets that contain $T$.
Designating the sets that do not contain $F$ gives the same consequence relation, because the map that swaps $\mathbf{B}$ and $\mathbf{N}$ and fixes $\mathbf{T}$ and $\mathbf{F}$ is an automorphism of the algebra.

We check the entry $\mathbf{N} \land \mathbf{B}$.
Since $T \notin \mathbf{N}$, we get $T \notin \mathbf{N} \land \mathbf{B}$, and since $F \in \mathbf{B}$, we get $F \in \mathbf{N} \land \mathbf{B}$, so the value is $\mathbf{F}$.
Double negation $\neg \neg p \models_{\mathsf{FDE}} p$ holds, since $T \in \neg \neg x$ iff $F \in \neg x$ iff $T \in x$.
Explosion $p \land \neg p \models_{\mathsf{FDE}} q$ fails at $p = \mathbf{B}$, $q = \mathbf{F}$.
Restricting to $\{\mathbf{T}, \mathbf{F}, \mathbf{N}\}$ gives the [[strong Kleene matrix|74R8A41V6M]], and restricting to $\{\mathbf{T}, \mathbf{F}, \mathbf{B}\}$ gives the matrix of $\mathsf{LP}$.
The [[concept page|KXTP4P3GHT]] gives the motivation and the uses.

## Explanations

### L1 human

Each sentence carries a set of reports: "true", "false", both or none.
"Not" swaps the two reports.
"And" is reported true when both parts are, and false when one part is.
An argument is valid when "reported true" passes from the premises to the conclusion.

### L2 human

Compute truth and falsity of a formula in two separate passes.
For example, at $p = \mathbf{B}$, $p \land \neg p$ is told true, since both $p$ and $\neg p$ are told true.
It is also told false, so $p \land \neg p = \mathbf{B}$.
Watch out: the truth order and the inclusion order on $\mathbf{4}$ are different, and $\land$ is the meet only for the truth order.
