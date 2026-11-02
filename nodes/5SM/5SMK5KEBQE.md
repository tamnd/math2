---
tag: 5SMK5KEBQE
kind: statement
role: theorem
name: May recognition principle
msc: [55P47, 55P48]
uses: [T78YG90VVT, A7VB2NSGJ2, 2JFF5F3EGF, 4Q3WY1RX91]
about: [A7VB2NSGJ2, T78YG90VVT]
sources:
  - url: https://en.wikipedia.org/wiki/Infinite_loop_space_machine
---

## Statement

Let $\mathcal{O}$ be an [[$E_\infty$ operad|T78YG90VVT]], and let $X$ be an $\mathcal{O}$-algebra in spaces, with the homotopy type of a CW complex.
Suppose $X$ is grouplike: the monoid $\pi_0(X)$, with the product induced by any binary operation of $\mathcal{O}$, is a group.
Then $X$ is weakly equivalent to an [[infinite loop space|A7VB2NSGJ2]].
More precisely, there is a connective $\Omega$-spectrum $E$ with $E_0$ [[weakly equivalent|4Q3WY1RX91]] to $X$, and this equivalence is compatible with the $\mathcal{O}$-structures.

## Remarks

May proved the principle in 1972 by building the spectrum from iterated bar constructions.
The key input is his approximation theorem.
It says that, for a connected space $Y$, the free algebra on $Y$ over the little $n$-cubes operad is weakly equivalent to $\Omega^n \Sigma^n Y$.
Boardman and Vogt gave another proof with their theory of homotopy-everything spaces.
The finite version holds too: a grouplike algebra over the little $n$-cubes operad is weakly equivalent to an $n$-fold [[loop space|2JFF5F3EGF]].
If $X$ is not grouplike, the zeroth space of the spectrum is instead the group completion of $X$.

At work: the disjoint union $\coprod_{n \ge 0} B\Sigma_n$ is an algebra over the Barratt–Eccles operad, but $\pi_0 = \N$ is not a group.
Its group completion is $\Omega^\infty \Sigma^\infty S^0 = QS^0$, which is the [[Barratt–Priddy–Quillen theorem|ZD7BNADK4H]].

## Explanations

### L1 human

Infinite loop spaces carry a multiplication that is commutative and associative up to all higher homotopies.
The recognition principle says that this property characterizes them.
Any space with such a coherent multiplication, in which every element has an inverse up to homotopy, is an infinite loop space.
So to show that a space comes from a cohomology theory, it is enough to find the multiplicative structure.

### L2 human

The principle is an "infinite loop space machine": it turns $E_\infty$ spaces into spectra.
It applies to classifying spaces of symmetric monoidal categories, which is how algebraic K-theory spectra are built.
It also shows that spaces such as $BO$, $BU$ and $BTop$ are infinite loop spaces, which gives new cohomology theories and operations.
Different machines, by May, Segal and Boardman–Vogt, give equivalent spectra by the uniqueness theorem of May and Thomason.
