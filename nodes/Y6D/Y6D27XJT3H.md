---
tag: Y6D27XJT3H
kind: statement
role: theorem
name: The ω-models of RCA0 are exactly the Turing ideals
msc: ["03B30", "03D80"]
topics: [BY8AAFN7C5]
audience: grad
about: [XQENB067R3]
uses: [XQENB067R3, DNXCKXZZ08, PA4PYQ1PZ0, TN9G24VABN]
sources:
  - url: https://en.wikipedia.org/wiki/Reverse_mathematics
    locator: ω-models and β-models
---

## Statement

A *Turing ideal* is a nonempty family $\mathcal{S} \subseteq \mathcal{P}(\N)$ such that:

1. if $X, Y \in \mathcal{S}$, then $X \oplus Y = \set{2n : n \in X} \cup \set{2n + 1 : n \in Y}$ is in $\mathcal{S}$;
2. if $X \in \mathcal{S}$ and $Y$ is [[Turing reducible|PA4PYQ1PZ0]] to $X$, then $Y \in \mathcal{S}$.

For every nonempty $\mathcal{S} \subseteq \mathcal{P}(\N)$, the $\omega$-structure $(\N, \mathcal{S})$ is a model of [[RCA0|XQENB067R3]] if and only if $\mathcal{S}$ is a Turing ideal.

## Remarks

### Why each hypothesis is needed

- The number part must be standard. A model of $\mathsf{RCA}_0$ with non-standard numbers has sets that are not subsets of $\N$, and Turing reducibility does not apply to them.
- Closure under join is needed for comprehension with two set parameters. If $A$ and $B$ have incomparable Turing degrees, the family of sets computable from $A$ or from $B$ is closed downward. It does not contain $A \oplus B$, since $A \oplus B \le_T A$ would give $B \le_T A$.

### Consequences

- The computable sets form the least $\omega$-model of $\mathsf{RCA}_0$.
- A sentence of $L_2$ that fails in some Turing ideal is not provable in $\mathsf{RCA}_0$.
- The intersection of any family of Turing ideals is a Turing ideal, when it is nonempty.

### Converse

Both directions are part of the statement.

### Generalizations

The same proof shows that the $\omega$-models of $\mathsf{ACA}_0$ are the Turing ideals closed under the Turing jump.
The $\omega$-models of $\mathsf{WKL}_0$ are the Turing ideals in which every infinite binary tree has a path.

## Explanations

### L1 human

A family of sets satisfies the axioms of computable mathematics exactly when two things hold.
It can combine two of its sets into one.
It contains every set that a computer can decide with one of its sets as oracle.

### L2 human

The theorem turns questions about $\omega$-models into questions of computability theory.
For example, to show that a principle is not provable in $\mathsf{RCA}_0$, one finds a Turing ideal where it fails, often the computable sets.
A trap is to forget the parameters: comprehension may use any finite list of sets from $\mathcal{S}$, and the join reduces the list to one set.
