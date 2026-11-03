---
tag: 11K6SVNXMH
kind: statement
role: theorem
name: Lie's theorem
msc: [17B30, 17B10]
uses: [5JJYBJ6A8K, W7A2R0GR3T, TZAZ163QGK, 0PF6TM8TWT, 1ZB13N78XW, 0N6960W0BV, 0N4XY7Z3NN]
about: [W7A2R0GR3T, TZAZ163QGK]
sources:
  - url: https://en.wikipedia.org/wiki/Lie%27s_theorem
same_as:
  wikidata: Q20971632
  wikipedia: Lie's theorem
---

## Statement

Let $k$ be an [[algebraically closed field|0PF6TM8TWT]] of [[characteristic|1ZB13N78XW]] $0$.
Let $\mathfrak g$ be a finite-dimensional [[solvable|W7A2R0GR3T]] [[Lie algebra|5JJYBJ6A8K]] over $k$.
Let $V$ be a nonzero finite-dimensional vector space over $k$, and let $\rho \colon \mathfrak g \to \mathfrak{gl}(V)$ be a [[representation|TZAZ163QGK]].
Then there are a nonzero $v \in V$ and a linear form $\lambda \colon \mathfrak g \to k$ such that $\rho(x) v = \lambda(x) v$ for all $x \in \mathfrak g$.
Consequently, $V$ has a basis in which every $\rho(x)$ is an [[upper triangular matrix|0N4XY7Z3NN]].

## Remarks

The proof is by induction on $\dim \mathfrak g$.
Choose an ideal $\mathfrak h$ of codimension $1$, which exists since $[\mathfrak g, \mathfrak g] \ne \mathfrak g$, and a common [[eigenvector|0N6960W0BV]] of $\mathfrak h$ with weight $\lambda$.
The key lemma uses characteristic $0$ through a trace argument and shows that $\lambda$ vanishes on $[\mathfrak g, \mathfrak h]$.
Then the weight space of $\lambda$ is stable under all of $\mathfrak g$.
An eigenvector in it of an element outside $\mathfrak h$ does the job.
The triangular form follows by applying the first part to $V / kv$ and inducting on $\dim V$.

Both hypotheses on $k$ are needed.
Over $\R$, the abelian Lie algebra spanned by the rotation generator $\begin{pmatrix} 0 & -1 \\ 1 & 0 \end{pmatrix}$ acting on $\R^2$ has no real eigenvector.
In characteristic $p > 0$, let $V = k^p$ with basis $e_0, \dots, e_{p-1}$, let $x e_i = i e_i$ and $y e_i = e_{i+1}$ with indices mod $p$.
Then $[x, y] = y$, so $x$ and $y$ span a solvable Lie algebra.
The eigenvectors of $x$ are the nonzero multiples of the $e_i$, and none of them is an eigenvector of $y$.

## Explanations

### L1 human

Lie's theorem says that a solvable Lie algebra of matrices over the complex numbers can be put into upper triangular form all at once.
In other words, there is one basis that works for every matrix of the algebra simultaneously.
For a single matrix this is the familiar fact that every complex matrix can be triangularized.

### L2 human

The theorem shows that the irreducible finite-dimensional representations of a solvable Lie algebra over an algebraically closed field of characteristic $0$ are one-dimensional.
Applied to the adjoint representation, it gives a chain of ideals of every dimension and shows that $[\mathfrak g, \mathfrak g]$ is nilpotent, using Engel's theorem.
It is a key step toward Cartan's criterion, the structure theory of semisimple Lie algebras and the conjugacy of Borel subalgebras.
The analogue for connected solvable linear algebraic groups is the Lie–Kolchin theorem.
