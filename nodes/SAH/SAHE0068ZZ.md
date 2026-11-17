---
tag: SAHE0068ZZ
kind: example
name: The intersection of two sets is a subset of each
msc: ["00A35", "03E20"]
topics: [958EF46EYJ]
audience: school
instance_of: [CX38X989TB]
uses: [CX38X989TB, 0ZNMMA9TF5, 0BJR9QR08E]
sources:
  - url: https://en.wikipedia.org/wiki/Intersection_(set_theory)
    locator: Basic properties
  - book: isbn:9781108439534
    locator: Section 3.3
---

## Example

Statement: for all sets $A$ and $B$, $A \cap B \subseteq A$.
The statement has two universal quantifiers.
The first runs over all pairs of sets.
The second is hidden in the definition of a [[subset|0BJR9QR08E]]: $S \subseteq T$ means that for every $x$, if $x \in S$, then $x \in T$.
We [[prove the universal statement|CX38X989TB]] by opening both quantifiers.

1. Let $A$ and $B$ be arbitrary sets.
2. To prove $A \cap B \subseteq A$, we must prove: for every $x$, if $x \in A \cap B$, then $x \in A$.
3. Let $x$ be arbitrary, and assume $x \in A \cap B$.
4. By the definition of the [[intersection|0ZNMMA9TF5]], $x \in A$ and $x \in B$.
5. In particular $x \in A$.
6. The element $x$ was arbitrary in step 3, so $A \cap B \subseteq A$.
7. The sets $A$ and $B$ were arbitrary in step 1, so the statement holds for all sets $A$ and $B$.

In the same way, $A \cap B \subseteq B$.

## Remarks

The example shows nested universal statements.
Each "for all" becomes a "let", and the "let" lines come in the same order as the quantifiers.
The final lines 6 and 7 close the quantifiers in the reverse order; in a written proof they are usually left implicit.

The proof does not use any property of $A$ and $B$.
So it also covers the cases $A = B$, $A \cap B = \varnothing$ and $B = \varnothing$.
For example, with $A = \{1, 2, 3\}$ and $B = \{2, 3, 4\}$, we get $A \cap B = \{2, 3\} \subseteq A$.

The converse inclusion $A \subseteq A \cap B$ is not true for all sets.
With $A = \{1, 2\}$ and $B = \{2\}$, the element $1$ is in $A$ but not in $A \cap B$.
It holds exactly when $A \subseteq B$.

## Explanations

### L1 human

The intersection of two groups of people is the people who are in both groups.
Each such person is in particular in the first group.
So the intersection is part of the first group.
For example, if the first group is $\{1, 2, 3\}$ and the second is $\{2, 3, 4\}$, the intersection is $\{2, 3\}$, and $2$ and $3$ are in the first group.
The proof says this for an arbitrary person in an arbitrary pair of groups.

### L2 human

We prove a second inclusion with the same pattern: for all sets $A$ and $B$, $A \subseteq A \cup B$.

1. Let $A$ and $B$ be arbitrary sets.
2. Let $x$ be arbitrary with $x \in A$.
3. Then the statement "$x \in A$ or $x \in B$" is true, because its first part is true.
4. By the definition of the [[union|0X1GSWNBN1]], $x \in A \cup B$.
5. So every element of $A$ is in $A \cup B$, that is, $A \subseteq A \cup B$.

The typical use: an inclusion $S \subseteq T$ is proved by "let $x \in S$" and a chain of definitions that ends with "$x \in T$".
Two inclusions give an equality of sets, and this pattern is treated in the topic [[proof patterns for common goals|MEKKHHQTKB]].

A trap: a Venn diagram with two overlapping discs suggests the result but does not prove it.
It shows only one arrangement of the sets, not the cases where one set is inside the other or the sets are disjoint.
