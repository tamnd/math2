---
tag: 2PVQY9PCT4
kind: statement
role: theorem
name: Elliptic regularity
msc: [35J15, 35B65, 35D30]
uses: [XY8GEQSWPR, SJZX81A783, M4CEZ5K9HP, C3EC148VZD, 0V33BNKZ9S]
about: [XY8GEQSWPR, SJZX81A783]
sources:
  - url: https://en.wikipedia.org/wiki/Elliptic_operator
---

## Statement

Let $U \subseteq \R^n$ be a bounded open set and let $m \ge 0$ be an integer.
Let
$$L u = -\sum_{i,j=1}^{n} \partial_j \big( a_{ij}(x) \, \partial_i u \big) + \sum_{i=1}^{n} b_i(x) \, \partial_i u + c(x) \, u,$$
where $a_{ij} = a_{ji}$, $b_i$ and $c$ are in $C^{m+1}(\overline{U})$.
Assume that $L$ is uniformly [[elliptic|XY8GEQSWPR]]: there is $\theta > 0$ with $\sum_{i,j} a_{ij}(x) \xi_i \xi_j \ge \theta \abs{\xi}^2$ for all $x \in U$ and $\xi \in \R^n$.
Let $f \in H^m(U)$, and let $u \in H^1(U)$ be a [[weak solution|SJZX81A783]] of $L u = f$ in $U$.
Here $H^k(U) = W^{k,2}(U)$ is the [[Sobolev space|M4CEZ5K9HP]] of functions on $U$ whose [[weak derivatives|C3EC148VZD]] up to order $k$ lie in $L^2(U)$.

1. Let $V$ be an open set whose closure is a compact subset of $U$. Then $u \in H^{m+2}(V)$, and
$$\norm{u}_{H^{m+2}(V)} \le C \big( \norm{f}_{H^m(U)} + \norm{u}_{L^2(U)} \big),$$
where $C$ depends only on $m$, $U$, $V$ and the coefficients of $L$.
2. If the coefficients of $L$ and $f$ are [[smooth|0V33BNKZ9S]] on $\overline{U}$, then $u$ agrees almost everywhere with a smooth function on $U$.

## Remarks

Proof idea for $m = 0$: multiply the weak form by a cut-off function and test it with difference quotients $D_k^h u$ of $u$ in the direction $e_k$.
Uniform ellipticity bounds $\norm{D_k^h \nabla u}_{L^2}$ on $V$ independently of $h$, and a uniform bound on difference quotients implies that the weak derivative $\partial_k \nabla u$ exists in $L^2(V)$.
The case of general $m$ follows by induction, since a derivative of $u$ solves an equation of the same form with a right-hand side in $H^{m-1}$.
Part 2 follows from part 1 for all $m$ together with the Sobolev embedding theorem, which puts $H^{k}$ inside $C^j$ for $k > j + n/2$.

Example: a weak solution $u \in H^1(U)$ of $\Delta u = 0$ is smooth; this is Weyl's lemma, and $u$ is then a classical harmonic function.

Ellipticity is needed.
For the wave operator $\partial_t^2 - \partial_x^2$ in the plane, $u(t, x) = \abs{x - t}$ is a weak solution of $\partial_t^2 u - \partial_x^2 u = 0$ that is not differentiable on the line $x = t$.

The regularity is local: without conditions on the boundary of $U$ and on the boundary values, $u$ need not be in $H^{m+2}(U)$ up to the boundary.
For the Dirichlet problem with $u \in H^1_0(U)$ and $\partial U$ of class $C^{m+2}$, the same conclusion holds on all of $U$.

## Explanations

### L1 human

Elliptic regularity says that solutions of elliptic equations are as smooth as the data allow, and in fact two derivatives smoother than the right-hand side.
One may first find a rough solution, defined only through integrals against test functions.
The theorem then shows that this rough solution is automatically smooth when the coefficients and the right-hand side are smooth.
For Laplace's equation, every weak solution is a genuine smooth harmonic function.

### L2 human

The standard way to solve a linear elliptic problem has two steps.
First one gets a weak solution in $H^1$ from the Lax–Milgram theorem or the Riesz representation theorem.
Then elliptic regularity upgrades it to $H^{m+2}$, and with Sobolev embeddings to a classical solution.
The same pattern holds in other function spaces: the Calderón–Zygmund estimates give the $W^{2,p}$ version for $1 < p < \infty$, and the Schauder estimates give the $C^{2,\alpha}$ version.
Hyperbolic operators have no such property, since their solutions propagate singularities of the data.
