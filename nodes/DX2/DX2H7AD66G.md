---
tag: DX2H7AD66G
kind: concept
name: Reduction to a special case
aliases: [reduction-to-a-special-case, normalization-argument, reduction-to-normal-form]
msc: ["00A35", "26D05"]
topics: [MEKKHHQTKB, G9JFJGY4TQ]
audience: ug1
specializes: [0B94TKFQJX]
uses: [0B94TKFQJX, 2C3PAQ7H50, XNCV97HTZ8, 0WCP0PVET6, M2FAMD9HZN]
sources:
  - url: https://en.wikipedia.org/wiki/Homogeneous_function
    locator: lead section
  - url: https://en.wikipedia.org/wiki/Completing_the_square
    locator: lead section
  - book: isbn:9780691164076
    locator: Part III
---

## Summary

Reduction to a special case removes the parameters that cannot change the answer, and then proves the claim for one tidy representative.

Here is the pattern on a real goal: $\lvert u \cdot v \rvert \le \lVert u \rVert \, \lVert v \rVert$ for vectors $u$ and $v$ in $\mathbb{R}^n$.
If $u = 0$ or $v = 0$, both sides are $0$.
Otherwise, replacing $u$ by $su$ with $s > 0$ multiplies both sides by $s$, so you may assume $\lVert u \rVert = \lVert v \rVert = 1$.
For unit vectors, $0 \le \lVert u - v \rVert^2 = 2 - 2\, u \cdot v$ and $0 \le \lVert u + v \rVert^2 = 2 + 2\, u \cdot v$ give $-1 \le u \cdot v \le 1$, which is the claim.

In general, the [[proof|0B94TKFQJX]] has two steps.
First find transformations that do not change the truth of the statement, such as scaling, translation, rotation or a change of variables.
Then move every instance to a special one, a normal form, and prove the statement there, where fewer parameters remain.

## Motivation

In the Cauchy-Schwarz inequality, the lengths of $u$ and $v$ carry no information, since both sides scale in the same way.
Keeping them in the proof only hides the one step that matters.
The same happens in the general quadratic equation $ax^2 + bx + c = 0$, which a division and a translation turn into $y^2 = d$.

Typical normalizations are "the vector has length $1$", "one variable equals $1$", "the leading coefficient is $1$" and "one vertex is at the origin".
Each one makes the remaining proof shorter and puts the key step in plain view.
George Pólya lists specialization among the heuristics of problem solving: a special case that is general enough contains the whole problem.

## Notation

A normalization usually appears as an assumption: "we may assume $\lVert u \rVert = 1$" or "without loss of generality $b = 1$", as in [[a sentence using wlog|K35RJ9YHC0]].
A polynomial $f$ is [[homogeneous of degree $d$|2C3PAQ7H50]] when $f(tx) = t^d f(x)$ for every $t$ and $x$.
For a nonzero vector $u$, the unit vector $u / \lVert u \rVert$ is its [[normalization|M2FAMD9HZN]].
A substitution such as $x = y - \tfrac{b}{2a}$ comes with its inverse $y = x + \tfrac{b}{2a}$, which shows that it is a bijection.

## Remarks

### Why the reduction is valid

Let $G$ be a set of transformations of the instances, and $S$ a set of special instances.
If $P(x)$ holds exactly when $P(g(x))$ holds, for every $g \in G$, and every instance is moved into $S$ by some $g$, then $P$ on $S$ gives $P$ everywhere.
Both conditions need a check: the transformation must preserve the statement, and it must reach every instance.

For homogeneous $f$ and $g$ of the same degree $d$ and $t > 0$, $f(tx) \ge g(tx)$ is $t^d f(x) \ge t^d g(x)$, which is equivalent to $f(x) \ge g(x)$.
So it is enough to prove the inequality on the unit sphere, or with one positive variable equal to $1$.
Distances, angles and areas do not change under translations and rotations, so a proof may put one point at the origin and one line on the $x$-axis.
Reductions compose: the quadratic formula uses a division by $a$ and then a translation.

### Where the pattern appears

[[Cauchy-Schwarz by reduction to unit vectors|N8Z4J61ZHV]] works the opening goal in full.
[[A homogeneous inequality reduced to one variable|KG3RKYJRNY]] sets $b = 1$ in $a^3 + b^3 \ge a^2 b + a b^2$ and reaches $(t - 1)^2 (t + 1) \ge 0$.
[[Completing the square|XNCV97HTZ8]] turns $ax^2 + bx + c = 0$ into $y^2 = \tfrac{b^2 - 4ac}{4a^2}$, which gives [[the quadratic formula|NXNBXZWFZ1]].

