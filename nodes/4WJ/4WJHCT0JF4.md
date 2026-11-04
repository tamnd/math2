---
tag: 4WJHCT0JF4
kind: proof
name: Proof of the distributive laws for sets
msc: ["03E20"]
proves: 08N6EVA7DV
uses: [0SJ3RX9TXA, 0TB16T2C97, 07KVB4JSC7, 0HBRW4E6G1, 0RYYK8PG4S]
methods: [0WCP0PVET6]
sources:
  - url: https://proofwiki.org/wiki/Intersection_Distributes_over_Union
  - url: https://proofwiki.org/wiki/Union_Distributes_over_Intersection
---

## Proof

We show that each side has the same elements as the other. Two [[sets|0SJ3RX9TXA]] with the same elements are equal, by the [[axiom of extensionality|0TB16T2C97]]. Let $A$, $B$ and $C$ be sets.

1. Let $x \in A \cap (B \cup C)$. By the definition of [[intersection|0HBRW4E6G1]], $x \in A$ and $x \in B \cup C$. By the definition of [[union|07KVB4JSC7]], $x \in B$ or $x \in C$.
2. In step 1, if $x \in B$, then $x \in A \cap B$. If $x \in C$, then $x \in A \cap C$. In both cases $x \in (A \cap B) \cup (A \cap C)$.
3. Conversely, let $x \in (A \cap B) \cup (A \cap C)$. Then $x \in A \cap B$ or $x \in A \cap C$.
4. In step 3, if $x \in A \cap B$, then $x \in A$ and $x \in B \subseteq B \cup C$. If $x \in A \cap C$, then $x \in A$ and $x \in C \subseteq B \cup C$. In both cases $x \in A \cap (B \cup C)$.
5. By steps 2 and 4, the sets $A \cap (B \cup C)$ and $(A \cap B) \cup (A \cap C)$ have the same elements. So they are equal.
6. Let $x \in A \cup (B \cap C)$. Then $x \in A$ or $x \in B \cap C$.
7. In step 6, if $x \in A$, then $x \in A \cup B$ and $x \in A \cup C$. If $x \in B \cap C$, then $x \in B$, so $x \in A \cup B$, and $x \in C$, so $x \in A \cup C$.
8. By step 7, in both cases $x \in (A \cup B) \cap (A \cup C)$.
9. Conversely, let $x \in (A \cup B) \cap (A \cup C)$. Then $x \in A \cup B$ and $x \in A \cup C$. By the [[law of excluded middle|0RYYK8PG4S]], either $x \in A$ or $x \notin A$.
10. In step 9, if $x \in A$, then $x \in A \cup (B \cap C)$.
11. In step 9, if $x \notin A$, then $x \in A \cup B$ forces $x \in B$, and $x \in A \cup C$ forces $x \in C$. So $x \in B \cap C \subseteq A \cup (B \cap C)$.
12. By steps 8, 10 and 11, the sets $A \cup (B \cap C)$ and $(A \cup B) \cap (A \cup C)$ have the same elements. So they are equal.

## Idea

Membership in a union is an "or", and membership in an intersection is an "and". So each set law reduces to a statement about an element, checked by splitting into cases. For the second law, the useful split is whether or not $x$ lies in $A$.
