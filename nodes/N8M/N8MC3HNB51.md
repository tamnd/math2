---
tag: N8MC3HNB51
kind: proof
name: Proof of the soundness of the Danos-Regnier criterion
msc: ["03F52", "05C05"]
topics: [98QF5J4W16]
audience: research
proves: SBY2YQ8EN6
uses: [6G6M2V85RZ, H408H4WHBA]
methods: [12MQ2NJ29A, 0WCP0PVET6, 0NTF6DMVAP]
sources:
  - doi: 10.1007/BF01622878
    locator: pages 181-203
    note: Danos and Regnier, The structure of multiplicatives, Archive for Mathematical Logic 28 (1989)
  - url: https://plato.stanford.edu/entries/logic-linear/
    locator: 2.3 Proof nets
    note: Di Cosmo and Miller, Linear Logic, Stanford Encyclopedia of Philosophy, revision of 2023-09-16
---

## Proof

This node proves the soundness direction and the count of links in full.
It does not prove sequentialization, the converse direction; that proof is in the paper of Danos and Regnier cited here.

We use the facts that a finite graph is a tree if and only if it is connected and has one edge fewer than vertices.
We also use that two disjoint trees, joined by one new edge, form a tree.

**Soundness.**
Let $\pi$ be a derivation of MLL without units, and let $s$ be a switching of the [[translation|6G6M2V85RZ]] $N(\pi)$.
We show by induction on $\pi$ that the correction graph $G_s$ is a tree.

1. Axiom: $N(\pi)$ has two vertices and one edge, and no $\mathbin{\wp}$ link.
   Its only correction graph is a tree.
2. $\otimes$ rule on $\pi_1$ and $\pi_2$: the $\mathbin{\wp}$ links of $N(\pi)$ lie in $N(\pi_1)$ or $N(\pi_2)$.
   So $s$ restricts to switchings $s_1$ and $s_2$ of the parts.
3. By the induction hypothesis, $G_{s_1}$ and $G_{s_2}$ are trees.
4. $G_s$ adds to their disjoint union one vertex $A \otimes B$ and the edges $A \otimes B - A$ and $A \otimes B - B$, with $A$ in the first tree and $B$ in the second.
5. The first new edge makes the first tree larger by a leaf, which is still a tree.
   The second new edge joins it to the second tree, so $G_s$ is a tree.
6. $\mathbin{\wp}$ rule on $\pi$: $s$ restricts to a switching of $N(\pi)$, and $G_s$ adds one vertex $A \mathbin{\wp} B$ with one edge to the chosen premise.
7. A tree with a new leaf is a tree, so $G_s$ is a tree.
8. Cut on $\pi_1$ and $\pi_2$: $G_s$ is the disjoint union of two trees, by the induction hypothesis, with one new edge between them.
   So it is a tree.

Each switching of $N(\pi)$ arises in this way, so every correction graph of a proof net is a tree.

**Count of links.**
Let a proof net have $a$ axiom links, $t$ links of type $\otimes$, $w$ links of type $\mathbin{\wp}$ and $c$ cut links.

1. Each occurrence is the conclusion of exactly one link.
   Axiom links have two conclusions, $\otimes$ and $\mathbin{\wp}$ links have one, and cut links have none.
   So there are $2a + t + w$ vertices.
2. A correction graph has $a + c$ edges from axiom and cut links, $2t$ edges from $\otimes$ links and $w$ edges from $\mathbin{\wp}$ links.
3. A correction graph is a tree by soundness, so $a + c + 2t + w = 2a + t + w - 1$.
4. This simplifies to $a = t + c + 1$.

## Idea

Each rule of MLL joins its premises into one connected piece and adds one edge per new vertex, so the correction graphs stay trees.
The $\mathbin{\wp}$ rule has one premise, so only one of its two edges may stay; with both edges, a cycle could form.

## Variants

Sequentialization is proved by induction on the structure: a terminal $\mathbin{\wp}$ link can be removed, and otherwise some terminal $\otimes$ link or cut link splits the structure into two parts that satisfy the criterion.
The SEP entry on linear logic describes a criterion by graph contraction due to Danos and Regnier, in a form by Guerrini, Martini and Masini.
