---
tag: 6ZRRH96VZT
kind: statement
role: lemma
name: Nine lemma
msc: ["18G35", "18E10"]
uses: [Y9CZ3MTNF1, KJKNJMGKZZ, WV898P4X16, Q8AYGD93CW]
about: [KJKNJMGKZZ]
sources:
  - url: https://en.wikipedia.org/wiki/Nine_lemma
same_as:
  wikidata: Q2645980
  wikipedia: Nine lemma
---

## Statement

Let $\mathcal{A}$ be an [[abelian category|Y9CZ3MTNF1]], such as the category of modules over a ring.
Consider a [[commutative diagram|WV898P4X16]]
$$\begin{array}{ccccccccc} & & 0 & & 0 & & 0 & & \\ & & \downarrow & & \downarrow & & \downarrow & & \\ 0 & \to & A_1 & \to & B_1 & \to & C_1 & \to & 0 \\ & & \downarrow & & \downarrow & & \downarrow & & \\ 0 & \to & A_2 & \to & B_2 & \to & C_2 & \to & 0 \\ & & \downarrow & & \downarrow & & \downarrow & & \\ 0 & \to & A_3 & \to & B_3 & \to & C_3 & \to & 0 \\ & & \downarrow & & \downarrow & & \downarrow & & \\ & & 0 & & 0 & & 0 & & \end{array}$$
in $\mathcal{A}$ in which the three columns are [[short exact sequences|KJKNJMGKZZ]].

1. If the second and third rows are short exact, then the first row is short exact.
2. If the first and second rows are short exact, then the third row is short exact.

## Remarks

For part 1, apply the [[snake lemma|Q8AYGD93CW]] to the map from the second row to the third row given by the vertical morphisms.
Since the columns are exact, the kernels of these vertical morphisms are $A_1, B_1, C_1$ and their cokernels are $0$.
The exact sequence of the snake lemma becomes $0 \to A_1 \to B_1 \to C_1 \to 0$, which is the first row.
Part 2 is the dual statement and follows in the same way from the map from the first row to the second row, whose cokernels are $A_3, B_3, C_3$.
Example: let $A \subseteq B \subseteq C$ be modules.
Take the rows $0 \to A \to A \to 0 \to 0$, then $0 \to B \to C \to C/B \to 0$, then $0 \to B/A \to C/A \to C/B \to 0$, with the evident maps.
The columns $0 \to A \to B \to B/A \to 0$, $0 \to A \to C \to C/A \to 0$ and $0 \to 0 \to C/B \to C/B \to 0$ are short exact, and so are the first two rows.
Part 2 gives that the third row is short exact, which is the third isomorphism theorem $(C/A)/(B/A) \cong C/B$.

## Explanations

### L1 human

The nine lemma is about a three-by-three grid of objects in which every column is a short exact sequence.
If two of the rows are short exact as well, either the bottom two or the top two, then the remaining row is short exact too.
It is a bookkeeping tool: exactness in two directions propagates through the grid.

### L2 human

The lemma is also called the $3 \times 3$ lemma.
It is a quick consequence of the snake lemma, and it is used to compare filtrations and to build short exact sequences of quotients.
A typical use is the third isomorphism theorem in an abelian category.
It also appears when one shows that constructions such as the mapping cone or the total complex respect short exact sequences.
