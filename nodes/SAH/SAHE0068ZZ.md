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
The second hides in the definition of a [[subset|0BJR9QR08E]]: $S \subseteq T$ means that for every $x$, if $x \in S$, then $x \in T$.
We [[prove the universal statement|CX38X989TB]] by opening both quantifiers in order.

1. Let $A$ and $B$ be arbitrary sets.
2. To prove $A \cap B \subseteq A$, we must prove that for every $x$, if $x \in A \cap B$, then $x \in A$.
3. Let $x$ be arbitrary, and assume $x \in A \cap B$.
4. By the definition of the [[intersection|0ZNMMA9TF5]], $x \in A$ and $x \in B$.
5. In particular, $x \in A$.
6. The element $x$ was arbitrary in step 3, so every element of $A \cap B$ lies in $A$, and $A \cap B \subseteq A$.
7. The sets $A$ and $B$ were arbitrary in step 1, so the statement holds for all sets $A$ and $B$.

The same steps with "$x \in B$" in step 5 give $A \cap B \subseteq B$.

## Remarks

The example shows how nested universal statements unfold.
Each "for all" becomes a "let", and the "let" lines come in the same order as the quantifiers.
Steps 6 and 7 close the quantifiers in the reverse order, and a written proof usually leaves them unsaid.

The proof uses no property of $A$ and $B$, so it also covers the special cases $A = B$, $A \cap B = \varnothing$ and $B = \varnothing$.
With numbers, $A = \{1, 2, 3\}$ and $B = \{2, 3, 4\}$ give $A \cap B = \{2, 3\}$, and both $2$ and $3$ lie in $A$.

The reverse inclusion $A \subseteq A \cap B$ is not true for all sets.
With $A = \{1, 2\}$ and $B = \{2\}$, the element $1$ is in $A$ but not in $A \cap B$.
The reverse inclusion holds exactly when $A \subseteq B$.

## Explanations

### L1 human

The intersection of two clubs is the set of people who belong to both clubs.
Each such person belongs, in particular, to the first club.
So the intersection is part of the first club.
If the first club is $\{1, 2, 3\}$ and the second is $\{2, 3, 4\}$, the intersection is $\{2, 3\}$, and $2$ and $3$ are in the first club.
The proof says the same thing for an arbitrary person and an arbitrary pair of clubs.

### L2 human

The same pattern proves that $A \subseteq A \cup B$ for all sets $A$ and $B$.
Let $A$ and $B$ be arbitrary sets, and let $x$ be arbitrary with $x \in A$.
Then the statement "$x \in A$ or $x \in B$" is true, because its first part is true.
By the definition of the [[union|0X1GSWNBN1]], this says $x \in A \cup B$, so every element of $A$ lies in $A \cup B$.
The typical use is the one shown: an inclusion $S \subseteq T$ is proved by "let $x \in S$" and a chain of definitions that ends with "$x \in T$".
Two inclusions give an equality of sets, and the topic [[proof patterns for common goals|MEKKHHQTKB]] treats that pattern.
Watch out: a Venn diagram with two overlapping discs suggests the result but does not prove it.
The diagram shows one arrangement of the sets, and it misses the cases where one set lies inside the other or the sets are disjoint.
