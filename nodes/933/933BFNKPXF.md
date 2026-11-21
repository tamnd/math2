---
tag: 933BFNKPXF
kind: concept
name: Generic structures and Hrushovski amalgamation
aliases: [generic-structure-hrushovski-amalgamation, hrushovski-amalgamation, self-sufficient-embedding, predimension]
msc: ["03C15", "03C45", "03C50"]
topics: [ZS8X8KS54R]
audience: research
uses: [HJVRBDQSGG, XSCSX39GEZ, V5CKNFP3HC, 00C0BR7D7H, B3XW32T6EH, T7JW5QY6KR]
sources:
  - url: https://en.wikipedia.org/wiki/Hrushovski_construction
    locator: The construction
  - book: isbn:9780521587136
---

## Summary

Hrushovski amalgamation is a variant of the Fraïssé construction in which substructures are replaced by *self-sufficient* substructures.
One fixes a *predimension* $\delta$ on finite structures, such as $\delta(A) = \lvert A \rvert - \lvert E(A) \rvert$ for a [[graph|00C0BR7D7H]] $A$ with edge set $E(A)$.
For finite $A \subseteq B$, write $A \le B$ when $\delta(A') \ge \delta(A)$ for every $A'$ with $A \subseteq A' \subseteq B$.
The class $\mathcal{K}_0$ of finite structures with $\delta \ge 0$ on all substructures has amalgamation for $\le$, and its *generic structure* is the analogue of the [[Fraïssé limit|HJVRBDQSGG]].
Hrushovski used this method to build a strongly minimal set that refutes Zilber's trichotomy conjecture; see [[the Hrushovski construction|B3XW32T6EH]].

## Motivation

A Fraïssé limit is often too symmetric: its theory is usually unstable or very simple geometrically.
Restricting the allowed embeddings to self-sufficient ones keeps the amalgamation machinery but changes which configurations the limit must realize.
The predimension controls how "free" each new point is, so the generic carries a dimension function that behaves like a pregeometry.
This gives new [[stable theories|T7JW5QY6KR]] with prescribed geometric behavior.

## Notation

$A \le B$ is read "$A$ is self-sufficient (or strong, or closed) in $B$".
The generic is often written $M_0$.
For infinite $M$, $A \le M$ means $A \le B$ for every finite $B$ with $A \subseteq B \subseteq M$.

## Remarks

### Examples

- In the path $a - b - c$ with $\delta = \lvert A \rvert - \lvert E(A) \rvert$, the set $\set{a}$ is self-sufficient and $\set{a, c}$ is not; see [[this example|59GB1S1Y7R]].
- With the trivial predimension $\delta(A) = \lvert A \rvert$, every substructure is self-sufficient, and the generic is the ordinary Fraïssé limit; see [[this example|VM7H3WR4RE]].

### Non-examples

- Free amalgamation over a set that is not self-sufficient can leave $\mathcal{K}_0$; see [[this non-example|DZXJ7E4HBF]].

### Basic properties

- $\delta$ is submodular: $\delta(A \cup B) + \delta(A \cap B) \le \delta(A) + \delta(B)$, since every edge of $A$ or of $B$ lies in $A \cup B$.
- $\le$ is transitive, and if $A \le B$ and $C \subseteq B$, then $A \cap C \le C$.
- If $A \le B$ and $A \subseteq C$ in $\mathcal{K}_0$, the free amalgam $D$ of $B$ and $C$ over $A$ lies in $\mathcal{K}_0$, and $C \le D$.
- So $(\mathcal{K}_0, \le)$ has the [[amalgamation property|XSCSX39GEZ]] for self-sufficient embeddings, and a countable generic exists and is unique.

### History

Hrushovski introduced the method in his 1993 paper constructing a new strongly minimal set.
The version without collapse, with $\mathcal{K}_0$ as above, is called the ab initio construction.

### Common errors

- To use ordinary embeddings. The class $\mathcal{K}_0$ need not have free amalgamation over arbitrary substructures.
- To expect the generic to be strongly minimal. The ab initio generic is $\omega$-stable of infinite rank; strong minimality needs a further collapse step.

## Explanations

### L1 human

Each vertex brings one unit of freedom, and each edge uses one up.
A set is self-sufficient when adding more vertices from the big structure never lowers the remaining freedom.
Gluing only along such sets keeps the freedom count from going negative, and that is what makes a generic structure exist.

### L2 human

We check submodularity on two edges sharing a vertex.

1. Let $A = \set{a, b}$ with $a \sim b$, and $B = \set{b, c}$ with $b \sim c$.
2. $\delta(A) = \delta(B) = 2 - 1 = 1$, and $\delta(A \cap B) = \delta(\set{b}) = 1$.
3. $\delta(A \cup B) = 3 - 2 = 1$.
4. So $1 + 1 \le 1 + 1$, with equality here.

The typical use is to prove that self-sufficient closures exist and are finite.
A trap is to forget the edges between $A \setminus B$ and $B \setminus A$; they make $\delta(A \cup B)$ smaller, which is why the inequality goes this way.

### L3 human

The generic $M_0$ carries a dimension $d(X) = \min \set{\delta(B) : X \subseteq B \subseteq M_0 \text{ finite}}$, which defines a pregeometry.
After the collapse step, the resulting strongly minimal set has a geometry that is not locally modular, yet it interprets no infinite field, against Zilber's conjecture.
Variants of the method give fusions of strongly minimal theories, pseudo-exponential fields, and new $\aleph_0$-categorical structures.
