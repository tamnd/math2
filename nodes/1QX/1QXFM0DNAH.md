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

Cars at a crossing, charge at a junction, atoms in a reaction and goods in an economy all obey one rule: what goes in equals what comes out.
Each such rule of balance is one linear equation, so each problem below becomes a [[system of linear equations|0GT4WWGWH2]].
We set up and solve four of them: a traffic network, an electric circuit, a chemical reaction and an economy with two sectors.

**Part 1: traffic around a block.**
Four one-way streets go around a city block, with the corners $A$, $B$, $C$, $D$ in clockwise order.
Let $x_1, x_2, x_3, x_4$ be the flows, in cars per hour, on the streets $A \to B$, $B \to C$, $C \to D$ and $D \to A$.
Outside streets bring $400$ cars per hour into $A$, $200$ into $B$ and $300$ into $D$.
Outside streets take $500$ cars per hour out of $B$, $300$ out of $C$ and $100$ out of $D$.
At each corner the flow in equals the flow out, and this gives one equation per corner.

1. At $A$, $400 + x_4 = x_1$, so $x_1 - x_4 = 400$.
2. At $B$, $x_1 + 200 = x_2 + 500$, so $x_1 - x_2 = 300$.
3. At $C$, $x_2 = x_3 + 300$, so $x_2 - x_3 = 300$.
4. At $D$, $x_3 + 300 = x_4 + 100$, so $x_3 - x_4 = -200$.
5. We eliminate as in [[Gaussian elimination|0JVJ2WCXZH]].
   Steps 1 and 2 give $x_2 = x_1 - 300 = x_4 + 100$, and step 3 then gives $x_3 = x_2 - 300 = x_4 - 200$.
6. Step 4 becomes $(x_4 - 200) - x_4 = -200$, which holds for every $x_4$.
   So the system has rank $3$, and $x_4$ is a free variable.
7. Put $x_4 = t$.
   In [[parametric form|KQT68YPHD1]] the solutions are
$$(x_1, x_2, x_3, x_4) = (400, 100, -200, 0) + t\,(1, 1, 1, 1).$$
8. A flow on a one-way street cannot be negative.
   The condition $x_3 = t - 200 \ge 0$ gives $t \ge 200$, and then the other three flows are positive too.
9. For $t = 200$ the flows are $(600, 300, 0, 200)$.
   Check: $600 - 200 = 400$, $600 - 300 = 300$, $300 - 0 = 300$ and $0 - 200 = -200$.

The vector $(1, 1, 1, 1)$ spans the [[null space|0PHDYNR24D]] of the coefficient matrix.
It describes extra cars that drive around the block, and these change no balance at any corner.

