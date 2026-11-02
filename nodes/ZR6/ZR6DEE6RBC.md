---
tag: ZR6DEE6RBC
kind: statement
role: theorem
name: Whitney–Graustein theorem
msc: [57R42, 53A04]
uses: [06JMR2XWXW, 0D032NSZKY, 0X7SBS8E0F, 9YA6S6HD9V]
about: [06JMR2XWXW]
sources:
  - url: https://en.wikipedia.org/wiki/Regular_homotopy
---

## Statement

Let a *regular closed curve* be a $1$-periodic map $\gamma \colon \R \to \R^2$ of class $C^1$ with $\gamma'(t) \ne 0$ for all $t$.
Its *turning number* is the degree of the map $t \mapsto \gamma'(t) / \norm{\gamma'(t)}$ from $\R / \Z$ to the unit circle.
A *regular homotopy* between $\gamma_0$ and $\gamma_1$ is a continuous family $(\gamma_u)_{u \in [0, 1]}$ of regular closed curves such that $(u, t) \mapsto \gamma_u'(t)$ is continuous.
Two regular closed curves in the plane are regularly homotopic if and only if they have the same turning number.

## Remarks

The turning number is the [[winding number|0X7SBS8E0F]] of the derivative $\gamma'$ around $0$.
It is invariant under regular homotopy, because it is an integer that depends continuously on $u$.
For the converse, one reparametrises both curves proportionally to arc length.
Their unit tangent maps have the same degree, so they are joined by a [[homotopy|9YA6S6HD9V]] of maps to the circle.
Integrating these tangent fields and correcting the closing condition gives the required family.
Example: the circle $t \mapsto (\cos 2\pi t, \sin 2\pi t)$ has turning number $1$, and the figure eight $t \mapsto (\sin 4\pi t, \sin 2\pi t)$ has turning number $0$.
So these two curves are homotopic as maps but not regularly homotopic.
The theorem was proved by Hassler Whitney in 1937, who credited the result to William Graustein.

## Explanations

### L1 human

Draw a closed loop on paper, and imagine moving it around smoothly without ever making a sharp corner.
The loop may cross itself during the motion, but its velocity must never vanish.
The theorem says that one number decides which loops can be turned into each other this way.
It is the number of full turns that the direction of the pencil makes in one trip around.

### L2 human

The theorem classifies immersions of the circle into the plane up to regular homotopy by the integer turning number.
Smale later extended this classification to immersions of spheres, which led to the eversion of the sphere.
For a regular closed curve of class $C^2$, the turning number equals the total signed curvature divided by $2\pi$.
