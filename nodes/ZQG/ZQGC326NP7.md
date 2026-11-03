---
tag: ZQGC326NP7
kind: statement
role: proposition
name: Pauli exclusion principle
msc: [81V74, 81V72]
uses: [Y64G7W4BEC, EY0X2NKA3S, 0MDMZ965VE]
about: [Y64G7W4BEC]
sources:
  - url: https://en.wikipedia.org/wiki/Pauli_exclusion_principle
same_as:
  wikidata: Q131594
  wikipedia: Pauli exclusion principle
---

## Statement

Let $\mathfrak{h}$ be a complex Hilbert space and let $n \ge 2$.
Let $P_-$ be the orthogonal projection of $\mathfrak{h}^{\otimes n}$ onto the antisymmetric subspace $\mathcal{H}_-^{(n)}$.
This subspace is the state space of $n$ [[identical fermions|Y64G7W4BEC]].
Let $v_1, \dots, v_n \in \mathfrak{h}$.

1. If $v_i = v_j$ for some $i \ne j$, then $P_-(v_1 \otimes \cdots \otimes v_n) = 0$.
2. More generally, $P_-(v_1 \otimes \cdots \otimes v_n) = 0$ if and only if $v_1, \dots, v_n$ are linearly dependent.
3. If $\dim \mathfrak{h} = d$ is finite, then $\dim \mathcal{H}_-^{(n)} = \binom{d}{n}$; in particular $\mathcal{H}_-^{(n)} = \set{0}$ when $n > d$.

## Remarks

The space $\mathcal{H}_-^{(n)}$ is the $n$-th exterior power of $\mathfrak{h}$, and $P_-(v_1 \otimes \cdots \otimes v_n)$ is, up to the factor $1/n!$, the wedge product $v_1 \wedge \cdots \wedge v_n$ in the [[exterior algebra|0MDMZ965VE]].
If $v_i = v_j$, the transposition $\tau = (ij)$ fixes the product vector $w = v_1 \otimes \cdots \otimes v_n$, so $P_- w = P_-(U_\tau w) = -P_- w$, and hence $P_- w = 0$.
The other parts are standard facts about exterior powers.
A wedge product vanishes exactly on dependent vectors, and the wedges of increasing basis vectors form a basis.

Example: for electrons in an atom, $\mathfrak{h}$ contains the spin factor $\C^2$.
Each orbital, a one-dimensional subspace of $L^2(\R^3)$, together with the spin factor gives a two-dimensional space, so by part 3 at most two electrons occupy one orbital.

The statement is about fermions only.
For bosons the symmetric projection $P_+$ of $v \otimes v \otimes \cdots \otimes v$ is that vector itself, which is not $0$ when $v \ne 0$, so any number of bosons can share one state.

## Explanations

### L1 human

No two electrons can be in exactly the same quantum state.
The reason is that the state of several electrons must change sign when two of them are swapped.
If two of them were in the same state, swapping them would change nothing and change the sign at once, which forces the state to be zero.
This is why electrons fill shells in atoms one after another instead of all falling into the lowest level.

### L2 human

In the mathematical model, the exclusion principle is a property of exterior powers: $v \wedge v = 0$.
In second quantization it appears as the relation $a^*(f)^2 = 0$ for the fermionic [[creation operators|7N0J4DF8N5]].
A basis of the $n$-fermion space is given by Slater determinants of $n$ different one-particle basis states.
The principle underlies the stability of ordinary matter and the theory of metals and white dwarf stars.
