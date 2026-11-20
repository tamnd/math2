---
tag: AC3XJ3DC9X
kind: example
name: Fibonacci numbers by diagonalizing the Fibonacci matrix
msc: ["15A20", "11B39"]
topics: [Z6S6PWMJPH]
audience: ug1
instance_of: [0TNR9BQ871, 07SQCNV233, D0AP2R7272]
illustrates: [0Y95Z7MT02]
uses: [0Y17PEKF24, 0YA7X86K05, 0ZND7NQ970, 0B5H4208Z9]
sources:
  - url: https://en.wikipedia.org/wiki/Fibonacci_sequence
    locator: Matrix form
  - url: https://en.wikipedia.org/wiki/Diagonalizable_matrix
    locator: Application to matrix functions
---

## Example

The [[Fibonacci numbers|0GA9K57A39]] are $F_0 = 0$, $F_1 = 1$ and $F_{k+1} = F_k + F_{k-1}$ for $k \ge 1$.
Let $A = \begin{pmatrix} 1 & 1 \\ 1 & 0 \end{pmatrix}$ over $\R$.
We compute $A^k$ by [[diagonalization|07SQCNV233]] and obtain [[Binet's formula|0404D8TN7Y]].

1. The recurrence in vector form is $\begin{pmatrix} F_{k+1} \\ F_k \end{pmatrix} = A \begin{pmatrix} F_k \\ F_{k-1} \end{pmatrix}$. By induction on $k \ge 1$, $A^k = \begin{pmatrix} F_{k+1} & F_k \\ F_k & F_{k-1} \end{pmatrix}$.
2. For example, $A^2 = \begin{pmatrix} 2 & 1 \\ 1 & 1 \end{pmatrix}$, $A^3 = \begin{pmatrix} 3 & 2 \\ 2 & 1 \end{pmatrix}$, $A^4 = \begin{pmatrix} 5 & 3 \\ 3 & 2 \end{pmatrix}$, $A^5 = \begin{pmatrix} 8 & 5 \\ 5 & 3 \end{pmatrix}$ and $A^6 = \begin{pmatrix} 13 & 8 \\ 8 & 5 \end{pmatrix}$.
3. The characteristic polynomial is $p_A = (t - 1) t - 1 = t^2 - t - 1$.
4. Its roots are $\varphi = \frac{1 + \sqrt 5}{2}$ and $\psi = \frac{1 - \sqrt 5}{2}$. They are distinct, so $A$ is diagonalizable by [[distinct eigenvalues imply diagonalizable|0Y95Z7MT02]].
5. From $p_A$, we get $\varphi + \psi = 1$, $\varphi \psi = -1$ and $\varphi^2 = \varphi + 1$.
6. Eigenvectors: $A (\varphi, 1) = (\varphi + 1, \varphi) = (\varphi^2, \varphi) = \varphi (\varphi, 1)$. In the same way, $A(\psi, 1) = \psi (\psi, 1)$.
7. Let $P = \begin{pmatrix} \varphi & \psi \\ 1 & 1 \end{pmatrix}$. Then $\det P = \varphi - \psi = \sqrt 5$ and $P^{-1} = \frac{1}{\sqrt 5} \begin{pmatrix} 1 & -\psi \\ -1 & \varphi \end{pmatrix}$.
8. So $A = P \operatorname{diag}(\varphi, \psi) P^{-1}$, and $A^k = P \operatorname{diag}(\varphi^k, \psi^k) P^{-1}$.
9. The entry $(2, 1)$ of $A^k$ is row $2$ of $P \operatorname{diag}(\varphi^k, \psi^k)$, which is $(\varphi^k, \psi^k)$, times column $1$ of $P^{-1}$, which is $\frac{1}{\sqrt 5}(1, -1)$.
10. By step 1, this entry is $F_k$. So $F_k = \dfrac{\varphi^k - \psi^k}{\sqrt 5}$ for $k \ge 1$, and the formula also gives $F_0 = 0$.

Check of the first terms:

- $k = 1$: $(\varphi - \psi)/\sqrt 5 = \sqrt 5 / \sqrt 5 = 1$.
- $k = 2$: $(\varphi^2 - \psi^2)/\sqrt 5 = (\varphi - \psi)(\varphi + \psi)/\sqrt 5 = 1$.
- $k = 3$: $\varphi^3 = \varphi^2 + \varphi = 2 \varphi + 1$ and $\psi^3 = 2 \psi + 1$, so the formula gives $2(\varphi - \psi)/\sqrt 5 = 2$.
- $k = 4$: $\varphi^4 = 3 \varphi + 2$ and $\psi^4 = 3 \psi + 2$, so the formula gives $3$.
- The formula gives $0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55$ for $k = 0, \dots, 10$.

## Remarks

- Since $|\psi| < 1$, the term $\psi^k / \sqrt 5$ has absolute value less than $\tfrac{1}{2}$. So $F_k$ is the integer nearest to $\varphi^k / \sqrt 5$.
- For $k = 10$, $\varphi^{10} / \sqrt 5 \approx 55.0036$, and $F_{10} = 55$.
- The ratio $F_{k+1} / F_k$ tends to $\varphi \approx 1.618$, the dominant eigenvalue. This is the power method for $A$.
- Taking determinants in step 1 gives Cassini's identity $F_{k+1} F_{k-1} - F_k^2 = \det A^k = (-1)^k$.
- The same method solves every [[linear recurrence|0YA7X86K05]] whose characteristic polynomial has distinct roots.
- The method needs $\sqrt 5$ in the field. Over $\mathbb{Q}$, $A$ is not diagonalizable, since $p_A$ has no rational root, so the computation takes place in $\mathbb{Q}(\sqrt 5)$ or $\R$.

## Explanations

### L1 human

Each Fibonacci number is the sum of the two before it.
A $2 \times 2$ matrix moves the pair of the last two numbers one step forward.
This matrix has two special directions, with stretch factors about $1.618$ and $-0.618$.
Writing the start in these directions gives a direct formula for each Fibonacci number.

### L2 human

Compute $F_{12}$ with the formula of step 10.

1. $\varphi^{12} \approx 321.9969$ and $|\psi^{12}| \approx 0.0031$.
2. $F_{12} = (\varphi^{12} - \psi^{12}) / \sqrt 5$, and $\sqrt 5 \approx 2.2361$.
3. So $F_{12} \approx 321.9969 / 2.2361 \approx 144.0014$, and the nearest integer is $144$.
4. Check by the recurrence: $F_{11} = 34 + 55 = 89$ and $F_{12} = 55 + 89 = 144$.

The typical use is a closed formula for a linear recurrence, from the eigenvalues of its companion matrix.
The trap is to forget the term $\psi^k$: it is small, but without it $\varphi^k / \sqrt 5$ is never an integer.

### L3 human

The matrix $A$ is the companion matrix of $t^2 - t - 1$, and its eigenvalues lie in the quadratic field $\mathbb{Q}(\sqrt 5)$.
The ring $\mathbb{Z}[\varphi]$ and the identity $\varphi^k = F_k \varphi + F_{k-1}$ give the same formula without matrices.
For an odd prime $p \ne 5$, $A$ is diagonalizable over $\mathbb{F}_p$ exactly when $5$ is a square mod $p$.
This explains periodicity facts about the Fibonacci numbers mod $p$.
For $p = 5$, $p_A = (t - 3)^2$ over $\mathbb{F}_5$, and $A$ is not diagonalizable, since $A \ne 3I$.
