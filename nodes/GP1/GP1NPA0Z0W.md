---
tag: GP1NPA0Z0W
kind: example
name: Long-term behavior of a migration model by diagonalization
msc: ["15A20", "60J10"]
topics: [Z6S6PWMJPH]
audience: ug1
instance_of: [0TNR9BQ871, 07SQCNV233]
illustrates: [0Y95Z7MT02]
uses: [0Y17PEKF24, 0ZND7NQ970, 0B5H4208Z9]
sources:
  - url: https://en.wikipedia.org/wiki/Diagonalizable_matrix
    locator: Application to matrix functions
  - book: isbn:9780321982384
    locator: Section 5.3
---

## Example

Each year, $10\%$ of the people in a city move to its suburbs, and $20\%$ of the people in the suburbs move to the city.
Let $x_k = (c_k, s_k)$ be the shares of the population in the city and in the suburbs after $k$ years, and start with $x_0 = (1, 0)$.
Column $j$ of the matrix lists where the people of place $j$ go, so $x_{k+1} = A x_k$ with
$$A = \begin{pmatrix} 0.9 & 0.2 \\ 0.1 & 0.8 \end{pmatrix}.$$
We find $x_k$ for every $k$ with [[powers of a diagonalizable matrix|0TNR9BQ871]].

1. The characteristic polynomial is
   $$p_A(t) = (t - 0.9)(t - 0.8) - 0.02 = t^2 - 1.7 t + 0.7 = (t - 1)(t - 0.7).$$
2. The eigenvalues $1$ and $0.7$ are distinct, so $A$ is [[diagonalizable|07SQCNV233]] by [[distinct eigenvalues imply diagonalizable|0Y95Z7MT02]].
3. Eigenvectors: $A(2, 1) = (1.8 + 0.2, \, 0.2 + 0.8) = (2, 1)$, and $A(1, -1) = (0.9 - 0.2, \, 0.1 - 0.8) = 0.7 \, (1, -1)$.
4. Put them into the columns of $P$.
   Then $\det P = -3$, and
   $$P = \begin{pmatrix} 2 & 1 \\ 1 & -1 \end{pmatrix}, \qquad P^{-1} = \frac{1}{3} \begin{pmatrix} 1 & 1 \\ 1 & -2 \end{pmatrix}.$$
5. Multiply out $P \operatorname{diag}(1, r) P^{-1}$ with $r = 0.7^k$:
   $$A^k = \frac{1}{3} \begin{pmatrix} 2 + r & 2 - 2r \\ 1 - r & 1 + 2r \end{pmatrix}.$$
   For $k = 1$, $r = 0.7$ gives $\tfrac{1}{3} \begin{pmatrix} 2.7 & 0.6 \\ 0.3 & 2.4 \end{pmatrix} = A$.
6. The coordinates of $x_0$ in the eigenvector basis are $P^{-1} x_0 = (\tfrac{1}{3}, \tfrac{1}{3})$, so
   $$x_k = \tfrac{1}{3} (2, 1) + \tfrac{1}{3} \, 0.7^k \, (1, -1) = \Big(\tfrac{2}{3} + \tfrac{1}{3} \, 0.7^k, \ \tfrac{1}{3} - \tfrac{1}{3} \, 0.7^k\Big).$$
7. Check: the formula gives $x_1 = (0.9, 0.1)$, $x_2 = (0.83, 0.17)$ and $x_3 = (0.781, 0.219)$.
   Direct multiplication gives $A(0.9, 0.1) = (0.83, 0.17)$ and $A(0.83, 0.17) = (0.781, 0.219)$.
8. Since $0.7^k \to 0$, the shares tend to $(\tfrac{2}{3}, \tfrac{1}{3})$, and $A^k \to \tfrac{1}{3} \begin{pmatrix} 2 & 2 \\ 1 & 1 \end{pmatrix}$.

## Remarks

### The steady state

The limit $(\tfrac{2}{3}, \tfrac{1}{3})$ is the eigenvector for $1$ whose entries add up to $1$.
It is the stationary distribution of the [[Markov chain|0G48PYM96Q]] with transition matrix $A$: in that state, $0.1 \cdot \tfrac{2}{3}$ people leave the city each year and $0.2 \cdot \tfrac{1}{3}$ arrive, and these are equal.
The eigenvalue $1$ is no accident.
The columns of $A$ add up to $1$, so the row vector $(1, 1)$ satisfies $(1, 1) A = (1, 1)$, and $A$ and its transpose have the same eigenvalues.

### Every start gives the same limit

Take any start with $c_0 + s_0 = 1$.
Its coordinate along $(2, 1)$ is the first entry of $P^{-1} x_0$, which is $\tfrac{1}{3}(c_0 + s_0) = \tfrac{1}{3}$.
So the limit is always $\tfrac{1}{3}(2, 1)$, and only the size of the part along $(1, -1)$ depends on the start.
That part is multiplied by $0.7$ each year, so the second eigenvalue sets the speed of convergence.
With a migration rate that makes the second eigenvalue $0.95$, the shares would approach the same kind of limit much more slowly.

## Explanations

### L1 human

People move between a city and its suburbs every year with fixed rates.
The matrix says how the shares change in one year.
One special split of the population does not change at all: two thirds in the city and one third in the suburbs.
In that split as many people move in as move out.
Any other split differs from it by a part that shrinks by $30\%$ each year, so the shares approach the balance.

### L2 human

Let us start instead with $x_0 = (0.5, 0.5)$.
The coordinates are
$$P^{-1} x_0 = \tfrac{1}{3} (0.5 + 0.5, \ 0.5 - 1) = \Big(\tfrac{1}{3}, -\tfrac{1}{6}\Big).$$
So the shares after $k$ years are
$$x_k = \tfrac{1}{3} (2, 1) - \tfrac{1}{6} \, 0.7^k \, (1, -1) = \Big(\tfrac{2}{3} - \tfrac{1}{6} \, 0.7^k, \ \tfrac{1}{3} + \tfrac{1}{6} \, 0.7^k\Big).$$
For $k = 1$ this is $(0.55, 0.45)$, and direct multiplication gives $A(0.5, 0.5) = (0.45 + 0.1, \, 0.05 + 0.4) = (0.55, 0.45)$.
The limit is again $(\tfrac{2}{3}, \tfrac{1}{3})$.
The typical use is to read the steady state and the speed of approach from the two eigenvalues.
The trap is to read the rows of $A$ as the "from" places: here column $j$ lists where the people of place $j$ go, and the rows would give a different chain.

### L3 human

For a column-stochastic matrix with positive entries, the [[Perron-Frobenius theorem|62NS7PV1M9]] gives a simple eigenvalue $1$ with a positive eigenvector, and every other eigenvalue has absolute value less than $1$.
Then $A^k$ converges to the rank-one projection onto the stationary distribution, even when $A$ is not diagonalizable.
Diagonalization makes the rate explicit: the error decays like $|\lambda_2|^k$, where $\lambda_2$ is the other eigenvalue of largest absolute value.
