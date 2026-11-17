---
tag: 73MVVFTCY7
kind: example
name: A Herbrand model built from a finite model
msc: ["03B10"]
topics: [NJDME6F845]
audience: ug2
instance_of: [HKW429DSDK]
uses: [JAKSE2A1D4, B9C9NTWHZJ, 1WTCZB4DVB]
sources:
  - url: https://en.wikipedia.org/wiki/Herbrand_structure
    locator: lead section
---

## Example

Let $L = \set{a, f, R}$, with $a$ a constant, $f$ unary and $R$ a binary relation symbol.
Let $\Sigma = \set{\forall x \, R(x, f(x)), \ \forall x \, \neg R(x, x)}$.
The structure $\mathcal{M}$ with domain $\set{0, 1}$, $a^{\mathcal{M}} = 0$, $f^{\mathcal{M}}(n) = 1 - n$ and $R^{\mathcal{M}} = \set{(0, 1), (1, 0)}$ is a model of $\Sigma$.
We build the [[Herbrand model|JAKSE2A1D4]] of the [[theorem on Herbrand models|B9C9NTWHZJ]] and check it.

1. The Herbrand universe is $\set{f^n(a) : n \in \N}$.
2. In $\mathcal{M}$, the value of $f^n(a)$ is $n \bmod 2$, by induction on $n$, because $f^{\mathcal{M}}$ swaps $0$ and $1$.
3. The construction sets $(f^m(a), f^n(a)) \in R^{\mathcal{H}}$ if and only if $(m \bmod 2, n \bmod 2) \in R^{\mathcal{M}}$, that is, if and only if $m + n$ is odd.
4. First sentence: under $x \mapsto f^m(a)$, the term $f(x)$ has value $f^{m+1}(a)$, and $m + (m + 1) = 2m + 1$ is odd. So $R(x, f(x))$ holds for every $m$.
5. Second sentence: under $x \mapsto f^m(a)$, $R(x, x)$ would need $2m$ odd, which is false. So $\neg R(x, x)$ holds for every $m$.
6. By the clause for $\forall$ of [[satisfaction|1WTCZB4DVB]], $\mathcal{H}$ is a model of $\Sigma$.

## Remarks

The example shows that the Herbrand model can be infinite although the given model is finite: the terms $a$ and $f(f(a))$ are different, though they have the same value $0$ in $\mathcal{M}$.
The Herbrand model is not unique: the Herbrand structure with $R(f^m(a), f^n(a))$ true exactly when $n = m + 1$ is also a model of $\Sigma$.
Equality would break the construction: adding the sentence $f(f(a)) = a$, which is true in $\mathcal{M}$, gives a set with no Herbrand model.

## Explanations

### L1 human

The small world has two points, and $f$ flips them.
The world of names has infinitely many names $a, f(a), f(f(a)), \ldots$, and we relate two names when the points they name are related.
All the "for all" rules of the small world then hold in the world of names.

### L2 human

We check one instance in each structure.

1. In $\mathcal{M}$, take $x \mapsto 1$. Then $f(x)$ has value $0$, and $(1, 0) \in R^{\mathcal{M}}$.
2. In $\mathcal{H}$, the corresponding term is $f(a)$, with $m = 1$. Then $f(x)$ has value $f^2(a)$, and $1 + 2 = 3$ is odd, so $R$ holds.

The typical use is to see the proof of the theorem on a concrete case.
A trap is to define $R^{\mathcal{H}}$ by the terms alone, without the values in $\mathcal{M}$; the construction copies the atoms of $\mathcal{M}$ through the values.
