---
tag: Q6P4T6YH9Z
kind: example
name: The irreflexive point splits the lattice of normal modal logics
msc: ["03B45", "06B20"]
topics: [SPQVNPZDTB]
audience: research
instance_of: [EZ011FT3GT]
uses: [EZ011FT3GT, 8AF7AN5HE1, NRNKV2YYWJ]
sources:
  - url: https://en.wikipedia.org/wiki/Normal_modal_logic
    locator: Common normal modal logics
  - url: https://builds.openlogicproject.org/
    locator: Modal Logic
---

## Example

Let $\bullet$ be the one-point irreflexive frame, and let $\mathsf{KD} = \mathsf{K} \oplus \lozenge \top$, the logic of [[serial|NRNKV2YYWJ]] frames.
A pair $\langle L_1, L_2 \rangle$ *splits* $\mathrm{NExt}(\mathsf{K})$ if every normal modal logic $L$ satisfies exactly one of $L \subseteq L_1$ and $L_2 \subseteq L$.
We show that $\langle \mathrm{Log}(\bullet), \mathsf{KD} \rangle$ splits the [[lattice of normal modal logics|EZ011FT3GT]].

1. Not both: $\lozenge \top$ is false at $\bullet$, so $\mathsf{KD} \not\subseteq \mathrm{Log}(\bullet)$.
   If $L \subseteq \mathrm{Log}(\bullet)$ and $\mathsf{KD} \subseteq L$, then $\mathsf{KD} \subseteq \mathrm{Log}(\bullet)$, which is false.
2. At least one, for an inconsistent $L$: then $L$ contains every formula, so $\mathsf{KD} \subseteq L$.
3. At least one, for a consistent $L$ with a dead end: consider the canonical model of $L$, as in [[Makinson's theorem|8AF7AN5HE1]].
   If some world has no successor, then $L \subseteq \mathrm{Log}(\bullet)$ by Case 1 of that theorem.
4. At least one, for a consistent $L$ without a dead end: every maximal $L$-consistent set $\Gamma$ has a successor $\Delta$.
   Then $\lozenge \top \in \Gamma$, since otherwise $\square \bot \in \Gamma$ and so $\bot \in \Delta$, which is impossible.
5. A formula that belongs to every maximal $L$-consistent set is a theorem of $L$, by Lindenbaum's lemma.
   So $\lozenge \top \in L$, and $\mathsf{KD} \subseteq L$.
6. So every normal modal logic is below $\mathrm{Log}(\bullet)$ or above $\mathsf{KD}$, and not both.

## Remarks

The example is the simplest splitting of the lattice.
It cuts $\mathrm{NExt}(\mathsf{K})$ into the logics of the irreflexive point and the logics that prove seriality.
The upper logic is axiomatized by one formula, the splitting formula of the frame, and for $\bullet$ it is $\lozenge \top$.

The frame $\bullet$ has no cycles, and Blok proved that the logic of a finite rooted frame splits $\mathrm{NExt}(\mathsf{K})$ exactly when the frame has no cycles.
The reflexive point $\circ$ has a cycle of length one, so it gives no splitting.
In $\mathrm{NExt}(\mathsf{K4})$ every finite rooted transitive frame gives a splitting, and so splittings there axiomatize logics by excluding finite frames.

Watch out: the lower side contains logics such as $\mathsf{K}$, which have many frames without dead ends.
The test is about what the logic proves, not about each of its frames.

## Explanations

### L1 human

A splitting divides all logics into two groups with a single test.
Here the test is: does the logic prove that every world has a next world?
If it does not, it fits inside the logic of one dead-end point.
If it does, it lies above the logic of seriality.

### L2 human

We sort three logics.
$\mathsf{S4}$ proves $\square \bot \to \bot$, an instance of T, and this formula is equivalent to $\lozenge \top$, so $\mathsf{S4}$ is on the upper side.
$\mathsf{GL}$ does not prove $\lozenge \top$, since a single irreflexive point is a frame of $\mathsf{GL}$, so $\mathsf{GL} \subseteq \mathrm{Log}(\bullet)$.
$\mathsf{K}$ itself is on the lower side, since $\bullet$ validates $\mathsf{K}$.
The typical use of a splitting is to decide where a given logic lies with respect to a finite frame, by checking one formula.
