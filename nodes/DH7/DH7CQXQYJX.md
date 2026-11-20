---
tag: DH7CQXQYJX
kind: statement
role: theorem
name: Linear systems of ODEs by eigenvectors
aliases: [general-solution-of-a-linear-system-with-a-full-set-of-real-eigenvectors]
msc: ["34A30", "15A18"]
topics: [K0FNC6CWZN]
audience: ug2
uses: [0VJF99CZ0Z, 0ZND7NQ970, 0B5H4208Z9, 0CRMGPAH83]
about: [0469V0EN5N]
sources:
  - url: https://github.com/jirilebl/diffyqs/blob/658bcae9fb710f3fae2c9da4ca4524ce157453af/ch-systems.tex#L4365
    locator: ch-systems.tex:4365
  - book: isbn:9780321982384
    locator: Section 5.7
---

## Statement

Let $A$ be a real $n \times n$ matrix.
A solution of the [[homogeneous linear system with constant coefficients|0VJF99CZ0Z]] $x' = A x$ is a differentiable function $x : \mathbb R \to \mathbb C^n$ with $x'(t) = A x(t)$ for all $t$.
The derivative of a complex-valued function is the derivative of its real part plus $i$ times the derivative of its imaginary part.

1. **Eigen-solutions.** If $\lambda \in \mathbb C$ is an [[eigenvalue|0ZND7NQ970]] of $A$ with an [[eigenvector|0B5H4208Z9]] $v \in \mathbb C^n$, then $x(t) = e^{\lambda t} v$ is a solution.
2. **General solution.** Suppose that $v_1, \dots, v_n$ is a basis of $\mathbb C^n$ with $A v_j = \lambda_j v_j$, and let $P$ be the matrix with the columns $v_1, \dots, v_n$. Then the $n$ solutions $e^{\lambda_j t} v_j$ are [[linearly independent|0CRMGPAH83]], and every solution is
$$x(t) = c_1 e^{\lambda_1 t} v_1 + \dots + c_n e^{\lambda_n t} v_n, \qquad (c_1, \dots, c_n)^{\mathsf T} = P^{-1} x(0).$$
In particular, a solution is determined by its value $x(0)$.
If all $\lambda_j$ and $v_j$ are real and $x(0)$ is real, then all $c_j$ are real.
3. **Real solutions from complex eigenvalues.** Let $\lambda = \alpha + i \beta$ with $\beta \ne 0$ be an eigenvalue of $A$, with the eigenvector $v = a + i b$, where $a, b \in \mathbb R^n$. Then
$$\operatorname{Re}(e^{\lambda t} v) = e^{\alpha t} (a \cos \beta t - b \sin \beta t), \qquad \operatorname{Im}(e^{\lambda t} v) = e^{\alpha t} (a \sin \beta t + b \cos \beta t)$$
are real solutions.
Suppose also that $A$ has a basis of eigenvectors of $\mathbb C^n$.
Then $A$ has such a basis made of real eigenvectors for the real eigenvalues and of pairs $v$, $\bar v$ for the pairs $\lambda$, $\bar \lambda$ of non-real eigenvalues.
Replace the two solutions $e^{\lambda t} v$ and $e^{\bar\lambda t} \bar v$ of each pair by the two real solutions above.
The resulting $n$ real solutions are independent, and every real solution is a real combination of them.

## Remarks

### Why each hypothesis is needed

- *$v$ must be an eigenvector for $\lambda$.* If $e^{\lambda t} v$ is a solution, then at $t = 0$ its derivative $\lambda v$ equals $A v$. So no other vector gives a solution of this form.
- *Part 2 needs a basis of eigenvectors.* The matrix $A = \begin{pmatrix} 0 & 1 \\ 0 & 0 \end{pmatrix}$ has only the eigenvalue $0$, with the eigenvectors $c (1, 0)$. The function $x(t) = (t, 1)$ is a solution, since $x' = (1, 0) = A x$. It is not of the form $c\, e^{0 t} (1, 0)$, because its second entry is $1$.
- *Part 3 needs $A$ real.* For the $1 \times 1$ complex matrix $A = (i)$, the function $e^{i t}$ is a solution. Its real part $\cos t$ is not, since $(\cos t)' = -\sin t$ but $i \cos t$ is not real.

### Consequences

