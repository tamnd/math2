---
tag: E8DZ9CPEEE
kind: example
name: Lights Out puzzle
msc: ["15A06", "91A46", "12E20"]
topics: [K0FNC6CWZN]
audience: ug1
instance_of: [0GT4WWGWH2]
illustrates: [0W4FSW1TVB, PDH3HKXWAZ]
uses: [0GT4WWGWH2, 0ZXZ82FTX2, 0JVJ2WCXZH, 0ZC9YTXZRY, 0PHDYNR24D, 0W4FSW1TVB, PDH3HKXWAZ, JD8FEPHM6T]
sources:
  - url: https://en.wikipedia.org/wiki/Lights_Out_(game)
    locator: Mathematics
  - url: https://en.wikipedia.org/wiki/Lights_Out_(game)
    locator: lead section
---

## Example

Lights Out is a handheld puzzle with an $n \times n$ grid of lights, some of them on at the start.
Pressing a cell switches that light and its horizontal and vertical neighbors, each from on to off or from off to on.
The aim is to switch all lights off.
A player who tries at random soon asks two questions: can every start be solved, and which cells must be pressed?
Linear algebra over the [[finite field|0ZXZ82FTX2]] $\mathbb F_2 = \{0, 1\}$ answers both.
We solve the $3 \times 3$ game completely, and we explain the $4 \times 4$ and $5 \times 5$ games.

**Part 1: the model.**

1. A state is a vector $b \in \mathbb F_2^{n^2}$, with $b_c = 1$ when the light $c$ is on.
   We number the cells row by row.
2. Switching a light is adding $1$ in $\mathbb F_2$, where $1 + 1 = 0$.
   So pressing a cell twice changes nothing, and the order of presses does not matter.
   A strategy is therefore a vector $x \in \mathbb F_2^{n^2}$, with $x_c = 1$ when we press the cell $c$.
3. Let $A$ be the $n^2 \times n^2$ matrix whose column $c$ is the pattern switched by the cell $c$.
   Then the strategy $x$ switches the pattern $A x$.
4. So $x$ switches the state $b$ off exactly when $A x = b$ over $\mathbb F_2$.
   Solving Lights Out means solving a [[system of linear equations|0GT4WWGWH2]] over $\mathbb F_2$.
5. The matrix $A$ is symmetric, because the cell $c$ switches the cell $d$ exactly when $d$ switches $c$.

**Part 2: the $3 \times 3$ game.**
The matrix is
$$A = \begin{pmatrix}
1&1&0&1&0&0&0&0&0\\
1&1&1&0&1&0&0&0&0\\
0&1&1&0&0&1&0&0&0\\
1&0&0&1&1&0&1&0&0\\
0&1&0&1&1&1&0&1&0\\
0&0&1&0&1&1&0&0&1\\
0&0&0&1&0&0&1&1&0\\
0&0&0&0&1&0&1&1&1\\
0&0&0&0&0&1&0&1&1
\end{pmatrix}.$$

1. [[Gaussian elimination|0JVJ2WCXZH]] over $\mathbb F_2$ gives $9$ pivots.
   So $A$ has [[rank|0ZC9YTXZRY]] $9$ and is invertible over $\mathbb F_2$.
2. So every state of the $3 \times 3$ game has exactly one solution without repeated presses.
3. Suppose that only the center is on.
   Press the five cells of the plus shape, which are the center and its four neighbors.
   The center is switched $5$ times, each edge cell $2$ times (by itself and by the center), and each corner $2$ times (by its two edge neighbors).
   So only the center changes.
4. Suppose that only the top left corner is on.
   Press the cells in the pattern $\begin{smallmatrix} 1&0&1\\0&0&1\\1&1&0 \end{smallmatrix}$.
   The top left corner is switched once, by itself, and every other cell is switched twice.
   For example, the top middle cell is switched by the two top corners.
5. Suppose that the four corners are on.
   Press the four corners.
   Each corner is switched once, and each edge cell twice, by its two neighboring corners.
6. Suppose that all nine lights are on.
   Press the four corners and the center.
   Each corner is switched once, each edge cell three times (by two corners and the center), and the center once.

**Part 3: rank, quiet patterns and solvability on larger boards.**

1. Over $\mathbb F_2$, the rank of $A$ is $4$ for $n = 2$, $9$ for $n = 3$, $12$ for $n = 4$ and $23$ for $n = 5$.
2. By the [[rank-nullity theorem|0W4FSW1TVB]], the [[null space|0PHDYNR24D]] of $A$ has dimension $0$, $0$, $4$ and $2$ in these cases.
3. A vector of the null space is a *quiet pattern*, because pressing it changes nothing.
   For $n = 4$, one quiet pattern is $\begin{smallmatrix} 0&1&1&1\\1&0&1&0\\1&1&0&0\\1&0&0&0 \end{smallmatrix}$.
