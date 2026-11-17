---
tag: THJV0NFPDQ
kind: concept
name: Physical arguments in mathematics
aliases: [mechanical-method, physical-reasoning-in-mathematics, mathematical-mechanic]
msc: ["00A35", "00A79", "70C20", "49Q05"]
topics: [DME0TPC348]
audience: ug2
uses: [8DHD3H1CJ9, 0HNK6KT05K, ZC3YKMKRGP, 0B94TKFQJX]
sources:
  - url: https://en.wikipedia.org/wiki/The_Method_of_Mechanical_Theorems
    locator: lead section
  - url: https://en.wikipedia.org/wiki/Fermat_point
    locator: lead section
  - url: https://en.wikipedia.org/wiki/Plateau%27s_problem
    locator: lead section
  - url: https://en.wikipedia.org/wiki/Mathematics_and_Plausible_Reasoning
    locator: lead section
---

## Summary

A physical argument in mathematics finds or explains a mathematical result by imagining a physical system whose laws force the result.
Typical systems are levers and weights, strings in equilibrium, soap films and electric currents.
The argument rests on two kinds of assumption: that ideal objects obey the physical laws exactly, and that an equilibrium or a minimum exists.
So a physical argument is [[plausible reasoning|8DHD3H1CJ9]], and its result needs a later mathematical [[proof|0B94TKFQJX]].
Archimedes found the volume of the sphere by balancing slices on a lever, and he then proved it by a different, geometric method.

## Motivation

Physical intuition is old and reliable in its own domain.
A body at rest is in balance, a hanging chain takes the shape of least potential energy, and a soap film shrinks to the least area it can reach.
Each of these facts turns a mathematical question into a question about a familiar system.
The system often gives the answer at once, and it sometimes shows why the answer is true.

