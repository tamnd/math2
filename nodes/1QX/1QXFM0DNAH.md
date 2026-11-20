---
tag: 1QXFM0DNAH
kind: example
name: Applications of linear systems
msc: ["15A06", "15A99", "91B66"]
topics: [K0FNC6CWZN]
audience: school
instance_of: [0GT4WWGWH2]
illustrates: [PDH3HKXWAZ, ACDFDABVQK]
uses: [0GT4WWGWH2, 0JVJ2WCXZH, 04KGXJG1A2, KQT68YPHD1, 0PHDYNR24D, 8XWC7RKNN1]
sources:
  - book: isbn:9780321982384
    locator: Section 1.6
  - book: isbn:9780321982384
    locator: Section 2.6
  - url: https://en.wikipedia.org/wiki/Kirchhoff%27s_circuit_laws
    locator: lead section
  - url: https://en.wikipedia.org/wiki/Chemical_equation
    locator: Balancing chemical equations
  - url: https://en.wikipedia.org/wiki/Input%E2%80%93output_model
    locator: Origins
---

## Example

We model four problems from outside mathematics as [[systems of linear equations|0GT4WWGWH2]] and solve each one.
In each problem, one linear equation expresses one rule of balance: what goes in equals what goes out.
The four problems are a traffic network, an electric circuit, a chemical reaction and an economy with two sectors.

**Part 1: traffic in a network of one-way streets.**
Four one-way streets go around a block, with the intersections $A$, $B$, $C$, $D$ in clockwise order.
Let $x_1, x_2, x_3, x_4$ be the flows, in cars per hour, on the streets $A \to B$, $B \to C$, $C \to D$ and $D \to A$.
Outside streets bring $400$ cars per hour into $A$, $200$ into $B$ and $300$ into $D$.
Outside streets take $500$ cars per hour out of $B$, $300$ out of $C$ and $100$ out of $D$.
At each intersection, the flow in equals the flow out.

1. At $A$: $400 + x_4 = x_1$, so $x_1 - x_4 = 400$.
2. At $B$: $x_1 + 200 = x_2 + 500$, so $x_1 - x_2 = 300$.
3. At $C$: $x_2 = x_3 + 300$, so $x_2 - x_3 = 300$.
4. At $D$: $x_3 + 300 = x_4 + 100$, so $x_3 - x_4 = -200$.
5. [[Gaussian elimination|0JVJ2WCXZH]]: steps 1 and 2 give $x_2 = x_1 - 300$, and with step 1 this is $x_2 = x_4 + 100$.
6. Step 3 then gives $x_3 = x_2 - 300 = x_4 - 200$.
7. Step 4 becomes $(x_4 - 200) - x_4 = -200$, which is true for every $x_4$. So the four equations have rank $3$, and $x_4$ is a free variable.
8. In [[parametric form|KQT68YPHD1]], with $x_4 = t$, the solutions are $(x_1, x_2, x_3, x_4) = (400, 100, -200, 0) + t (1, 1, 1, 1)$.
9. The vector $(1, 1, 1, 1)$ spans the [[null space|0PHDYNR24D]] of the coefficient matrix: extra cars that drive around the block change no balance.
10. A flow on a one-way street cannot be negative. The condition $x_3 = t - 200 \ge 0$ gives $t \ge 200$, and then the other three flows are positive.
11. So the flow on the street $D \to A$ is at least $200$ cars per hour. For $t = 200$ the flows are $(600, 300, 0, 200)$.
12. Check for $t = 200$: $600 - 200 = 400$, $600 - 300 = 300$, $300 - 0 = 300$ and $0 - 200 = -200$.

