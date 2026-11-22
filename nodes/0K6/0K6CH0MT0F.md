---
tag: 0K6CH0MT0F
kind: concept
name: Alternating multilinear map
aliases: [alternating-form, alternating-n-linear-form]
msc: ["15A69", "15A75"]
topics: [DTBK11SR77]
audience: ug2
specializes: [0443XNARDV]
uses: [0443XNARDV, 0NZ8JA25WK, 0310REJJY8, 0CRMGPAH83]
sources:
  - url: https://en.wikipedia.org/wiki/Alternating_multilinear_map
    locator: Definition
  - url: https://en.wikipedia.org/wiki/Determinant
    locator: As an alternating multilinear form
same_as:
  wikidata: Q4736615
  wikipedia: Alternating multilinear map
---

## Summary

An alternating multilinear map is a rule that takes several vectors, is linear in each of them, and gives zero as soon as two of them are equal.
Signed area and signed volume are maps of this kind, and the [[determinant|00KDZRW4C0]] is the one that gives the unit cube volume $1$.
Let $K$ be a [[commutative ring|0310REJJY8]], let $M$ and $N$ be [[modules|0NZ8JA25WK]] over $K$, and let $n \ge 1$.
A map $f \colon M^n \to N$ is an *alternating multilinear map* when it satisfies two conditions.
First, $f$ is [[multilinear|0443XNARDV]]: it is $K$-linear in each argument when the other arguments are fixed.
Second, $f(v_1, \dots, v_n) = 0$ whenever $v_i = v_j$ for some $i \neq j$.
When $N = K$, the map is an *alternating $n$-linear form*, and the [[formal definition|0MSWYWHYF5]] states this exactly.

## Motivation

What properties does the signed area of a parallelogram have?
It is linear in each side, it is zero when the two sides are equal, and it is $1$ for the unit square.
These three properties already force the formula $u_1 v_2 - u_2 v_1$, so the formula is a consequence and not a choice.
Alternating multilinear maps are the maps with the first two properties, in any number of arguments.
They give a definition of the determinant that starts from what the determinant does, not from a formula.

The same idea appears wherever orientation and volume appear.
The [[cross product|0N5N15HWZ7]] in physics is an alternating bilinear map, and the differential forms of calculus on manifolds are alternating forms on tangent spaces.
In the sub-area on determinants, the [[existence and uniqueness theorem|1C8RRWHD45]] turns the idea into the definition of the determinant, and the theorem on [[multiplicativity|04CPJ6AF00]] is proved with it.

## Notation

The alternating $n$-linear maps $M^n \to N$ form a $K$-module, written $\operatorname{Alt}^n(M; N)$ or $L^n_a(M; N)$, and $\operatorname{Alt}^n(M)$ when $N = K$.
Some books say "skew-symmetric" or "antisymmetric" for the sign rule $f(\dots, v, \dots, w, \dots) = -f(\dots, w, \dots, v, \dots)$.
Watch out: that sign rule is weaker than "alternating" in characteristic $2$, so the two words are not synonyms.

## Remarks

### A first example: signed area

Let $\omega(u, v) = u_1 v_2 - u_2 v_1$ on $\mathbb{R}^2$.
For $u = (2, 1)$ and $v = (1, 3)$ we get
$$\omega(u, v) = 2 \cdot 3 - 1 \cdot 1 = 5, \qquad \omega(v, u) = 1 \cdot 1 - 3 \cdot 2 = -5.$$
The parallelogram with sides $u$ and $v$ has area $5$, and the sign records the order of the sides.
For the parallel pair $u = (2, 1)$ and $w = (4, 2)$ we get $\omega(u, w) = 4 - 4 = 0$, a flat parallelogram.
The [[signed area form|VFFVMRTVRZ]] checks bilinearity and the alternating property in full.

### More examples

The [[scalar triple product|059Q2XWJDC]] $(u, v, w) \mapsto u \cdot (v \times w)$ on $\mathbb{R}^3$ is trilinear and vanishes when two of the vectors are equal; the [[triple product example|DT0H0YQ4H7]] works through all three pairs.
The cross product $(u, v) \mapsto u \times v$ from $(\mathbb{R}^3)^2$ to $\mathbb{R}^3$ is alternating with values in a vector space, since $u \times u = 0$.
The determinant of the rows of an $n \times n$ matrix is an alternating $n$-linear form on $K^n$.
For $k \le n$ and fixed columns $j_1 < \dots < j_k$, the determinant of the $k \times k$ block of entries in these columns is an alternating $k$-linear form on $K^n$.

### What it is not

The [[dot product|0S52TNNTH9]] on $\mathbb{R}^2$ is bilinear but not alternating, because $e_1 \cdot e_1 = 1 \neq 0$.
The form $f(x, y) = xy$ on the field $\mathbb{F}_2$ satisfies the sign rule, because $-1 = 1$ there, but it is not alternating, because $f(1, 1) = 1$; the [[non-example over F2|QFAWSF1A04]] gives the details.
The [[permanent|X9B1XETBPF]], $ad + bc$ for a $2 \times 2$ matrix, is multilinear in the rows, but it is $2$ on the matrix with rows $(1, 1)$ and $(1, 1)$, as the [[permanent example|K9T8BNTZ2G]] explains.
The map $(u, v) \mapsto u_1 v_2 - u_2 v_1 + 1$ fails earlier: it is not multilinear, since a multilinear map is $0$ when one argument is $0$.

