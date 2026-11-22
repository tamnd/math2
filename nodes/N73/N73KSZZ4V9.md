---
tag: N73KSZZ4V9
kind: example
name: A Markov chain with two states
msc: ["15A18", "60J10"]
topics: [6R1D6QPY3S]
audience: ug1
instance_of: [32M8VY9A1M]
uses: [32M8VY9A1M, 039HF58KQ5, 0ZND7NQ970, 0B5H4208Z9]
sources:
  - url: https://en.wikipedia.org/wiki/Eigenvalues_and_eigenvectors
    locator: Markov chains
  - book: isbn:9780134860244
---

## Example

A chain has two states, $1$ and $2$.
From state $1$ it stays with probability $9/10$ and moves with probability $1/10$; from state $2$ it moves or stays with probability $1/2$ each.
The transition matrix, with entry $(i, j)$ the probability of a step from $i$ to $j$, is
$$P = \begin{pmatrix} 9/10 & 1/10 \\ 1/2 & 1/2 \end{pmatrix},$$
and each row sums to $1$.
A probability row vector $\pi$ with $\pi P = \pi$ is a *stationary distribution*, and it is a [[left eigenvector|32M8VY9A1M]] for the eigenvalue $1$.

1. Since each row sums to $1$, multiplying $P$ by the column of ones adds up each row:
$$P \begin{pmatrix} 1 \\ 1 \end{pmatrix} = \begin{pmatrix} 1 \\ 1 \end{pmatrix}.$$
   So $1$ is an [[eigenvalue|0ZND7NQ970]] of $P$, with the right [[eigenvector|0B5H4208Z9]] $(1, 1)^{\mathsf{T}}$.
2. The trace is $\tfrac{9}{10} + \tfrac{1}{2} = \tfrac{7}{5}$ and the determinant is $\tfrac{9}{20} - \tfrac{1}{20} = \tfrac{2}{5}$, so the [[characteristic polynomial|039HF58KQ5]] is
$$p_P(t) = t^2 - \tfrac{7}{5} t + \tfrac{2}{5} = (t - 1)\big(t - \tfrac{2}{5}\big).$$
   Check: $1 + \tfrac{2}{5} = \tfrac{7}{5}$ and $1 \cdot \tfrac{2}{5} = \tfrac{2}{5}$.
3. To find $\pi = (a, b)$, write out $\pi P = \pi$.
   The first entry gives $\tfrac{9}{10} a + \tfrac{1}{2} b = a$, that is, $b = \tfrac{1}{5} a$.
   With $a + b = 1$ this gives $a = \tfrac{5}{6}$ and $b = \tfrac{1}{6}$.
4. Check both entries of $\pi P$ for $\pi = (5/6, 1/6)$:
$$\tfrac{5}{6} \cdot \tfrac{9}{10} + \tfrac{1}{6} \cdot \tfrac{1}{2} = \tfrac{45}{60} + \tfrac{5}{60} = \tfrac{5}{6}, \qquad \tfrac{5}{6} \cdot \tfrac{1}{10} + \tfrac{1}{6} \cdot \tfrac{1}{2} = \tfrac{5}{60} + \tfrac{5}{60} = \tfrac{1}{6}.$$
   So $\pi P = \pi$.
5. For the eigenvalue $2/5$, the row $(1, -1)$ is a left eigenvector:
$$(1, -1) P = \big(\tfrac{9}{10} - \tfrac{1}{2}, \; \tfrac{1}{10} - \tfrac{1}{2}\big) = \big(\tfrac{2}{5}, -\tfrac{2}{5}\big) = \tfrac{2}{5}(1, -1).$$

## Remarks

The right eigenvector $(1, 1)^{\mathsf{T}}$ and the left eigenvector $\pi$ belong to the same eigenvalue $1$, but they are different vectors.
The left eigenvector $(1, -1)$ for $2/5$ has product $1 - 1 = 0$ with the right eigenvector $(1, 1)^{\mathsf{T}}$ for $1$, as biorthogonality requires.

The second eigenvalue controls the speed of the chain.
Every starting distribution $\mu$ with entries summing to $1$ can be written $\mu = \pi + c(1, -1)$, so after $k$ steps
$$\mu P^k = \pi + c \big(\tfrac{2}{5}\big)^k (1, -1),$$
which tends to $\pi$ because $\lvert 2/5 \rvert < 1$.
If the chain left state $1$ with probability $1/2$ in place of $1/10$, the matrix would have all entries $1/2$, the second eigenvalue would be $0$, and the chain would reach $(1/2, 1/2)$ after one step.

## Explanations

### L1 human

Think of state $1$ as a sunny day and state $2$ as a rainy day.
A sunny day is followed by sun nine times in ten, and a rainy day is followed by sun half the time.
In the long run the chain spends $5/6$ of the days in sun and $1/6$ in rain.
The row $(5/6, 1/6)$ does not change after one more step, and that is what it means to be a left eigenvector with factor $1$.

### L2 human

The typical use is to find the long-run distribution by solving $\pi P = \pi$ together with $a + b = 1$, as in step 3.
The second eigenvalue $2/5$ then says how fast the chain forgets its start: the distance to $\pi$ shrinks by the factor $2/5$ at each step.
Watch out: solving $Pv = v$ gives only the column of ones, which says nothing about the long run, because the chain acts on rows from the left of $P$.