4. For $n = 5$, the null space is spanned by
$$N_1 = \begin{smallmatrix} 0&1&1&1&0\\1&0&1&0&1\\1&1&0&1&1\\1&0&1&0&1\\0&1&1&1&0 \end{smallmatrix}, \qquad N_2 = \begin{smallmatrix} 1&0&1&0&1\\1&0&1&0&1\\0&0&0&0&0\\1&0&1&0&1\\1&0&1&0&1 \end{smallmatrix}.$$
   Check for $N_2$: each pressed cell is switched by itself and by one pressed vertical neighbor, so twice.
   Each other cell has $0$ or $2$ pressed neighbors.
5. The system $A x = b$ has a solution exactly when $b \cdot y = 0$ for every quiet pattern $y$.
   If $A x = b$ and $A y = 0$, then $b \cdot y = x^{\mathsf T} A^{\mathsf T} y = x^{\mathsf T} A y = 0$, since $A$ is symmetric.
   Conversely, the states orthogonal to the null space form a subspace of dimension $n^2 - \dim \operatorname{Nul} A = \operatorname{rank} A$.
   This subspace contains the column space, which has the same dimension, so the two are equal.
6. For $n = 5$, the state with only the center on is orthogonal to $N_1$ and $N_2$, so it is solvable.
   The state with only one corner on has $b \cdot N_2 = 1$, so it is not solvable.
7. By the [[structure of the solution set|PDH3HKXWAZ]], a solvable $5 \times 5$ state has exactly $2^2 = 4$ solutions, one for each quiet pattern added.
   Only $2^{23}$ of the $2^{25}$ states, a quarter, are solvable.

## Remarks

### What the example shows

The rank decides everything.
When $A$ is invertible, as for $n = 2$ and $n = 3$, every state has exactly one solution.
When $A$ has a null space, a state is solvable only if it is orthogonal to the quiet patterns, and then the quiet patterns give the other solutions.
The board size changes the answer in a way that is hard to guess, since the rank is full for $n = 2, 3$ but not for $n = 4, 5$.

### Watch out: work over $\mathbb F_2$

The computation must be done over $\mathbb F_2$.
Over $\mathbb R$, the same $0$-$1$ matrix can have a different rank.
For $n = 4$, the real rank is $14$, while the rank over $\mathbb F_2$ is $12$.
Also, a real solution with entries such as $\tfrac12$ or $-1$ says nothing about presses.

### History

The game was released by Tiger Electronics in 1995, on a $5 \times 5$ grid.
In 1998, Anderson and Feil used linear algebra to show that not all $5 \times 5$ states are solvable, that each solvable state has exactly four solutions, and that a solvable state must be orthogonal to two fixed vectors.

### Where the theory lives

The $2 \times 2$ case is worked out in [[the Lights Out puzzle on a 2 by 2 board|JD8FEPHM6T]].
The general facts used here are the rank-nullity theorem and the structure of the solution set, which hold over every field.

### Try it

First, start from the $3 \times 3$ board with all lights off and press all nine cells.
Each corner is switched $3$ times, each edge cell $4$ times and the center $5$ times.
So the corners and the center end up on, and the edge cells end up off.

Second, decide whether the $5 \times 5$ state with only the top middle cell on is solvable.
The top middle entry of $N_1$ is $1$, so $b \cdot N_1 = 1$, and the state is not solvable.

## Explanations

### L1 human

In Lights Out, each press switches a light and its neighbors, and you want all lights off.
Pressing a button twice does nothing, and the order of presses does not matter.
So the only question is which buttons to press, once each.
This is a puzzle of yes-or-no choices, and it becomes a system of equations in which $1 + 1 = 0$.
On the $3 \times 3$ board, if only the center light is on, pressing the plus shape of five buttons turns it off.

### L2 human

To solve a Lights Out board, do these steps.

1. Write the matrix $A$ of the board and the state $b$.
2. Row reduce the augmented matrix $[A \mid b]$ over $\mathbb F_2$.
3. If a row $[0 \cdots 0 \mid 1]$ appears, the state is not solvable.
   Otherwise, read off a solution, and add quiet patterns to get the others.

The typical use beyond games is any problem where switches act by "on or off" and the effects add modulo $2$, as in error-correcting codes.
The trap is to row reduce with ordinary arithmetic.
Over $\mathbb F_2$, the row operation "add row $i$ to row $j$" is also "subtract", and every nonzero pivot is $1$.

### L3 human

The matrix of the $n \times n$ game is $A = I + L$, where $L$ is the adjacency matrix of the grid graph, so $A$ is the adjacency matrix of the grid with a loop at each vertex.
Its null space over $\mathbb F_2$ is described by Chebyshev-like polynomials over $\mathbb F_2$, and its dimension depends on $n$ in an irregular way.
Variants on other graphs, with more colors over $\mathbb F_p$, or on the torus, give other linear systems over finite fields.
The solvability criterion $\operatorname{Col}(A) = \operatorname{Nul}(A^{\mathsf T})^{\perp}$ holds over every field, because it only uses dimension counts.
