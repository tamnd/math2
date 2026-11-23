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

For any two truth degrees, one of the two implications between them is fully true, and the prelinearity axiom records this.

Let $*$ be a left-continuous [[t-norm|BHGCVPAJW0]] with residuum $\Rightarrow$, which exists by [[the left-continuity statement|D1R4D2HEPP]].
For all $x, y, c \in [0, 1]$ the following hold.

1. $\max(x \Rightarrow y, \ y \Rightarrow x) = 1$.
2. $((x \Rightarrow y) \Rightarrow c) \Rightarrow (((y \Rightarrow x) \Rightarrow c) \Rightarrow c) = 1$.

So the prelinearity axiom BL6 of [[BL|3AQ5GHTXA4]] has value $1$ under every evaluation in the standard algebra of $*$.

## Remarks

### A worked case

Take the Łukasiewicz t-norm with $x = 0.3$, $y = 0.6$ and $c = 0.5$.
Then $x \Rightarrow y = 1$ and $y \Rightarrow x = 0.7$.
The inner values are $1 \Rightarrow 0.5 = 0.5$ and $0.7 \Rightarrow 0.5 = 0.8$, and then $0.8 \Rightarrow 0.5 = 0.7$.
So item 2 reads $0.5 \Rightarrow 0.7 = 1$.

### Why each hypothesis is needed

Left-continuity is needed for the residuum to exist, and without a residuum the formula has no value.
The linear order of $[0, 1]$ is needed as well.
In a Heyting algebra that is not a chain, prelinearity can fail, as [[the fork|6S7TSV01WB]] shows.
Of the t-norm axioms, the proof uses only commutativity, the bound $a * b \le a$, the unit law $1 * a = a$ and residuation.

### Consequences

The axiom BL6, also called MTL6, is sound for the standard semantics of [[MTL|PT5PHKJDYM]] and of BL.
The same proof works in every linearly ordered commutative integral residuated lattice, so prelinearity is valid in every MTL-chain.
Identities are preserved by subdirect products, so $(x \Rightarrow y) \lor (y \Rightarrow x) = 1$ holds in every subdirect product of such chains.

### What prelinearity separates

Intuitionistic logic does not prove $(p \to q) \lor (q \to p)$, and adding it gives [[Gödel-Dummett logic|474SGS2N0X]].
So prelinearity is a law of chains, not a law of all residuated lattices.

### Generalizations

For algebras that are not chains, the identity $(x \Rightarrow y) \lor (y \Rightarrow x) = 1$ is taken as part of the definition of an MTL-algebra.
It is the algebraic form of the axiom, and item 1 is its case for the chain $[0, 1]$.

## History

Prelinearity is one of the axioms in Hájek's 1998 axiomatization of BL.
Esteva and Godo kept it when they introduced MTL in 2001.

## Explanations

### L1 human

For any two degrees of truth, one is at most the other.
So one of "$x$ implies $y$" and "$y$ implies $x$" is fully true.
The prelinearity axiom states this fact inside the logic.

### L2 human

The proof splits into the two cases $x \le y$ and $y \le x$.
In each case one implication is $1$, and $1 \Rightarrow c = c$.
Watch out: item 1 uses $\max$ because $[0, 1]$ is a chain, and in a general lattice the join need not be one of its two arguments.

### L3 human

Prelinearity is the logical form of the subdirect decomposition into chains.
In Kripke semantics for intuitionistic logic, the formula $(p \to q) \lor (q \to p)$ corresponds to a frame condition: the worlds above any world form a chain.
The fork violates this condition.
