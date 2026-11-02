---
tag: J5VXNMFVZB
kind: statement
role: lemma
name: Pettis lemma
msc: [22A05, "54E52"]
uses: [92700QAB5Y, 0XGCZ4GDZ6, FZ7237VY65, 0ZCY0Z80B6]
about: [92700QAB5Y, FZ7237VY65]
sources:
  - url: https://en.wikipedia.org/wiki/Steinhaus_theorem
---

## Statement

Let $G$ be a [[topological group|92700QAB5Y]] with identity $e$.
Let $A \subseteq G$ be a set that has the [[Baire property|FZ7237VY65]] and is not [[meagre|0XGCZ4GDZ6]].
Then the set $A^{-1} A = \set{a^{-1} b : a, b \in A}$ is a [[neighbourhood|0ZCY0Z80B6]] of $e$.

## Remarks

Since $A$ has the Baire property and is not meagre, there is a nonempty open set $U$ such that $A$ differs from $U$ by a meagre set.
Since $G$ is not meagre, the Banach category theorem and homogeneity show that no nonempty open subset of $G$ is meagre.
For $g$ near $e$, the open set $U \cap gU$ is nonempty, so it is not meagre.
The set $A \cap gA$ differs from it by a meagre set, so $A \cap gA$ is not empty and $g \in A A^{-1}$.
Applying this to $A^{-1}$, which also has the Baire property and is not meagre, gives the statement for $A^{-1}A$.
It is the category analogue of the Steinhaus theorem on sets of positive measure.
A standard application: a homomorphism between Polish groups that is Baire measurable is continuous.
The hypothesis that $A$ is not meagre is needed.
In $\R$ the set $\Z$ is closed, so it has the Baire property, but it is meagre, and $\Z - \Z = \Z$ is not a neighbourhood of $0$.

## Explanations

### L1 human

A set in a group can be large in a topological sense, called not meagre, even when it has no interior.
The lemma says that such a set, if it is reasonably well behaved, produces a whole neighbourhood of the identity when you take all quotients $a^{-1} b$ of its elements.
So largeness of $A$ turns into an open set inside $A^{-1} A$.

### L2 human

The lemma is the main tool of automatic continuity results in descriptive set theory.
To show a homomorphism $f$ is continuous at $e$, take a neighbourhood $V$ of the identity in the target and a smaller symmetric $W$ with $W^{-1} W \subseteq V$.
If $f^{-1}(W)$ has the Baire property and is not meagre, the lemma shows that $f^{-1}(V)$ contains a neighbourhood of $e$.
