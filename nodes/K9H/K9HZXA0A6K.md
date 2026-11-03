---
tag: K9HZXA0A6K
kind: statement
role: theorem
name: Korn's inequality
msc: [74B05, "46E35", 35Q74]
uses: [M4CEZ5K9HP, 1GNKQ7NBAG, 8QS6QMJF5Z, 6W00ZECYT0, 85KK79FCN5]
about: [6W00ZECYT0]
sources:
  - url: https://en.wikipedia.org/wiki/Korn%27s_inequality
same_as:
  wikidata: Q3154002
  wikipedia: Korn's inequality
---

## Statement

Let $n \ge 2$ and let $\Omega \subseteq \R^n$ be a bounded [[Lipschitz domain|1GNKQ7NBAG]].
For $u \in H^1(\Omega; \R^n)$, the [[Sobolev space|M4CEZ5K9HP]] of vector fields with square-integrable first derivatives, let $\varepsilon(u) = \tfrac12 (\nabla u + (\nabla u)^T)$ be its symmetric gradient, the [[strain tensor|8QS6QMJF5Z]].
Write $\norm{\cdot}$ for the norm of $L^2(\Omega)$.

1. (First Korn inequality) For every $u \in H^1_0(\Omega; \R^n)$, $\norm{\nabla u}^2 \le 2 \norm{\varepsilon(u)}^2$.
2. (Second Korn inequality) There is a constant $K$, depending only on $\Omega$, such that $\norm{u}_{H^1(\Omega)} \le K \big( \norm{u} + \norm{\varepsilon(u)} \big)$ for every $u \in H^1(\Omega; \R^n)$.

## Remarks

The first inequality has a short proof: for smooth $u$ with compact support, integration by parts twice gives $\int_\Omega \partial_j u_i \, \partial_i u_j = \int_\Omega (\nabla \cdot u)^2$, hence $2 \norm{\varepsilon(u)}^2 = \norm{\nabla u}^2 + \norm{\nabla \cdot u}^2 \ge \norm{\nabla u}^2$; density finishes the proof.
The second inequality is much deeper, since it controls all derivatives of $u$ by only their symmetric combinations.
Its standard proofs use the lemma that a distribution in $H^{-1}(\Omega)$ whose gradient lies in $H^{-1}(\Omega)$ belongs to $L^2(\Omega)$.
Some regularity of $\partial \Omega$ is needed for this.
On a connected $\Omega$, $\varepsilon(u) = 0$ exactly when $u(x) = a + Bx$ with $B$ skew-symmetric, an infinitesimal rigid displacement; so $\norm{u}$ cannot be dropped from the second inequality.
Combined with compactness, it gives $\norm{u}_{H^1} \le K' \norm{\varepsilon(u)}$ for all $u$ that vanish on a part of $\partial \Omega$ of positive surface measure.

## Explanations

### L1 human

The strain of a deformation measures only stretching and shearing, and it ignores rotation.
One might fear that a deformation could have small strain but large twisting gradients.
Korn's inequality says this cannot happen, apart from rigid motions of the whole body.
Small strain everywhere forces the whole gradient of the displacement to be small.

### L2 human

Korn's inequality is the key estimate in the existence theory of [[linear elasticity|6W00ZECYT0]].
The elastic energy $\int_\Omega \varepsilon(u) : C : \varepsilon(u)$ only controls the symmetric gradient, and Korn's inequality makes it coercive on $H^1$, once rigid motions are excluded by boundary conditions.
Then the [[Lax–Milgram theorem|85KK79FCN5]] gives existence and uniqueness of weak solutions of the displacement and mixed boundary value problems.
It plays the same role for the Stokes equations and in finite element error analysis for elasticity.
