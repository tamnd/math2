---
tag: 4P2BAT6YC3
kind: statement
role: theorem
name: Strengthened finite Ramsey theorem
msc: ["05D10", "03F30"]
topics: [T6FK1E7GJ1]
audience: grad
uses: [00TQV3F5S4, YSZ82MRXT8, 0MWKJ44V5A, MPSCREYC3M]
about: [00TQV3F5S4, YSZ82MRXT8]
history:
  first_stated: "1977"
  notes: "Paris and Harrington stated this principle in 'A mathematical incompleteness in Peano arithmetic', Handbook of Mathematical Logic (1977)."
sources:
  - wikipedia: en:3875355@r1367028911
    locator: Paris–Harrington theorem, section Strengthened finite Ramsey theorem
    note: adopted
    mention: wikipedia://en/3875355#63IX
    sections: [Statement]
  - url: https://en.wikipedia.org/wiki/Paris–Harrington_theorem
    locator: Strengthened finite Ramsey theorem
inventory: [AC9YJ8WWJ9]
---

## Statement

The strengthened finite Ramsey theorem is the finite Ramsey theorem with one extra demand: the one-colored set must have at least as many elements as its least element.
That small demand makes the theorem true but unprovable in Peano arithmetic.

For a set $S$ and $n \ge 1$, let $[S]^n$ be the set of the $n$-element subsets of $S$.
A *$k$-coloring* of $[S]^n$ is a map $c : [S]^n \to \{ 1, \dots, k \}$.
A set $Y \subseteq S$ is *homogeneous* for $c$ if $c$ is constant on $[Y]^n$.
A finite nonempty set $Y$ of positive integers is *large*, or *relatively large*, if $\lvert Y \rvert \ge \min Y$.

**Theorem** (strengthened finite Ramsey theorem, $\mathrm{PH}$).
For all positive integers $n$, $k$ and $m$ there is a positive integer $N$ with the following property.
For every $k$-coloring $c$ of $[\{ 1, \dots, N \}]^n$ there is a large homogeneous set $Y \subseteq \{ 1, \dots, N \}$ with $\lvert Y \rvert \ge m$.

The [[proof|Q0RKBRZXBD]] derives the theorem from the infinite [[Ramsey theorem|00TQV3F5S4]] by compactness.
The theorem is provable in $\mathsf{ZFC}$ and in [[second-order arithmetic|DC60FYCSPM]].
By the [[Paris-Harrington theorem|509ZWA0R26]], it is not provable in [[Peano arithmetic|MPSCREYC3M]] $\mathsf{PA}$.

## Remarks

### What "large" means

The set $\{ 3, 5, 8 \}$ is large: it has $3$ elements, and its least element is $3$.
The set $\{ 5, 8, 9 \}$ is not large: it also has $3$ elements, but its least element is $5$.
So largeness ties the size of a set to where the set starts.
A set that starts at $1$ is always large, and a set that starts at $100$ needs at least $100$ elements.

### A first case by hand

Take exponent $n = 1$, so that we color single points, with $k = 2$ colors and $m = 3$.
A set of points is homogeneous when all its points have the same color.
We show that $N = 5$ works and $N = 4$ does not.

Color each point of $\{ 1, 2, 3, 4, 5 \}$ red or blue.
By the pigeonhole principle, one color class $Y$ has $\lvert Y \rvert = j \ge 3$ points.
The least point of a $j$-element subset of $\{ 1, \dots, 5 \}$ is at most $5 - j + 1$, so:
$$\min Y \le 6 - j \le j, \quad \text{because } j \ge 3.$$
So $Y$ is a large homogeneous set with at least $3$ elements.

For $N = 4$, color $\{ 1, 2 \}$ red and $\{ 3, 4 \}$ blue.
Every homogeneous set lies inside one class, so it has at most $2$ elements, and $m = 3$ fails.
So the least $N$ for these parameters is $5$.

### Why each hypothesis is needed

The word "large" is the whole difference.
Without it, the statement is the [[finite Ramsey theorem|YSZ82MRXT8]], and $\mathsf{PA}$ proves that with explicit bounds.

The points are positive integers.
If $0$ were allowed, the set $\{ 0 \}$ would be large, and largeness would mean nothing near the bottom.

The number $k$ of colors is fixed before $N$ is chosen.
If the colors could grow with $N$, we could give each $n$-set its own color.
Then a homogeneous set has at most $n$ elements, so $m = n + 1$ fails for every $N$.

The theory must be named.
$\mathsf{PA}$ does not prove $\mathrm{PH}$, while $\mathsf{PA}$ plus the $1$-consistency of $\mathsf{PA}$ proves it, and so does $\mathsf{ZFC}$.

### What it gives you