**Part 2: currents in an electric circuit.**
Two junctions $P$ and $Q$ are joined by three branches.
The left branch has a $12$ V battery and a $2\ \Omega$ resistor, and its current $I_1$ flows from $Q$ to $P$.
The right branch has a $6$ V battery and a $2\ \Omega$ resistor, and its current $I_2$ flows from $Q$ to $P$.
The middle branch has a $4\ \Omega$ resistor, and its current $I_3$ flows from $P$ to $Q$.
Both batteries push current towards $P$.
[[Kirchhoff's circuit laws|9B0V41V2F8]] give the equations: the current law at a junction, and the voltage law around a closed loop with Ohm's law $V = RI$.

1. The current law at $P$: $I_1 + I_2 = I_3$, so $I_1 + I_2 - I_3 = 0$.
2. The voltage law on the loop of the left and middle branches: $2 I_1 + 4 I_3 = 12$.
3. The voltage law on the loop of the right and middle branches: $2 I_2 + 4 I_3 = 6$.
4. In matrix form:
$$\begin{pmatrix} 1 & 1 & -1 \\ 2 & 0 & 4 \\ 0 & 2 & 4 \end{pmatrix} \begin{pmatrix} I_1 \\ I_2 \\ I_3 \end{pmatrix} = \begin{pmatrix} 0 \\ 12 \\ 6 \end{pmatrix}.$$
5. Steps 2 and 3 give $I_1 = 6 - 2 I_3$ and $I_2 = 3 - 2 I_3$.
6. Put these into step 1: $(6 - 2 I_3) + (3 - 2 I_3) = I_3$, so $9 = 5 I_3$ and $I_3 = 1.8$ A.
7. Then $I_1 = 6 - 3.6 = 2.4$ A and $I_2 = 3 - 3.6 = -0.6$ A.
8. Check: $2.4 - 0.6 - 1.8 = 0$, $2 \cdot 2.4 + 4 \cdot 1.8 = 12$ and $2 \cdot (-0.6) + 4 \cdot 1.8 = 6$.
9. The determinant of the matrix is $1 \cdot (0 - 8) - 1 \cdot (8 - 0) + (-1) \cdot (4 - 0) = -20 \ne 0$. So the solution is unique, by the [[invertible matrix theorem|ACDFDABVQK]].
10. The sign of $I_2$ is negative. So the current in the right branch flows from $P$ to $Q$, against the push of its own battery.

**Part 3: balancing a chemical equation.**
Propane burns in oxygen and gives carbon dioxide and water:
$$x_1\, \mathrm{C_3H_8} + x_2\, \mathrm{O_2} \to x_3\, \mathrm{CO_2} + x_4\, \mathrm{H_2O}.$$
We want positive integers $x_1, x_2, x_3, x_4$ such that each element has the same number of atoms on the two sides.

1. Carbon: $3 x_1 = x_3$.
2. Hydrogen: $8 x_1 = 2 x_4$.
3. Oxygen: $2 x_2 = 2 x_3 + x_4$.
4. This is the [[homogeneous system|04KGXJG1A2]] $M x = 0$ with
$$M = \begin{pmatrix} 3 & 0 & -1 & 0 \\ 8 & 0 & 0 & -2 \\ 0 & 2 & -2 & -1 \end{pmatrix}.$$
5. Take $x_1 = t$. Step 1 gives $x_3 = 3t$, step 2 gives $x_4 = 4t$, and step 3 gives $x_2 = (6t + 4t)/2 = 5t$.
6. So the null space of $M$ is the line spanned by $(1, 5, 3, 4)$, and $M$ has rank $3$.
7. The smallest positive integer solution is $t = 1$: $\mathrm{C_3H_8} + 5\, \mathrm{O_2} \to 3\, \mathrm{CO_2} + 4\, \mathrm{H_2O}$.
8. Check: carbon $3 = 3$, hydrogen $8 = 4 \cdot 2$, oxygen $5 \cdot 2 = 3 \cdot 2 + 4$.

**Part 4: the input-output model of an economy with two sectors.**
An economy has two sectors, manufacturing and services.
To make one unit of output, manufacturing uses $0.5$ unit of manufacturing and $0.25$ unit of services.
To make one unit of output, services use $0.2$ unit of manufacturing and $0.4$ unit of services.
The consumers outside the two sectors demand $d = (50, 30)$ units.
We want the total output $x = (x_1, x_2)$ that covers the needs of the two sectors and the outside demand.
This is the [[input-output model|PF15E9SVQV]], with the consumption matrix $C$ whose column $j$ lists the inputs for one unit of sector $j$.

1. The consumption matrix is $C = \begin{pmatrix} 0.5 & 0.2 \\ 0.25 & 0.4 \end{pmatrix}$.
2. Output equals internal use plus outside demand: $x = C x + d$. So $(I - C) x = d$.
3. $I - C = \begin{pmatrix} 0.5 & -0.2 \\ -0.25 & 0.6 \end{pmatrix}$, and $\det(I - C) = 0.3 - 0.05 = 0.25$.
4. By the [[formula for the inverse of a 2 × 2 matrix|8XWC7RKNN1]], $(I - C)^{-1} = \dfrac{1}{0.25} \begin{pmatrix} 0.6 & 0.2 \\ 0.25 & 0.5 \end{pmatrix} = \begin{pmatrix} 2.4 & 0.8 \\ 1 & 2 \end{pmatrix}$.
5. So $x = (I - C)^{-1} d = (2.4 \cdot 50 + 0.8 \cdot 30,\ 1 \cdot 50 + 2 \cdot 30) = (144, 110)$.
6. Check: $C x = (0.5 \cdot 144 + 0.2 \cdot 110,\ 0.25 \cdot 144 + 0.4 \cdot 110) = (94, 80)$, and $x - C x = (50, 30) = d$.

## Remarks

The four problems show the three cases of the [[structure of the solution set|PDH3HKXWAZ]].
The circuit and the economy have exactly one solution, because the coefficient matrix is invertible.
The traffic network has infinitely many solutions, a particular solution plus the null space.
The chemical equation is homogeneous, and only the null space matters.

In the traffic problem, the four equations add up to $0 = 0$, because every car that enters the network also leaves it.
This is why one equation is redundant and the rank is $3$, not $4$.

In the circuit, if the right battery has $10$ V instead of $6$ V, step 3 becomes $2 I_2 + 4 I_3 = 10$.
Then $I_3 = 13/5 = 2.6$ A, $I_1 = 0.8$ A and $I_2 = -0.2$ A.

In the economy, all entries of $(I - C)^{-1}$ are nonnegative.
So a larger outside demand never needs a smaller output.
The entry $2.4$ says that one more unit of outside demand for manufacturing needs $2.4$ units of manufacturing in total, because manufacturing also uses its own output.
The columns of $C$ add up to $0.75$ and $0.6$, both less than $1$, and this makes every sector productive.
Leontief was the first to describe a national economy by a matrix.
The economic theory of the model belongs to [[input-output model|PF15E9SVQV]] in mathematical economics.

A system of the same kind gives the coefficients of a polynomial through given points, in [[polynomial interpolation by a linear system|NR58EBS932]].
The incidence matrix of a graph turns the current law into one matrix equation, in [[matrices of graphs|JFWP2SBCF0]].

## Explanations

### L1 human

Many problems in science count things that are kept: cars at a crossing, electric charge at a junction, atoms in a reaction, goods in an economy.
Each rule "what goes in equals what goes out" is one linear equation.
For example, if $400$ cars arrive at a crossing and $x$ cars leave it, then $x = 400$.
With several crossings we get several equations, and we solve them together.
Sometimes there is exactly one answer, and sometimes there are many answers, such as cars that circle the block.

### L2 human

The method has four steps.

1. Name the unknowns, and fix a direction for each flow or current.
2. Write one equation for each rule of balance.
3. Solve the system by row reduction, and write the free variables as parameters.
4. Check the answer in the original equations, and apply the conditions of the problem, such as positive flows or integer coefficients.

The typical use is a network with many nodes, where a computer solves a large sparse system.
The trap is to read a negative answer as an error.
A negative current only means that the current flows against the chosen direction.
A second trap is to forget the outside conditions: in the traffic network, the linear algebra allows $t = 0$, but then a flow is negative.

### L3 human

The traffic network and the circuit are both governed by the incidence matrix $B$ of a directed graph: conservation at the nodes says $B x = b$.
For a connected graph with $n$ nodes, $B$ has rank $n - 1$, and its null space is the cycle space of the graph, of dimension $m - n + 1$ for $m$ edges.
The free parameter $t$ of the traffic network is the one cycle around the block.
The input-output model needs $(I - C)^{-1} = I + C + C^2 + \cdots$, a series that converges when the spectral radius of $C$ is less than $1$.
Its nonnegativity is a fact about nonnegative matrices that belongs to Perron-Frobenius theory in matrix theory.
Balancing chemical equations uses only the null space, and a reaction with a null space of dimension $2$ or more is a mixture of independent reactions.
