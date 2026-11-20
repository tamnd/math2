---
tag: Y9FRWY8YX4
kind: example
name: Steady-state vectors of Markov chains
msc: ["15B51", "60J10", "15A18"]
topics: [K0FNC6CWZN]
audience: ug1
instance_of: [TA8QR5HFAY]
illustrates: [HBE0MHJ2ZP]
uses: [YVNZGHHZJ5, TA8QR5HFAY, 0ZND7NQ970, 0PHDYNR24D, 0TNR9BQ871, HBE0MHJ2ZP, 2F1B461YN7]
sources:
  - url: https://en.wikipedia.org/wiki/Stochastic_matrix
    locator: lead section
  - url: https://en.wikipedia.org/wiki/Perron%E2%80%93Frobenius_theorem
    locator: lead section
---

## Example

A car rental company has three offices $1$, $2$ and $3$.
A car rented at office $j$ is returned at office $i$ with the probability $p_{ij}$, and the rentals last one week.
Let $x_k$ be the vector of the fractions of the fleet at the three offices after $k$ weeks.
Then $x_{k+1} = P x_k$ with
$$P = \begin{pmatrix} 0.5 & 0.2 & 0.3 \\ 0.3 & 0.8 & 0.3 \\ 0.2 & 0 & 0.4 \end{pmatrix}.$$
We find the [[steady-state vector|TA8QR5HFAY]] $q$, the probability vector with $P q = q$, and we show that $x_k \to q$ from every start.

1. $P$ is a [[column-stochastic matrix|YVNZGHHZJ5]]: its entries are nonnegative, and each column sums to $1$ ($0.5 + 0.3 + 0.2$, $0.2 + 0.8 + 0$ and $0.3 + 0.3 + 0.4$).
2. $1$ is an [[eigenvalue|0ZND7NQ970]] of $P$. The reason: the row vector $(1, 1, 1)$ satisfies $(1, 1, 1) P = (1, 1, 1)$, so $P^{\mathsf T}$ has the eigenvalue $1$, and $P$ has the same characteristic polynomial as $P^{\mathsf T}$.
3. The steady state lies in the [[null space|0PHDYNR24D]] of $P - I = \begin{pmatrix} -0.5 & 0.2 & 0.3 \\ 0.3 & -0.2 & 0.3 \\ 0.2 & 0 & -0.6 \end{pmatrix}$.
4. The third row gives $x_1 = 3 x_3$. The first row gives $-1.5 x_3 + 0.2 x_2 + 0.3 x_3 = 0$, so $x_2 = 6 x_3$. The second row then holds: $0.9 x_3 - 1.2 x_3 + 0.3 x_3 = 0$.
5. So the null space is spanned by $(3, 6, 1)$. Divide by the sum $10$: $q = (0.3, 0.6, 0.1)$.
6. Check: $P q = (0.15 + 0.12 + 0.03,\ 0.09 + 0.48 + 0.03,\ 0.06 + 0 + 0.04) = (0.3, 0.6, 0.1)$.
7. $P$ is regular: $P$ has a zero entry, but $P^2 = \begin{pmatrix} 0.37 & 0.26 & 0.33 \\ 0.45 & 0.7 & 0.45 \\ 0.18 & 0.04 & 0.22 \end{pmatrix}$ has only positive entries.
8. Convergence. The matrix $P^2$ is stochastic with positive entries. By the theorem on [[eigenvalues and steady state of a positive stochastic matrix|HBE0MHJ2ZP]], $(P^2)^m y \to q$ for every probability vector $y$. Apply this to $y = x_0$ and $y = P x_0$: both $x_{2m}$ and $x_{2m+1}$ tend to $q$.
9. The rate. The characteristic polynomial is $(\lambda - 1)(\lambda - 0.5)(\lambda - 0.2)$, with the eigenvectors $q$, $(1, -3, 2)$ and $(1, 0, -1)$.
10. For $x_0 = (1, 0, 0)$, all cars at office $1$: $x_0 = q + 0.2 (1, -3, 2) + 0.5 (1, 0, -1)$. By the formula for [[powers of a diagonalizable matrix|0TNR9BQ871]],
$$x_k = q + 0.2 \cdot 0.5^k (1, -3, 2) + 0.5 \cdot 0.2^k (1, 0, -1).$$
11. The values are $x_1 = (0.5, 0.3, 0.2)$, $x_2 = (0.37, 0.45, 0.18)$, $x_3 = (0.329, 0.525, 0.146)$, $x_5 \approx (0.3064, 0.5812, 0.1123)$ and $x_{10} \approx (0.3002, 0.5994, 0.1004)$. The error halves each week, as the second eigenvalue $0.5$ says.

