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
The definitions we unfold are those of [[union|0X1GSWNBN1]] and [[intersection|0ZNMMA9TF5]]: $x \in B \cup C$ means that $x \in B$ or $x \in C$, and $x \in A \cap B$ means that $x \in A$ and $x \in B$.

1. ($\subseteq$) Let $x$ be an arbitrary element of $A \cap (B \cup C)$.
   Then $x \in A$ and $x \in B \cup C$, so $x \in B$ or $x \in C$, and we argue by [[cases|0WCP0PVET6]].
2. If $x \in B$, then $x \in A \cap B$, because $x \in A$ as well.
   So $x \in (A \cap B) \cup (A \cap C)$ by the definition of union.
3. If $x \in C$, then $x \in A \cap C$ in the same way, and again $x \in (A \cap B) \cup (A \cap C)$.
4. The two cases cover all possibilities, so $A \cap (B \cup C) \subseteq (A \cap B) \cup (A \cap C)$.
5. ($\supseteq$) Let $x$ be an arbitrary element of $(A \cap B) \cup (A \cap C)$.
   Then $x \in A \cap B$ or $x \in A \cap C$.
6. If $x \in A \cap B$, then $x \in A$ and $x \in B$.
   From $x \in B$ we get $x \in B \cup C$, so $x \in A \cap (B \cup C)$.
7. If $x \in A \cap C$, then $x \in A$ and $x \in C \subseteq B \cup C$, so again $x \in A \cap (B \cup C)$.
8. So $(A \cap B) \cup (A \cap C) \subseteq A \cap (B \cup C)$.
   Steps 4 and 8 give both inclusions, and the two sets are equal.

Check on small sets: take $A = \{1, 2, 3\}$, $B = \{2, 4\}$ and $C = \{3, 5\}$.
The left side is
$$A \cap \{2, 3, 4, 5\} = \{2, 3\},$$
and the right side is
$$\{2\} \cup \{3\} = \{2, 3\}.$$

## Remarks

Each half needs a case split, because the hypothesis of each half contains an "or".
That is the usual signal: an "or" in what you know becomes cases, and an "or" in what you want lets you pick the side that works.
The proof has the standard shape of element chasing: take an arbitrary element, unfold the definitions, reason about the element, and fold the definitions back.

The check with three small sets is not a proof, since it shows only that the law holds for those sets.
If you exchange $\cap$ and $\cup$ everywhere, the same method proves the second distributive law
$$A \cup (B \cap C) = (A \cup B) \cap (A \cup C),$$
again with cases in each half.
For numbers only the first form has an analogue, $a(b + c) = ab + ac$; the law $a + bc = (a + b)(a + c)$ fails, for example with $a = b = c = 1$, where $2 \ne 4$.

## Explanations

### L1 human

Think of a class.
Let $A$ be the students who play chess, $B$ those who sing, and $C$ those who swim.
The left side is the chess players who sing or swim.
The right side takes the chess players who sing and adds the chess players who swim.
Both descriptions pick out the same students, and the two halves of the proof show this for every class, not only for one.

### L2 human

The same method proves the absorption law $A \cup (A \cap B) = A$.

1. ($\subseteq$) Let $x \in A \cup (A \cap B)$, so $x \in A$ or $x \in A \cap B$.
   In the first case $x \in A$ at once, and in the second case $x \in A$ because every element of $A \cap B$ lies in $A$.
2. ($\supseteq$) Let $x \in A$.
   Then $x \in A \cup (A \cap B)$ by the definition of union.
3. Both inclusions hold, so $A \cup (A \cap B) = A$.

Laws like these let you shorten a long expression in sets before a harder proof starts.
Watch out: three overlapping circles in a Venn diagram suggest the law, but the proof must also cover sets that are empty, equal or nested, and only the element argument does that.
