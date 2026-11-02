---
tag: WGBR7JHBV4
kind: statement
role: theorem
name: Post's functional completeness theorem
msc: ["06E30", 08A40, 03B05]
uses: [TDZVCWYJ9F, 0X05GS525E, 0A7KV2WB7A]
about: [TDZVCWYJ9F]
sources:
  - url: https://en.wikipedia.org/wiki/Functional_completeness
---

## Statement

Let $F$ be a set of [[Boolean functions|0X05GS525E]], that is, of operations on $\set{0, 1}$ of arity at least $1$.
Then $F$ is [[functionally complete|TDZVCWYJ9F]] if and only if $F$ has the following five properties.

1. Some $f \in F$ does not preserve $0$, that is, $f(0, \dots, 0) = 1$.
2. Some $f \in F$ does not preserve $1$, that is, $f(1, \dots, 1) = 0$.
3. Some $f \in F$ is not [[monotone|0A7KV2WB7A]] for the order $0 \le 1$ applied coordinatewise.
4. Some $f \in F$ is not self-dual, where $f$ is self-dual if $f(\neg x_1, \dots, \neg x_n) = \neg f(x_1, \dots, x_n)$ for all inputs.
5. Some $f \in F$ is not affine, where $f$ is affine if $f(x_1, \dots, x_n) = c_0 + c_1 x_1 + \cdots + c_n x_n$ modulo $2$ for some $c_i \in \set{0, 1}$.

## Remarks

Each of the five classes is a clone and does not contain all Boolean functions, so a complete $F$ cannot lie inside one of them.
The converse is the real content: these five clones are the maximal clones of [[Post's lattice|MA20X7JCET]].
One can also prove it directly by building $\neg$ and the constants from the functions that escape the first four classes, and then $\wedge$ from a non-affine function.
Example: the NAND operation $x \uparrow y = \neg(x \wedge y)$ maps $(0, 0)$ to $1$ and $(1, 1)$ to $0$.
It is not monotone, since $0 \uparrow 0 = 1 > 0 = 1 \uparrow 1$, it is not self-dual, since $0 \uparrow 1 = 1 = 1 \uparrow 0$, and it is not affine.
So $\set{\uparrow}$ is functionally complete.

## Explanations

### L1 human

The theorem gives five simple tests for a set of logic gates.
The gates can build every truth table exactly when, for each test, at least one gate fails it.
The tests ask whether gates keep all-zeros at zero, keep all-ones at one, respect the order $0 < 1$, commute with negation, or are sums modulo $2$.

### L2 human

The result comes from Emil Post's study of the lattice of clones on $\set{0, 1}$.
It is the two-element case of a general picture: a set of operations on a finite set is complete exactly when it is contained in no maximal clone.
For larger finite sets the maximal clones are listed by [[Rosenberg's classification|GF1RK91VED]], and the analogue of the theorem has more cases.
It explains at once why $\set{\wedge, \vee}$ and $\set{\wedge, \vee, \to}$ are not complete, while $\set{\to, 0}$ is, with $0$ read as a constant unary function.
