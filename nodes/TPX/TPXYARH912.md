---
tag: TPXYARH912
kind: statement
role: theorem
name: Federer–Fleming compactness theorem
msc: [49Q15, 28A75, 49Q20]
uses: [EG4AJVEFT2, Y7P66D41Z8, 360H7MD9RD, 4NKP73KVVW]
about: [EG4AJVEFT2]
sources:
  - url: https://en.wikipedia.org/wiki/Current_(mathematics)
---

## Statement

Let $0 \le m \le n$, let $K \subseteq \R^n$ be compact, and let $C > 0$.
Let $(T_j)_{j \ge 1}$ be a sequence of [[integral currents|EG4AJVEFT2]] of dimension $m$ on $\R^n$ with support in $K$.
Assume $\mathbf{M}(T_j) + \mathbf{M}(\partial T_j) \le C$ for all $j$, where $\mathbf{M}$ is the mass and $\partial T_j = 0$ when $m = 0$.
Then there are a subsequence $(T_{j_i})$ and an integral $m$-current $T$ with support in $K$ such that $\mathbf{F}(T_{j_i} - T) \to 0$, where $\mathbf{F}$ is the [[flat norm|Y7P66D41Z8]].
Moreover $\mathbf{M}(T) \le \liminf_i \mathbf{M}(T_{j_i})$ and $\mathbf{M}(\partial T) \le \liminf_i \mathbf{M}(\partial T_{j_i})$.

## Remarks

Weak convergence of a subsequence follows from the mass bound by a diagonal argument on a countable dense set of forms.
The mass is lower semicontinuous under weak convergence, because it is a supremum of the continuous functionals $T \mapsto T(\omega)$.
The hard part is the closure statement: the weak limit is again integral, and the convergence holds in the flat norm.
Federer and Fleming proved it with the deformation theorem, which pushes currents onto a cubical grid; later proofs use slicing.

Example at work: let $B$ be an integral $(m-1)$-current with compact support that is the boundary of some integral $m$-current.
A minimising sequence for the mass among integral currents with boundary $B$ can be projected into a fixed ball without increasing mass, and its boundary masses are all $\mathbf{M}(B)$.
The theorem gives a limit with boundary $B$ and least mass, an [[area-minimizing current|4NKP73KVVW]].

The bound on $\mathbf{M}(\partial T_j)$ is needed.
In $\R$, let $T_j = \sum_{i=0}^{j-1} [\![i/j, \, i/j + 1/(2j)]\!]$, integral $1$-currents in $[0, 1]$ with mass $\frac{1}{2}$ and $\mathbf{M}(\partial T_j) = 2j$.
They converge weakly to $\frac{1}{2} [\![0, 1]\!]$, which has multiplicity $\frac{1}{2}$ and is not an integral current.

## Explanations

### L1 human

Generalised surfaces with integer multiplicities, with bounded area and bounded boundary length, inside a fixed bounded region, always have a convergent subsequence.
The limit is again such a surface, and area can only drop in the limit.
This is what makes it possible to find surfaces of least area by taking limits of better and better ones.

### L2 human

The theorem is the compactness step of the direct method of the calculus of variations for currents.
Combined with lower semicontinuity of mass, it solves the Plateau problem for integral currents in every dimension and codimension.
Regularity theory, such as the results of De Giorgi, Almgren and Allard, then shows that the minimisers are smooth away from a small singular set.
The same compactness, with the flat norm, underlies the theory of flat chains and of minimal surfaces obtained by min-max methods.
