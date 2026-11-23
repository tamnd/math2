---
tag: 1CEKMPZX9P
kind: example
name: A finite full frame is descriptive
msc: ["03B45"]
topics: [SPQVNPZDTB]
audience: research
instance_of: [GGG7BB78JB]
uses: [6W9MEGN982, ZJSX7AASB4]
sources:
  - url: https://en.wikipedia.org/wiki/General_frame
    locator: Types of frames
---

## Example

Take first the frame with $W = \{0, 1\}$ and the single arrow $0 R 1$, with all four subsets admissible.
At the pair $(1, 0)$, where $1 R 0$ fails, the admissible set $\{0\}$ has $m_R(\{0\}) = \emptyset$, which does not contain $1$, so tightness holds there.

Now let $(W, R)$ be any Kripke frame with $W$ finite, and let $\mathfrak{g} = (W, R, \mathcal{P}(W))$.
We check the conditions for a [[descriptive frame|6W9MEGN982]].

1. $\mathfrak{g}$ is a general frame, by [[full frames are general frames|ZJSX7AASB4]].
2. Differentiated: if $u \neq v$, then $a = \{u\}$ contains $u$ and not $v$.
3. Tight: let $u R v$ fail, and let $a = \{v\}$.
   Then $m_R(a) = \{ w : w R v \}$, and $u \notin m_R(a)$.
4. Compact: let $\mathcal{C} \subseteq \mathcal{P}(W)$ have the finite intersection property.
   Since $\mathcal{P}(W)$ is finite, $\mathcal{C}$ is finite.
   So $\bigcap \mathcal{C}$ is the intersection of a finite subfamily, and it is nonempty.
5. So $\mathfrak{g}$ is differentiated, tight and compact, that is, descriptive.

## Remarks

The example shows that, on finite frames, Kripke semantics and descriptive frame semantics agree.
That is why completeness proofs by finite models, such as proofs by filtration, never need general frames.
In algebraic terms, every finite modal algebra is the complex algebra of the Kripke frame on its atoms, and its dual frame is that Kripke frame again.

Two changes break the example.
If $W$ is infinite, step 4 fails, and the dual of $\mathcal{P}(W)$ is the ultrafilter extension of $(W, R)$, which has more worlds.
If we keep $W$ finite but admit fewer sets, step 2 can fail: on two worlds with only $\emptyset$ and $W$ admissible, nothing separates the worlds.

## Explanations

### L1 human

A frame with finitely many points has only finitely many regions.
Compactness is a condition about infinite families of regions, and here every family is finite.
So a finite picture of points and arrows, with every region allowed, is already the best-behaved kind of general frame.

### L2 human

Take $W = \{0, 1, 2\}$ with $0 R 1$ and $1 R 2$ only, and all subsets admissible.
For tightness at the pair $(0, 2)$, take $a = \{2\}$, and compute
$$m_R(\{2\}) = \{1\},$$
which does not contain $0$.
For the pair $(2, 0)$, take $a = \{0\}$; no world sees $0$, so $m_R(\{0\}) = \emptyset$.
For compactness, a family of subsets of a three-element set has at most $8$ members, so the finite intersection property already gives a common point.
The typical use is in completeness proofs by finite models, where the finite countermodel is automatically a descriptive frame of the logic.
