---
tag: 5KQCT1HMC3
kind: example
name: Number restrictions are not ALC concepts
msc: ["03B70", "03B45"]
topics: [CQM9SRN8PM]
audience: research
not_instance_of:
  - target: TXQ80B8ZSA
    note: the concept ≥ 2 r.⊤ is not equivalent to any ALC concept, because it separates two bisimilar interpretations
uses: [TXQ80B8ZSA, 7T740SFHHV, G8BHVS9715]
sources:
  - url: https://en.wikipedia.org/wiki/Description_logic
    locator: The description logic ALC
  - book: isbn:9780521695428
    locator: Baader et al., An Introduction to Description Logic
---

## Example

The number restriction ${\ge} 2\, r.\top$ denotes the objects with at least two $r$-successors.
We show that no [[ALC|TXQ80B8ZSA]] concept $C$ has $C^{\mathcal{I}} = ({\ge} 2\, r.\top)^{\mathcal{I}}$ in every interpretation $\mathcal{I}$.

1. Let $\mathcal{I}$ have domain $\set{d, e}$, $r^{\mathcal{I}} = \set{(d, e)}$, and every concept name empty.
2. Let $\mathcal{J}$ have domain $\set{d', e_1, e_2}$, $r^{\mathcal{J}} = \set{(d', e_1), (d', e_2)}$, and every concept name empty.
3. The relation $Z = \set{(d, d'), (e, e_1), (e, e_2)}$ is a [[bisimulation|7T740SFHHV]]. Related objects agree on all concept names, since these are empty. Each $r$-step from one side is matched on the other: $d \to e$ by $d' \to e_1$, and $d' \to e_i$ by $d \to e$. The objects $e$, $e_1$, $e_2$ have no successors.
4. By induction on concepts, if $(x, y) \in Z$, then $x \in C^{\mathcal{I}}$ iff $y \in C^{\mathcal{J}}$. The Boolean cases are immediate, and the case $\exists r.D$ uses the matching of steps in step 3; $\forall r.D$ is $\neg\exists r.\neg D$.
5. So every $\mathcal{ALC}$ concept contains $d$ in $\mathcal{I}$ iff it contains $d'$ in $\mathcal{J}$.
6. But $d \notin ({\ge} 2\, r.\top)^{\mathcal{I}}$, since $d$ has one successor, and $d' \in ({\ge} 2\, r.\top)^{\mathcal{J}}$, since $d'$ has two.
7. So no $\mathcal{ALC}$ concept is equivalent to ${\ge} 2\, r.\top$.

## Remarks

Under [[Schild's correspondence|G8BHVS9715]], this is the fact that basic modal logic cannot count successors; graded modalities $\Diamond_{\ge n}$ are needed.
The description logic $\mathcal{ALCQ}$ adds qualified number restrictions ${\ge} n\, r.C$ and ${\le} n\, r.C$, and its concept satisfiability is still PSPACE-complete with binary coding of numbers.
The same argument shows that $\mathcal{ALC}$ cannot express inverse roles or role intersection, by suitable bisimilar pairs.

## Explanations

### L1 human

"Has at least two children" cannot be said in the basic description logic.
A person with one child and a person with two children look the same to it, if the children look alike.
The logic sees only what kinds of children there are, not how many.

### L2 human

1. Build two interpretations that differ only in the number of $r$-successors.
2. Link them by a bisimulation.
3. Conclude that every $\mathcal{ALC}$ concept treats the two roots the same.

The typical use is to prove that a property is not expressible in a modal or description logic.
A trap: ${\ge} 2\, r.\top$ is not $\exists r.\top \sqcap \exists r.\top$; the two conjuncts may have the same witness.