The method also has a known weakness.
The physical system is an idealization: weightless strings, frictionless pulleys, films of zero thickness.
Its equilibrium is assumed to exist, and the assumption can be false for the mathematical problem.
The history of [[Dirichlet's principle|RKK3XHG4MR]] shows both sides: a physical argument gave the right theorem, and its proof took decades.

## Notation

Three physical principles appear in most arguments.

1. The law of the lever. Masses $m_1$ and $m_2$ at distances $d_1$ and $d_2$ on opposite sides of a fulcrum balance exactly when $m_1 d_1 = m_2 d_2$. A body acts as if its mass were at its [[centre of mass|0HNK6KT05K]].
2. The energy principle. A mechanical system with potential energy $U$ is in equilibrium at a critical point of $U$, and in stable equilibrium at a local minimum; this is the [[principle of virtual work|ZC3YKMKRGP]].
3. The balance of forces. In equilibrium, the forces on each point add up to the zero vector.

## Remarks

### Examples

1. [[Archimedes' lever argument for the volume of the sphere|QHY889QBEC]]: slices of a sphere and a cone, hung at one end of a lever, balance slices of a cylinder. The balance gives the volume $\frac43 \pi r^3$.
2. [[The Fermat point from weights on strings|1SXA826AZS]]: three equal weights on strings through holes in a table pull a knot to the point that minimizes the sum of distances to the holes. The balance of forces gives three angles of $120^\circ$.
3. Soap films. A wire frame dipped in soap solution carries a film that is a [[minimal surface|41X0YW2R9N]], at least locally. Films between two plates joined by pins show solutions of the [[Steiner tree problem|QK1AFSA023]]. Joseph Plateau's experiments led to [[Plateau's problem|DVYA6GD8RN]].
4. Electrical networks. If a resistor in a network is made larger, the current has fewer good paths, so the [[effective resistance|XAE5YJ3H68]] between two nodes cannot decrease. This is the [[Rayleigh monotonicity law|KX4152NVW8]], which also has proofs by Thomson's principle.

### Non-examples

1. [[Archimedes' quadrature of the parabola by exhaustion|SC3MSK6P4Q]]: a proof by inscribed triangles and the method of exhaustion uses only geometry. No physical law is assumed, so it is a mathematical proof and not a physical argument.
2. Applied mathematics, such as a model of the motion of a pendulum, uses mathematics to learn about a physical system. A physical argument goes in the opposite direction.
3. A measurement, such as weighing a cardboard disc to estimate $\pi$, is an experiment that gives an approximate number. It does not derive the exact result from a law.

### Basic properties

1. A physical argument proves its result only after its physical assumptions are replaced by mathematical facts.
2. The most common gap is existence. A physical system reaches some equilibrium, but the corresponding minimum of a mathematical functional may not exist.
3. An equilibrium found by balance of forces is a critical point of the energy. It need not be the global minimum, and soap films can rest in local minima.
4. The argument often contains the plan of a proof. Archimedes' balance of slices becomes an equality of integrals, and the energy principle becomes a variational argument.
5. Physical arguments work best for extremal problems and for identities between volumes, areas and moments.

### History

Archimedes described his mechanical method in a letter to Eratosthenes, now called "The Method of Mechanical Theorems".
He stated that the method gives results but does not prove them, and he proved the results by geometry in other works.
The text was lost until Johan Ludvig Heiberg identified it in 1906 in the Archimedes Palimpsest.
In the nineteenth century Joseph Plateau studied soap films experimentally, and Jesse Douglas and Tibor Radó solved Plateau's problem around 1930.
Bernhard Riemann used Dirichlet's principle, an argument from the equilibrium of heat or electricity, and Karl Weierstrass showed that the principle needs proof.
David Hilbert gave a rigorous form of it around 1900.
Pólya devoted a chapter of "Mathematics and Plausible Reasoning" to physical mathematics, and Mark Levi collected many such arguments in "The Mathematical Mechanic" (2009).

### Common errors

1. Treating the physical argument as a proof. The ideal assumptions and the existence of equilibrium must be proved.
2. Forgetting constraints of the physical model. In the Fermat point argument, the knot cannot pass through a hole, and this changes the answer when a triangle has an angle of $120^\circ$ or more.
3. Confusing a stable equilibrium with the global minimum. A soap film or a mechanical system can rest in a state of higher energy than the best one.

## Explanations

### L1 human

Sometimes a mathematical question can be answered by thinking about a machine.
Where should a warehouse go so that the total road length to three towns is smallest?
Tie three equal weights to strings, pass the strings through holes at the towns, and join them in a knot.
The knot settles where the weights are lowest, and that is where the total string length on the table is smallest.
The answer appears by itself, but a mathematician still has to prove that the machine is right.

### L2 human

We check the law of the lever with a simple balance.

1. Hang a mass of $3$ units at distance $2$ to the left of the fulcrum.
2. Hang a mass of $2$ units at distance $3$ to the right.
3. The moments are $3 \cdot 2 = 6$ and $2 \cdot 3 = 6$, so the lever balances.
4. Replace the right mass by two masses of $1$ unit at distances $2$ and $4$. The moment is $1 \cdot 2 + 1 \cdot 4 = 6$, so the lever still balances.

Step 4 shows that a body acts as if its whole mass were at its centre of mass, here at distance $3$.
The typical use: replace a body, or a family of slices, by one mass at its centre of mass.
A trap: the law holds for moments about the fulcrum; masses at the same distance on the same side add, but masses on opposite sides subtract.

### L3 human

Most physical arguments are variational.
A system in equilibrium minimizes an energy, and the mathematical content is the existence and characterization of the minimizer.
The calculus of variations turns the physical statement into an Euler-Lagrange equation, and existence needs compactness and lower semicontinuity.
Dirichlet's principle failed at exactly this point until Hilbert's work, and Plateau's problem needed new ideas for the same reason.
Archimedes' lever is an early form of the comparison of integrals: equal moments of slices at every height give equal moments of the solids.
The place of physical arguments among other plausible arguments is described in [[plausible reasoning|8DHD3H1CJ9]], and the strategies for finding them in the [[heuristics of discovery|X1NSTVGDNQ]].
