---
tag: 14WPPDDK8M
kind: concept
name: Stably embedded set
aliases: [stably-embedded-set, stable-embeddedness, stably-embedded]
msc: ["03C45", "03C07"]
topics: [SZRM3N6BXW]
audience: research
uses: [Q0HM88QQKN, CY1TXHF6KQ, EYTTQZ0E1S, 9V71Q3SD1G]
sources:
  - url: https://en.wikipedia.org/wiki/Stable_theory
    locator: Definition and alternate characterizations
  - book: isbn:9780521763240
  - book: isbn:9780198534372
---

## Summary

Let $T$ be a complete theory with [[monster model|EYTTQZ0E1S]] $\mathbb{M}$, and let $D$ be a $\emptyset$-[[definable set|CY1TXHF6KQ]], possibly in a sort of $\mathbb{M}^{\mathrm{eq}}$.
The set $D$ is *stably embedded* if, for every formula $\varphi(\bar x, \bar y)$ and every parameter tuple $\bar b$ from anywhere in $\mathbb{M}^{\mathrm{eq}}$, the trace $\varphi(\mathbb{M}, \bar b) \cap D^n$ is definable with parameters from $D$.
Equivalently, every [[type|9V71Q3SD1G]] over $D$ realized in $\mathbb{M}$ is definable over $D$; the exact page is [[this definition|FN98G2RH9W]].
Stably embedded sets can be studied as structures of their own, with the induced structure, without losing any definable sets.

## Motivation

A theory often contains a smaller structure, such as the residue field of a valued field or the field of constants of a differential field.
One wants to say that the model theory of the small structure is the model theory of its induced structure, the $\emptyset$-definable relations on it.
This fails if outside parameters cut out new subsets: then the small structure, seen from outside, is richer than its induced structure.
Stable embeddedness is exactly the condition that outside parameters give nothing new.
It is the hypothesis behind results that transfer properties from a sort to the whole theory, and behind the study of internality and orthogonality in stability theory.

## Notation

The induced structure is written $D_{\mathrm{ind}}$, or $D$ with its induced structure.
Some authors call the traces *externally definable sets*.
A stably embedded set whose induced structure is a known structure, such as a pure field, is called *pure* with that structure.

## Remarks

### Examples

- In a [[stable theory|T7JW5QY6KR]], every definable set is stably embedded, because every type over any set is definable.
- The field of constants of a differentially closed field of characteristic $0$ is stably embedded, with the induced structure of a pure algebraically closed field; see [[this example|1CHPFKRTKP]].
- The sort of classes of an equivalence relation with infinitely many infinite classes is stably embedded, with the induced structure of a pure set; see [[this example|55BAWM7NTC]].
- In an algebraically closed valued field, the residue field and the value group are stably embedded. Their induced structures are a pure algebraically closed field and a pure divisible ordered abelian group.
- The home sort is stably embedded in $M^{\mathrm{eq}}$: a parameter $\bar a / E$ can be replaced by its representative $\bar a$.

### Non-examples

- In the generic bipartite graph with parts $P$ and $Q$, the part $P$ is not stably embedded. The neighbors in $P$ of one $q \in Q$ form an infinite coinfinite set, while $P$-parameters define only finite and cofinite subsets of $P$; see [[this example|E151S293VQ]].
- In a dense linear order with a dense and codense predicate $P$, the set $P$ is not stably embedded. For $b \notin P$, the trace $\set{p \in P : p < b}$ is a cut of $P$ with no endpoint in $P$, and $P$-parameters define only finite unions of intervals with endpoints in $P$.

### Basic properties

- The uniform version holds by compactness: each formula $\varphi(\bar x, \bar y)$ has one formula $\psi(\bar x, \bar z)$ that defines all its traces on $D$ with parameters $\bar z$ from $D$.
- If $D$ is stably embedded, then the subsets of $D^n$ definable in $\mathbb{M}$ with any parameters are exactly the sets definable in $D_{\mathrm{ind}}$ with parameters from $D$.
- In a stable theory, all definable sets are stably embedded. This is Shelah's definability of types, applied to types over $D$.
- Stable embeddedness passes along $\emptyset$-definable bijections: if $f : D \to D'$ is one, then $D$ is stably embedded exactly when $D'$ is. It also passes from $D$ to each power $D^k$.

### History

Shelah's theorem on the definability of types in stable theories implies that every definable set in a stable theory is stably embedded.
Chatzidakis and Hrushovski studied stably embedded sets in their work on difference fields.
Haskell, Hrushovski and Macpherson used the stable embeddedness of the residue field and the value group in their work on algebraically closed valued fields.

### Common errors

- Checking only $\emptyset$-definable sets. Every $\emptyset$-definable trace is a relation of $D_{\mathrm{ind}}$ by definition; the condition is about parameters outside $D$.
- Confusing stable embeddedness with purity. The induced structure can have more $\emptyset$-definable relations than the obvious ones, and stable embeddedness alone does not identify them.
- Thinking that stable embeddedness requires a stable theory. The residue field and value group of a valued field are stably embedded, and the valued field is not stable.

## Explanations

### L1 human

Take a big structure and a smaller part of it that we can describe.
Some sets inside the small part are cut out with help from outside elements.
The part is stably embedded when outside help is never needed: each such set can be cut out from inside.
For example, in a field with a derivative, the numbers with derivative zero form a field.
Any set of such numbers that a formula cuts out is already cut out by polynomials with coefficients among those numbers.

### L2 human

We check that a trace on $D = P$ in a structure $(M, P)$ is a problem when $P$ is a cut of an order.

1. Let $M = (\mathbb{Q}, <, P)$, where $P$ is a dense and codense set, such as the dyadic rationals.
2. Take $b = 1/3$, which is not dyadic. The trace of $x < b$ on $P$ is $\set{p \in P : p < 1/3}$.
3. A finite union of intervals of $P$ with endpoints in $P$ has its supremum in $P \cup \set{\pm\infty}$.
4. The supremum of the trace is $1/3$, which is not in $P$. So the trace is not definable over $P$.

The typical use of the notion is to reduce a question about $D$ inside $\mathbb{M}$ to a question about $D_{\mathrm{ind}}$.
A trap is to apply this reduction without checking stable embeddedness, as in this example.

### L3 human

Stable embeddedness is the starting point of the theory of internality.
A definable set $X$ is internal to a stably embedded $D$ when $X$ lies in $\operatorname{dcl}(D \cup A)$ for a set of parameters $A$.
In a stable theory, the automorphisms fixing $D$ pointwise then induce on $X$ a type-definable group, the binding group.
In differential algebra, this gives the model theoretic form of differential Galois theory over the constants.
In valued fields, the residue field and the value group are stably embedded sorts among the [[imaginary elements|Q0HM88QQKN]], and their induced structures are the classical ones.
Outside stable theories, the theorem of Marker and Steinhorn is a result of the same kind.
For o-minimal $M \preceq N$ with $M$ Dedekind complete in $N$, it says that every type over $M$ realized in $N$ is definable.
