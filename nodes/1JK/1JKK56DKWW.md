---
tag: 1JKK56DKWW
kind: example
name: Three equivalent conditions for a subset
msc: ["00A35", "03E20"]
topics: [958EF46EYJ]
audience: ug1
instance_of: [TFQ1845T84]
uses: [TFQ1845T84, 0BJR9QR08E, 0ZNMMA9TF5, 0X1GSWNBN1, CX38X989TB]
sources:
  - url: https://en.wikipedia.org/wiki/Subset
    locator: Properties
  - book: isbn:9781108439534
    locator: Section 3.4
---

## Example

Statement: for sets $A$ and $B$, the following are equivalent.

1. $A \subseteq B$.
2. $A \cap B = A$.
3. $A \cup B = B$.

We [[prove the equivalence|TFQ1845T84]] by the cycle $(1) \Rightarrow (2) \Rightarrow (3) \Rightarrow (1)$.
Each set equality is proved by two inclusions, and each inclusion by an [[element argument|CX38X989TB]].

1. $(1) \Rightarrow (2)$.
   Assume $A \subseteq B$.
   The inclusion $A \cap B \subseteq A$ holds for all sets, because every element of $A \cap B$ lies in $A$.
   For the other inclusion, let $x \in A$; by (1), $x \in B$, so $x \in A \cap B$.
   Hence $A \cap B = A$.
2. $(2) \Rightarrow (3)$.
   Assume $A \cap B = A$.
   The inclusion $B \subseteq A \cup B$ holds for all sets.
   For the other inclusion, let $x \in A \cup B$, so $x \in A$ or $x \in B$.
   If $x \in B$, we are done.
   If $x \in A$, then $x \in A \cap B$ by (2), so $x \in B$.
   Hence $A \cup B = B$.
3. $(3) \Rightarrow (1)$.
   Assume $A \cup B = B$, and let $x \in A$.
   Then $x \in A \cup B = B$, so $A \subseteq B$.
4. Each condition implies the next one, and (3) implies (1).
   So each condition implies every other one by following the cycle, and the three are equivalent.

## Remarks

The cycle replaces six implications by three.
For example, $(2) \Rightarrow (1)$ was never proved on its own, but it follows by chaining $(2) \Rightarrow (3)$ and $(3) \Rightarrow (1)$.

The order of the cycle is a choice, and a good order puts each arrow where its proof is short.
Here $(3) \Rightarrow (1)$ takes one line, while a direct proof of $(3) \Rightarrow (2)$ would need its own element argument.
Step 2 also contains a small [[proof by cases|0WCP0PVET6]], because $x \in A \cup B$ means $x \in A$ or $x \in B$.

## Explanations

### L1 human

Think of $A$ as the students in the chess club and $B$ as the students in the school.
Every chess player is a student of the school: that is (1).
Then "chess players who are students" is the same group as "chess players": that is (2).
And "chess players or students" is the same group as "students": that is (3).
The proof shows that the three sentences say the same thing in different words.

### L2 human

Once the equivalence is proved, you check whichever condition is easiest and get the others for free.
Take $A = \{2, 4\}$ and $B = \{1, 2, 3, 4\}$.
Every element of $A$ is in $B$, so (1) holds.
By $(1) \Rightarrow (2)$ and $(1) \Rightarrow (3)$, with no further work,
$$A \cap B = A = \{2, 4\}, \qquad A \cup B = B = \{1, 2, 3, 4\}.$$
Check: the common elements of $A$ and $B$ are $2$ and $4$, and the union adds nothing to $B$.
The typical use of a TFAE theorem is exactly this: verify one condition and quote the rest.
Watch out: the cycle must close, since $(1) \Rightarrow (2)$ and $(2) \Rightarrow (3)$ alone do not show that (3) implies (1).
