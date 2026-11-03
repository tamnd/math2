---
tag: V0ZWMA3FTH
kind: statement
role: theorem
name: Engel's theorem
msc: [17B30, 17B05]
uses: [5JJYBJ6A8K, MEJ9PGMJ9H, 54XSPNAM1J, 063D5Z2C70, G8FEGYDSNE, WKSSTQ69AK, 0N4XY7Z3NN, 1ZAT1Z967A]
about: [MEJ9PGMJ9H]
sources:
  - url: https://en.wikipedia.org/wiki/Engel%27s_theorem
same_as:
  wikidata: Q3527069
  wikipedia: Engel's theorem
---

## Statement

Let $k$ be a field.

1. Let $V$ be a nonzero finite-dimensional vector space over $k$. Let $\mathfrak g$ be a [[Lie subalgebra|WKSSTQ69AK]] of the [[general linear Lie algebra|G8FEGYDSNE]] $\mathfrak{gl}(V)$. Assume that every element of $\mathfrak g$ is a [[nilpotent endomorphism|063D5Z2C70]] of $V$. Then there is a nonzero $v \in V$ with $x v = 0$ for all $x \in \mathfrak g$. Consequently, $V$ has a basis in which every element of $\mathfrak g$ is a strictly [[upper triangular matrix|0N4XY7Z3NN]].
2. Let $\mathfrak g$ be a finite-dimensional [[Lie algebra|5JJYBJ6A8K]] over $k$. Then $\mathfrak g$ is [[nilpotent|MEJ9PGMJ9H]] if and only if $\operatorname{ad} x \colon \mathfrak g \to \mathfrak g$, $y \mapsto [x, y]$, is a nilpotent endomorphism for every $x \in \mathfrak g$.

## Remarks

Part 1 is proved by induction on $\dim \mathfrak g$.
A maximal proper subalgebra $\mathfrak h$ of $\mathfrak g$ turns out to be an ideal of codimension $1$, so $\mathfrak g = \mathfrak h + kx$.
By induction the vectors killed by $\mathfrak h$ form a nonzero subspace $W$, and $x$ maps $W$ to itself; since $x$ is nilpotent, it kills some nonzero vector of $W$.
Part 2 follows by applying part 1 to the image of the [[adjoint representation|54XSPNAM1J]] in $\mathfrak{gl}(\mathfrak g)$ and inducting on the dimension through $\mathfrak g / Z(\mathfrak g)$.

It is not enough that a set of matrices consists of nilpotent ones.
In the [[special linear Lie algebra|1ZAT1Z967A]] $\mathfrak{sl}_2$, the matrices $e = \begin{pmatrix} 0 & 1 \\ 0 & 0 \end{pmatrix}$ and $f = \begin{pmatrix} 0 & 0 \\ 1 & 0 \end{pmatrix}$ are nilpotent, but no nonzero vector is killed by both.
The subalgebra they generate contains $[e, f] = \operatorname{diag}(1, -1)$, which is not nilpotent, so part 1 does not apply.
Also, in part 1 it is not enough that $\mathfrak g$ is a nilpotent Lie algebra.
The one-dimensional algebra spanned by the identity of $V$ is abelian, yet it kills no nonzero vector.

## Explanations

### L1 human

Engel's theorem says that nilpotence of single elements forces nilpotence of the whole algebra.
If every element of a Lie algebra of matrices is nilpotent, then in a suitable basis all of them are strictly upper triangular at once.
This is a strong conclusion, since the matrices need not commute.

### L2 human

The theorem is one of the first structural results in the theory of Lie algebras, and it holds over every field.
It gives the practical test for nilpotence: check that each $\operatorname{ad} x$ is nilpotent.
It is used in the proof of Lie's theorem and in the theory of Cartan subalgebras, which are nilpotent by definition.
It also underlies the Fitting decomposition of a module over a nilpotent Lie algebra.
For a finite-dimensional solvable Lie algebra $\mathfrak g$, it shows that $[\mathfrak g, \mathfrak g]$ is nilpotent in characteristic $0$, by combining with Lie's theorem.