In the long run, $60\%$ of the fleet is at office $2$, whatever the start.

## Remarks

The example shows the two facts of every regular stochastic matrix: a unique steady state, and convergence to it from every start.
The second largest absolute value of an eigenvalue sets the speed.

Regularity is needed, and the trap is real.
The matrix $\begin{pmatrix} 0 & 1 \\ 1 & 0 \end{pmatrix}$ is stochastic and has the steady state $(1/2, 1/2)$.
But it also has the eigenvalue $-1$ on the unit circle, and the start $(1, 0)$ gives the orbit $(1, 0), (0, 1), (1, 0), \dots$, which does not converge.
No power of this matrix is positive, so it is not regular.
The identity matrix $I_2$ is stochastic too, and every probability vector is a steady state, so the steady state is not unique.

Change one entry and see the effect.
If the column $3$ of $P$ changes from $(0.3, 0.3, 0.4)$ to $(0.1, 0.5, 0.4)$, the steady state moves to $(3, 7, 1)/11 \approx (0.273, 0.636, 0.091)$.
The other two eigenvalues become $0.35 \pm 0.132\, i$, of absolute value about $0.374$, so the convergence is faster and turns slightly around $q$.

The general theory of stochastic matrices rests on the [[Perron-Frobenius theorem|62NS7PV1M9]] for nonnegative matrices.
The probability theory of Markov chains, including the row convention $\pi P = \pi$ and the [[stationary distribution|0KRH5157WP]], belongs to probability theory.
A two-state model is worked out in [[a Markov chain with two states|N73KSZZ4V9]], and the ranking of web pages in [[PageRank as an eigenvector problem|9ZPQYZ5NDP]] is the same problem for a large matrix.

## Explanations

### L1 human

Imagine many cars that move each week between three offices, with fixed chances for each move.
After some weeks, the share of cars at each office stops changing, even though single cars keep moving.
This stable mixture is the steady-state vector.
Here it is $30\%$, $60\%$ and $10\%$, and we reach it from any start, for example from all cars at office $1$.

### L2 human

To find the steady state of a column-stochastic matrix $P$, do these steps.

1. Solve $(P - I) x = 0$. One equation is redundant, because the columns of $P - I$ sum to $0$.
2. Scale the solution so that its entries sum to $1$.
3. Check that some power of $P$ has only positive entries. Then every orbit converges to this vector.

The typical use is a long-run share: market shares, population shares, or the time a random walker spends at each place.
The trap is to assume convergence without regularity.
A stochastic matrix can have eigenvalues other than $1$ on the unit circle, such as $-1$ for the swap matrix, and then the orbits can oscillate forever.

### L3 human

For an irreducible stochastic matrix, the eigenvalues on the unit circle are the $h$-th roots of unity, where $h$ is the period of the chain.
The chain is regular exactly when it is irreducible and $h = 1$, and then $P^k \to q \mathbf{1}^{\mathsf T}$, a matrix of rank one.
The convergence in the total variation norm is geometric, with the rate given by the second eigenvalue, and this rate is the subject of mixing times.
For infinite state spaces, the same questions need operator theory and probability, and the answers change.
