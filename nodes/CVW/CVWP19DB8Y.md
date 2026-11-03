---
tag: CVWP19DB8Y
kind: definition
name: Quine–McCluskey algorithm
msc: [94C11, "06E30", 68W40]
defines: W0HDZBF5FC
uses: [0X05GS525E, 0GVDFAY4KW, 9DMSG5HAQX]
sources:
  - url: https://en.wikipedia.org/wiki/Quine%E2%80%93McCluskey_algorithm
---

## Definition

Let $f \colon \set{0,1}^n \to \set{0,1}$ be a [[Boolean function|0X05GS525E]], given by its set $M = f^{-1}(1)$ of minterms.
A *cube* is a word $t \in \set{0, 1, -}^n$; it stands for the conjunction of $x_i$ over the positions with $t_i = 1$ and $\neg x_i$ over the positions with $t_i = 0$.
A cube is an *implicant* of $f$ if every input in it, that is, every $x$ with $x_i = t_i$ whenever $t_i \ne -$, lies in $M$.
An implicant is *prime* if replacing any of its $0$'s or $1$'s by $-$ gives a cube that is not an implicant.
The *Quine–McCluskey algorithm* is the following [[algorithm|9DMSG5HAQX]].

1. Start with the list $L_0 = M$ of minterms, viewed as cubes without dashes.
2. For $j = 0, 1, \dots$, merge any two cubes of $L_j$ that have their dashes in the same positions and differ in exactly one other position.
   The merged cube has a dash at that position; put it in $L_{j+1}$ and mark the two cubes as used.
   Stop when $L_{j+1}$ is empty.
3. The unmarked cubes of all lists are the prime implicants of $f$.
4. Choose a set of prime implicants of smallest size whose cubes together contain $M$.
   First take the essential ones, those that are the only prime implicant containing some minterm.
   Then complete the cover by exhaustive search, for example with Petrick's method.

The output is the disjunction of the chosen cubes, a [[disjunctive normal form|0GVDFAY4KW]] of $f$ with the fewest terms.

## Remarks

Example: $n = 3$ and $M = \set{001, 011, 111}$.
Merging gives $0{-}1$ from $001, 011$ and ${-}11$ from $011, 111$; these two cannot be merged, so they are the prime implicants.
Both are essential, since $001$ lies only in $0{-}1$ and $111$ only in ${-}11$.
The result is $f = (\neg x_1 \wedge x_3) \vee (x_2 \wedge x_3)$.
Non-example of a merge: $001$ and $111$ differ in two positions, and the cube ${-}{-}1$ would contain $101 \notin M$, so step 2 must not merge them.
Inputs where $f$ is unspecified (don't-cares) may be added to $M$ in steps 1 to 3 and ignored in step 4.
