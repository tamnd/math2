---
tag: 1VFH9WT1RZ
kind: definition
name: Brouwer–Heyting–Kolmogorov interpretation
msc: ["03F55", "03B20"]
defines: 7B53ZGXXEQ
uses: [Q11N8X99FK, G958EQ8CWW, 0M28ASWG8T, 0H5GKDTB01, 0ZNX6DQ3EJ, 0XR7A7RSXB, 0B88PQTJ66, 0JW2FHW7G3]
sources:
  - url: https://en.wikipedia.org/wiki/Brouwer–Heyting–Kolmogorov_interpretation
---

## Definition

Let $D$ be a domain of objects, and let $A$, $B$ and $P(x)$ be statements about $D$.
The *Brouwer–Heyting–Kolmogorov interpretation* says what a proof of a compound statement is, by these clauses.

1. A proof of $A \wedge B$ is a pair $(a, b)$, where $a$ is a proof of $A$ and $b$ is a proof of $B$.
2. A proof of $A \vee B$ is a pair $(i, c)$ with $i \in \set{0, 1}$. If $i = 0$, then $c$ is a proof of $A$. If $i = 1$, then $c$ is a proof of $B$.
3. A proof of $A \to B$ is a construction that transforms each proof of $A$ into a proof of $B$.
4. There is no proof of the absurdity $\bot$.
5. A proof of $\neg A$ is a proof of $A \to \bot$.
6. A proof of $\forall x\, P(x)$ is a construction that transforms each $d \in D$ into a proof of $P(d)$.
7. A proof of $\exists x\, P(x)$ is a pair $(d, p)$, where $d \in D$ and $p$ is a proof of $P(d)$.

These clauses give the meaning of [[conjunction|0M28ASWG8T]], [[disjunction|0H5GKDTB01]], [[implication|0ZNX6DQ3EJ]], [[negation|0XR7A7RSXB]], the [[universal quantifier|0B88PQTJ66]] and the [[existential quantifier|0JW2FHW7G3]] in [[intuitionistic logic|Q11N8X99FK]].

## Remarks

Example: $A \to \neg \neg A$ has a BHK proof.
Given a proof $a$ of $A$, the construction $f \mapsto f(a)$ sends each proof $f$ of $\neg A$ to a proof of $\bot$, so it is a proof of $\neg \neg A$.
Non-example: there is no known BHK proof of $\neg \neg A \to A$ for all $A$, because a proof of $\neg \neg A$ gives no construction of a proof of $A$.
The notion of "construction" is left informal.
Kleene's realizability reads it as a computable function, and the Curry–Howard correspondence reads it as a typed lambda term.