Let $\sigma(n, k, m)$ be the least $N$ in the theorem.
The case above gives $\sigma(1, 2, 3) = 5$.
For exponent $1$ the theorem is only the pigeonhole principle, and the values are small.
As the exponent grows, $\sigma$ grows so fast that the function $x \mapsto \sigma(x, x, x)$ eventually dominates every function that $\mathsf{PA}$ [[proves total|Z742YPHPNS]].
This is the growth form of the [[Paris-Harrington theorem|509ZWA0R26]].

### The converse and generalizations

The infinite Ramsey theorem gives $\mathrm{PH}$, but $\mathrm{PH}$ does not give the infinite Ramsey theorem back.
$\mathrm{PH}$ is a true sentence of first-order arithmetic, so it holds in the model of second-order arithmetic whose sets are the computable sets.
In that model the infinite Ramsey theorem for pairs fails, because Specker gave a computable $2$-coloring of pairs with no computable infinite homogeneous set.

The [[Kanamori-McAloon theorem|NM5WYBK6BG]] is a principle of the same kind: it uses regressive colorings and min-homogeneous sets in place of largeness.
Largeness itself can be strengthened to $\lvert Y \rvert \ge g(\min Y)$ for a fixed increasing function $g$, and the compactness proof still works.

### Watch out

A common slip is to check largeness against the number $N$ or against $m$ instead of against $\min Y$.
For example, with $m = 3$ the set $\{ 4, 5, 6 \}$ has $3 \ge m$ elements, but it is not large, because $3 < 4$.
Both conditions must hold at once: $\lvert Y \rvert \ge m$ and $\lvert Y \rvert \ge \min Y$.

A second slip is to read "unprovable" as "false".
The theorem is true, and $\mathsf{ZFC}$ proves it; only $\mathsf{PA}$ fails to prove it.

### Try it

First, which of $\{ 2, 7 \}$ and $\{ 4, 5, 6 \}$ is large?
The set $\{ 2, 7 \}$ is large, since $2 \ge 2$, and $\{ 4, 5, 6 \}$ is not, since $3 < 4$.

Second, find $\sigma(1, 2, 2)$, the least $N$ for exponent $1$, two colors and $m = 2$.
For $N = 2$ the coloring $\{ 1 \}$, $\{ 2 \}$ has no homogeneous set with $2$ points.
For $N = 3$ some class has $2$ points, and its least point is at most $2$, so the answer is $3$.

## History

Jeff Paris and Leo Harrington stated this principle in 1977, in "A mathematical incompleteness in Peano arithmetic" in the Handbook of Mathematical Logic.
In the same paper they showed that it is true but not provable in $\mathsf{PA}$.

## Explanations

### L1 human

Color the numbers from $1$ to $N$, or the pairs of them, with a few colors.
Ramsey's theorem says that a big enough $N$ always gives a big group with only one color.
The strengthened form asks a little more: the group must have at least as many members as its smallest member.
A group of three numbers that starts at $2$ or $3$ is allowed, but a group of three numbers that starts at $4$ is not.
The theorem is true, but the $N$ that it needs grows so fast that ordinary arithmetic cannot prove that it always exists.

### L2 human

We find the least $N$ for exponent $1$, three colors and $m = 2$.
A homogeneous set is a set of points of one color, and we need one with at least $2$ points and least point at most its size.
For $N = 3$, the coloring that gives $1$, $2$ and $3$ three different colors has only one-point classes, so $N = 3$ fails.
For $N = 4$, four points and three colors force a class $Y$ with $\lvert Y \rvert = j \ge 2$ points.
Its least point satisfies the bound:
$$\min Y \le 4 - j + 1 = 5 - j \le 3.$$
That is not enough when $j = 2$: the coloring with classes $\{ 1 \}$, $\{ 2 \}$ and $\{ 3, 4 \}$ has only the class $\{ 3, 4 \}$ with two points, and $2 < 3$.
So $N = 4$ fails too.
For $N = 5$, either some class has $3$ points, with least point at most $3$, or two classes have $2$ points each, and the smaller of their least points is at most $2$.
In both cases a large class with at least $2$ points exists, so the least $N$ is $5$.

The problem shows how largeness pushes $N$ up: the plain pigeonhole bound would stop at $N = 4$.
The typical use of the theorem is as a test case, a short statement about finite sets whose proof needs infinite methods.

### L3 human

The theorem is a $\Pi_2$ sentence, and its truth comes from the infinite Ramsey theorem by compactness, as in the [[proof|Q0RKBRZXBD]].
The condition $\lvert Y \rvert \ge \min Y$ ties the size of a homogeneous set to its position.
In a [[non-standard model|1QWN5CV4CG]] of $\mathsf{PA}$, this lets homogeneous sets cut out initial segments that are themselves models of $\mathsf{PA}$, which is the method of [[indicators|JWTZ8NVVGK]].
Over $\mathsf{PA}$, $\mathrm{PH}$ is equivalent to the $1$-consistency of $\mathsf{PA}$, and its witness function is measured against the [[fast-growing hierarchy|R6ZC4BJGXV]] at the level $\varepsilon_0$.
