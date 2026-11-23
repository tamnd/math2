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

A physical argument finds a mathematical result by imagining a machine whose laws force the result.
It often gives the answer fast and shows why it is true, and it still needs a mathematical proof afterwards.

Archimedes found the volume of a sphere with a lever.
Put a sphere of radius $r$ on an axis from $x = 0$ to $x = 2r$, next to a cone with its apex at $0$ and a base of radius $2r$ at $x = 2r$, and a cylinder of radius $2r$ over the same interval.
At distance $x$ from $0$, the slices have areas
$$\text{sphere: } \pi x (2r - x), \qquad \text{cone: } \pi x^2, \qquad \text{cylinder: } 4 \pi r^2.$$
Hang the sphere slice and the cone slice at distance $2r$ on the other side of a fulcrum at $0$, and leave the cylinder slice where it is, at distance $x$.
The moments balance, since
$$2r \cdot \pi \bigl( x(2r - x) + x^2 \bigr) = 4 \pi r^2 x = x \cdot 4 \pi r^2.$$
Add over all slices, and put the whole cylinder at its center of mass, at distance $r$:
$$2r \left( V_{\text{sphere}} + \frac{8 \pi r^3}{3} \right) = r \cdot 8 \pi r^3, \qquad V_{\text{sphere}} = \frac{4}{3} \pi r^3.$$
Archimedes wrote that this method finds results but does not prove them, and he proved them by geometry in other works.

Typical machines in such arguments are levers and weights, strings in balance, soap films and electric currents.
The argument rests on two kinds of assumption: that ideal objects obey the physical laws exactly, and that a balance or a minimum exists.
So a physical argument is [[plausible reasoning|8DHD3H1CJ9]], and its result needs a later [[proof|0B94TKFQJX]].

## Motivation

Physical intuition is old and reliable in its own domain.
A body at rest is in balance, a hanging chain takes the shape of least potential energy, and a soap film shrinks to the least area it can reach.
Each of these facts turns a mathematical question into a question about a familiar system.
The system often gives the answer at once, and sometimes it shows why the answer is true.

