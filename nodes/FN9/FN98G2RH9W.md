---
tag: FN98G2RH9W
kind: definition
name: Stably embedded set
aliases: [stably-embedded-set-definition, stable-embeddedness-definition]
msc: ["03C45", "03C07"]
topics: [SZRM3N6BXW]
audience: research
defines: 14WPPDDK8M
uses: [CY1TXHF6KQ, EYTTQZ0E1S, 120S3V3975, 9V71Q3SD1G, 1NR3HAWG9D]
sources:
  - url: https://en.wikipedia.org/wiki/Stable_theory
    locator: Definition and alternate characterizations
  - book: isbn:9780521763240
  - book: isbn:9780198534372
---

## Definition

Let $T$ be a complete theory with [[monster model|EYTTQZ0E1S]] $\mathbb{M}$.
Let $D$ be a $\emptyset$-[[definable set|CY1TXHF6KQ]] of $\mathbb{M}$, or a $\emptyset$-definable set in a sort of $\mathbb{M}^{\mathrm{eq}}$; see [[imaginary elements|120S3V3975]].

The set $D$ is *stably embedded* if the following holds for every $n \ge 1$.
For every formula $\varphi(\bar x, \bar y)$, with $\bar x$ an $n$-tuple of variables of the sort of $D$, and every tuple $\bar b$ of $\mathbb{M}^{\mathrm{eq}}$, the set
$$\varphi(\mathbb{M}, \bar b) \cap D^n$$
is definable with parameters from $D$.

The *induced structure* on $D$ is the structure $D_{\mathrm{ind}}$ with universe $D$ and one $k$-ary relation for each $\emptyset$-definable subset of $D^k$, for each $k$.

## Notation

Some authors write "$D$ is stably embedded in $\mathbb{M}$" or "$D$ is stably embedded in $T$".
The sets $\varphi(\mathbb{M}, \bar b) \cap D^n$ are the *traces* on $D$ of the definable sets, or the *externally definable* subsets of $D^n$.
So $D$ is stably embedded when every trace on $D$ is definable inside $D_{\mathrm{ind}}$ with parameters from $D$.

## Remarks

Two equivalent forms are often used.

1. Uniform form. By [[compactness|1NR3HAWG9D]], $D$ is stably embedded exactly when for each $\varphi(\bar x, \bar y)$ there is a formula $\psi(\bar x, \bar z)$ such that each trace $\varphi(\mathbb{M}, \bar b) \cap D^n$ equals $\psi(\mathbb{M}, \bar c) \cap D^n$ for some $\bar c$ in $D$.
2. Types. $D$ is stably embedded exactly when every [[type|9V71Q3SD1G]] over $D$ that is realized in $\mathbb{M}$ is definable over $D$.

Example: the constants of a differentially closed field of characteristic $0$ form a stably embedded set; see [[this example|1CHPFKRTKP]].

Non-example: one side of the generic bipartite graph is not stably embedded; see [[this example|E151S293VQ]].

## Explanations

### L1 human

Take a structure and a part of it that can be described by a rule.
Using outside elements, we can cut out pieces of that part.
The part is stably embedded when each such piece can already be cut out using elements of the part itself.
So, as far as the part can tell, outside elements give no new information.

### L2 human

We check stable embeddedness of the home sort $M$ inside $M^{\mathrm{eq}}$.

1. Let $\varphi(\bar x, e)$ be a formula with an imaginary parameter $e = \bar a / E$, and $\bar x$ real.
2. Since $e = \pi_E(\bar a)$, the formula $\varphi(\bar x, \pi_E(\bar a))$ defines the same set, with the real parameter $\bar a$.
3. By the conservativity of $M^{\mathrm{eq}}$, this set is defined by an $L$-formula with parameters $\bar a$ from $M$.

The typical use is to transfer questions about a definable set to its induced structure.
A trap is to check only $\emptyset$-definable sets: every $\emptyset$-definable trace is in $D_{\mathrm{ind}}$ by definition, and the content of the condition is in the outside parameters.
