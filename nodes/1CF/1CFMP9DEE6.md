---
tag: 1CFMP9DEE6
kind: example
name: Completeness of KD45 by canonicity
msc: ["03B45"]
topics: [SKY7AQFG1V]
audience: grad
instance_of: [TVE4F04KME]
uses: [TVE4F04KME, NM4CB7QAYT, FXTCKYR3AQ, E87G6ZTMTN, NS4AC3W4FM, SC0BSJ3GT6]
sources:
  - url: https://en.wikipedia.org/wiki/Kripke_semantics
    locator: Correspondence and completeness
---

## Example

Let $\mathsf{KD45} = \mathsf{K} + \mathrm{D} + \mathrm{4} + \mathrm{5}$, the usual logic of belief.
We show with the [[canonical model|TVE4F04KME]] that $\mathsf{KD45}$ is exactly the logic of the frames that are serial, transitive and Euclidean.

Let $(W^c, R^c)$ be the canonical frame of $\mathsf{KD45}$.
Its worlds are the maximal $\mathsf{KD45}$-consistent sets, and $\Gamma R^c \Delta$ holds when every $\varphi$ with $\square\varphi \in \Gamma$ lies in $\Delta$.
The [[completeness theorem for K to S5|FXTCKYR3AQ]] proves three facts about any normal logic, one axiom at a time.
A logic that contains $\mathrm{D}$ has a serial canonical frame, a logic that contains $\mathrm{4}$ has a transitive one, and a logic that contains $\mathrm{5}$ has a Euclidean one.
$\mathsf{KD45}$ contains all three axioms, so $R^c$ is serial, transitive and Euclidean at once.

Now let $\mathsf{KD45} \nvdash \varphi$.
Then $\{ \neg\varphi \}$ is consistent, and [[Lindenbaum's lemma|SC0BSJ3GT6]] extends it to a maximal consistent set $\Gamma$.
By the [[truth lemma|NM4CB7QAYT]], $\varphi$ is false at $\Gamma$ in the canonical model.
So $\varphi$ fails on a serial, transitive, Euclidean frame, and this is completeness.

In the other direction, these frames validate $\mathrm{D}$, $\mathrm{4}$ and $\mathrm{5}$, so by [[soundness|E87G6ZTMTN]] they validate every theorem of $\mathsf{KD45}$.
So $\mathsf{KD45}$ is exactly the set of formulas valid on all serial, transitive, Euclidean frames.

Check: $\mathsf{KD45}$ does not prove axiom $\mathrm{T}$.
The frame of [[a Euclidean relation that is neither reflexive nor symmetric|NS4AC3W4FM]] has $W = \{ a, b \}$ and $R = \{ (a, b), (b, b) \}$.
It is serial, transitive and Euclidean, and with $V(p) = \{ b \}$ the formula $\square p$ is true at $a$ while $p$ is false there.

## Remarks

### Why the properties combine

Each frame property is proved once, for every normal logic that contains the matching axiom.
The proof for $\mathrm{D}$ uses only $\lozenge\top \in \Gamma$, the proof for $\mathrm{4}$ uses only $\square\varphi \to \square\square\varphi \in \Gamma$, and the proof for $\mathrm{5}$ uses only $\lozenge\varphi \to \square\lozenge\varphi \in \Gamma$.
None of these proofs uses the other axioms, so the three properties hold together in the canonical frame of any logic that contains all three.

### Nearby logics

The same argument shows that $\mathsf{K45}$ is complete for transitive Euclidean frames and that $\mathsf{KD4}$ is complete for serial transitive frames.
If we add $\mathrm{T}$, the logic becomes $\mathsf{S5}$, also written $\mathsf{KT5}$.
Its canonical frame is reflexive and Euclidean, and a reflexive Euclidean relation is an equivalence relation.

### Watch out

The method works here because $\mathrm{D}$, $\mathrm{4}$ and $\mathrm{5}$ are each canonical.
Not every axiom is: the provability logic $\mathsf{GL}$ has a canonical frame that does not validate it, as [[the GL example|E61769H6KG]] shows.

## Explanations

### L1 human

The logic KD45 describes belief.
Its rules say that beliefs never contradict each other, and that the agent knows what it believes and what it does not believe.
To show that these rules are complete, we build one large model out of all consistent descriptions of a world.
Each rule forces one property of the arrows in this model, and each property comes from its own rule, so all three hold at once.
So every formula that the rules do not prove fails somewhere in a model of the right shape.

### L2 human

We test the formula $\square p \to p$, which $\mathsf{KD45}$ does not prove.
Lindenbaum's lemma gives a maximal consistent $\Gamma$ that contains $\square p$ and $\neg p$.
Seriality gives some $\Delta$ with $\Gamma R^c \Delta$, and $p \in \Delta$ since $\square p \in \Gamma$.
But $\Gamma$ is not a successor of itself, since $\square p \in \Gamma$ and $p \notin \Gamma$.
So the canonical frame of $\mathsf{KD45}$ is not reflexive, as it should not be.
The typical use of canonicity is to prove completeness for a new combination of axioms with no new work.
