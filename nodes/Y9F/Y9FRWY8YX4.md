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

A car rental company has three offices, and a car rented at one office may be returned at any of them.
The manager wants to know where the fleet ends up after many weeks, so that each office has enough parking.
A car rented at office $j$ is returned at office $i$ with probability $p_{ij}$, and each rental lasts one week.
If $x_k$ lists the fractions of the fleet at the three offices after $k$ weeks, then $x_{k+1} = P x_k$ with
$$P = \begin{pmatrix} 0.5 & 0.2 & 0.3 \\ 0.3 & 0.8 & 0.3 \\ 0.2 & 0 & 0.4 \end{pmatrix}.$$
We use the column convention: column $j$ lists where the cars of office $j$ go, so each column sums to $1$.
We find the [[steady-state vector|TA8QR5HFAY]] $q$, the probability vector with $P q = q$, and we show that $x_k \to q$ from every start.

1. $P$ is a [[column-stochastic matrix|YVNZGHHZJ5]].
   Its entries are nonnegative, and its columns sum to $0.5 + 0.3 + 0.2 = 1$, $0.2 + 0.8 + 0 = 1$ and $0.3 + 0.3 + 0.4 = 1$.
2. So $1$ is an [[eigenvalue|0ZND7NQ970]] of $P$.
   The row vector $(1, 1, 1)$ satisfies $(1, 1, 1) P = (1, 1, 1)$, so $P^{\mathsf T}$ has the eigenvalue $1$, and $P$ has the same characteristic polynomial as $P^{\mathsf T}$.
3. The steady state lies in the [[null space|0PHDYNR24D]] of
$$P - I = \begin{pmatrix} -0.5 & 0.2 & 0.3 \\ 0.3 & -0.2 & 0.3 \\ 0.2 & 0 & -0.6 \end{pmatrix}.$$
4. The third row gives $x_1 = 3 x_3$.
   The first row gives $-1.5 x_3 + 0.2 x_2 + 0.3 x_3 = 0$, so $x_2 = 6 x_3$.
   The second row then holds as well, since $0.9 x_3 - 1.2 x_3 + 0.3 x_3 = 0$.
5. So the null space is spanned by $(3, 6, 1)$, and dividing by the sum $10$ gives $q = (0.3, 0.6, 0.1)$.
   Check: $P q = (0.15 + 0.12 + 0.03,\ 0.09 + 0.48 + 0.03,\ 0.06 + 0 + 0.04) = (0.3, 0.6, 0.1)$.
6. $P$ is regular, which means that some power of $P$ has only positive entries.
   $P$ itself has a zero entry, but
$$P^2 = \begin{pmatrix} 0.37 & 0.26 & 0.33 \\ 0.45 & 0.7 & 0.45 \\ 0.18 & 0.04 & 0.22 \end{pmatrix}$$
   has only positive entries.
7. The matrix $P^2$ is stochastic with positive entries.
   By the theorem on [[eigenvalues and steady state of a positive stochastic matrix|HBE0MHJ2ZP]], $(P^2)^m y \to q$ for every probability vector $y$.
   Apply this to $y = x_0$ and to $y = P x_0$: both $x_{2m}$ and $x_{2m+1}$ tend to $q$, so $x_k \to q$.
8. To see the speed, factor the characteristic polynomial as $(\lambda - 1)(\lambda - 0.5)(\lambda - 0.2)$.
   The eigenvectors are $q$, $(1, -3, 2)$ and $(1, 0, -1)$.
9. Start with all cars at office $1$, so $x_0 = (1, 0, 0) = q + 0.2\, (1, -3, 2) + 0.5\, (1, 0, -1)$.
   The formula for [[powers of a diagonalizable matrix|0TNR9BQ871]] gives
$$x_k = q + 0.2 \cdot 0.5^k\, (1, -3, 2) + 0.5 \cdot 0.2^k\, (1, 0, -1).$$
10. The first states are $x_1 = (0.5, 0.3, 0.2)$, $x_2 = (0.37, 0.45, 0.18)$ and $x_3 = (0.329, 0.525, 0.146)$.
    Later, $x_5 \approx (0.3064, 0.5812, 0.1123)$ and $x_{10} \approx (0.3002, 0.5994, 0.1004)$.
    The error roughly halves each week, as the second eigenvalue $0.5$ predicts.

In the long run $60\%$ of the fleet is at office $2$, whatever the start, so office $2$ needs the most parking.

## Remarks

