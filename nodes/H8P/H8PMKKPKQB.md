---
tag: H8PMKKPKQB
kind: example
name: The liar in first-degree entailment fixed points
aliases: [fde-liar]
msc: ["03A05", "03B53"]
topics: [6Q4JJ2MMV8]
audience: grad
instance_of: [WH94DG6D3Q]
illustrates: [4CBCWZQZ12]
uses: [AWEG5PR3GF, XRRGJK0927, 4204V9JTCV, SFPSB6JPTC]
sources:
  - url: https://plato.stanford.edu/entries/liar-paradox/
    locator: "Liar Paradox, 4.1.2 Paraconsistent"
  - url: https://plato.stanford.edu/entries/logic-manyvalued/
    locator: 2.3 True, False, Neither, and Both
---

## Example

We use the four values $\mathbf{T}, \mathbf{F}, \mathbf{B}, \mathbf{N}$ of [[first-degree entailment|AWEG5PR3GF]].
Here $\neg$ swaps $\mathbf{T}$ and $\mathbf{F}$, and it fixes $\mathbf{B}$ and $\mathbf{N}$.
An *FDE interpretation* is any pair $(E, A)$ of subsets of $\mathbb{N}$.
Let $n$ be the value of the term $t$.
Then $\|T(t)\|$ is $\mathbf{T}$ if $n \in E \setminus A$, $\mathbf{F}$ if $n \in A \setminus E$, $\mathbf{B}$ if $n \in E \cap A$, and $\mathbf{N}$ otherwise.
The jump puts $\ulcorner \varphi \urcorner$ into $E$ if $T \in \|\varphi\|$ and into $A$ if $F \in \|\varphi\|$, and it puts all non-sentences into $A$.
Let $\lambda$ be the liar from the [[proof of the diagonal lemma|SFPSB6JPTC]], and let $(E, A)$ be a fixed point.

1. $\|\lambda\| = \neg \|T(\ulcorner \lambda \urcorner)\|$, since $D(\underline{k}, m)$ is true only for $m = \ulcorner \lambda \urcorner$.
2. In a fixed point, $\|T(\ulcorner \lambda \urcorner)\| = \|\lambda\|$, by the definition of the jump.
3. So $v := \|\lambda\|$ satisfies $v = \neg v$.
4. $\neg \mathbf{T} = \mathbf{F} \ne \mathbf{T}$ and $\neg \mathbf{F} = \mathbf{T} \ne \mathbf{F}$. So $v \in \{\mathbf{B}, \mathbf{N}\}$: the liar is a glut or a gap.
5. *A fixed point with a gap.* Take the least Kripke fixed point. Its pair is disjoint, and on $\{\mathbf{T}, \mathbf{N}, \mathbf{F}\}$ the FDE tables are the strong Kleene tables.
6. So it is an FDE fixed point, and the liar has value $\mathbf{N}$ there, by [[this example|XRRGJK0927]].
7. *A fixed point with a glut.* Take an LP fixed point. Its pair covers $\mathbb{N}$, and on $\{\mathbf{T}, \mathbf{B}, \mathbf{F}\}$ the FDE tables are the LP tables.
8. So it is an FDE fixed point, and the liar has value $\mathbf{B}$ there, by [[this example|4204V9JTCV]].
9. So in FDE the liar is never classical, and it is a [[glut|WH94DG6D3Q]] in some fixed points and a [[gap|4CBCWZQZ12]] in others.

## Remarks

The SEP entry notes that paracomplete and paraconsistent approaches are compatible.
It names an FDE-based transparent truth theory, with neither excluded middle nor explosion, and it names Visser (1984) and Woodruff (1984) among others.
Step 4 is the whole reason that the liar has no classical value in any of these semantics.
The choice between gap and glut is then a choice of fixed point.

## Explanations

### L1 human

First-degree entailment has four values: true, false, both, and neither.
The liar must have the same value as its own negation.
Only "both" and "neither" are equal to their negation.
So the liar is both or neither, and different models choose differently.

### L2 human

1. Compute $\neg$ on each value: $\neg \mathbf{T} = \mathbf{F}$, $\neg \mathbf{F} = \mathbf{T}$, $\neg \mathbf{B} = \mathbf{B}$, $\neg \mathbf{N} = \mathbf{N}$.
2. The fixed values of $\neg$ are $\mathbf{B}$ and $\mathbf{N}$.
3. The liar needs a fixed value of $\neg$, so its value is $\mathbf{B}$ or $\mathbf{N}$.

The typical use is to compare the gap view and the glut view in one framework.
The trap is to think that the four-valued framework decides between them; it allows both.
