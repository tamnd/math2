---
tag: TF4XRDB5NK
kind: statement
role: theorem
name: Bertrand's theorem
msc: [70F05, 70K42, 70H12]
uses: [APR7XN00N3, 7147M98XNR, TYXD1T6FRX, 0YG0ZJPTWG, 0AA97XA70K]
about: [APR7XN00N3]
sources:
  - url: https://en.wikipedia.org/wiki/Bertrand%27s_theorem
same_as:
  wikidata: Q2493651
  wikipedia: Bertrand's theorem
---

## Statement

Let $U \colon (0, \infty) \to \R$ be a smooth function.
Consider a particle of unit mass in $\R^3 \setminus \set{0}$ that moves in the [[central force|APR7XN00N3]] field with potential $U(\norm{x})$, that is, $x'' = - U'(\norm{x}) \, x / \norm{x}$.
Assume that some motion that is defined for all $t \in \R$ stays in a bounded set, stays away from $0$, and is not a circle.
Assume also that every motion that is defined for all $t \in \R$, stays in a bounded set and stays away from $0$ is [[periodic|0AA97XA70K]].
Then there are constants $c \in \R$ and $k > 0$ such that either $U(r) = - \frac{k}{r} + c$ for all $r > 0$, or $U(r) = k r^2 + c$ for all $r > 0$.

## Remarks

Both cases occur: for the [[Kepler problem|TYXD1T6FRX]] the bounded orbits are ellipses with a focus at $0$, and for the isotropic [[harmonic oscillator|0YG0ZJPTWG]] they are ellipses centred at $0$.
Idea of the proof: by conservation of [[angular momentum|7147M98XNR]] the motion is planar, and the radius oscillates in the effective potential $U(r) + \frac{\ell^2}{2 r^2}$, where $\ell$ is the angular momentum.
The orbit closes exactly when the angle swept between two successive pericentres is a rational multiple of $2 \pi$.
For orbits close to a stable circular orbit of radius $\rho$, this angle is $2 \pi / \sqrt{3 + \rho \, U''(\rho) / U'(\rho)}$.
By continuity it must be the same rational multiple of $2 \pi$ for all such $\rho$.
This forces $U'(r)$ to be a power $r^{\beta^2 - 3}$ times a constant, and a study of orbits with large amplitude leaves only $\beta = 1$ and $\beta = 2$.

The assumption that bounded orbits exist that are not circles is necessary.
For example, take the repulsive potential $U(r) = 1/r$.
The second derivative of $\norm{x}^2$ in time is $2 \norm{x'}^2 + 2 / \norm{x}$.
Along a motion with $\norm{x} \le R$ it would stay above $2/R$, which is impossible for all $t \in \R$, so no motion is bounded.
So the second assumption holds, but $U$ is not of the two forms with $k > 0$.

## Explanations

### L1 human

Under the gravity of a single star, a planet that stays near the star goes around on an ellipse and returns exactly to where it started.
Bertrand's theorem says that this is very rare.
Consider all forces that pull toward a centre with a strength depending only on the distance.
Only two of them have this property for every bounded orbit: the inverse-square law of gravity and the force of an ideal spring.

### L2 human

For any other central force, a typical bounded orbit is a rosette whose pericentre turns a little at each revolution and never closes.
So closed planetary orbits are a strong test of the inverse-square law.
The small observed precession of the orbit of Mercury shows that the Newtonian force of the Sun is perturbed, by the other planets and by general relativity.
In the Kepler problem the closedness of orbits is explained by the conservation of the Laplace–Runge–Lenz vector, and in the oscillator by the separation into two oscillations with equal frequency.
