---
tag: D0ZADJFPQE
kind: statement
role: proposition
name: Prelinearity holds for every left-continuous t-norm
aliases: [prelinearity-for-left-continuous-t-norms]
msc: ["03B52", "06F05"]
topics: [WZP584JQ06]
audience: grad
about: [3AQ5GHTXA4, PT5PHKJDYM, P4T18C5736]
uses: [BHGCVPAJW0, D1R4D2HEPP]
proofs: [V1A4G16JRZ]
sources:
  - url: https://en.wikipedia.org/wiki/Monoidal_t-norm_logic
    locator: Axioms; MTL-algebras
  - url: https://en.wikipedia.org/wiki/BL_(logic)
    locator: Axioms
  - url: https://plato.stanford.edu/entries/logic-fuzzy/
    locator: "2. MTL: A fundamental fuzzy logic"
---

## Statement

Let $*$ be a left-continuous [[t-norm|BHGCVPAJW0]] with residuum $\Rightarrow$, which exists by [[the left-continuity statement|D1R4D2HEPP]].
For all $x, y, c \in [0, 1]$:

1. $\max(x \Rightarrow y, \ y \Rightarrow x) = 1$;
2. $((x \Rightarrow y) \Rightarrow c) \Rightarrow (((y \Rightarrow x) \Rightarrow c) \Rightarrow c) = 1$.

So the prelinearity axiom BL6 of [[BL|3AQ5GHTXA4]] has the value $1$ under every evaluation in the standard algebra of $*$.

## Remarks

### Why each hypothesis is needed

1. Left-continuity is needed for the residuum to exist; without a residuum the formula has no value.
2. The linear order of $[0, 1]$ is needed: in a Heyting algebra that is not a chain, prelinearity can fail, as [[the fork|6S7TSV01WB]] shows.
3. The t-norm axioms are used only through commutativity, the inequality $a * b \le a$ and the unit law $1 * a = a$.

### Consequences

1. The axiom BL6, also called MTL6, is sound for the standard semantics of [[MTL|PT5PHKJDYM]] and of BL.
2. The same proof works in every linearly ordered commutative integral residuated lattice, so prelinearity is valid in every MTL-chain.
3. Since validity is preserved by subdirect products, the identity $(x \Rightarrow y) \lor (y \Rightarrow x) = 1$ holds in every subdirect product of such chains.

### Converse

The statement is not an equivalence, so it has no converse in the strict sense.
A related fact: intuitionistic logic does not prove the form $(p \to q) \lor (q \to p)$, and adding it gives [[Gödel-Dummett logic|474SGS2N0X]].
So prelinearity is a law of chains, not a law of all residuated lattices.

### Generalizations

For algebras that are not chains, SEP and Wikipedia take the identity $(x \Rightarrow y) \lor (y \Rightarrow x) = 1$ as part of the definition of an MTL-algebra.
This identity is the algebraic form of the axiom.

## History

Wikipedia reports that the prelinearity axiom is in Hájek's 1998 axioms for BL, and that Esteva and Godo kept it in MTL in 2001.

## Explanations

### L1 human

For any two degrees of truth, one is at most the other.
So one of "$x$ implies $y$" and "$y$ implies $x$" is fully true.
The prelinearity axiom states this fact inside the logic.

### L2 human

The proof splits into the two cases $x \le y$ and $y \le x$.
In each case one implication is $1$, and $1 \Rightarrow c = c$.
A trap: item 1 uses $\max$ because $[0, 1]$ is a chain; in a general lattice the join is not one of its two arguments.

### L3 human

Prelinearity is the logical form of the subdirect decomposition into chains.
In Kripke semantics for intuitionistic logic, the form $(p \to q) \lor (q \to p)$ corresponds to a frame condition: the worlds above any world form a total order.
The fork violates this condition.
