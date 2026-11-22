---
tag: 0MSWYWHYF5
kind: definition
name: Alternating multilinear map
msc: ["15A69", "15A75"]
topics: [DTBK11SR77]
audience: ug2
defines: 0K6CH0MT0F
uses: [0SDMPMCN43, 09VDS2W1E8, 0GYGHKX834]
sources:
  - url: https://en.wikipedia.org/wiki/Alternating_multilinear_map
    locator: Definition
---

## Definition

We define the multilinear maps that vanish whenever two of their arguments are equal.
Let $K$ be a [[commutative ring|0GYGHKX834]], let $M$ and $N$ be [[modules|09VDS2W1E8]] over $K$, and let $n \ge 1$.
A [[multilinear map|0SDMPMCN43]] $f \colon M^n \to N$ is *alternating* when
$$f(v_1, \dots, v_n) = 0$$
for each family $(v_1, \dots, v_n)$ in $M^n$ with $v_i = v_j$ for some $i \neq j$.
When $N = K$, an alternating multilinear map is an *alternating $n$-linear form* on $M$.

## Notation

The set of alternating multilinear maps $M^n \to N$ is written $\operatorname{Alt}^n(M; N)$.
It is a $K$-module under pointwise addition and scalar multiplication, because a sum or a multiple of maps that vanish on repeated arguments also vanishes there.
For square matrices, "alternating in the rows" means alternating as a function of the $n$ rows, each row an element of $K^n$.

## Remarks

The definition has two conditions, and each one does its own work.
Multilinearity makes the map compatible with sums and multiples in each slot.
The vanishing condition is what brings in orientation: it forces a change of sign when two arguments are exchanged, as the [[antisymmetry lemma|VJZVSTWYYW]] shows.
When $K$ is a field, $M$ and $N$ are vector spaces, and this is the usual definition of linear algebra.

The condition asks for equal arguments in any two positions, not only in neighboring positions.
For a multilinear map the two versions agree.
Zero on equal neighbors already forces a sign change under each exchange of neighbors, and a sequence of such exchanges moves any repeated pair next to each other.

For an example, take $f(u, v) = u_1 v_2 - u_2 v_1$ on $\mathbb{R}^2$.
It is bilinear, and $f(u, u) = u_1 u_2 - u_2 u_1 = 0$, so it is alternating.
For a case that fails, take $g(u, v) = u_1 v_2 + u_2 v_1$.
It is bilinear, and $g(e_1, e_1) = g(e_2, e_2) = 0$, but $g((1, 1), (1, 1)) = 2$, so it is not alternating.
So a check on basis vectors alone is not enough.

The sign rule alone does not imply the vanishing condition when $2$ cannot be cancelled.
Over $\mathbb{F}_2$ the [[form xy|QFAWSF1A04]] satisfies the sign rule but is not alternating.
The concept page on [[alternating multilinear maps|0K6CH0MT0F]] gives more examples and the main properties.

## Explanations

### L1 human

An alternating map gives zero as soon as two inputs are the same.
It follows that swapping two inputs changes the sign of the value.
The signed area of the parallelogram spanned by two arrows in the plane is an alternating map of two arrows.
For $(2, 1)$ and $(1, 3)$ it is $5$, after the swap it is $-5$, and for two equal arrows it is $0$.

### L2 human

To check that a multilinear map $f$ is alternating, put the same vector $u$ in two positions and show that the value is $0$ for every $u$.
For $f(u, v) = u_1 v_2 - u_2 v_1$ this gives $u_1 u_2 - u_2 u_1 = 0$.
Watch out: testing only basis vectors is not enough, as the form $g$ above shows.
A test with $u = e_1 + e_2$ would have caught it, because $g(e_1 + e_2, e_1 + e_2) = g(e_1, e_2) + g(e_2, e_1) = 2$.

### L3 human

Alternating maps $M^n \to N$ are the same as linear maps $\Lambda^n M \to N$ from the exterior power.
In characteristic $2$ every alternating bilinear form is symmetric, but not every symmetric form is alternating, as $xy$ on $\mathbb{F}_2$ shows.
This is why the definition uses the vanishing condition and not the sign rule: it gives the right theory in every characteristic.