The method also has a known weakness.
The physical system is an ideal one: strings without weight, pulleys without friction, films without thickness.
Its balance is assumed to exist, and the assumption can be false for the mathematical problem.
The history of [[Dirichlet's principle|RKK3XHG4MR]] shows both sides: a physical argument gave the right theorem, and its proof took about fifty years.

## Notation

Three physical principles appear in most arguments.
The law of the lever says that masses $m_1$ and $m_2$ at distances $d_1$ and $d_2$ on opposite sides of a fulcrum balance exactly when $m_1 d_1 = m_2 d_2$, and a body acts as if its mass were at its [[center of mass|0HNK6KT05K]].
The energy principle says that a mechanical system is in balance at a critical point of its potential energy, and in stable balance at a local minimum; this is the [[principle of virtual work|ZC3YKMKRGP]].
The balance of forces says that in balance the forces on each point add up to the zero vector.

## Remarks

### Levers and strings

[[Archimedes' lever argument for the volume of the sphere|QHY889QBEC]] gives the full argument of the Summary, slice by slice.
[[The Fermat point from weights on strings|1SXA826AZS]] uses strings instead.
Three equal weights hang on strings through three holes in a table, and the strings are tied in one knot.
The knot settles where the sum of its distances to the holes is least, and the balance of three equal forces gives three angles of $120^\circ$ at the knot.

### Films and currents

A wire frame dipped in soap solution carries a film that is a [[minimal surface|41X0YW2R9N]], at least locally.
Films between two plates joined by pins show solutions of the [[Steiner tree problem|QK1AFSA023]], and Joseph Plateau's experiments led to [[Plateau's problem|DVYA6GD8RN]].

In an electrical network, a larger resistor leaves the current fewer good paths, so the [[effective resistance|XAE5YJ3H68]] between two nodes cannot decrease.
That is the [[Rayleigh monotonicity law|KX4152NVW8]], which also has a proof from Thomson's principle.

### What it is not

[[Archimedes' quadrature of the parabola by exhaustion|SC3MSK6P4Q]] is a proof by inscribed triangles and the method of exhaustion.
It assumes no physical law, so it is a mathematical proof and not a physical argument.
Applied mathematics, such as a model of a pendulum, uses mathematics to learn about a physical system, which is the opposite direction.
A measurement, such as weighing a cardboard disc to estimate $\pi$, gives an approximate number and derives nothing exact from a law.

### The rules you can use

A physical argument proves its result only after its physical assumptions are replaced by mathematical facts.
The most common gap is existence: a physical system reaches some balance, but the minimum of the corresponding mathematical functional may not exist.
A balance found from forces is a critical point of the energy, and it need not be the global minimum, since soap films can rest in local minima.
The argument often contains the plan of a proof: Archimedes' balance of slices becomes an equality of integrals, and the energy principle becomes a variational argument.

### Watch out

A physical argument is not a proof, however convincing the machine is.

Remember the constraints of the model.
In the Fermat point argument the knot cannot pass through a hole, and when a triangle has an angle of $120^\circ$ or more, the knot stops at that corner and the three angles of $120^\circ$ never appear.

Do not confuse a stable balance with the global minimum.
A soap film or a mechanical system can rest in a state of higher energy than the best one.

### History

Archimedes described his mechanical method in a letter to Eratosthenes, now called *The Method of Mechanical Theorems*.
The text was lost until Johan Ludvig Heiberg identified it in 1906 in the Archimedes Palimpsest.
In the nineteenth century Plateau studied soap films by experiment, and Jesse Douglas and Tibor Radó solved Plateau's problem around 1930.
Bernhard Riemann used Dirichlet's principle, Karl Weierstrass showed that it needs a proof, and David Hilbert gave it a rigorous form around 1900.
Pólya gave a chapter of *Mathematics and Plausible Reasoning* to physical mathematics, and Mark Levi collected many such arguments in *The Mathematical Mechanic* (2009).

### Try it

A mass of $3$ sits at distance $2$ to the left of a fulcrum; where must a mass of $4$ sit on the right?
It needs $4 d = 3 \cdot 2$, so $d = 1.5$.

Check the balance of slices at $x = r$ in the Summary.
The sphere slice has area $\pi r^2$ and the cone slice $\pi r^2$, so the left moment is $2r \cdot 2\pi r^2 = 4 \pi r^3$, and the cylinder slice gives $r \cdot 4 \pi r^2 = 4 \pi r^3$.

## Explanations

### L1 human

Sometimes a mathematical question can be answered by thinking about a machine.
Where should a warehouse go so that the total road length to three towns is least?
Tie three equal weights to strings, pass the strings through holes at the towns, and join them in a knot.
The knot settles where the weights hang lowest, and that is where the total string length on the table is least.
The answer appears by itself, but a mathematician still has to prove that the machine is right.

### L2 human

We check the law of the lever with a simple balance.
Hang a mass of $3$ units at distance $2$ to the left of the fulcrum, and a mass of $2$ units at distance $3$ to the right.
The moments are $3 \cdot 2 = 6$ and $2 \cdot 3 = 6$, so the lever balances.
Now replace the right mass by two masses of $1$ unit at distances $2$ and $4$.
The moment is $1 \cdot 2 + 1 \cdot 4 = 6$, so the lever still balances.
This shows that a body acts as if its whole mass were at its center of mass, here at distance $3$.

The typical use: replace a body, or a family of slices, by one mass at its center of mass, as Archimedes did with the cylinder.
Watch out: masses on the same side add their moments, but masses on opposite sides subtract.

### L3 human

Most physical arguments are variational.
A system in balance minimizes an energy, and the mathematical content is the existence and description of the minimizer.
The calculus of variations turns the physical statement into an Euler-Lagrange equation, and existence needs compactness and lower semicontinuity.
Dirichlet's principle failed at exactly this point until Hilbert's work, and Plateau's problem needed new ideas for the same reason.
Archimedes' lever is an early form of the comparison of integrals: equal moments of slices at every height give equal moments of the solids.
Physical arguments sit next to the other sources of belief in [[plausible reasoning|8DHD3H1CJ9]], and the strategies for finding them are among the [[heuristics of discovery|X1NSTVGDNQ]].
