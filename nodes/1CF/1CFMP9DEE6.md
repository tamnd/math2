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

Let $\mathsf{KD45} = \mathsf{K} + \mathrm{D} + \mathrm{4} + \mathrm{5}$.
We show with the [[canonical model|TVE4F04KME]] that $\mathsf{KD45}$ is the logic of the serial, transitive and Euclidean frames.
Let $(W^c, R^c)$ be the canonical frame of $\mathsf{KD45}$: the worlds are the maximal $\mathsf{KD45}$-consistent sets, and $\Gamma R^c \Delta$ when $\square\varphi \in \Gamma$ implies $\varphi \in \Delta$.

1. $\mathsf{KD45}$ contains $\mathrm{D}$, so its canonical frame is serial, by [[completeness of K, T, D, K4, S4, B and S5|FXTCKYR3AQ]].
2. $\mathsf{KD45}$ contains $\mathrm{4}$, so its canonical frame is transitive, by the same page.
3. $\mathsf{KD45}$ contains $\mathrm{5}$, so its canonical frame is Euclidean, by the same page.
4. Let $\mathsf{KD45} \nvdash \varphi$. Then $\set{\neg\varphi}$ is consistent, and [[Lindenbaum's lemma|SC0BSJ3GT6]] extends it to a maximal consistent set $\Gamma$.
5. By the [[truth lemma|NM4CB7QAYT]], $\varphi$ is false at $\Gamma$ in the canonical model.
6. So $\varphi$ fails on a serial, transitive, Euclidean frame, by steps 1 to 3. This is completeness.
7. By [[soundness|E87G6ZTMTN]], every theorem of $\mathsf{KD45}$ is valid on these frames, since they validate $\mathrm{D}$, $\mathrm{4}$ and $\mathrm{5}$.
8. So $\mathsf{KD45}$ is exactly the set of formulas valid on all serial, transitive, Euclidean frames.
9. The frame of [[a Euclidean relation that is neither reflexive nor symmetric|NS4AC3W4FM]] is serial, transitive and Euclidean, and it refutes $\mathrm{T}$ at $a$. So $\mathsf{KD45} \nvdash \mathrm{T}$.

## Remarks

The example shows how the canonical model method combines.
Each frame property is proved once, for every normal logic that contains the matching axiom, not for one logic at a time.
For $\mathrm{D}$ the proof uses $\lozenge\top \in \Gamma$, for $\mathrm{4}$ it uses $\square\varphi \to \square\square\varphi \in \Gamma$, and for $\mathrm{5}$ it uses $\lozenge\varphi \to \square\lozenge\varphi \in \Gamma$.
None of these proofs uses the other axioms, so the three properties hold together in the canonical frame of $\mathsf{KD45}$.
The same argument gives completeness of $\mathsf{K45}$ for transitive Euclidean frames and of $\mathsf{KD4}$ for serial transitive frames.
If we add $\mathrm{T}$, the logic becomes $\mathsf{S5}$, and the canonical frame becomes reflexive and Euclidean, hence an equivalence relation.

## Explanations

### L1 human

The logic KD45 is a logic of belief: beliefs are consistent, and the agent knows what it believes and what it does not believe.
To show that this list of rules is complete, one builds one big model out of all consistent descriptions of a world.
Each rule forces one property of the arrows in this model.
Since each property comes from its own rule, all three properties hold at once.
So every formula that the rules do not prove fails somewhere in a model of the right shape.

### L2 human

1. We test the formula $\square p \to p$, which $\mathsf{KD45}$ does not prove.
2. Step 4 gives a maximal consistent $\Gamma$ that contains $\square p$ and $\neg p$.
3. Step 1 gives some $\Delta$ with $\Gamma R^c \Delta$, and $p \in \Delta$ since $\square p \in \Gamma$.
4. $\Gamma$ itself is not a successor of $\Gamma$, since $\square p \in \Gamma$ and $p \notin \Gamma$, so the canonical frame is not reflexive.

The typical use of canonicity is to prove completeness for a new combination of axioms with no new work.
A trap: not every axiom is canonical, so this method fails for some logics, for example the logic $\mathsf{GL}$ of provability.