- If $A$ has a basis of eigenvectors and every eigenvalue has negative real part, then every solution tends to $0$ as $t \to \infty$, because $\abs{e^{\lambda t}} = e^{(\operatorname{Re} \lambda) t}$.
- Example with real eigenvalues: $A = \begin{pmatrix} 1 & 2 \\ 2 & 1 \end{pmatrix}$ has the eigenvalues $3$ and $-1$, with the eigenvectors $(1, 1)$ and $(1, -1)$. For $x(0) = (3, 1) = 2 (1, 1) + (1, -1)$, the solution is $x(t) = 2 e^{3t} (1, 1) + e^{-t} (1, -1)$. The origin is a saddle point.
- Example with complex eigenvalues: $A = \begin{pmatrix} 1 & -1 \\ 1 & 1 \end{pmatrix}$ has the eigenvalues $1 \pm i$, and $v = (1, -i)$ for $1 + i$, so $a = (1, 0)$ and $b = (0, -1)$. Part 3 gives the real solutions $e^{t} (\cos t, \sin t)$ and $e^{t} (\sin t, -\cos t)$. They spiral out from the origin, because the real part $1$ is positive.

### Converse

The converse of part 1 is true: if $e^{\lambda t} v$ with $v \ne 0$ is a solution, then $A v = \lambda v$, by the first item above.
The converse of part 2 is also true.
If every solution is a combination of solutions $e^{\lambda t} v$, then the values at $t = 0$ of these solutions span $\mathbb C^n$, because there is a solution for every initial value.
So the eigenvectors of $A$ span $\mathbb C^n$, and $A$ has a basis of eigenvectors.
The existence of a solution for every initial value is a theorem of ODE theory, and the [[matrix exponential|020M04FN1H]] gives it as $x(t) = e^{t A} x(0)$.

### Generalizations

- For every square matrix, the solutions are $x(t) = e^{t A} x(0)$. When $A$ has no eigenbasis, its Jordan form gives terms $t^m e^{\lambda t}$.
- The inhomogeneous system $x' = A x + f(t)$ has the solutions $x = x_{\mathrm p} + x_{\mathrm h}$, with one particular solution and a solution of the homogeneous system.
- The discrete analogue $x_{k+1} = A x_k$ has $\lambda^k v$ in place of $e^{\lambda t} v$, as in [[linear discrete dynamical systems|2F1B461YN7]].
- The existence, uniqueness and stability theory of differential equations belongs to ODE theory.

## Explanations

### L1 human

In some problems, several quantities change at rates that depend on all of them, such as the amounts of a substance in two connected tanks.
In a few special directions, the system only stretches or shrinks: these are the eigenvector directions.
Along such a direction, the solution grows or decays exponentially, like money with interest.
Every other solution is a mixture of these simple ones.
For the matrix with rows $(1, 2)$ and $(2, 1)$, one direction grows like $e^{3t}$, and the other decays like $e^{-t}$.

### L2 human

To solve $x' = A x$ with $x(0) = x_0$, do these steps.

1. Find the eigenvalues $\lambda_j$ and a basis of eigenvectors $v_j$.
2. Solve $P c = x_0$ for the coefficients $c_j$.
3. Write $x(t) = \sum_j c_j e^{\lambda_j t} v_j$.
4. For a real answer with complex eigenvalues, take the real and imaginary parts of $e^{\lambda t} v$ for one eigenvalue of each conjugate pair.

Worked example: $A = \begin{pmatrix} 1 & 2 \\ 2 & 1 \end{pmatrix}$ and $x_0 = (3, 1)$.
Steps 1 and 2 give $c = (2, 1)$, so $x(t) = (2 e^{3t} + e^{-t},\ 2 e^{3t} - e^{-t})$.
Check the first entry: $x_1' = 6 e^{3t} - e^{-t}$, and $x_1 + 2 x_2 = 6 e^{3t} - e^{-t}$.

The typical use is in mechanics, circuits and chemical kinetics, where the eigenvalues give the rates and the frequencies.
The trap is to keep only the real part of $e^{\lambda t} v$.
One pair of complex eigenvalues gives two real solutions, the real part and the imaginary part.

### L3 human

The map $x \mapsto x(0)$ is an isomorphism from the solution space onto $\mathbb C^n$, and the flow $x(0) \mapsto x(t)$ is the linear map $e^{t A}$.
In an eigenbasis, $e^{t A} = P \operatorname{diag}(e^{\lambda_1 t}, \dots, e^{\lambda_n t}) P^{-1}$, and the system decouples into $n$ scalar equations.
The same idea solves the heat and wave equations, where the eigenvectors of a differential operator are functions such as $\sin k x$.
The phase portraits of the real $2 \times 2$ systems, with nodes, saddles, spirals and centres, are classified by the trace and the determinant of $A$.
