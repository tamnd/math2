---
tag: SGNK5FWABD
kind: proof
name: Proof that ALC is a notational variant of multimodal K
msc: ["03B70", "03B45"]
topics: [CQM9SRN8PM]
audience: research
proves: G8BHVS9715
uses: [TXQ80B8ZSA, 6BQ71KQ6QT, FXTCKYR3AQ, E87G6ZTMTN]
methods: [12MQ2NJ29A, 0NTF6DMVAP]
sources:
  - url: https://en.wikipedia.org/wiki/Description_logic
    locator: Modal logic
  - book: isbn:9780521695428
    locator: Baader et al., An Introduction to Description Logic
---

## Proof

We use the notation of [[the correspondence theorem|G8BHVS9715]].
Fix an interpretation $\mathcal{I}$ and write $M = M_{\mathcal{I}}$.

Part 1, by structural induction on $C$.

1. $C = A_j$: $d \in A_j^{\mathcal{I}}$ iff $d \in V(p_j)$ iff $M, d \models p_j$.
2. $C = \top$ or $C = \bot$: both sides hold for every $d$, or for no $d$.
3. $C = \neg D$: $d \in (\neg D)^{\mathcal{I}}$ iff $d \notin D^{\mathcal{I}}$ iff, by the induction hypothesis, $M, d \not\models \tau(D)$ iff $M, d \models \neg\tau(D)$.
4. $C = D \sqcap E$ and $C = D \sqcup E$: membership in an intersection or union is the conjunction or disjunction of memberships, and the induction hypothesis applies to $D$ and $E$.
5. $C = \exists r_i.D$: $d \in C^{\mathcal{I}}$ iff some $e$ with $(d, e) \in r_i^{\mathcal{I}}$ has $e \in D^{\mathcal{I}}$. By the induction hypothesis this holds iff some $e$ with $(d, e) \in r_i^{\mathcal{I}}$ has $M, e \models \tau(D)$, iff $M, d \models \Diamond_i \tau(D)$, since $r_i^{\mathcal{I}}$ is the $i$th relation of $M$.
6. $C = \forall r_i.D$: the same argument with "every" in place of "some" gives $d \in C^{\mathcal{I}}$ iff $M, d \models \Box_i \tau(D)$.

Part 2.

7. A Kripke model $(W, R_1, \dots, R_n, V)$ with $W \neq \emptyset$ determines the interpretation with $\Delta^{\mathcal{I}} = W$, $r_i^{\mathcal{I}} = R_i$ and $A_j^{\mathcal{I}} = V(p_j)$, and this is the only $\mathcal{I}$ with $M_{\mathcal{I}}$ equal to the given model.
8. Define $\sigma$ from $\mathcal{L}_n$ to concepts by the inverse clauses: $\sigma(p_j) = A_j$, $\sigma(\Diamond_i\varphi) = \exists r_i.\sigma(\varphi)$, $\sigma(\Box_i\varphi) = \forall r_i.\sigma(\varphi)$, and the Boolean clauses. Structural induction shows $\tau(\sigma(\varphi)) = \varphi$ and $\sigma(\tau(C)) = C$, so $\tau$ is a bijection.

Part 3.

9. If $d \in C^{\mathcal{I}}$, then $M_{\mathcal{I}}, d \models \tau(C)$ by part 1. Conversely, if $N, w \models \tau(C)$ for a Kripke model $N$, then $N = M_{\mathcal{I}}$ for some $\mathcal{I}$ by step 7, and $w \in C^{\mathcal{I}}$ by part 1. So $C$ is satisfiable iff $\tau(C)$ is.
10. $\models C \sqsubseteq D$ fails iff some $\mathcal{I}$ and $d$ have $d \in C^{\mathcal{I}}$ and $d \notin D^{\mathcal{I}}$. By part 1 and step 7, this holds iff some Kripke model and world make $\tau(C)$ true and $\tau(D)$ false, that is, iff $\tau(C) \to \tau(D)$ is not valid.
11. $\mathsf{K}_n$ is sound and complete for the class of all Kripke models with $n$ relations, by the same canonical model argument as for $\mathsf{K}$, see [[soundness|E87G6ZTMTN]] and [[completeness|FXTCKYR3AQ]]. So $\tau(C) \to \tau(D)$ is valid iff $\mathsf{K}_n \vdash \tau(C) \to \tau(D)$. ∎

## Idea

The semantic clauses of $\mathcal{ALC}$ and of multimodal Kripke semantics are the same clauses with different names: domain for worlds, roles for accessibility relations, concept names for atoms.
So the translation is a renaming, and induction on concepts checks that it preserves meaning.

## Variants

1. The same induction proves that the standard translation $\mathrm{ST}_x$ maps each concept to a first-order formula with one free variable that defines $C^{\mathcal{I}}$; with $\tau$ this gives the standard translation of modal logic.
2. Adding a TBox, the same induction shows that $\mathcal{I}$ is a model of $\mathcal{T}$ iff every $\tau(D) \to \tau(E)$ with $D \sqsubseteq E \in \mathcal{T}$ holds at every world of $M_{\mathcal{I}}$.