The translation $x = y - \tfrac{a}{3}$ turns a [[cubic equation|T9D2XJS8NK]] $x^3 + ax^2 + bx + c = 0$ into a depressed cubic $y^3 + py + q = 0$.
The $y^2$ terms $-ay^2$ and $+ay^2$ cancel, so the [[cubic formula|FB6J5WAT5V]] needs proof for depressed cubics only.
Every triangle is the image of $(0, 0)$, $(1, 0)$, $(0, 1)$ under an affine map, which keeps lines and midpoints, so the medians meet at one point, the [[centroid|0X7EEWES5G]], because they do so at $(\tfrac13, \tfrac13)$ for that triangle.
By the [[principal axis theorem|0PR5P9Z4KM]], a rotation turns a [[quadratic form|0RBQS1JJCR]] in two variables into $\lambda_1 x^2 + \lambda_2 y^2$, so facts about [[ellipses|0VKCCEXBJ1]] can be proved for $\tfrac{x^2}{a^2} + \tfrac{y^2}{b^2} = 1$.

### When the reduction is not allowed

[[Reduction to the unit case for an inhomogeneous inequality|YQXE13QY9Z]]: $x^2 \ge x$ holds for $\lvert x \rvert = 1$, but the two sides scale differently, and the claim fails at $x = \tfrac12$.
"The three medians of a triangle have equal length" holds for an equilateral triangle, and affine maps reach every triangle, but they do not preserve length.
The triangle $(0, 0)$, $(2, 0)$, $(0, 2)$ has medians of lengths $\sqrt 2$, $\sqrt 5$ and $\sqrt 5$.
A check of "the angles of a quadrilateral add up to $2\pi$" on a square proves nothing, because no admissible transformation moves every quadrilateral to a square.

### Watch out

A reduction may miss some instances: the zero vector has no normalization, so it needs its own line, as in a [[proof by cases|0WCP0PVET6]].
One scaling fixes one quantity, so "wlog $a = b = 1$" in a homogeneous inequality in $a$ and $b$ proves only the case $a = b$.
For an odd degree $d$ and $t < 0$, the factor $t^d$ is negative and reverses an inequality, so scale only by positive numbers unless you track the sign.
Scaling an inequality whose two sides have different degrees changes the statement.

### History

Completing the square appears in a geometric form in the work of al-Khwarizmi in the ninth century.
In "Ars Magna" (1545), Gerolamo Cardano solved cubic equations, and removing the square term by a translation reduces the general cubic to a depressed one.
In "How to Solve It" (1945), George Pólya included specialization in his short dictionary of heuristics.

### Try it

Prove $a^2 + b^2 \ge 2ab$ for real $a$ and $b$ by reducing to $b = 1$.
The case $b = 0$ is $a^2 \ge 0$; otherwise divide by $b^2 > 0$ and set $t = a/b$, so the claim becomes $t^2 + 1 \ge 2t$, that is, $(t - 1)^2 \ge 0$.

Why can you not "assume $x = 1$" to prove $x^3 \ge x^2$ for $x \ge 0$?
The two sides have degrees $3$ and $2$, so scaling changes the claim, and indeed it fails at $x = \tfrac12$.

## Explanations

### L1 human

Some facts about shapes do not depend on where the shape is or how large it is.
For example, the diagonal of a square is $\sqrt 2$ times its side, whatever the size of the square.
To check such a fact, draw the square with side $1$ and one corner at the origin.
The diagonal goes from $(0, 0)$ to $(1, 1)$, and its length is $\sqrt{1 + 1} = \sqrt 2$.
A larger square is a scaled copy, and scaling multiplies the side and the diagonal by the same number.

### L2 human

We prove $x^2 + xy + y^2 \ge 0$ for all real $x$ and $y$ by reduction to $y = 1$.

1. Both sides are homogeneous of degree $2$: replacing $(x, y)$ by $(sx, sy)$ multiplies the left side by $s^2$.
2. The case $y = 0$ is $x^2 \ge 0$, and it comes first because the scaling of step 3 cannot reach it.
3. If $y \neq 0$, let $t = x / y$, so $x^2 + xy + y^2 = y^2 (t^2 + t + 1)$ with $y^2 > 0$.
   It is enough to show $t^2 + t + 1 \ge 0$, the case $y = 1$.
4. Completing the square gives $t^2 + t + 1 = (t + \tfrac12)^2 + \tfrac34 > 0$.
5. So $x^2 + xy + y^2 \ge 0$, with equality only for $x = y = 0$.

The method fits an inequality or identity with more parameters than its truth depends on.
Watch out for the instances the transformation cannot reach, such as $y = 0$ here.

### L3 human

A group $G$ acts on the set of instances, the statement $P$ is $G$-invariant, and the set $S$ meets every orbit; then $P$ on $S$ implies $P$ everywhere, and $S$ is a set of normal forms.
Linear algebra is full of such normal forms.
Statements invariant under similarity, such as the [[Cayley-Hamilton theorem|0F765KFC2J]], can be checked on the [[Jordan normal form|085HQ5G5TE]] over an algebraically closed field.
Statements about finitely generated modules over a principal ideal domain reduce to the [[Smith normal form|MV28Z5N9XX]].
In analysis, translations and dilations reduce many estimates to the unit ball, and homogeneity fixes the exponents in inequalities such as the Sobolev inequality.
The transformations are symmetries of the statement, which links the method to [[symmetry arguments|H840D9TM2X]], and the [[density argument|J2J35J3055]] reduces to a dense class instead of a normal form.
