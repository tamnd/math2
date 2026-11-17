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

For a set $S$ and $n \ge 1$, let $[S]^n$ be the set of the $n$-element subsets of $S$.
A *$k$-colouring* of $[S]^n$ is a map $c : [S]^n \to \set{1, \dots, k}$.
A set $Y \subseteq S$ is *homogeneous* for $c$ if $c$ is constant on $[Y]^n$.
A finite nonempty set $Y$ of positive integers is *large* if $\abs{Y} \ge \min Y$.

**Theorem** (strengthened finite Ramsey theorem, $\mathrm{PH}$).
For all positive integers $n$, $k$ and $m$ there is a positive integer $N$ with the following property.
For every $k$-colouring $c$ of $[\set{1, \dots, N}]^n$ there is a large homogeneous set $Y \subseteq \set{1, \dots, N}$ with $\abs{Y} \ge m$.

The [[proof|~35cec6ef]] derives it from the infinite Ramsey theorem by compactness.
The theorem is true and provable in $\mathsf{ZFC}$, and in [[second-order arithmetic|DC60FYCSPM]].
By the [[Paris-Harrington theorem|509ZWA0R26]], it is not provable in [[Peano arithmetic|MPSCREYC3M]] $\mathsf{PA}$.

## Remarks

### Why each hypothesis is needed

- The word "large" is what makes the theorem strong. Without it, the statement is the [[finite Ramsey theorem|YSZ82MRXT8]], which $\mathsf{PA}$ proves.
- The colours are on a set of *positive* integers. If $0$ were allowed, then $Y = \set{0}$ would always be large, and the condition would say nothing for $m = 1$.
- The number of colours $k$ is finite. With infinitely many colours, the colouring that gives every $n$-set its own colour has no homogeneous set of size $n + 1$.
- The theory matters: $\mathsf{PA}$ does not prove $\mathrm{PH}$, but $\mathsf{PA}$ plus the $1$-consistency of $\mathsf{PA}$ proves it, and so does $\mathsf{ZFC}$.

### Consequences

- For $n = 1$, $k = 2$ and $m = 3$, the least $N$ is $5$. If $\set{1, \dots, 5}$ has two colours, one colour class $Y$ has at least $3$ points, and its least point is at most $3 \le \abs{Y}$.
- For $N = 4$ the colouring with classes $\set{1, 2}$ and $\set{3, 4}$ has no homogeneous set with $3$ points, so $N = 4$ is too small.
- The least $N$, as a function of $n$, $k$ and $m$, grows faster than every function that $\mathsf{PA}$ proves total. This is the content of the [[Paris-Harrington theorem|509ZWA0R26]].

### Converse

The converse, from $\mathrm{PH}$ back to the infinite Ramsey theorem, is false in a precise sense.
$\mathrm{PH}$ is a true sentence of first-order arithmetic, so it holds in the world of computable sets.
There the infinite Ramsey theorem for pairs fails, because Specker gave a computable colouring of pairs with no computable infinite homogeneous set.

### Generalizations

- The [[Kanamori-McAloon theorem|~53c52c9d]] replaces "large" by min-homogeneity for regressive colourings, and it is also unprovable in $\mathsf{PA}$.
- "Large" can be replaced by other notions of largeness of finite sets, for example $\abs{Y} \ge f(\min Y)$ for a fixed function $f$.

## History

Jeff Paris and Leo Harrington stated this principle in 1977, in "A mathematical incompleteness in Peano arithmetic" in the Handbook of Mathematical Logic.
They showed in the same paper that it is true but not provable in $\mathsf{PA}$.

## Explanations

### L1 human

Colour the numbers from $1$ to $N$, or the pairs of them, with a few colours.
Ramsey's theorem says that a big enough $N$ always gives a large group with only one colour.
The strengthened form asks a little more: the group must have at least as many members as its smallest member.
For example a group of three numbers that starts at $2$ or $3$ is allowed, but a group of three numbers that starts at $4$ is not.
The theorem is true, but the $N$ that it needs grows so fast that ordinary arithmetic cannot prove that it exists.

### L2 human

A worked check for $n = 1$, $k = 2$ and $m = 3$, where a colouring of $1$-element sets is a colouring of points.

1. Let $N = 5$, and colour each point of $\set{1, 2, 3, 4, 5}$ red or blue.
2. One colour class $Y$ has at least $3$ points, by the pigeonhole principle.
3. Every subset of a colour class is homogeneous, because $n = 1$.
4. The class $Y$ has at least $3$ points among $5$, so its least point is at most $5 - \abs{Y} + 1 \le \abs{Y}$. So $Y$ is large.
5. For $N = 4$, the classes $\set{1, 2}$ and $\set{3, 4}$ have only $2$ points each, so no homogeneous set has $3$ points.

The typical use of the theorem is as a test case: a short statement about finite sets that needs infinite methods.
The trap: "unprovable" here means unprovable in $\mathsf{PA}$, not false and not unprovable in $\mathsf{ZFC}$.

### L3 human

The theorem is a $\Pi_2$ sentence, and its truth comes from the infinite [[Ramsey theorem|00TQV3F5S4]] by compactness, as in the [[proof|~35cec6ef]].
The condition $\abs{Y} \ge \min Y$ ties the size of a homogeneous set to its position, and this lets homogeneous sets in non-standard models define initial segments that are models of $\mathsf{PA}$.
This is the start of the method of [[indicators|~1d28aa25]].
Over a weak base theory $\mathrm{PH}$ is equivalent to the $1$-consistency of $\mathsf{PA}$, and its least witness grows like the function $f_{\varepsilon_0}$ of the [[fast-growing hierarchy|~24c8db71]].
