---
tag: ~d50dbda7
kind: proof
name: Proof that Horn sentences are the sentences preserved under reduced products
aliases: [proof-of-horn-sentences-and-reduced-products]
msc: ["03C20", "03C40"]
topics: [JYJHB4YBAH]
audience: research
proves: ~a403cb4d
uses: [8RRECJJM3G, F4WRD396PB, EY20BF96SJ, 7CVJCQKY41, 6TF2JBTPPJ, 0MN2MER9WN]
methods: [0NTF6DMVAP]
sources:
  - url: https://arxiv.org/abs/1905.10673
    locator: Section 1
---

## Proof

This proof gives part 1 in full and reduces part 2 to two cited results: Keisler's theorem under the continuum hypothesis, and Galvin's lemma that preservation under reduced products is arithmetical.

**Part 1.**

1. Let $\varphi$ be a Horn sentence, $F$ a filter on a nonempty set $I$, and $\mathcal{M}_i \models \varphi$ for all $i \in I$.
2. The set $\set{i \in I : \mathcal{M}_i \models \varphi}$ is $I$, which lies in $F$.
3. By [[the preservation theorem for Horn formulas|8RRECJJM3G]], $\prod_{i \in I} \mathcal{M}_i / F \models \varphi$.

**Reduction to a finite signature.**

4. Let $L_0 \subseteq L$ be the finite set of symbols that occur in $\varphi$. The [[reduct|EY20BF96SJ]] of a reduced product to $L_0$ is the reduced product of the reducts, with the same filter, by the definition of the [[reduced product|F4WRD396PB]].
5. Every $L_0$-structure has an expansion to $L$, since domains are nonempty.
6. So $\varphi$ is preserved under reduced products of $L$-structures if and only if it is preserved under reduced products of $L_0$-structures. A Horn $L_0$-sentence equivalent to $\varphi$ over $L_0$-structures stays equivalent over $L$-structures, by taking reducts. So it suffices to prove part 2 for finite signatures.

**Part 2.**

7. Fix a coding of the finite signatures and of their sentences by natural numbers. Let $A(\varphi)$ say "$\varphi$ is preserved under reduced products", and let $B(\varphi)$ say "some Horn sentence $\psi$ over the symbols of $\varphi$ has $\vdash \varphi \leftrightarrow \psi$".
8. $B$ is an [[arithmetical|7CVJCQKY41]] property: it asks for a number $\psi$ and a number coding a formal proof. By Galvin's lemma, $A$ is equivalent in ZFC to an arithmetical property $A'$.
9. Keisler's theorem is a theorem of ZFC together with the [[continuum hypothesis|0MN2MER9WN]]. It gives $A(\varphi) \rightarrow B(\varphi)$ for every $\varphi$ over a finite signature.
10. The [[constructible universe|6TF2JBTPPJ]] $\mathbf{L}$ is a model of ZFC in which the continuum hypothesis holds. So Keisler's theorem and Galvin's lemma both hold in $\mathbf{L}$, and in $\mathbf{L}$ the statement $\forall \varphi \, (A'(\varphi) \rightarrow B(\varphi))$ is true.
11. This statement is arithmetical, and $\mathbf{L}$ has the same natural numbers as the universe, with the same arithmetic. So the statement also holds in the universe.
12. By Galvin's lemma in the universe, $A(\varphi) \rightarrow B(\varphi)$ for every sentence $\varphi$ over a finite signature, and by step 6 for every $L$-sentence.

## Idea

Part 1 is an induction on formulas that never needs to choose between two atoms, so a filter is enough.
For part 2, the set-theoretic hypothesis is removed by noting that the statement to be proved is about natural numbers only, and such statements cannot change between the universe and an inner model in which the hypothesis holds.

## Variants

- Goldbring and Keisler prove the continuous analogue in the same two stages: first under the continuum hypothesis, then without it, by converting general structures into first-order structures and back instead of repeating Galvin's argument.
- For universal sentences, the [[characterization of universal Horn classes|~b2077580]] gives a direct proof without any set theory.
