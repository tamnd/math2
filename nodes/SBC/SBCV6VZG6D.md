---
tag: SBCV6VZG6D
kind: statement
role: fact
name: Euler's laws of motion
msc: [70A05, 74A99]
uses: [X01DZTS224, HXGCGHS070, KNBP19FG6K, 7147M98XNR, 0N5N15HWZ7]
about: [X01DZTS224]
sources:
  - url: https://en.wikipedia.org/wiki/Euler%27s_laws_of_motion
same_as:
  wikidata: Q5408983
  wikipedia: Euler's laws of motion
---

## Statement

Let a [[continuum body|X01DZTS224]] move in $\R^3$ with mass density $\rho$, velocity field $v$ and body force per unit mass $b$.
Let $t(x, n)$ be its traction field of [[stress|HXGCGHS070]].
For every part of the body, let $P_t$ be the region it occupies at time $t$, with outward unit normal $n$ on $\partial P_t$.
Euler's laws of motion postulate that, for every part and every time $t$:

1. (balance of linear momentum) $$\frac{d}{dt} \int_{P_t} \rho v\, dV = \int_{\partial P_t} t(x, n)\, dA + \int_{P_t} \rho b\, dV;$$
2. (balance of angular momentum about the origin) $$\frac{d}{dt} \int_{P_t} x \times \rho v\, dV = \int_{\partial P_t} x \times t(x, n)\, dA + \int_{P_t} x \times \rho b\, dV,$$

where $\times$ is the [[cross product|0N5N15HWZ7]].

## Remarks

These are axioms of continuum mechanics, not consequences of other results; they extend [[Newton's laws of motion|KNBP19FG6K]] from point masses to bodies.
The first law says that the rate of change of the total linear momentum of a part equals the total external force on it.
The second says the same for [[angular momentum|7147M98XNR]] and torque.
For a rigid body, the first law reduces to $m\, \ddot{x}_c = F$, where $m$ is the mass, $x_c$ the centre of mass and $F$ the resultant external force.
In a point-mass theory with central forces the second law follows from the first.
For continua it is an independent postulate, and it is what makes the Cauchy stress tensor symmetric.

## Explanations

### L1 human

Euler's laws say that a body speeds up in proportion to the net force on it, and spins up in proportion to the net torque.
They apply to every piece of the body, however it is cut out.
The forces on a piece come from its neighbours, through its surface, and from outside fields such as gravity, through its volume.

### L2 human

Applied to small pieces, the first law yields Cauchy's stress theorem and then the local Cauchy momentum equation.
The second law then reduces to the symmetry of the stress tensor.
Together with conservation of mass and a constitutive equation, these laws give a closed system of field equations for the motion.
