---
tag: ~c4bcd5dd
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

Lights Out is played on an $n \times n$ grid of lights.
Pressing a cell switches that light and its horizontal and vertical neighbors, each from on to off or from off to on.
The aim is to switch all lights off.
We solve the $3 \times 3$ game by linear algebra over the [[finite field|0ZXZ82FTX2]] $\mathbb F_2 = \{0, 1\}$, and we explain the $4 \times 4$ and $5 \times 5$ games.

**Part 1: the model.**

1. A state is a vector $b \in \mathbb F_2^{n^2}$, with $b_c = 1$ when the light $c$ is on. Number the cells row by row.
2. Pressing a cell twice changes nothing, and the order of presses does not matter, because switching is addition of $1$ in $\mathbb F_2$. So a strategy is a vector $x \in \mathbb F_2^{n^2}$, with $x_c = 1$ when we press the cell $c$.
3. Let $A$ be the $n^2 \times n^2$ matrix whose column $c$ is the pattern switched by the cell $c$. The strategy $x$ switches the pattern $A x$.
4. So $x$ switches the state $b$ off exactly when $A x = b$ over $\mathbb F_2$. Solving Lights Out means solving a [[system of linear equations|0GT4WWGWH2]] over $\mathbb F_2$.
5. The matrix $A$ is symmetric: the cell $c$ switches the cell $d$ exactly when $d$ switches $c$.

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

1. [[Gaussian elimination|0JVJ2WCXZH]] over $\mathbb F_2$, where $1 + 1 = 0$, gives $9$ pivots. So $A$ has [[rank|0ZC9YTXZRY]] $9$ and is invertible over $\mathbb F_2$.
2. So every state of the $3 \times 3$ game has exactly one solution without repeated presses.
3. *Only the centre is on.* Press the five cells of the plus shape: the centre and its four neighbors. The centre is switched $5$ times, each edge cell $3$ times and each corner $2$ times, so only the centre changes.
4. *Only the top left corner is on.* Press the cells in the pattern $\begin{smallmatrix} 1&0&1\\0&0&1\\1&1&0 \end{smallmatrix}$. The top left corner is switched once (by itself), and every other cell an even number of times. For example, the top middle cell is switched by the two top corners.
5. *The four corners are on.* Press the four corners. Each corner is switched once, and each edge cell twice, by its two neighboring corners.
6. *All nine lights are on.* Press the four corners and the centre. Each corner is switched once, each edge cell by two corners and the centre, and the centre once.

**Part 3: rank, quiet patterns and solvability on larger boards.**

1. Over $\mathbb F_2$, the rank of $A$ is $4$ for $n = 2$, $9$ for $n = 3$, $12$ for $n = 4$ and $23$ for $n = 5$.
2. By the [[rank-nullity theorem|0W4FSW1TVB]], the [[null space|0PHDYNR24D]] of $A$ has dimension $0$, $0$, $4$ and $2$ in these cases.
3. A vector of the null space is a *quiet pattern*: pressing it changes nothing. For $n = 4$, one quiet pattern is $\begin{smallmatrix} 0&1&1&1\\1&0&1&0\\1&1&0&0\\1&0&0&0 \end{smallmatrix}$.
4. For $n = 5$, the null space is spanned by
$$N_1 = \begin{smallmatrix} 0&1&1&1&0\\1&0&1&0&1\\1&1&0&1&1\\1&0&1&0&1\\0&1&1&1&0 \end{smallmatrix}, \qquad N_2 = \begin{smallmatrix} 1&0&1&0&1\\1&0&1&0&1\\0&0&0&0&0\\1&0&1&0&1\\1&0&1&0&1 \end{smallmatrix}.$$
Check for $N_2$: each cell of the columns $1$, $3$, $5$ in the rows $1, 2, 4, 5$ is switched by itself and by one vertical neighbor, so twice. Each other cell has $0$ or $2$ pressed neighbors.
5. Solvability: $A x = b$ has a solution exactly when $b \cdot y = 0$ for every quiet pattern $y$. Proof: if $A x = b$ and $A y = 0$, then $b \cdot y = x^{\mathsf T} A^{\mathsf T} y = x^{\mathsf T} A y = 0$, since $A$ is symmetric. Conversely, the states orthogonal to the null space form a subspace of dimension $n^2 - \dim \operatorname{Nul} A = \operatorname{rank} A$, which contains the column space of the same dimension.
6. For $n = 5$: the state with only the centre on is orthogonal to $N_1$ and $N_2$, so it is solvable. The state with only one corner on has $b \cdot N_2 = 1$, so it is not solvable.
7. By the [[structure of the solution set|PDH3HKXWAZ]], a solvable $5 \times 5$ state has exactly $2^2 = 4$ solutions, one for each quiet pattern added. Only $2^{23}$ of the $2^{25}$ states, a quarter, are solvable.

## Remarks

The example shows that the rank decides everything.
When $A$ is invertible, as for $n = 2$ and $n = 3$, every state has exactly one solution.
When $A$ has a null space, a state is solvable only if it is orthogonal to the quiet patterns, and then the quiet patterns give the other solutions.
The board size changes the answer in a way that is hard to guess: the rank is full for $n = 2, 3$ but not for $n = 4, 5$.

The computation must be done over $\mathbb F_2$.
Over $\mathbb R$, the same $0$-$1$ matrix has another rank in general, and a real solution says nothing about presses.

The game was released by Tiger Electronics in 1995, on a $5 \times 5$ grid.
In 1998, Anderson and Feil used linear algebra to show that not all $5 \times 5$ states are solvable, that each solvable state has exactly four solutions, and that a solvable state must be orthogonal to two fixed vectors.
The $2 \times 2$ case is worked out in [[the Lights Out puzzle on a 2 by 2 board|JD8FEPHM6T]].

## Explanations

### L1 human

In Lights Out, each press switches a light and its neighbors, and you want all lights off.
Pressing a button twice does nothing, and the order of presses does not matter.
So the only question is which buttons to press, once each.
This is a puzzle of yes-or-no choices, and it becomes a system of equations where $1 + 1 = 0$.
On the $3 \times 3$ board, if only the centre light is on, pressing the plus shape of five buttons turns it off.

### L2 human

To solve a Lights Out board, do these steps.

1. Write the matrix $A$ of the board and the state $b$.
2. Row reduce the augmented matrix $[A \mid b]$ over $\mathbb F_2$.
3. If a row $[0 \cdots 0 \mid 1]$ appears, the state is not solvable. Otherwise, read off a solution, and add quiet patterns to get the others.

The typical use beyond games is any problem where switches act by "on or off" and the effects add modulo $2$, as in error-correcting codes.
The trap is to row reduce with ordinary arithmetic: over $\mathbb F_2$, the row operation "add row $i$ to row $j$" is also "subtract", and every nonzero pivot is $1$.

### L3 human

The matrix of the $n \times n$ game is $A = I + L$, where $L$ is the adjacency matrix of the grid graph, so $A$ is the adjacency matrix of the grid with a loop at each vertex.
Its null space over $\mathbb F_2$ is described by Chebyshev-like polynomials over $\mathbb F_2$, and its dimension depends on $n$ in an irregular way.
Variants on other graphs, with more colors over $\mathbb F_p$, or on the torus, give other linear systems over finite fields.
The solvability criterion $\operatorname{Col}(A) = \operatorname{Nul}(A^{\mathsf T})^{\perp}$ holds over every field, because it only uses dimension counts.
