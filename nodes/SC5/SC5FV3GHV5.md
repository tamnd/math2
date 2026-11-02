---
tag: SC5FV3GHV5
kind: statement
role: theorem
name: Ladyzhenskaya–Babuška–Brezzi condition
msc: [65N30, 65N12, 76D07]
uses: [HM2HHE3J51, 0SQZMXB6GP, 86KRHS6X22, 4A82S5FVRT, 85KK79FCN5, S417YNEJ6M]
about: [87VMQ892VW]
sources:
  - url: https://en.wikipedia.org/wiki/Ladyzhenskaya%E2%80%93Babu%C5%A1ka%E2%80%93Brezzi_condition
same_as:
  wikidata: Q55648034
  wikipedia: Ladyzhenskaya–Babuška–Brezzi condition
---

## Statement

Let $V$ and $Q$ be real [[Hilbert spaces|HM2HHE3J51]].
Let $a \colon V \times V \to \R$ and $b \colon V \times Q \to \R$ be bounded [[bilinear forms|0SQZMXB6GP]], and let $f \in V'$ and $g \in Q'$, where $'$ denotes the [[continuous dual space|4A82S5FVRT]].
Consider the saddle-point problem: find $(u, p) \in V \times Q$ with
$$a(u, v) + b(v, p) = f(v) \ \text{ for all } v \in V, \qquad b(u, q) = g(q) \ \text{ for all } q \in Q.$$
Let $V_h \subseteq V$ and $Q_h \subseteq Q$ be finite-dimensional subspaces, and let $Z_h = \set{v \in V_h : b(v, q) = 0 \text{ for all } q \in Q_h}$.
Assume that there are constants $\alpha > 0$ and $\beta > 0$, independent of $h$, such that:

1. $a$ is [[coercive|86KRHS6X22]] on $Z_h$: $a(v, v) \ge \alpha \norm{v}_V^2$ for all $v \in Z_h$;
2. the inf-sup condition, or LBB condition, holds:
$$\inf_{q \in Q_h \setminus \set{0}} \ \sup_{v \in V_h \setminus \set{0}} \frac{b(v, q)}{\norm{v}_V \norm{q}_Q} \ge \beta.$$

Then the discrete problem, posed with $V_h$ and $Q_h$ in place of $V$ and $Q$, has a unique solution $(u_h, p_h)$.
If the continuous problem has a solution $(u, p)$, then
$$\norm{u - u_h}_V + \norm{p - p_h}_Q \le C \Big( \inf_{v \in V_h} \norm{u - v}_V + \inf_{q \in Q_h} \norm{p - q}_Q \Big),$$
where $C$ depends only on $\alpha$, $\beta$ and the bounds of $a$ and $b$.

## Remarks

The same two conditions with $V$, $Q$ and the [[kernel|S417YNEJ6M]] $Z = \set{v \in V : b(v, q) = 0 \text{ for all } q \in Q}$ give existence and uniqueness for the continuous problem; this is Brezzi's theorem.
The inf-sup condition says that the operator $B \colon V \to Q'$ given by $b$ maps onto $Q'$ with a bounded right inverse.
So one first finds $u_g$ with $b(u_g, q) = g(q)$ and $\norm{u_g} \le \norm{g} / \beta$.
Then one solves for $u - u_g$ in $Z$ by the [[Lax–Milgram theorem|85KK79FCN5]].
Finally one recovers $p$ from the first equation, using the inf-sup condition again.
The point of the discrete theorem is that $\beta$ does not depend on $h$; otherwise the constant $C$ can blow up as the mesh is refined.

Example: for the Stokes equations, $V = H^1_0(\Omega)^d$, $Q = L^2_0(\Omega)$, $a(u, v) = \int_\Omega \nabla u : \nabla v$ and $b(v, q) = -\int_\Omega q \, \nabla \cdot v$.
The Taylor–Hood pair, continuous piecewise quadratic velocities with continuous piecewise linear pressures, satisfies the inf-sup condition uniformly on suitable meshes.

Necessity: the pair of continuous piecewise linear velocities and pressures on a triangle mesh violates the condition.
The discrete problem then has spurious pressure modes or a constant $\beta_h$ that tends to $0$, and the computed pressure oscillates.

## Explanations

### L1 human

Some problems have two unknowns that play different roles, such as the velocity and the pressure of a slow viscous flow.
When both are approximated by finite elements, the two spaces must be balanced.
If the pressure space is too rich compared with the velocity space, the pressure is not controlled and the computation fails.
The inf-sup condition is the exact test of this balance.

### L2 human

The condition is the key stability requirement of [[mixed finite element methods|87VMQ892VW]].
It replaces the coercivity of the Lax–Milgram setting, which a saddle-point problem never has on the whole space $V \times Q$.
Checking it for a given pair of spaces is often done with a Fortin operator: a bounded projection $\Pi_h \colon V \to V_h$ with $b(v - \Pi_h v, q) = 0$ for all $q \in Q_h$.
Stable pairs include Taylor–Hood elements for Stokes flow and [[Raviart–Thomas elements|DVB79BK06Y]] with piecewise constants for the mixed Poisson problem.
