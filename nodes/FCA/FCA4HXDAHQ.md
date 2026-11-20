---
tag: FCA4HXDAHQ
kind: example
name: The formal languages over a nonempty alphabet admit no converse
msc: ["03G15", "68Q45"]
topics: [QYA4H5Y7VR]
audience: research
not_instance_of:
  - target: GQK4DSA11K
    note: no unary operation on the languages satisfies the converse axioms together with Tarski's axiom
uses: [RDSY11X6N2, TB04CWS3R1, 5MFZ4VNY6D]
sources:
  - url: https://en.wikipedia.org/wiki/Relation_algebra
---

## Example

Let $\Sigma$ be an alphabet with a letter $a$, and let $A = \mathcal{P}(\Sigma^*)$ be the [[residuated Boolean algebra of languages|TB04CWS3R1]], with concatenation as $;$ and $1' = \set{\varepsilon}$.
Clauses 1 to 3 of [[the definition|RDSY11X6N2]] hold.
We show that no map $c : A \to A$ satisfies both $c(c(x)) = x$ and clause 6, $c(x) ; -(x ; y) \le -y$.

1. Suppose $c$ is such a map, and put $u = c(\set{a})$, so $c(u) = \set{a}$.
2. Clause 6 with $x = u$ and $y = \Sigma^*$ gives $\set{a} ; -(u ; \Sigma^*) \le -\Sigma^* = \emptyset$.
3. For a language $L$, $\set{a} L = \emptyset$ only if $L = \emptyset$; so $u \Sigma^* = \Sigma^*$.
4. In particular $\varepsilon \in u \Sigma^*$. A product $v w$ of words is empty only if $v = w = \varepsilon$, so $\varepsilon \in u$.
5. Clause 6 with $x = \set{a}$ and $y = \set{\varepsilon}$ gives $u ; -\set{a} \le -\set{\varepsilon}$.
6. Since $\varepsilon \in u$, the left side contains $\varepsilon \cdot \varepsilon = \varepsilon$, as $\varepsilon \in -\set{a}$.
7. The right side does not contain $\varepsilon$, a contradiction.

So the algebra of languages is not a [[relation algebra|GQK4DSA11K]] for any choice of converse.

## Remarks

1. Word reversal $\breve{L} = \set{w^{R} : w \in L}$ satisfies clauses 4 and 5, so the failure lies in clause 6.
2. With reversal, clause 6 for $x = \set{a}$ and $y = \Sigma^*$ has left side $\set{a} ; -(\set{a} ; \Sigma^*)$, which contains $a = a \varepsilon$, since $\varepsilon \notin a \Sigma^*$; the right side is empty.
3. For the empty alphabet, $A = \set{\emptyset, \set{\varepsilon}}$ and concatenation is meet, so $A$ is a relation algebra.

## Explanations

### L1 human

Languages can be joined, complemented and concatenated, much like relations.
But there is no way to reverse a language that satisfies all the laws of reversing a relation.

### L2 human

1. In relations, $\breve{R} ; -(R ; 1)$ is empty, because $R ; 1$ contains every pair that starts where $R$ has a pair.
2. In languages with reversal, $\set{a} ; -(\set{a} ; \Sigma^*)$ is not empty: it contains the word $a$, since $\varepsilon$ is not in $a \Sigma^*$.
3. Concatenation does not cancel letters, while composition followed by converse can return to the starting point.

The typical use: this example shows that the relation algebra axioms say more than residuation plus an involution.
The trap: word reversal looks like a converse, and it does satisfy $\breve{(x ; y)} = \breve{y} ; \breve{x}$.
