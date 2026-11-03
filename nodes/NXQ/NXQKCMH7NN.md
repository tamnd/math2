---
tag: NXQKCMH7NN
kind: statement
role: theorem
name: Schmidt decomposition
msc: [81P40, 15A18]
uses: [EY0X2NKA3S, 0S9GGTR0EX, 000NPTMX6J, 09VMDSRXWJ, SQ3J7AVMKM, CHNXT8CCK7]
about: [EY0X2NKA3S]
sources:
  - url: https://en.wikipedia.org/wiki/Schmidt_decomposition
same_as:
  wikidata: Q2246292
  wikipedia: Schmidt decomposition
---

## Statement

Let $H_A$ and $H_B$ be complex Hilbert spaces of finite dimensions $n$ and $m$.
Let $\psi$ be a nonzero vector of the [[tensor product|EY0X2NKA3S]] $H_A \otimes H_B$.
Then there are an integer $r$ with $1 \le r \le \min(n, m)$, real numbers $\lambda_1 \ge \dots \ge \lambda_r > 0$, and [[orthonormal|0S9GGTR0EX]] families $e_1, \dots, e_r$ in $H_A$ and $f_1, \dots, f_r$ in $H_B$ such that
$$\psi = \sum_{i=1}^{r} \lambda_i \, e_i \otimes f_i.$$
The number $r$ and the numbers $\lambda_1, \dots, \lambda_r$ are determined by $\psi$.

## Remarks

Fix orthonormal bases and write $\psi = \sum_{j,k} c_{jk} \, u_j \otimes v_k$.
The [[singular value decomposition|000NPTMX6J]] $C = U \Sigma V^*$ of the $n \times m$ matrix $C = (c_{jk})$ gives the result.
The $\lambda_i$ are the nonzero [[singular values|09VMDSRXWJ]] of $C$, the $e_i$ come from the columns of $U$, and the $f_i$ from the columns of $\overline{V}$.
Uniqueness of $r$ and of the $\lambda_i$ follows because they are the rank and the singular values of $C$.

The $\lambda_i$ are the *Schmidt coefficients* and $r$ is the *Schmidt rank*.
If $\psi$ is a unit vector, then $\sum_i \lambda_i^2 = 1$.
The [[partial traces|SQ3J7AVMKM]] of $|\psi\rangle\langle\psi|$ are $\rho_A = \sum_i \lambda_i^2 |e_i\rangle\langle e_i|$ and $\rho_B = \sum_i \lambda_i^2 |f_i\rangle\langle f_i|$.
So the two reduced states have the same nonzero eigenvalues.
A unit vector $\psi$ is [[entangled|CHNXT8CCK7]] if and only if its Schmidt rank is at least $2$.

Example: $\psi = \tfrac12(|00\rangle + |01\rangle + |10\rangle + |11\rangle) = |{+}\rangle \otimes |{+}\rangle$ with $|{+}\rangle = (|0\rangle + |1\rangle)/\sqrt{2}$ has Schmidt rank $1$, although it has four terms in the standard basis.

The decomposition is special to two factors.
For three or more factors, a vector in general has no expansion $\sum_i \lambda_i \, e_i \otimes f_i \otimes g_i$ with orthonormal families in each factor.

## Explanations

### L1 human

Any state of two quantum systems can be written as a sum of matched pairs of states.
Each term pairs a state of the first system with a state of the second, and different terms use perpendicular states on both sides.
The weights of the terms measure how strongly the two systems are linked.
With one term, the systems are independent; with several, they are entangled.

### L2 human

The Schmidt decomposition is the singular value decomposition in the language of tensor products.
It shows at once that the two reduced density matrices of a pure state share their nonzero spectrum, so they have the same von Neumann entropy.
That common entropy is the standard measure of entanglement of a pure bipartite state.
The decomposition is also the main step in the proof that purifications exist and are unique up to a unitary on the purifying system.
