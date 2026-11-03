---
tag: B155C8KRHR
kind: definition
name: Iterative learning control
msc: [93C55, 93B52, 93C83]
defines: 2RKN6NED1W
uses: [7NYES2D0Z4, 0ZND7NQ970]
sources:
  - url: https://en.wikipedia.org/wiki/Iterative_learning_control
---

## Definition

Fix a trial length $N \ge 1$.
Consider a discrete-time system that is run repeatedly, with trial index $j = 0, 1, 2, \dots$:
$$x_j(t+1) = A x_j(t) + B u_j(t), \qquad 0 \le t \le N - 1,$$
with output $y_j(t) = C x_j(t)$ for $0 \le t \le N$.
Every trial starts from the same initial state $x_j(0) = x_0$.
Let $y_d(1), \dots, y_d(N)$ be a reference output, the same for all trials, and let $e_j(t) = y_d(t) - y_j(t)$ be the tracking error of trial $j$.
An *iterative learning control* law computes the input of the next trial from the data of past trials.
The typical form is
$$u_{j+1}(t) = u_j(t) + L \, e_j(t+1), \qquad 0 \le t \le N - 1,$$
with a learning gain matrix $L$ and an initial input $u_0$.
The law is convergent if $e_j(t) \to 0$ as $j \to \infty$, for each $t = 1, \dots, N$.

## Remarks

Stack the signals of one trial into vectors $\mathbf{u}_j = (u_j(0), \dots, u_j(N-1))$ and $\mathbf{e}_j = (e_j(1), \dots, e_j(N))$.
Then $\mathbf{y}_j = \mathbf{P} \mathbf{u}_j + \mathbf{d}$, where $\mathbf{P}$ is block lower triangular with the Markov parameters $CB, CAB, \dots$ and $\mathbf{d}$ comes from $x_0$.
The update gives $\mathbf{e}_{j+1} = (I - \mathbf{P} \mathbf{L}) \mathbf{e}_j$, with $\mathbf{L} = \operatorname{diag}(L, \dots, L)$.
The matrix $I - \mathbf{P}\mathbf{L}$ is block lower triangular with diagonal blocks $I - CBL$.
So the error tends to $0$ for every reference and every initial input exactly when all [[eigenvalues|0ZND7NQ970]] of $I - CBL$ have modulus less than $1$.
Example: the scalar system $x(t+1) = 2 x(t) + u(t)$, $y = x$, with $L = 1/2$.
Here $CB = 1$ and $1 - CBL = 1/2$, so the learning converges, even though the system itself is unstable.
Non-example: a [[feedback|7NYES2D0Z4]] law $u_j(t) = K e_j(t)$ that uses only the current trial does not learn across trials; it gives the same error in every trial.
