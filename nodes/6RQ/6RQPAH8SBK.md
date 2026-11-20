---
tag: 6RQPAH8SBK
kind: definition
name: Coherence space
msc: ["03F52", "03B70", "68Q55"]
topics: [98QF5J4W16]
audience: research
defines: WSGZ5HGK1X
uses: [0BYX1D7C2E, D9RY4667K6, 0A7KV2WB7A, H408H4WHBA]
sources:
  - url: https://en.wikipedia.org/wiki/Coherent_space
    locator: Definitions
  - url: https://en.wikipedia.org/wiki/Coherent_space
    locator: Stable functions
  - url: https://en.wikipedia.org/wiki/Coherent_space
    locator: Trace
  - book: isbn:9780521371810
    note: Girard, Lafont and Taylor, Proofs and Types
  - doi: 10.1016/0304-3975(87)90045-4
    locator: pages 1-101
    note: Girard, Linear logic, Theoretical Computer Science 50 (1987)
---

## Definition

A *coherence space* $A$ is a set $|A|$, the *web*, with a reflexive and symmetric relation $\frown$ on $|A|$, the *coherence*.
A *clique* of $A$ is a set $a \subseteq |A|$ with $\alpha \frown \beta$ for all $\alpha, \beta \in a$; this is a [[clique|0BYX1D7C2E]] of the graph $(|A|, \frown)$.
$\mathrm{Cl}(A)$ is the set of cliques, ordered by inclusion.

The connectives of [[linear logic|H408H4WHBA]] act on coherence spaces as follows.

1. $A^{\perp}$ has web $|A|$, and $\alpha \frown \beta$ in $A^{\perp}$ if and only if $\alpha = \beta$ or not $\alpha \frown \beta$ in $A$.
2. $A \otimes B$ has web $|A| \times |B|$, and $(\alpha, \beta) \frown (\alpha', \beta')$ if and only if $\alpha \frown \alpha'$ and $\beta \frown \beta'$.
3. $A \mathbin{\wp} B = (A^{\perp} \otimes B^{\perp})^{\perp}$ and $A \multimap B = A^{\perp} \mathbin{\wp} B$.
4. $A \mathbin{\&} B$ has web the disjoint union of $|A|$ and $|B|$, with the coherence of each part, and every token of $A$ coheres with every token of $B$.
5. $A \oplus B = (A^{\perp} \mathbin{\&} B^{\perp})^{\perp}$, so tokens from different parts do not cohere.
6. $1$ and $\bot$ have a one-token web, and $\top$ and $0$ have the empty web.
7. $!A$ has as web the finite cliques of $A$, and $a \frown a'$ if and only if $a \cup a'$ is a clique of $A$.

A function $F \colon \mathrm{Cl}(A) \to \mathrm{Cl}(B)$ is *stable* if it has three properties.

1. It is [[monotone|0A7KV2WB7A]]: $a \subseteq a'$ implies $F(a) \subseteq F(a')$.
2. It is continuous: $F(\bigcup_i a_i) = \bigcup_i F(a_i)$ for each [[directed|D9RY4667K6]] family of cliques.
3. It is stable: if $a \cup a'$ is a clique, then $F(a \cap a') = F(a) \cap F(a')$.

The *trace* of $F$ is the set of pairs $(a, \beta)$ with $a$ a finite clique, $\beta \in F(a)$, and $\beta \notin F(a')$ for every $a' \subsetneq a$.
A stable function is *linear* if each $a$ in its trace has exactly one element.

## Notation

Unfolding item 3, $(\alpha, \beta) \frown (\alpha', \beta')$ in $A \multimap B$ if and only if two conditions hold.
First, $\alpha \frown \alpha'$ implies $\beta \frown \beta'$.
Second, $\alpha \frown \alpha'$ and $\beta = \beta'$ imply $\alpha = \alpha'$.

## Remarks

### Basic facts

1. $(A^{\perp})^{\perp} = A$, since for distinct tokens the coherence of $A^{\perp}$ is the negation of that of $A$.
2. A stable $F$ is determined by its trace: $F(a) = \set{\beta \mid (a', \beta) \in \mathrm{Tr}(F) \text{ for some } a' \subseteq a}$.
3. A linear $F$ is determined by the set of pairs $(\alpha, \beta)$ with $(\set{\alpha}, \beta)$ in its trace, and this set is a clique of $A \multimap B$.
4. A stable $F$ from $A$ to $B$ corresponds to a linear map from $!A$ to $B$, by sending $(a, \beta)$ in its trace to the token $(a, \beta)$ of $!A \multimap B$.

## Explanations

### L1 human

A coherence space is a set of facts with a rule that says which facts can be true together.
A point is a set of facts that can all be true together.
A stable function turns points into points, and each output fact comes from one smallest group of input facts.

### L2 human

We check the stability of the identity of the flat space $B$ with web $\set{t, f}$, $t$ and $f$ incoherent.

1. The cliques are $\emptyset$, $\set{t}$ and $\set{f}$.
2. If $a \cup a'$ is a clique, then $a$ and $a'$ are not $\set{t}$ and $\set{f}$, so one contains the other.
3. Then $F(a \cap a')$ is the image of the smaller one, which is $F(a) \cap F(a')$ by monotonicity.
4. The trace is $\set{(\set{t}, t), (\set{f}, f)}$, so the identity is linear.

The typical use of the trace is to write a stable function as a set of tokens.
A trap: the condition of stability applies only when $a \cup a'$ is a clique, not for all pairs $a$, $a'$.
