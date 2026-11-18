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

The direction from $w \mathrel{\underline{\leftrightarrow}} w'$ to $w \equiv w'$ is [[bisimulation invariance|TKFFTAX30E]].
For the other direction, let $E = \set{(w, w') \in W \times W' : w \equiv w'}$.
It suffices to show that $E$ satisfies the atom, zig and zag clauses of a [[bisimulation|7T740SFHHV]], because then every pair in $E$ is a pair of bisimilar worlds.

Part A: the image-finite case.

1. Atom clause. If $w E w'$, then $w$ and $w'$ agree on each variable $p$, since $p$ is a formula.
2. Zig clause. Let $w E w'$ and $w R v$. We show that some successor $v'$ of $w'$ has $v E v'$, by contradiction. Assume that no successor of $w'$ is equivalent to $v$.
3. Case: $w'$ has no successor. Then $\lozenge \top$ is true at $w$, because $w R v$, and false at $w'$. This contradicts $w \equiv w'$.
4. Case: $w'$ has successors. By image-finiteness they form a finite list $v'_1, \ldots, v'_n$ with $n \geq 1$.
5. For each $i$, $v \not\equiv v'_i$, so some formula has different truth values at $v$ and $v'_i$. Replacing it by its negation if needed, we get $\psi_i$ with $\mathfrak{M}, v \models \psi_i$ and $\mathfrak{M}', v'_i \not\models \psi_i$.
6. Let $\psi = \psi_1 \wedge \cdots \wedge \psi_n$. Then $v \models \psi$, so $w \models \lozenge \psi$.
7. Each successor $v'_i$ of $w'$ falsifies $\psi_i$, so it falsifies $\psi$. Hence $w' \not\models \lozenge \psi$. This contradicts $w \equiv w'$.
8. Zag clause. The argument of steps 2 to 7 with the two models exchanged uses image-finiteness of $\mathfrak{M}$ at $w$.
9. So $E$ is a bisimulation when it is nonempty, and item 1 of the theorem follows.

Part B: the m-saturated case.

10. The atom clause holds as in step 1.
11. Zig clause. Let $w E w'$ and $w R v$. Let $\Sigma = \set{\psi : \mathfrak{M}, v \models \psi}$ be the modal theory of $v$.
12. Let $\Delta \subseteq \Sigma$ be finite. Then $v \models \bigwedge \Delta$, so $w \models \lozenge \bigwedge \Delta$. Since $w \equiv w'$, also $w' \models \lozenge \bigwedge \Delta$.
13. So every finite subset of $\Sigma$ is true at some successor of $w'$. By m-saturation of $\mathfrak{M}'$, some successor $v'$ of $w'$ makes all of $\Sigma$ true.
14. If $\mathfrak{M}, v \not\models \chi$, then $\neg \chi \in \Sigma$, so $\mathfrak{M}', v' \not\models \chi$. With step 13 this gives $v \equiv v'$, that is, $v E v'$.
15. Zag clause. The same argument with the models exchanged uses m-saturation of $\mathfrak{M}$.
16. So $E$ is a bisimulation when it is nonempty, and item 2 of the theorem follows.

## Idea

The proof shows that modal equivalence is itself a bisimulation.
If a move had no equivalent answer, one formula for each possible answer would separate it, and the diamond of their conjunction would separate the starting worlds.
Image-finiteness makes the conjunction finite; m-saturation replaces it by a compactness argument over the successors.

## Variants

A game version: if Spoiler wins the bisimulation game in $n$ rounds on image-finite models, induction on $n$ builds a separating formula of modal depth at most $n$.
For finite models one can compute $E$ directly by partition refinement: start with the partition by variables and split blocks until the zig and zag clauses hold.
Part A is a special case of Part B, because every image-finite model is m-saturated.
Suppose that no successor of $w$ satisfies all of $\Sigma$.
Pick for each of the finitely many successors a formula of $\Sigma$ that fails there.
These formulas form a finite subset of $\Sigma$ that is true at no successor.
