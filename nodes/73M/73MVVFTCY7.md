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

Let $L = \{ a, f, R \}$, with $a$ a constant, $f$ unary and $R$ a binary relation symbol.
Let
$$\Sigma = \{ \forall x \, R(x, f(x)), \ \forall x \, \neg R(x, x) \}.$$
The structure $\mathcal{M}$ with domain $\{ 0, 1 \}$, $a^{\mathcal{M}} = 0$, $f^{\mathcal{M}}(n) = 1 - n$ and $R^{\mathcal{M}} = \{ (0, 1), (1, 0) \}$ is a model of $\Sigma$.
Check: $f^{\mathcal{M}}$ sends $0$ to $1$ and $1$ to $0$, and both pairs $(0, 1)$ and $(1, 0)$ lie in $R^{\mathcal{M}}$, while $(0, 0)$ and $(1, 1)$ do not.
We build the [[Herbrand model|JAKSE2A1D4]] from the proof of the [[theorem on Herbrand models|B9C9NTWHZJ]] and check it.

1. The Herbrand universe is $\{ f^n(a) : n \in \mathbb{N} \}$, since $a$ is the only constant and $f$ the only function symbol.
2. In $\mathcal{M}$, the value of $f^n(a)$ is $n \bmod 2$, by induction on $n$, because $f^{\mathcal{M}}$ swaps $0$ and $1$.
3. The construction puts $(f^m(a), f^n(a)) \in R^{\mathcal{H}}$ exactly when $(m \bmod 2, n \bmod 2) \in R^{\mathcal{M}}$.
   That happens exactly when one of $m, n$ is even and the other odd, that is, when $m + n$ is odd.
4. First sentence.
   Under $x \mapsto f^m(a)$, the term $f(x)$ has the value $f^{m+1}(a)$, and $m + (m + 1) = 2m + 1$ is odd.
   So $R(x, f(x))$ holds for every $m$.
5. Second sentence.
   Under $x \mapsto f^m(a)$, the atom $R(x, x)$ would need $m + m = 2m$ to be odd, which is false.
   So $\neg R(x, x)$ holds for every $m$.
6. Every element of $H(L)$ is some $f^m(a)$, so by the clause for $\forall$ of [[satisfaction|1WTCZB4DVB]], $\mathcal{H}$ is a model of $\Sigma$.

## Remarks

The example shows that the Herbrand model can be infinite although the given model is finite.
The terms $a$ and $f(f(a))$ are different elements of $\mathcal{H}$, though both have the value $0$ in $\mathcal{M}$.

The Herbrand model is not unique.
The Herbrand structure in which $R(f^m(a), f^n(a))$ holds exactly when $n = m + 1$ is also a model: $R(x, f(x))$ holds with $n = m + 1$, and $R(x, x)$ would need $m = m + 1$.

Equality breaks the construction.
The sentence $f(f(a)) = a$ is true in $\mathcal{M}$, but $\Sigma \cup \{ f(f(a)) = a \}$ has no Herbrand model, because $f(f(a))$ and $a$ are different terms.

## Explanations

### L1 human

The small world has two points, and $f$ flips them.
The world of names has infinitely many names $a, f(a), f(f(a))$, and so on.
We relate two names exactly when the points that they name are related.
All the "for all" rules of the small world then hold in the world of names.

### L2 human

We follow one instance of the first sentence through both structures.
In $\mathcal{M}$, take $x \mapsto 1$; then $f(x)$ has the value $0$, and $(1, 0) \in R^{\mathcal{M}}$.
In $\mathcal{H}$, the matching term is $f(a)$, with $m = 1$; then $f(x)$ has the value $f^2(a)$, and $1 + 2 = 3$ is odd, so $R$ holds.
The typical use is to see the proof of the theorem on a concrete case.
Watch out: define $R^{\mathcal{H}}$ through the values in $\mathcal{M}$, not by looking at the terms alone, because the construction copies the atoms of $\mathcal{M}$.