**Part 2: currents in a circuit.**
Two junctions $P$ and $Q$ are joined by three branches.
The left branch has a $12$ V battery and a $2\ \Omega$ resistor, and its current $I_1$ flows from $Q$ to $P$.
The right branch has a $6$ V battery and a $2\ \Omega$ resistor, and its current $I_2$ flows from $Q$ to $P$.
The middle branch has a $4\ \Omega$ resistor, and its current $I_3$ flows from $P$ to $Q$.
Both batteries push current towards $P$.
[[Kirchhoff's circuit laws|9B0V41V2F8]] give the equations: the current law at a junction, and the voltage law around a closed loop together with Ohm's law $V = RI$.

1. The current law at $P$ gives $I_1 + I_2 - I_3 = 0$.
2. The voltage law on the loop of the left and middle branches gives $2 I_1 + 4 I_3 = 12$.
3. The voltage law on the loop of the right and middle branches gives $2 I_2 + 4 I_3 = 6$.
4. In matrix form the system is
$$\begin{pmatrix} 1 & 1 & -1 \\ 2 & 0 & 4 \\ 0 & 2 & 4 \end{pmatrix} \begin{pmatrix} I_1 \\ I_2 \\ I_3 \end{pmatrix} = \begin{pmatrix} 0 \\ 12 \\ 6 \end{pmatrix}.$$
5. Its determinant is $1 \cdot (0 - 8) - 1 \cdot (8 - 0) + (-1) \cdot (4 - 0) = -20$.
   This is not $0$, so the solution is unique by the [[invertible matrix theorem|ACDFDABVQK]].
6. Steps 2 and 3 give $I_1 = 6 - 2 I_3$ and $I_2 = 3 - 2 I_3$.
   Put these into step 1:
$$(6 - 2 I_3) + (3 - 2 I_3) = I_3, \qquad \text{so } I_3 = \tfrac{9}{5} = 1.8 \text{ A}.$$
7. Then $I_1 = 6 - 3.6 = 2.4$ A and $I_2 = 3 - 3.6 = -0.6$ A.
   Check: $2.4 - 0.6 - 1.8 = 0$, $2 \cdot 2.4 + 4 \cdot 1.8 = 12$ and $2 \cdot (-0.6) + 4 \cdot 1.8 = 6$.

The current $I_2$ is negative.
So in the right branch the current flows from $P$ to $Q$, against the push of its own battery, because the stronger left battery wins.

**Part 3: balancing a chemical equation.**
Propane burns in oxygen and gives carbon dioxide and water:
$$x_1\, \mathrm{C_3H_8} + x_2\, \mathrm{O_2} \to x_3\, \mathrm{CO_2} + x_4\, \mathrm{H_2O}.$$
We want positive integers $x_1, x_2, x_3, x_4$ such that each element has the same number of atoms on the two sides.

1. Carbon gives $3 x_1 = x_3$, hydrogen gives $8 x_1 = 2 x_4$, and oxygen gives $2 x_2 = 2 x_3 + x_4$.
2. This is the [[homogeneous system|04KGXJG1A2]] $M x = 0$ with
$$M = \begin{pmatrix} 3 & 0 & -1 & 0 \\ 8 & 0 & 0 & -2 \\ 0 & 2 & -2 & -1 \end{pmatrix}.$$
3. Put $x_1 = t$.
   Then $x_3 = 3t$, $x_4 = 4t$ and $x_2 = (6t + 4t)/2 = 5t$.
4. So the null space of $M$ is the line spanned by $(1, 5, 3, 4)$, and $M$ has rank $3$.
5. The smallest positive integer solution has $t = 1$:
$$\mathrm{C_3H_8} + 5\, \mathrm{O_2} \to 3\, \mathrm{CO_2} + 4\, \mathrm{H_2O}.$$
   Check: carbon $3 = 3$, hydrogen $8 = 4 \cdot 2$, oxygen $5 \cdot 2 = 3 \cdot 2 + 4$.

**Part 4: an economy with two sectors.**
An economy has two sectors, manufacturing and services.
One unit of manufacturing output uses $0.5$ unit of manufacturing and $0.25$ unit of services.
One unit of services output uses $0.2$ unit of manufacturing and $0.4$ unit of services.
Consumers outside the two sectors demand $d = (50, 30)$ units.
Which total output $x = (x_1, x_2)$ covers the needs of both sectors and the outside demand?
This is the [[input-output model|PF15E9SVQV]], and column $j$ of its consumption matrix $C$ lists the inputs for one unit of sector $j$.

1. The consumption matrix is $C = \begin{pmatrix} 0.5 & 0.2 \\ 0.25 & 0.4 \end{pmatrix}$.
2. Output equals internal use plus outside demand, $x = C x + d$, so $(I - C) x = d$.
3. We have $I - C = \begin{pmatrix} 0.5 & -0.2 \\ -0.25 & 0.6 \end{pmatrix}$ and $\det(I - C) = 0.3 - 0.05 = 0.25$.
4. The [[formula for the inverse of a 2 × 2 matrix|8XWC7RKNN1]] gives
$$(I - C)^{-1} = \frac{1}{0.25} \begin{pmatrix} 0.6 & 0.2 \\ 0.25 & 0.5 \end{pmatrix} = \begin{pmatrix} 2.4 & 0.8 \\ 1 & 2 \end{pmatrix}.$$
5. So $x = (I - C)^{-1} d = (2.4 \cdot 50 + 0.8 \cdot 30,\ 50 + 2 \cdot 30) = (144, 110)$.
   Check: $C x = (72 + 22,\ 36 + 44) = (94, 80)$, and $x - C x = (50, 30) = d$.

## Remarks

### Three kinds of answer

The four problems show the three cases of the [[structure of the solution set|PDH3HKXWAZ]].
The circuit and the economy have exactly one solution, because their coefficient matrices are invertible.
The traffic network has infinitely many solutions, a particular solution plus the null space.
The chemical equation is homogeneous, so only the null space matters, and we pick the smallest positive integer vector in it.

Why is one traffic equation redundant?
The four equations add up to $0 = 0$, because every car that enters the block also leaves it.
So the rank is $3$, not $4$, and one free parameter remains.

### Change a number

Give the right battery $10$ V instead of $6$ V.
Step 3 of part 2 becomes $2 I_2 + 4 I_3 = 10$, so $I_2 = 5 - 2 I_3$, and the current law gives
$$(6 - 2 I_3) + (5 - 2 I_3) = I_3, \qquad I_3 = \tfrac{11}{5} = 2.2 \text{ A}.$$
Then $I_1 = 6 - 4.4 = 1.6$ A and $I_2 = 5 - 4.4 = 0.6$ A.
Check: $1.6 + 0.6 = 2.2$, $3.2 + 8.8 = 12$ and $1.2 + 8.8 = 10$.
Now $I_2$ is positive, so the right battery is strong enough to push its own current forward.

### What the inverse matrix says

All entries of $(I - C)^{-1}$ in part 4 are nonnegative.
So a larger outside demand never needs a smaller output.
The entry $2.4$ says that one more unit of outside demand for manufacturing needs $2.4$ units of manufacturing in total, because manufacturing also uses its own output.
The columns of $C$ add up to $0.75$ and $0.6$, both less than $1$, so each sector uses less than one unit of input value per unit of output, and this makes the economy productive.
The economic theory belongs to the [[input-output model|PF15E9SVQV]] in mathematical economics.

### Watch out

A negative answer is not always an error.
The current $I_2 = -0.6$ A only means that the current flows against the direction that we chose.
A negative traffic flow is different: on a one-way street it is impossible.
The linear algebra allows $t = 0$ in part 1, but then $x_3 = -200$, so you must apply the conditions of the problem after you solve the system.

### Try it

First, balance $x_1\, \mathrm{H_2} + x_2\, \mathrm{O_2} \to x_3\, \mathrm{H_2O}$.
Hydrogen gives $2 x_1 = 2 x_3$ and oxygen gives $2 x_2 = x_3$, so the null space is spanned by $(2, 1, 2)$, and the equation is $2\, \mathrm{H_2} + \mathrm{O_2} \to 2\, \mathrm{H_2O}$.

Second, in part 4 raise the outside demand for services from $30$ to $40$.
The output grows by $10$ times column $2$ of $(I - C)^{-1}$, that is by $(8, 20)$, so $x = (152, 130)$.

## Explanations

### L1 human

Many problems in science count things that are kept: cars at a crossing, charge at a junction, atoms in a reaction.
Each rule "what goes in equals what comes out" is one equation.
For example, if $400$ cars arrive at a crossing and no car stays there, the cars that leave also number $400$.
With several crossings we get several equations, and we solve them together.
Sometimes there is exactly one answer, and sometimes there are many, such as extra cars that circle the block.

### L2 human

Here is a typical problem: a junction network where you know some currents and want the rest.
You name the unknowns and fix a direction for each, write one equation for each rule of balance, and row reduce.
In part 2 this gave three equations with a nonzero determinant, so one answer, $(I_1, I_2, I_3) = (2.4, -0.6, 1.8)$.
In part 1 the equations were dependent, so the answer was a line of solutions, $(400, 100, -200, 0) + t(1, 1, 1, 1)$, and the condition $t \ge 200$ came from outside the algebra.
Real networks have thousands of nodes, and a computer solves the same kind of sparse system.
The method does not change: balance at each node, then elimination, then a check against the physical conditions.

### L3 human

The traffic network and the circuit are both governed by the incidence matrix $B$ of a directed graph, and conservation at the nodes says $B x = b$.
For a connected graph with $n$ nodes and $m$ edges, $B$ has rank $n - 1$, and its null space is the cycle space of dimension $m - n + 1$.
The free parameter $t$ of part 1 is the one cycle around the block, and [[matrices of graphs|JFWP2SBCF0]] works this out in general.
The input-output model needs $(I - C)^{-1} = I + C + C^2 + \cdots$, a series that converges when the spectral radius of $C$ is less than $1$.
Its nonnegativity is a fact about nonnegative matrices from Perron-Frobenius theory.
A reaction whose matrix has a null space of dimension $2$ or more is a mixture of independent reactions, and chemists then need more information to fix the coefficients.
The same kind of system gives a polynomial through given points, in [[polynomial interpolation by a linear system|NR58EBS932]].