### The rules you can use

An alternating map changes sign when two arguments are exchanged.
To see it, expand $0 = f(x + y, x + y)$ by bilinearity in the two positions, and the two mixed terms $f(x, y) + f(y, x)$ must cancel.
Repeating this for a product of transpositions gives $f(v_{\sigma(1)}, \dots, v_{\sigma(n)}) = \operatorname{sgn}(\sigma) f(v_1, \dots, v_n)$.
The [[antisymmetry lemma|VJZVSTWYYW]] proves these rules, and also the converse when $2y = 0$ forces $y = 0$ in $N$.

An alternating map is zero on every family in which one vector is a combination of the others, so over a field it is zero on every [[linearly dependent|0CRMGPAH83]] family.
So on a vector space of dimension $n$, every alternating $k$-linear map with $k > n$ is zero.
At the top degree $k = n$, the alternating forms on $K^n$ are exactly the multiples $c \det$, a free module of rank $1$, by the [[existence and uniqueness theorem|1C8RRWHD45]].

### Watch out

Do not read "alternating" as "antisymmetric".
They agree when $2$ can be cancelled, but in characteristic $2$ the form $xy$ on $\mathbb{F}_2$ is antisymmetric and not alternating.
Do not treat a multilinear map as a linear map on $M^n$ either.
For a bilinear map, $f(2u, 2v) = 4 f(u, v)$, not $2 f(u, v)$, and in general $f(u + u', v + v') \neq f(u, v) + f(u', v')$.
Finally, the word "alternating" does not mean that the values alternate in sign; it refers to the vanishing on repeated arguments.

### History

The algebra of alternating products of vectors goes back to Grassmann's theory of extension, published in 1844.

### Try it

Is $f(u, v) = u_1 v_2 + u_2 v_1$ alternating on $\mathbb{R}^2$?
No: it is bilinear, but $f((1, 1), (1, 1)) = 2 \neq 0$.

An alternating bilinear form $f$ on $\mathbb{R}^2$ has $f(e_1, e_2) = 3$.
What is $f((1, 2), (3, 4))$?
Every such form is $3\omega$, so the value is $3 \cdot (1 \cdot 4 - 2 \cdot 3) = -6$.

## Explanations

### L1 human

An alternating map takes several arrows and gives a number, or sometimes another arrow.
If you stretch one arrow, the answer stretches by the same factor, and if one arrow is a sum, the answer is a sum too.
If two arrows are the same, the answer is zero.
The signed area of a parallelogram is the standard example.
For the sides $(2, 0)$ and $(0, 3)$ the area is $6$, and for two equal sides the parallelogram is flat and the area is $0$.

### L2 human

Here is a typical problem: find the alternating bilinear form $f$ on $\mathbb{R}^3$ with $f(e_1, e_2) = 1$, $f(e_1, e_3) = 0$ and $f(e_2, e_3) = 2$, and compute $f(u, v)$ for $u = (1, 1, 0)$ and $v = (0, 1, 1)$.
Write $u = e_1 + e_2$ and $v = e_2 + e_3$, and expand by bilinearity:
$$f(u, v) = f(e_1, e_2) + f(e_1, e_3) + f(e_2, e_2) + f(e_2, e_3) = 1 + 0 + 0 + 2 = 3.$$
The term $f(e_2, e_2)$ vanishes because $f$ is alternating.
In general the same expansion gives
$$f(u, v) = 1 \cdot (u_1 v_2 - u_2 v_1) + 0 \cdot (u_1 v_3 - u_3 v_1) + 2 \cdot (u_2 v_3 - u_3 v_2),$$
and with our vectors this is $1 \cdot 1 + 0 + 2 \cdot 1 = 3$ again.
So an alternating bilinear form on $\mathbb{R}^3$ is fixed by its three values on pairs of basis vectors, one for each choice of two coordinates.
That is the typical use: the alternating property cuts a multilinear map down to its values on increasing tuples of basis vectors.

### L3 human

The alternating $k$-linear maps $M^k \to N$ correspond to the linear maps $\Lambda^k M \to N$, where $\Lambda^k M$ is the $k$-th exterior power of $M$.
This universal property is the starting point of [[exterior algebra|3BHDPE74HF]].
For $M$ free of rank $n$, the module $\Lambda^k M$ is free of rank $\binom{n}{k}$, as the L2 problem shows for $n = 3$ and $k = 2$.
At $k = n$ the rank is $1$, and the determinant of an endomorphism is the scalar by which it acts on this line, as the page on the [[determinant of a linear map|0X0HQYSZ0K]] explains.
On manifolds, alternating forms on the tangent spaces are the differential forms, and integrating a top form generalizes the volume of a parallelotope.
