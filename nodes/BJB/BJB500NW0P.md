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

We prove [[the completeness theorem|FXTCKYR3AQ]] by showing that each axiom forces one property of the canonical relation, and then we apply the truth lemma.

Let $\Lambda$ be one of the seven logics, with [[canonical model|TVE4F04KME]] $\mathfrak{M}^\Lambda = (W^\Lambda, R^\Lambda, V^\Lambda)$.
We write $\square^{-1}\Gamma = \{ \varphi : \square\varphi \in \Gamma \}$, so $\Gamma R^\Lambda \Delta$ means $\square^{-1}\Gamma \subseteq \Delta$.
By the box lemma of [[the truth lemma|NM4CB7QAYT]], $\Gamma R^\Lambda \Delta$ also means that $\lozenge\varphi \in \Gamma$ for every $\varphi \in \Delta$.
Each maximal consistent set contains $\Lambda$ and is closed under modus ponens.

### Each axiom gives one property

1. Axiom $\mathrm{T}$ gives reflexivity.
   Let $\square\varphi \in \Gamma$.
   The instance $\square\varphi \to \varphi$ lies in $\Gamma$, so $\varphi \in \Gamma$.
   Hence $\square^{-1}\Gamma \subseteq \Gamma$, that is, $\Gamma R^\Lambda \Gamma$.
2. Axiom $\mathrm{D}$ gives seriality.
   By [[necessitation|G989VP2NGP]], $\square\top \in \Lambda \subseteq \Gamma$, and the instance $\square\top \to \lozenge\top$ of $\mathrm{D}$ gives $\lozenge\top \in \Gamma$.
   The existence lemma of [[the truth lemma|NM4CB7QAYT]] then gives $\Delta$ with $\Gamma R^\Lambda \Delta$.
3. Axiom $\mathrm{4}$ gives transitivity.
   Let $\Gamma R^\Lambda \Delta$, $\Delta R^\Lambda \Theta$ and $\square\varphi \in \Gamma$.
   The instance $\square\varphi \to \square\square\varphi$ gives $\square\square\varphi \in \Gamma$.
   So $\square\varphi \in \Delta$, since $\Gamma R^\Lambda \Delta$, and then $\varphi \in \Theta$, since $\Delta R^\Lambda \Theta$.
   Hence $\Gamma R^\Lambda \Theta$.
4. Axiom $\mathrm{B}$ gives symmetry.
   Let $\Gamma R^\Lambda \Delta$ and $\varphi \in \Gamma$.
   The instance $\varphi \to \square\lozenge\varphi$ gives $\square\lozenge\varphi \in \Gamma$, so $\lozenge\varphi \in \Delta$.
   So $\lozenge\varphi \in \Delta$ for every $\varphi \in \Gamma$, and the box lemma, read from $\Delta$ to $\Gamma$, gives $\Delta R^\Lambda \Gamma$.
5. Axiom $\mathrm{5}$ gives the Euclidean property.
   Let $\Gamma R^\Lambda \Delta$, $\Gamma R^\Lambda \Theta$ and $\varphi \in \Theta$.
   The box lemma for $\Gamma R^\Lambda \Theta$ gives $\lozenge\varphi \in \Gamma$.
   The instance $\lozenge\varphi \to \square\lozenge\varphi$ of $\mathrm{5}$ gives $\square\lozenge\varphi \in \Gamma$, so $\lozenge\varphi \in \Delta$.
   This holds for every $\varphi \in \Theta$, so the box lemma gives $\Delta R^\Lambda \Theta$.

### The combinations

6. For $\mathsf{S4} = \mathsf{KT4}$, steps 1 and 3 give a reflexive transitive relation.
   For $\mathsf{B} = \mathsf{KTB}$, steps 1 and 4 give a reflexive symmetric relation.
7. For $\mathsf{S5} = \mathsf{KT5}$, steps 1 and 5 give a reflexive Euclidean relation.
   If $w R v$, then $w R v$ and $w R w$ give $v R w$ by the Euclidean property, so $R$ is symmetric.
8. If $w R v$ and $v R u$, then $v R w$ by symmetry, and $v R w$ with $v R u$ give $w R u$ by the Euclidean property.
   So $R$ is an equivalence relation.
9. For $\mathsf{K}$ there is nothing to prove, and for $\mathsf{T} = \mathsf{KT}$, $\mathsf{D} = \mathsf{KD}$ and $\mathsf{K4}$ one step suffices.
   This gives part 3, canonicity, for every row.

### Completeness

10. We prove strong completeness by contraposition.
    Suppose $\varphi$ is not derivable in $\Lambda$ from any finite subset of $\Sigma$.
    Then $\Sigma \cup \{ \neg\varphi \}$ is $\Lambda$-consistent.
11. By Lindenbaum's lemma it lies in some $\Gamma \in W^\Lambda$, and by the truth lemma all of $\Sigma$ is true at $\Gamma$ while $\varphi$ is false there.
12. By step 9, $\mathfrak{M}^\Lambda$ is a model on a frame of $\mathsf{C}$, so $\varphi$ is not a local consequence of $\Sigma$ over $\mathsf{C}$.
    This is part 1.
13. Part 1 with $\Sigma = \emptyset$ says that a formula valid on $\mathsf{C}$ is a theorem of $\Lambda$.
    The other direction is [[soundness|E87G6ZTMTN]] with the frame conditions of [[common modal axiom schemata|FDFQFWPM4X]].
    This is part 2.

## Idea

Each axiom, read inside maximal consistent sets, forces one property of the canonical relation.
The truth lemma then turns the canonical model into a countermodel for each non-theorem, and that countermodel lives on a frame of the right class.
The axioms $\mathrm{B}$ and $\mathrm{5}$ put a $\lozenge$ under a $\square$, so they are handled with the diamond form of the canonical relation.

## Variants

The same steps prove canonicity of every combination of $\mathrm{T}$, $\mathrm{D}$, $\mathrm{B}$, $\mathrm{4}$ and $\mathrm{5}$, for example $\mathsf{KD45}$ and $\mathsf{K45}$, as in [[the KD45 example|1CFMP9DEE6]].

Kripke's original proofs of 1963 used semantic tableaux instead of maximal consistent sets.

For a proof that also gives finite models, combine this theorem with [[filtration|6ZZSHAKG5F]], as in [[the finite model property theorem|XNPJK6B921]].
