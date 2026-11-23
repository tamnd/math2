---
tag: 8AF7AN5HE1
kind: example
name: Makinson's theorem on the coatoms of the modal lattice
msc: ["03B45"]
topics: [SPQVNPZDTB]
audience: research
instance_of: [EZ011FT3GT]
uses: [EZ011FT3GT, SC0BSJ3GT6, NRNKV2YYWJ, NGHWZ9Y7ZV, TVE4F04KME, NM4CB7QAYT]
sources:
  - url: https://en.wikipedia.org/wiki/Normal_modal_logic
    locator: Common normal modal logics
  - url: https://en.wikipedia.org/wiki/Kripke_semantics
    locator: Canonical models
---

## Example

Let $\circ$ be the one-point reflexive frame and $\bullet$ the one-point irreflexive frame.
We show that every consistent normal modal logic $L$ is contained in $\mathrm{Log}(\circ)$ or in $\mathrm{Log}(\bullet)$, so that these two logics are the only coatoms of the [[lattice of normal modal logics|EZ011FT3GT]].

The [[canonical model|TVE4F04KME]] of $L$ has the maximal $L$-consistent sets as worlds, with $\Gamma R \Delta$ when $\square \varphi \in \Gamma$ implies $\varphi \in \Delta$, and $V(p) = \{ \Gamma : p \in \Gamma \}$.
It is nonempty by [[Lindenbaum's lemma|SC0BSJ3GT6]], and by the [[truth lemma|NM4CB7QAYT]] every theorem of $L$ is true at every world.

### Substitution and the case without successors

1. For $\varphi \in L$ and a map $s$ from variables to $\{\top, \bot\}$, let $\varphi^s$ be the result of the substitution.
   Then $\varphi^s \in L$ by closure under substitution, and $\varphi^s$ has no variables.
2. Case 1: some world $\Gamma$ of the canonical model has no successor.
   By induction on formulas, a variable-free formula $\chi$ is true at $\Gamma$ exactly when it is true at $\bullet$, since at both points every $\square \psi$ is true and every $\lozenge \psi$ is false.
3. Each $\varphi^s$ is true at $\Gamma$, by the truth lemma, so it is true at $\bullet$.
   The valuations on $\bullet$ correspond to the maps $s$, so $\varphi$ is valid on $\bullet$, and $L \subseteq \mathrm{Log}(\bullet)$.

### The serial case and the conclusion

4. Case 2: every world has a successor, so the model is [[serial|NRNKV2YYWJ]].
   By induction, every variable-free $\chi$ is true at all worlds or false at all worlds, with the same value that it has at $\circ$.
5. The induction step for $\square \chi$: if $\chi$ is true everywhere, so is $\square \chi$.
   If $\chi$ is false everywhere, $\square \chi$ is false everywhere, because every world has a successor; the case $\lozenge \chi$ is dual.
6. As in step 3, each $\varphi^s$ is true in the model, so it is true at $\circ$, and $L \subseteq \mathrm{Log}(\circ)$.
7. Both logics are consistent, since $\bot$ is false on a one-point frame.
   Neither contains the other, because $\square \bot \in \mathrm{Log}(\bullet) \setminus \mathrm{Log}(\circ)$ and $\square p \to p \in \mathrm{Log}(\circ) \setminus \mathrm{Log}(\bullet)$.
8. So the consistent logics are exactly the logics below one of the two, and the two are the maximal consistent logics, that is, the coatoms.

## Remarks

The example shows that the top of the lattice is simple, while the part near $\mathsf{K}$ is very complex.
David Makinson proved the theorem in 1971.
$\mathrm{Log}(\circ)$ is $\mathsf{K} \oplus (\square p \leftrightarrow p)$, often called $\mathsf{Triv}$, and $\mathrm{Log}(\bullet)$ is $\mathsf{K} \oplus \square \bot$, often called $\mathsf{Ver}$.

A consequence is that every consistent normal modal logic is valid on a one-point frame.
So it has at least one Kripke frame, though it can still be [[Kripke incomplete|W67YJQTT50]].
Case 2 also shows that every logic not contained in $\mathrm{Log}(\bullet)$ proves $\lozenge \top$, which is the [[splitting of the lattice by the irreflexive point|Q6P4T6YH9Z]].

Watch out: the proof uses the canonical model only for its worlds and the truth lemma, and it does not need $L$ to be complete.

## Explanations

### L1 human

Strengthen a modal logic step by step without making it contradictory.
At the end you reach one of exactly two logics.
In one, "necessarily $A$" means just "$A$"; in the other, everything is necessary.
These are the logics of a single point that sees itself and of a single point that sees nothing.

### L2 human

We place two logics.
The canonical model of $\mathsf{S4}$ is reflexive, so every world has a successor, Case 2 applies, and $\mathsf{S4} \subseteq \mathrm{Log}(\circ)$.
Check: $\circ$ is reflexive and transitive, so it validates T and 4.
For $\mathsf{GL}$, substitute $\bot$ for $p$ in Löb's axiom $\square(\square p \to p) \to \square p$.
$$\square(\square \bot \to \bot) \to \square \bot$$
This formula is $\square \lozenge \top \to \square \bot$.
At $\circ$ the antecedent is true and the consequent false, so $\mathsf{GL} \not\subseteq \mathrm{Log}(\circ)$, and therefore $\mathsf{GL} \subseteq \mathrm{Log}(\bullet)$.
The typical use is to place a logic below a known one by a substitution argument with constants.
