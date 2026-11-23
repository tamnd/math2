---
tag: Y79T9EYZ2G
kind: proof
name: Proof of the Hennessy-Milner theorem
msc: ["03B45", "68Q85"]
topics: [SPQVNPZDTB]
audience: grad
proves: DBDNYXA7ME
uses: [7T740SFHHV, TKFFTAX30E, NGHWZ9Y7ZV]
methods: [0J0XBKG64S, 0NTF6DMVAP]
sources:
  - url: https://en.wikipedia.org/wiki/Hennessy%E2%80%93Milner_logic
    locator: lead section
  - url: https://builds.openlogicproject.org/
    locator: Modal Logic
---

## Proof

We show that modal equivalence $\equiv$ itself satisfies the three clauses of a bisimulation.
The direction from $w \mathrel{\underline{\leftrightarrow}} w'$ to $w \equiv w'$ is [[bisimulation invariance|TKFFTAX30E]].
For the other direction, let $E = \{(w, w') \in W \times W' : w \equiv w'\}$.
If $E$ satisfies the atom, zig and zag clauses of a [[bisimulation|7T740SFHHV]], then every pair in $E$ is a pair of bisimilar worlds, which is what we want.

Part A: the image-finite case.

1. Atom clause.
   If $w E w'$, then $w$ and $w'$ agree on each variable $p$, because $p$ is itself a formula.
2. Zig clause.
   Let $w E w'$ and $w R v$; we show that some successor $v'$ of $w'$ has $v E v'$.
   Assume, for a contradiction, that no successor of $w'$ is equivalent to $v$.
3. If $w'$ has no successor, then $\lozenge \top$ is true at $w$, because $w R v$, and false at $w'$.
   This contradicts $w \equiv w'$.
4. Otherwise, image-finiteness lets us list the successors of $w'$ as $v'_1, \ldots, v'_n$ with $n \geq 1$.
5. For each $i$ we have $v \not\equiv v'_i$, so some formula takes different values at $v$ and $v'_i$.
   Replacing it by its negation if needed, we get $\psi_i$ with $\mathfrak{M}, v \models \psi_i$ and $\mathfrak{M}', v'_i \not\models \psi_i$.
6. Let $\psi = \psi_1 \wedge \cdots \wedge \psi_n$.
   Then $v \models \psi$, so $w \models \lozenge \psi$.
7. Each successor $v'_i$ of $w'$ falsifies $\psi_i$ and so falsifies $\psi$, hence $w' \not\models \lozenge \psi$.
   This contradicts $w \equiv w'$, so zig holds.
8. Zag clause.
   The argument of steps 2 to 7, with the two models exchanged, uses image-finiteness of $\mathfrak{M}$ at $w$.
9. So $E$ is a bisimulation when it is nonempty, and item 1 of the theorem follows.

Part B: the m-saturated case.

10. The atom clause holds as in step 1.
11. Zig clause.
    Let $w E w'$ and $w R v$, and let $\Sigma = \{\psi : \mathfrak{M}, v \models \psi\}$ be the modal theory of $v$.
12. Let $\Delta \subseteq \Sigma$ be finite.
    Then $v \models \bigwedge \Delta$, so $w \models \lozenge \bigwedge \Delta$, and $w \equiv w'$ gives $w' \models \lozenge \bigwedge \Delta$.
13. So every finite subset of $\Sigma$ is true at some successor of $w'$.
    By m-saturation of $\mathfrak{M}'$, some successor $v'$ of $w'$ makes all of $\Sigma$ true.
14. If $\mathfrak{M}, v \not\models \chi$, then $\neg \chi \in \Sigma$, so $\mathfrak{M}', v' \not\models \chi$.
    Together with step 13, this gives $v \equiv v'$, that is, $v E v'$.
15. Zag clause.
    The same argument with the models exchanged uses m-saturation of $\mathfrak{M}$.
16. So $E$ is a bisimulation when it is nonempty, and item 2 of the theorem follows.

## Idea

The proof shows that modal equivalence is already a bisimulation.
Suppose a move had no equivalent answer.
Then, for each possible answer, one formula would separate it from the move, and the diamond of the conjunction of these formulas would separate the starting worlds.
Image-finiteness keeps that conjunction finite, and m-saturation replaces it by a compactness argument over the successors.

## Variants

Part A is a special case of Part B, because every image-finite model is m-saturated.
To see this, suppose that no successor of $w$ satisfies all of $\Sigma$.
Pick, for each of the finitely many successors, a formula of $\Sigma$ that fails there.
These formulas form a finite subset of $\Sigma$ that holds at no successor.

There is also a game version.
If Spoiler wins the bisimulation game in $n$ rounds on image-finite models, induction on $n$ builds a separating formula of modal depth at most $n$.
For finite models one can compute $E$ directly by partition refinement: start with the partition by variables, and split blocks until the zig and zag clauses hold.
