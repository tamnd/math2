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
We compute $A^k$ by [[diagonalization|07SQCNV233]] and obtain [[Binet's formula|0404D8TN7Y]]
$$F_k = \frac{\varphi^k - \psi^k}{\sqrt 5}, \qquad \varphi = \frac{1 + \sqrt 5}{2}, \quad \psi = \frac{1 - \sqrt 5}{2}.$$

1. The recurrence in vector form is $\begin{pmatrix} F_{k+1} \\ F_k \end{pmatrix} = A \begin{pmatrix} F_k \\ F_{k-1} \end{pmatrix}$.
   By induction on $k \ge 1$ this gives
   $$A^k = \begin{pmatrix} F_{k+1} & F_k \\ F_k & F_{k-1} \end{pmatrix}.$$
   For example, $A^2 = \begin{pmatrix} 2 & 1 \\ 1 & 1 \end{pmatrix}$, $A^3 = \begin{pmatrix} 3 & 2 \\ 2 & 1 \end{pmatrix}$ and $A^4 = \begin{pmatrix} 5 & 3 \\ 3 & 2 \end{pmatrix}$.
2. The characteristic polynomial is
   $$p_A(t) = (t - 1) t - 1 = t^2 - t - 1.$$
3. Its roots are $\varphi$ and $\psi$.
   They are distinct, so $A$ is diagonalizable over $\R$ by [[distinct eigenvalues imply diagonalizable|0Y95Z7MT02]].
   Reading off the coefficients of $p_A$ gives $\varphi + \psi = 1$ and $\varphi \psi = -1$, and $p_A(\varphi) = 0$ gives $\varphi^2 = \varphi + 1$.
4. The vector $(\varphi, 1)$ is an eigenvector for $\varphi$, because
   $$A \begin{pmatrix} \varphi \\ 1 \end{pmatrix} = \begin{pmatrix} \varphi + 1 \\ \varphi \end{pmatrix} = \begin{pmatrix} \varphi^2 \\ \varphi \end{pmatrix} = \varphi \begin{pmatrix} \varphi \\ 1 \end{pmatrix}.$$
   In the same way, $(\psi, 1)$ is an eigenvector for $\psi$.
5. Put the eigenvectors into the columns of $P$.
   Then $\det P = \varphi - \psi = \sqrt 5$, and
   $$P = \begin{pmatrix} \varphi & \psi \\ 1 & 1 \end{pmatrix}, \qquad P^{-1} = \frac{1}{\sqrt 5} \begin{pmatrix} 1 & -\psi \\ -1 & \varphi \end{pmatrix}.$$
6. Check $A = P \operatorname{diag}(\varphi, \psi) P^{-1}$ by multiplying out, with $\varphi^2 - \psi^2 = (\varphi - \psi)(\varphi + \psi) = \sqrt 5$ and $\varphi \psi (\psi - \varphi) = \sqrt 5$:
   $$\begin{pmatrix} \varphi^2 & \psi^2 \\ \varphi & \psi \end{pmatrix} \frac{1}{\sqrt 5} \begin{pmatrix} 1 & -\psi \\ -1 & \varphi \end{pmatrix} = \frac{1}{\sqrt 5} \begin{pmatrix} \varphi^2 - \psi^2 & \varphi \psi (\psi - \varphi) \\ \varphi - \psi & 0 \end{pmatrix} = \begin{pmatrix} 1 & 1 \\ 1 & 0 \end{pmatrix}.$$
7. So $A^k = P \operatorname{diag}(\varphi^k, \psi^k) P^{-1}$.
   Its entry $(2, 1)$ is row $2$ of $P \operatorname{diag}(\varphi^k, \psi^k)$, which is $(\varphi^k, \psi^k)$, times column $1$ of $P^{-1}$, which is $\tfrac{1}{\sqrt 5}(1, -1)$.
8. By step 1 this entry is $F_k$, so $F_k = (\varphi^k - \psi^k) / \sqrt 5$ for $k \ge 1$.
   For $k = 0$ the formula gives $0 = F_0$ as well.

Check the first terms.
For $k = 1$ the formula gives $(\varphi - \psi)/\sqrt 5 = 1$, and for $k = 2$ it gives $(\varphi - \psi)(\varphi + \psi)/\sqrt 5 = 1$.
For $k = 3$, the rule $\varphi^2 = \varphi + 1$ gives $\varphi^3 = \varphi^2 + \varphi = 2 \varphi + 1$, and in the same way $\psi^3 = 2 \psi + 1$, so the formula gives $2(\varphi - \psi)/\sqrt 5 = 2$.
For $k = 4$, $\varphi^4 = 3 \varphi + 2$ and $\psi^4 = 3 \psi + 2$, so the formula gives $3$.

## Remarks

### The nearest integer

Since $|\psi| \approx 0.618 < 1$, the term $\psi^k / \sqrt 5$ has absolute value less than $\tfrac{1}{2}$ for every $k \ge 0$.
So $F_k$ is the integer nearest to $\varphi^k / \sqrt 5$.
For $k = 10$, $\varphi^{10} / \sqrt 5 \approx 55.0036$, and indeed $F_{10} = 55$.
The ratio $F_{k+1} / F_k$ tends to $\varphi \approx 1.618$, the eigenvalue of larger absolute value, which is [[power iteration|H4MQD841BR]] for $A$.

### More from the matrix

Taking determinants in step 1 gives [[Cassini's identity|01WQZK97Z5]], since $\det A^k = (\det A)^k$:
$$F_{k+1} F_{k-1} - F_k^2 = (-1)^k.$$
The same method solves every [[linear recurrence|0YA7X86K05]] whose characteristic polynomial has distinct roots, through the [[companion matrix|0ZCWPNZTQ3]] of the recurrence.

### What changes with the field

The method needs $\sqrt 5$ in the field.
Over $\mathbb{Q}$ the polynomial $t^2 - t - 1$ has no root, because its only possible rational roots are $\pm 1$, so $A$ has no eigenvalue in $\mathbb{Q}$ and is not diagonalizable over $\mathbb{Q}$.
The computation therefore takes place in $\mathbb{Q}(\sqrt 5)$ or in $\R$, and the final answer is still an integer.

## Explanations

### L1 human

Each Fibonacci number is the sum of the two before it.
A $2 \times 2$ matrix moves the pair of the last two numbers one step forward.
This matrix has two special directions, with stretch factors about $1.618$ and $-0.618$.
After many steps the first factor wins, and each Fibonacci number is about $1.618$ times the one before.
Writing the start in the two special directions gives a direct formula for every Fibonacci number.

### L2 human

Let us compute $F_{12}$ with the formula.
The two powers are $\varphi^{12} \approx 321.9969$ and $\psi^{12} \approx 0.0031$, and $\sqrt 5 \approx 2.2361$.
So
$$F_{12} = \frac{\varphi^{12} - \psi^{12}}{\sqrt 5} \approx \frac{321.9938}{2.2361} \approx 144.0,$$
and the nearest integer is $144$.
Check by the recurrence: $F_{11} = 34 + 55 = 89$ and $F_{12} = 55 + 89 = 144$.
The typical use is a closed formula for a linear recurrence from the eigenvalues of its matrix.
The trap is to drop the term $\psi^k$: it is small, but $\varphi^k / \sqrt 5$ alone is never an integer for $k \ge 1$.
Indeed $\varphi^k = F_k \varphi + F_{k-1}$ gives $\varphi^k / \sqrt 5 = F_k / 2 + (F_k + 2 F_{k-1}) / (2 \sqrt 5)$, and the last term is irrational because $F_k + 2 F_{k-1} > 0$.

### L3 human

The matrix $A$ is the companion matrix of $t^2 - t - 1$, whose roots generate the quadratic field $\mathbb{Q}(\sqrt 5)$.
In the ring $\mathbb{Z}[\varphi]$ the identity $\varphi^k = F_k \varphi + F_{k-1}$ gives the same formula without matrices.
Over a finite field $\mathbb{F}_p$ with $p$ an odd prime other than $5$, the discriminant $5$ of $p_A$ is nonzero, so $A$ is diagonalizable over $\mathbb{F}_p$ exactly when $5$ is a square mod $p$.
In that case both eigenvalues lie in $\mathbb{F}_p^{\times}$, so $A^{p-1} = I$ and the Fibonacci numbers mod $p$ repeat with a period that divides $p - 1$; for $p = 11$ the period is $10$.
For $p = 5$, $p_A = (t - 3)^2$ over $\mathbb{F}_5$, and $A$ is not diagonalizable there, since $A \ne 3I$.
