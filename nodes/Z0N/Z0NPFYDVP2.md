---
tag: Z0NPFYDVP2
kind: statement
role: theorem
name: Sard–Smale theorem
msc: [58C25, 58B15, 57R45]
uses: [GFXQ6HEM65, 9K15AMGBV9, GRH8MCVN3N, Z7R8J71SJN]
about: [GFXQ6HEM65]
sources:
  - url: https://en.wikipedia.org/wiki/Sard%27s_theorem
---

## Statement

Let $M$ and $N$ be [[Banach manifolds|9K15AMGBV9]], with $M$ connected and second countable.
Let $f \colon M \to N$ be a [[Fredholm map|GFXQ6HEM65]] of class $C^k$ with index $\operatorname{ind} f$, where $k > \max(\operatorname{ind} f, 0)$.
A point $y \in N$ is a *regular value* of $f$ if $d f_x$ is surjective for every $x \in f^{-1}(y)$.
Then the set of regular values of $f$ is a [[residual set|GRH8MCVN3N]] in $N$, that is, it contains a countable intersection of open dense sets.

## Remarks

The theorem is due to Smale and extends [[Sard's theorem|Z7R8J71SJN]] to infinite dimension.
Measure zero has no meaning in an infinite-dimensional Banach space, so it is replaced by the Baire notion of a residual set.
The proof is local.
Near a point $x$, the Fredholm property lets one write $f$ in charts as $(u, v) \mapsto (u, g(u, v))$, with $u$ in a Banach space and $g$ with values in a finite-dimensional space.
The critical values near $x$ are then those of finite-dimensional maps, which have measure zero by Sard's theorem.
Fredholm maps are locally proper, so the critical values coming from a small closed neighbourhood form a closed set with empty interior.
Second countability gives countably many such pieces.

At a regular value $y$, the implicit function theorem shows that $f^{-1}(y)$ is a $C^k$ submanifold of $M$ of dimension $\operatorname{ind} f$, empty if the index is negative.
Example: if $f \colon M \to N$ is a smooth map between finite-dimensional manifolds, it is Fredholm of index $\dim M - \dim N$ and the theorem reduces to Sard's theorem, with residual in place of measure zero.

## Explanations

### L1 human

Sard's theorem says that almost every value of a smooth map is regular, so that its preimage is a nice manifold.
In infinite dimension there is no good notion of volume.
For Fredholm maps one can still say that regular values are generic: they form a set that is as large as possible in the sense of Baire.

### L2 human

The theorem is the basic transversality tool of global analysis.
Take a nonlinear elliptic equation, written as $f(x) = y$ with $f$ Fredholm.
The theorem shows that for generic data $y$ the solution set is a smooth finite-dimensional manifold.
One can also apply it to the projection onto the parameter space of the zero set of a universal family $F(x, \lambda)$, where $\lambda$ is a metric or a perturbation.
This gives the parametric transversality used for moduli spaces of instantons, of pseudoholomorphic curves and of Morse flow lines.

