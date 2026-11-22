---
tag: VJZVSTWYYW
kind: statement
role: lemma
name: Alternating multilinear maps are antisymmetric
msc: ["15A69", "15A75"]
topics: [DTBK11SR77]
audience: ug2
about: [0K6CH0MT0F]
uses: [0MSWYWHYF5, 0SK90238BH, 0515A6D2Y1, 0JB3DP1BMF, 0EVHJFTG9Z]
sources:
  - url: https://en.wikipedia.org/wiki/Alternating_multilinear_map
    locator: Properties
---

## Statement

An alternating map changes sign under every exchange of two arguments, picks up the sign of a permutation when its arguments are permuted, and vanishes on dependent families; the sign rule gives back the alternating property when $2$ can be cancelled.
Let $K$ be a commutative ring, let $M$ and $N$ be $K$-modules, and let $n \ge 2$.
Let $f \colon M^n \to N$ be multilinear, and let $v_1, \dots, v_n \in M$.

1. If $f$ is [[alternating|0MSWYWHYF5]], then exchanging two arguments changes the sign: for $i < j$,
$$f(\dots, v_j, \dots, v_i, \dots) = -f(\dots, v_i, \dots, v_j, \dots).$$
2. If $f$ is alternating, then $f(v_{\sigma(1)}, \dots, v_{\sigma(n)}) = \operatorname{sgn}(\sigma)\, f(v_1, \dots, v_n)$ for each permutation $\sigma$ in the [[symmetric group|0515A6D2Y1]] $S_n$, where $\operatorname{sgn}$ is the [[sign|0SK90238BH]].
3. If $f$ is alternating and some $v_i$ is a [[linear combination|0JB3DP1BMF]] of the other $v_k$, then $f(v_1, \dots, v_n) = 0$. When $K$ is a field, $f$ vanishes on each [[linearly dependent|0EVHJFTG9Z]] family.
4. Conversely, suppose that $f$ satisfies the sign rule of part 1, and that $2$ is a non-zero-divisor on $N$, that is, $2y = 0$ implies $y = 0$ for $y \in N$. Then $f$ is alternating.

## Remarks

### A check with numbers

Take the signed area $\omega(u, v) = u_1 v_2 - u_2 v_1$ with $u = (1, 2)$ and $v = (3, 4)$.
Then
$$\omega(u, v) = 1 \cdot 4 - 2 \cdot 3 = -2, \qquad \omega(v, u) = 3 \cdot 2 - 4 \cdot 1 = 2,$$
as part 1 says.
For part 3, take $w = 2u = (2, 4)$, so that the pair $(u, w)$ is dependent.
Linearity in the second argument gives $\omega(u, w) = 2\, \omega(u, u) = 0$.
Directly, $\omega(u, w) = 1 \cdot 4 - 2 \cdot 2 = 0$.

### Why each hypothesis is needed

Part 4 needs the condition on $2$.
Over the field $\mathbb{F}_2$ the form $f(x, y) = xy$ satisfies the sign rule, since $-xy = xy$ there, but $f(1, 1) = 1 \neq 0$; the [[non-example over F2|QFAWSF1A04]] gives the details.

Part 1 needs multilinearity.
The map $g(x, y) = (x - y)^2$ on $\mathbb{R}$ is zero on equal pairs, but $g(1, 0) = g(0, 1) = 1$, so it does not change sign.
The proof of part 1 expands $f(x + y, x + y)$, and that expansion is exactly what $g$ lacks.

### What it gives you

A swap of two rows of a matrix changes the sign of the determinant, which is one of the [[effects of row operations|09YB3WQG38]].
On a vector space of dimension $n$, every alternating $k$-linear map with $k > n$ is zero, since any $k$ vectors are then dependent.
And an alternating $n$-linear form on $K^n$ is fixed by its value on the standard basis, since part 2 turns each value on permuted basis vectors into $\pm$ that value; this is the heart of the [[existence and uniqueness theorem|1C8RRWHD45]].

### The converse of part 3

Part 4 is the converse of part 1 under the condition on $2$, and without that condition it is false.
Part 3 has no converse for a single form in general.
The form $\omega(u, v) = u_1 v_2 - u_2 v_1$ on $\mathbb{R}^3$ is zero on the independent pair $e_1, e_3$.
At the top degree the converse does hold: a nonzero alternating $n$-linear form on an $n$-dimensional vector space vanishes only on dependent families, because it is a nonzero multiple of a [[determinant in a basis|05CJSSXPR3]].

### Generalizations

Part 3 for modules that are not free uses only the linear combination, not a notion of dimension.
The same argument shows that an alternating map with values in any module vanishes on a family with a repeated vector in any two positions, whatever the order of the other arguments.

## Explanations

### L1 human

Suppose a rule gives zero whenever two inputs are equal, and grows in proportion with each input.
Then swapping two inputs changes the sign of the answer.
For the signed area of two arrows in the plane, the area of $(u, v)$ is minus the area of $(v, u)$.
For example the arrows $(1, 0)$ and $(0, 1)$ give $1 \cdot 1 - 0 \cdot 0 = 1$, and after the swap they give $0 \cdot 0 - 1 \cdot 1 = -1$.

### L2 human

Here is a typical use: how does the determinant change when the rows $r_1, r_2, r_3$ of a $3 \times 3$ matrix are reordered as $r_2, r_3, r_1$?
The reordering is the permutation $\sigma$ with $\sigma(1) = 2$, $\sigma(2) = 3$ and $\sigma(3) = 1$, a $3$-cycle.
A $3$-cycle is a product of two transpositions, for example $(1\,2\,3) = (1\,3)(1\,2)$, so $\operatorname{sgn}(\sigma) = (-1)^2 = 1$.
By part 2, the determinant does not change.
Check with $I_3$: the rows $e_2, e_3, e_1$ form a permutation matrix, and the rule of Sarrus gives the single nonzero product $a_{12} a_{23} a_{31} = 1$ on a down diagonal, so its determinant is $1$.
Watch out: in characteristic $2$ "antisymmetric" means the same as "symmetric", so the sign rule carries no information there, and only the alternating property does.

### L3 human

Part 4 shows that, away from characteristic $2$, alternating and antisymmetric multilinear maps are the same.
So in that case the exterior power can be built as the quotient of the tensor power by the antisymmetric relations $v \otimes w + w \otimes v$.
In characteristic $2$ these relations are too weak, and the correct relations are $v \otimes v = 0$, which is why the exterior algebra is defined with them.
A similar distinction appears for quadratic forms, where symmetric bilinear forms and quadratic forms no longer determine each other in characteristic $2$.
