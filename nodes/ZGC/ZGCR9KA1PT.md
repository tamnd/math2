---
tag: ZGCR9KA1PT
kind: statement
role: theorem
name: Three-moment equation
msc: [74K10, 74G05]
uses: [13FGKM7NQ0, Q6XAPXMGH0, KQPKN2D1R9, 0X7EEWES5G, SKVPKD5VZN, FCGFMFM68F]
about: [Q6XAPXMGH0]
sources:
  - url: https://en.wikipedia.org/wiki/Theorem_of_three_moments
same_as:
  wikidata: Q7782348
  wikipedia: Theorem of three moments
---

## Statement

Let a continuous beam with constant bending stiffness $EI$ rest on supports $0, 1, \dots, N$ at the same level, which do not settle.
Let span $i$ run from support $i - 1$ to support $i$ and have length $L_i$, and assume the [[Euler–Bernoulli beam equation|13FGKM7NQ0]].
Let $M_i$ be the [[bending moment|Q6XAPXMGH0]] at support $i$, with sagging taken positive.
For each span $i$, let $A_i$ be the area of the moment diagram of its loads on the span taken as simply supported.
Let $a_i$ be the distance of the [[centroid|0X7EEWES5G]] of that area from support $i - 1$, and $b_i = L_i - a_i$ its distance from support $i$.
Then for each interior support $n$, with $1 \le n \le N - 1$,
$$M_{n-1} L_n + 2 M_n (L_n + L_{n+1}) + M_{n+1} L_{n+1} = -\frac{6 A_n a_n}{L_n} - \frac{6 A_{n+1} b_{n+1}}{L_{n+1}}.$$

## Remarks

The proof writes the moment in each span as the free moment plus the linear moment from the support moments.
The slope of the beam at support $n$ is then computed from the left span and from the right span, for example by the moment-area theorems.
Setting the two slopes equal, since the beam is continuous over the support, gives the equation.

Example: for a uniform load $w_i$ on span $i$, the free diagram is a parabola with $A_i = w_i L_i^3/12$ and $a_i = b_i = L_i/2$, so the right side is $-(w_n L_n^3 + w_{n+1} L_{n+1}^3)/4$.
For two equal spans $L$ with load $w$ and simply supported ends, $M_0 = M_2 = 0$ gives $4 M_1 L = -wL^3/2$, so $M_1 = -wL^2/8$, a hogging moment over the middle support.

If the supports settle or the stiffness differs between spans, extra terms appear, and the equation above is false as written.

## Explanations

### L1 human

A long beam resting on many supports, like a bridge deck on piers, cannot be solved by balancing forces alone.
This theorem gives one linear equation for each inner support, linking the bending moments at three neighbouring supports.
Solving these equations gives all the support moments, and then everything else follows by statics.

### L2 human

A continuous beam is a [[statically indeterminate structure|SKVPKD5VZN]], and the support moments are a natural choice of redundant unknowns.
The equations form a tridiagonal linear system, which is easy to solve even for many spans.
Once the $M_i$ are known, each span is a simply supported beam with known end moments, and its [[shear and moment diagram|KQPKN2D1R9]] follows by superposition.
The same equation is often derived with the [[conjugate beam method|FCGFMFM68F]].
