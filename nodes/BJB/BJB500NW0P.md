---
tag: BJB500NW0P
kind: proof
name: Proof of completeness of K, T, D, K4, S4, B and S5
msc: ["03B45"]
topics: [SKY7AQFG1V]
audience: grad
proves: FXTCKYR3AQ
uses: [JS8W7PA6JK, TVE4F04KME, NM4CB7QAYT, E87G6ZTMTN, FDFQFWPM4X, G989VP2NGP]
methods: [0NTF6DMVAP, 0BB5TPGQ1N]
sources:
  - url: https://en.wikipedia.org/wiki/Kripke_semantics
    locator: Canonical models
  - url: https://builds.openlogicproject.org/
    locator: Boxes and Diamonds, chapter on frame completeness
---

## Proof

We prove [[the completeness theorem|FXTCKYR3AQ]].
Let $\Lambda$ be one of the seven logics, with [[canonical model|TVE4F04KME]] $\mathfrak{M}^\Lambda = (W^\Lambda, R^\Lambda, V^\Lambda)$.
We write $\square^{-1}\Gamma = \set{\varphi : \square\varphi \in \Gamma}$, so $\Gamma R^\Lambda \Delta$ means $\square^{-1}\Gamma \subseteq \Delta$.
By the box lemma of [[the truth lemma|NM4CB7QAYT]], $\Gamma R^\Lambda \Delta$ also means that $\lozenge\varphi \in \Gamma$ for every $\varphi \in \Delta$.
Each maximal consistent set contains $\Lambda$ and is closed under modus ponens.

1. Axiom $\mathrm{T}$ gives reflexivity. Let $\square\varphi \in \Gamma$. The instance $\square\varphi \to \varphi$ is in $\Gamma$, so $\varphi \in \Gamma$. Hence $\square^{-1}\Gamma \subseteq \Gamma$, that is, $\Gamma R^\Lambda \Gamma$.
2. Axiom $\mathrm{D}$ gives seriality. By [[necessitation|G989VP2NGP]], $\square\top \in \Lambda \subseteq \Gamma$. The instance $\square\top \to \lozenge\top$ of $\mathrm{D}$ gives $\lozenge\top \in \Gamma$.
3. The existence lemma of [[the truth lemma|NM4CB7QAYT]] then gives $\Delta$ with $\Gamma R^\Lambda \Delta$. So every world has a successor.
4. Axiom $\mathrm{4}$ gives transitivity. Let $\Gamma R^\Lambda \Delta$, $\Delta R^\Lambda \Theta$ and $\square\varphi \in \Gamma$. The instance $\square\varphi \to \square\square\varphi$ gives $\square\square\varphi \in \Gamma$.
5. So $\square\varphi \in \Delta$, since $\Gamma R^\Lambda \Delta$, and then $\varphi \in \Theta$, since $\Delta R^\Lambda \Theta$. Hence $\Gamma R^\Lambda \Theta$.
6. Axiom $\mathrm{B}$ gives symmetry. Let $\Gamma R^\Lambda \Delta$ and $\varphi \in \Gamma$. The instance $\varphi \to \square\lozenge\varphi$ gives $\square\lozenge\varphi \in \Gamma$, so $\lozenge\varphi \in \Delta$.
7. So $\lozenge\varphi \in \Delta$ for every $\varphi \in \Gamma$. By the box lemma, read from $\Delta$ to $\Gamma$, this is $\Delta R^\Lambda \Gamma$.
8. Axiom $\mathrm{5}$ gives the Euclidean property. Let $\Gamma R^\Lambda \Delta$, $\Gamma R^\Lambda \Theta$ and $\varphi \in \Theta$. By the box lemma for $\Gamma R^\Lambda \Theta$, $\lozenge\varphi \in \Gamma$.
9. The instance $\lozenge\varphi \to \square\lozenge\varphi$ of $\mathrm{5}$ gives $\square\lozenge\varphi \in \Gamma$, so $\lozenge\varphi \in \Delta$. By the box lemma, $\Delta R^\Lambda \Theta$.
10. The combinations. For $\mathsf{S4}$, steps 1 and 4 give a preorder. For $\mathsf{B}$, steps 1 and 6 give a reflexive symmetric relation.
11. For $\mathsf{S5}$, steps 1 and 8 give a reflexive Euclidean relation. If $w R v$, then $w R v$ and $w R w$ give $v R w$, so $R$ is symmetric.
12. If $w R v$ and $v R u$, then $v R w$ by symmetry, and $v R w$ with $v R u$ give $w R u$ by the Euclidean property. So $R$ is an equivalence relation.
13. For $\mathsf{K}$ there is nothing to prove. This gives part 3, canonicity, for every row.
14. Strong completeness, by contraposition. Let $\varphi$ not be derivable in $\Lambda$ from any finite subset of $\Sigma$. Then $\Sigma \cup \set{\neg\varphi}$ is $\Lambda$-consistent.
15. By Lindenbaum's lemma, it lies in some $\Gamma \in W^\Lambda$. By the truth lemma, all of $\Sigma$ is true at $\Gamma$ and $\varphi$ is false at $\Gamma$.
16. By step 13, $\mathfrak{M}^\Lambda$ is a model on a frame of $\mathsf{C}$. So $\varphi$ is not a local consequence of $\Sigma$ over $\mathsf{C}$. This is part 1.
17. Weak completeness. Part 1 with $\Sigma = \emptyset$ gives: if $\varphi$ is valid on $\mathsf{C}$, then $\Lambda \vdash \varphi$. The other direction is [[soundness|E87G6ZTMTN]] with the frame conditions of [[common modal axiom schemata|FDFQFWPM4X]]. This is part 2.

## Idea

Each axiom, read inside maximal consistent sets, forces one property of the canonical relation.
The truth lemma then turns the canonical model into a countermodel for each non-theorem, and it lives on a frame of the right class.
The axioms $\mathrm{B}$ and $\mathrm{5}$ are handled with the diamond form of the canonical relation, since they put a $\lozenge$ under a $\square$.

## Variants

1. The same steps prove canonicity of every combination of $\mathrm{T}$, $\mathrm{D}$, $\mathrm{B}$, $\mathrm{4}$ and $\mathrm{5}$, for example $\mathsf{KD45}$ and $\mathsf{K45}$, see [[the KD45 example|1CFMP9DEE6]].
2. Kripke's original proofs of 1963 used semantic tableaux instead of maximal consistent sets.
3. For a proof that also gives finite models, combine this theorem with [[filtration|6ZZSHAKG5F]], see [[the finite model property theorem|XNPJK6B921]].
