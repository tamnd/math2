---
tag: PR03MQRDPD
kind: example
name: The distributive law for sets by double inclusion
msc: ["00A35", "03E20"]
topics: [MEKKHHQTKB]
audience: school
instance_of: [MKHVRNW68H]
uses: [MKHVRNW68H, 0X1GSWNBN1, 0ZNMMA9TF5, 0WCP0PVET6]
sources:
  - url: https://en.wikipedia.org/wiki/Subset
    locator: lead section
  - book: isbn:9781108439534
    locator: Chapter 3
---

## Example

Let $A$, $B$ and $C$ be sets.
We prove the distributive law
$$A \cap (B \cup C) = (A \cap B) \cup (A \cap C)$$
by [[double inclusion|MKHVRNW68H]].
We use the definitions of [[union|0X1GSWNBN1]] and [[intersection|0ZNMMA9TF5]]: $x \in B \cup C$ means $x \in B$ or $x \in C$, and $x \in A \cap B$ means $x \in A$ and $x \in B$.

1. ($\subseteq$) Let $x$ be an arbitrary element of $A \cap (B \cup C)$. Then $x \in A$ and $x \in B \cup C$, by the definition of intersection.
2. Since $x \in B \cup C$, we have $x \in B$ or $x \in C$. We use a [[proof by cases|0WCP0PVET6]].
3. Case $x \in B$: with $x \in A$, this gives $x \in A \cap B$. So $x \in (A \cap B) \cup (A \cap C)$, by the definition of union.
4. Case $x \in C$: with $x \in A$, this gives $x \in A \cap C$. So again $x \in (A \cap B) \cup (A \cap C)$.
5. The two cases cover all possibilities, so $A \cap (B \cup C) \subseteq (A \cap B) \cup (A \cap C)$.
6. ($\supseteq$) Let $x$ be an arbitrary element of $(A \cap B) \cup (A \cap C)$. Then $x \in A \cap B$ or $x \in A \cap C$.
7. Case $x \in A \cap B$: then $x \in A$ and $x \in B$. From $x \in B$ we get $x \in B \cup C$, so $x \in A \cap (B \cup C)$.
8. Case $x \in A \cap C$: then $x \in A$ and $x \in C$. From $x \in C$ we get $x \in B \cup C$, so $x \in A \cap (B \cup C)$.
9. So $(A \cap B) \cup (A \cap C) \subseteq A \cap (B \cup C)$.
10. Steps 5 and 9 give the two inclusions, so the two sets are equal.

A check on small sets agrees with the law.
Take $A = \{1, 2, 3\}$, $B = \{2, 4\}$ and $C = \{3, 5\}$.
Then $B \cup C = \{2, 3, 4, 5\}$, and $A \cap (B \cup C) = \{2, 3\}$.
Also $A \cap B = \{2\}$ and $A \cap C = \{3\}$, so $(A \cap B) \cup (A \cap C) = \{2, 3\}$.

## Remarks

1. Each half of the proof needs a case split, because the hypothesis of each half contains the word "or".
2. The example shows the standard shape: "let $x$ be arbitrary", unfold the definitions, reason on the elements, fold the definitions again.
3. If we exchange $\cap$ and $\cup$ everywhere, the same method proves the other distributive law $A \cup (B \cap C) = (A \cup B) \cap (A \cup C)$. Each half again needs cases.
4. The numerical check with three small sets is not a proof. It only shows that the law does not fail for those three sets.
5. The law has the same form as $a(b + c) = ab + ac$ for numbers, with $\cap$ in the role of the product and $\cup$ in the role of the sum. For sets, unlike for numbers, the law also holds with the roles exchanged.

## Explanations

### L1 human

Think of a class of students.
Let $A$ be the students who play chess, $B$ the students who sing, and $C$ the students who swim.
The left side is the chess players who sing or swim.
The right side collects the chess players who sing, and adds the chess players who swim.
Both descriptions pick out the same students, and the two checks of the proof show this for every possible class.

### L2 human

We use the same method for the identity $A \cup (A \cap B) = A$, called an absorption law.

1. ($\subseteq$) Let $x \in A \cup (A \cap B)$. Then $x \in A$ or $x \in A \cap B$.
2. In the first case $x \in A$ directly. In the second case $x \in A$ because each element of $A \cap B$ is in $A$.
3. ($\supseteq$) Let $x \in A$. Then $x \in A \cup (A \cap B)$, by the definition of union.
4. Both inclusions hold, so $A \cup (A \cap B) = A$.

The typical use of such laws is to simplify a long expression in sets before a proof starts.
A trap is to prove the law only with a Venn diagram of three overlapping circles.
The diagram suggests the law, but the proof must work for sets in any position, including empty and equal sets.
