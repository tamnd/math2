---
tag: 5MWD3ZXDVR
kind: proof
name: Proof that equivalence classes form a partition
msc: ["03E20"]
proves: 01HT2CH8BH
uses: [0SGTMBEWRF, 082RMRSY26, 09CCE86A6D, 0W4RPA8QH3, 0TB16T2C97]
sources:
  - url: https://proofwiki.org/wiki/Fundamental_Theorem_on_Equivalence_Relations
---

## Proof

We check the three properties of a [[partition|09CCE86A6D]].

1. Let $\sim$ be an [[equivalence relation|0SGTMBEWRF]] on a set $A$. For $a \in A$, the [[equivalence class|082RMRSY26]] of $a$ is $[a] = \set{x \in A \mid x \sim a}$. Let $P = \set{[a] \mid a \in A}$.
2. Each $[a]$ is a subset of $A$ by its definition. So $P$ is a set of subsets of $A$.
3. Let $a \in A$. By reflexivity, $a \sim a$, so $a \in [a]$. Hence each block $[a]$ is nonempty.
4. By step 2, the union of the blocks is contained in $A$. By step 3, each $a \in A$ lies in the block $[a]$. So the union of the blocks is $A$.
5. Let $a, b \in A$ and suppose that some $c$ lies in $[a] \cap [b]$. Then $c \sim a$ and $c \sim b$.
6. In step 5, let $x \in [a]$, so $x \sim a$. By symmetry, $a \sim c$. By transitivity, $x \sim a$ and $a \sim c$ give $x \sim c$.
7. By transitivity again, $x \sim c$ and $c \sim b$ give $x \sim b$, so $x \in [b]$. Hence $[a] \subseteq [b]$.
8. Exchanging the roles of $a$ and $b$ in steps 6 and 7 gives $[b] \subseteq [a]$. So $[a]$ and $[b]$ have the same elements, and $[a] = [b]$ by the [[axiom of extensionality|0TB16T2C97]].
9. By steps 5 to 8, two blocks with a common element are equal. So two different blocks have no common element. Thus the blocks are pairwise [[disjoint|0W4RPA8QH3]].
10. By steps 3, 4 and 9, the blocks are nonempty, pairwise disjoint, and their union is $A$. So $P$ is a partition of $A$.

## Idea

Reflexivity puts each element in its own class, so the classes are nonempty and cover $A$. Symmetry and transitivity show that two classes sharing one element have exactly the same elements. So distinct classes cannot overlap.