### What the example shows

A regular stochastic matrix has exactly one steady state, and every start converges to it.
The second largest absolute value of an eigenvalue sets the speed, here $0.5$ per week.
The steady state is a property of the matrix alone, so the manager does not need to know where the cars were at the start.

### Watch out: regularity is needed

A stochastic matrix always has the eigenvalue $1$, but that alone does not give convergence.
The swap matrix $\begin{pmatrix} 0 & 1 \\ 1 & 0 \end{pmatrix}$ is stochastic and has the steady state $(\tfrac12, \tfrac12)$.
It also has the eigenvalue $-1$ on the unit circle, and the start $(1, 0)$ gives the orbit $(1, 0), (0, 1), (1, 0), \dots$, which never settles.
This matrix is irreducible, since each state leads to the other, but no power of it is positive, so it is not regular.

The steady state can also fail to be unique.
The identity matrix $I_2$ is stochastic, and every probability vector is a steady state of it.
So the correct test is regularity: some power of $P$ must have only positive entries.

### Change one column

Suppose that the cars of office $3$ now go to the three offices with probabilities $(0.1, 0.5, 0.4)$ instead of $(0.3, 0.3, 0.4)$.
The same elimination gives the steady state $(3, 7, 1)/11 \approx (0.273, 0.636, 0.091)$, so office $2$ gains share.
The other two eigenvalues become $0.35 \pm 0.132\, i$, of absolute value about $0.374$.
So the convergence is faster, and the states now spiral slightly around $q$.

### Where the theory lives

The general theory of stochastic matrices rests on the [[Perron-Frobenius theorem|62NS7PV1M9]] for nonnegative matrices.
Probability books often use the row convention $\pi P = \pi$ with rows that sum to $1$, and they call $\pi$ the [[stationary distribution|0KRH5157WP]]; that $P$ is the transpose of ours.
A two-state chain is worked out in [[a Markov chain with two states|N73KSZZ4V9]], and the ranking of web pages in [[PageRank as an eigenvector problem|9ZPQYZ5NDP]] is the same problem for a very large matrix.
Markov chains are a case of the [[linear discrete dynamical systems|2F1B461YN7]] of the previous example.

### Try it

First, find the steady state of $\begin{pmatrix} 0.9 & 0.2 \\ 0.1 & 0.8 \end{pmatrix}$.
The first row of $P - I$ gives $-0.1 x_1 + 0.2 x_2 = 0$, so $x_1 = 2 x_2$ and $q = (\tfrac23, \tfrac13)$.

Second, is $\begin{pmatrix} 0 & 0.5 \\ 1 & 0.5 \end{pmatrix}$ regular?
Its square is $\begin{pmatrix} 0.5 & 0.25 \\ 0.5 & 0.75 \end{pmatrix}$, which is positive, so it is regular and every orbit converges.

## Explanations

### L1 human

Imagine many cars that move each week between three offices, with fixed chances for each move.
After some weeks the share of cars at each office stops changing, even though single cars keep moving.
This stable mix is the steady-state vector.
Here it is $30\%$, $60\%$ and $10\%$, and the fleet reaches it from any start, for example from all cars at office $1$.

### L2 human

Here is a typical problem: in a town, each year $10\%$ of the people in the city move to the suburbs and $20\%$ of the people in the suburbs move to the city.
The column-stochastic matrix is $P = \begin{pmatrix} 0.9 & 0.2 \\ 0.1 & 0.8 \end{pmatrix}$, with city first.
One equation of $(P - I) x = 0$ is redundant, because the columns of $P - I$ sum to $0$, and the first row gives $x_1 = 2 x_2$.
Scaling to sum $1$ gives the steady state $(\tfrac23, \tfrac13)$.
All entries of $P$ are positive, so $P$ is regular and the split tends to two thirds in the city from every start.
This is the usual use of a steady state: a long-run share of a population, a market or the time that a random walker spends at each place.

### L3 human

For an irreducible stochastic matrix, the eigenvalues on the unit circle are exactly the $h$-th roots of unity, where $h$ is the period of the chain.
The chain is regular exactly when it is irreducible with $h = 1$, and then $P^k \to q \mathbf{1}^{\mathsf T}$, a matrix of rank one whose columns all equal $q$.
The convergence in total variation is geometric, with a rate set by the second eigenvalue, and the study of this rate is the theory of mixing times.
For infinite state spaces the same questions need operator theory and probability, and the answers can change.
