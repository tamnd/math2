---
tag: WSGZ5HGK1X
kind: concept
name: Coherence space
aliases: [coherent-space]
msc: ["03F52", "03B70", "68Q55"]
topics: [98QF5J4W16]
audience: research
uses: [2P2184B6HE, 0BYX1D7C2E]
sources:
  - url: https://en.wikipedia.org/wiki/Coherent_space
    locator: Definitions
  - url: https://en.wikipedia.org/wiki/Coherent_space
    locator: Linearity
  - url: https://plato.stanford.edu/entries/logic-linear/
    locator: 3.2 Semantics of proofs
    note: Di Cosmo and Miller, Linear Logic, Stanford Encyclopedia of Philosophy, revision of 2023-09-16
  - url: https://plato.stanford.edu/entries/logic-linear/
    locator: 1.1 A bit of history
    note: Di Cosmo and Miller, Linear Logic, Stanford Encyclopedia of Philosophy, revision of 2023-09-16
  - book: isbn:9780521371810
    note: Girard, Lafont and Taylor, Proofs and Types
---

## Summary

A *coherence space* is a set of *tokens*, its *web*, with a reflexive and symmetric relation called *coherence*; see [[the definition|6RQPAH8SBK]].
Its points are the [[cliques|0BYX1D7C2E]], the sets of pairwise coherent tokens.
Coherence spaces interpret the formulas of [[linear logic|2P2184B6HE]], and the proofs of a formula as cliques.
Maps between them are *stable functions*, and the *linear* stable functions are those that use each input token at most once.

## Motivation

A program that computes a value from an input reads only finite parts of the input.
A token is one piece of information, and a clique is a consistent set of pieces, such as a partial result.
A stable function produces each output token from a unique minimal part of the input.
When that part is always a single token, the function is linear: it reads its input once.

## Notation

We write $|A|$ for the web, $\alpha \frown \beta$ for coherence and $\mathrm{Cl}(A)$ for the set of cliques.
Some texts write $\alpha \sim \beta$ or $\alpha \asymp \beta$ for coherence.
The book "Proofs and Types" uses the name *coherence space*, and other texts use *coherent space*.

## Remarks

### Examples

1. The [[flat space of booleans|B2R55XVZMC]] has two incoherent tokens $t$ and $f$.
2. The [[trace of a stable function|E47Q7BMD8W]] lists the minimal inputs for each output token.
3. Every graph with a loop at each vertex gives a coherence space whose cliques are its cliques.

### Non-examples

The [[parallel or|WBJWGYGSNQ]] is monotone and continuous, but it is not stable.
A family of sets that is not closed under subsets, such as $\set{\set{1, 2}}$, is not the set of cliques of a coherence space.

### Basic properties

1. Every subset of a clique is a clique, and the union of a directed family of cliques is a clique.
2. The linear negation $A^{\perp}$ has the same web, and two distinct tokens cohere in $A^{\perp}$ exactly when they do not cohere in $A$.
3. A clique of $A$ and a clique of $A^{\perp}$ meet in at most one token.

### History

The SEP entry on linear logic states that Girard introduced linear logic in 1987 from a semantic analysis of the models of System F.
The same entry states that coherence spaces give a set-theoretic semantics of proofs, as Girard showed in 1987.
The Wikipedia article on coherent spaces states that linear stable functions were the original motivation for linear logic.

### Common errors

Coherence is reflexive, so a single token is always a clique, even in $A^{\perp}$.
For two distinct tokens, exactly one of "coherent in $A$" and "coherent in $A^{\perp}$" holds.

## Explanations

### L1 human

Think of a token as a fact about an object, such as "the answer is yes".
Two facts are coherent if they can both be true of one object.
A clique is a set of facts that fit together, and it describes the object in part.

### L2 human

We compute the linear negation and the tensor of the flat space $B$ with web $\set{t, f}$ and $t$, $f$ incoherent.

1. The cliques of $B$ are $\emptyset$, $\set{t}$ and $\set{f}$.
2. In $B^{\perp}$, the tokens $t$ and $f$ cohere, so the cliques are all four subsets of $\set{t, f}$.
3. In $B \otimes B$, $(\alpha, \beta) \frown (\alpha', \beta')$ if and only if $\alpha \frown \alpha'$ and $\beta \frown \beta'$, so only equal pairs cohere.
4. So the cliques of $B \otimes B$ are $\emptyset$ and the four singletons.

The typical use of these computations is to find the denotation of a proof as a clique.
A trap: $\set{t, f}$ is a clique of $B^{\perp}$ but not of $B$, so the two spaces have different points though they have the same web.

### L3 human

Coherence spaces with linear maps form a $*$-autonomous category, so they model classical linear logic.
The SEP entry names $*$-autonomous categories, after Barr, among the categorical models of linear logic.
The exponential $!A$ has as web the finite cliques of $A$, and the stable maps from $A$ to $B$ are the linear maps from $!A$ to $B$.
This splitting of the function space matches the Girard translation of $A \to B$ as ${!A} \multimap B$.
