---
tag: CPQWYPXQPN
kind: proof
name: Proof of the eigenvalue criteria for stability of linear systems via the Jordan normal form
msc: [34D20, 34A30]
proves: 0SKVEMXJWF
uses: [0VJF99CZ0Z, 0YC8JT513J, 0K665H5V1S, 02903SSA48, 092S6VBECQ, 05Y1JAM3Y5, 0RFWW56Y22, 0WS1A8E2P9, 085HQ5G5TE, 0PBFS92AJP, 0419GJC84P, 04BD23PSK5, 0WM7DJCM6G, F6PH4JEGS5, 0CT6CBGTYY, 0TYMASG33Y, 0K1KKMFHYH, 053QVHF6N7, 039HF58KQ5, 03XVP8Q4GY, 06YSJVR356, TR48YQGCCA]
sources:
  - url: https://www.mat.univie.ac.at/~gerald/ftp/book-ode/ode.pdf
    locator: Section 3.2, Corollaries 3.5 and 3.6
---

## Proof

We reduce both kinds of stability to the behaviour of the entries of $e^{tA}$, and compute these entries from the Jordan normal form of $A$.

Reduction to the matrix exponential.

1. Let $\norm{\cdot}$ be the Euclidean norm on $\C^n$. For a complex $n \times n$ matrix $M = (m_{ij})$, the [[Cauchy–Schwarz inequality|0RFWW56Y22]] applied to each row gives $\norm{M z} \le \left( \sum_{i,j} \abs{m_{ij}}^2 \right)^{1/2} \norm{z}$ for $z \in \C^n$.
2. Let $e_1, \dots, e_n$ be the standard basis. Then $\abs{m_{ij}} \le \norm{M e_j}$, because $m_{ij}$ is the $i$-th coordinate of $M e_j$.
3. By the theorem on the [[derivative of the matrix exponential|0YC8JT513J]], $t \mapsto e^{tA} x_0$ is the unique solution of $x' = Ax$, $x(0) = x_0$ on $\R$. So the [[flow|02903SSA48]] of the [[linear system|0VJF99CZ0Z]] is $\varphi_t(x_0) = e^{tA} x_0$, defined for all $t \in \R$.
4. Claim A: $0$ is [[Lyapunov stable|092S6VBECQ]] if and only if all entries of $e^{tA}$ are bounded on $[0, \infty)$.
5. Proof of "if". Let $c$ bound all entries. By step 1, $\norm{e^{tA} x_0} \le n c \norm{x_0}$ for $t \ge 0$. Given $\varepsilon > 0$, the number $\delta = \varepsilon / (nc + 1)$ works.
6. Proof of "only if". Take $\varepsilon = 1$ and its $\delta > 0$. The vector $y = (\delta/2) e_j$ has $\norm{y} < \delta$, so $\norm{e^{tA} y} < 1$ for $t \ge 0$. By linearity $\norm{e^{tA} e_j} < 2/\delta$, and step 2 bounds every entry by $2/\delta$.
7. Claim B: $0$ is [[asymptotically stable|05Y1JAM3Y5]] if and only if all entries of $e^{tA}$ tend to $0$ as $t \to \infty$.
8. Proof of "only if". Let $\eta > 0$ be as in the definition. For $y = (\eta/2) e_j$ we have $e^{tA} y \to 0$. So the column $e^{tA} e_j$ tends to $0$, for each $j$.
9. Proof of "if". By step 1, $e^{tA} x_0 \to 0$ for every $x_0$. Each entry is continuous and tends to $0$. So it is below $1$ in modulus for $t \ge T$, and bounded on $[0, T]$ by the [[extreme value theorem|0WS1A8E2P9]]. By Claim A, $0$ is also Lyapunov stable.

Entries of $e^{tJ}$.

10. By the [[Jordan normal form|085HQ5G5TE]] over $\C$, there are an invertible complex matrix $P$ and a block diagonal matrix $J$ with $A = P J P^{-1}$. The diagonal blocks are [[Jordan blocks|0PBFS92AJP]] $J_{k_1}(\lambda_1), \dots, J_{k_r}(\lambda_r)$.
11. We have $(P J P^{-1})^m = P J^m P^{-1}$ for each $m \ge 0$. The entries of $P X P^{-1}$ are fixed linear combinations of the entries of $X$. Taking limits of partial sums in the [[matrix exponential|0K665H5V1S]] gives $e^{tA} = P e^{tJ} P^{-1}$.
12. Since also $e^{tJ} = P^{-1} e^{tA} P$, the entries of $e^{tA}$ are all bounded on $[0, \infty)$ if and only if those of $e^{tJ}$ are. The same holds for convergence of all entries to $0$.
13. Powers of a block diagonal matrix are block diagonal, with the powers of the blocks on the diagonal. So $e^{tJ}$ is block diagonal with blocks $e^{t J_{k_i}(\lambda_i)}$.
14. Fix a block $J_k(\lambda) = \lambda I + N$. Here $N$ has ones just above the diagonal and zeros elsewhere. By induction on $j$, $N^j$ has ones at the places $(p, p + j)$ and zeros elsewhere. So $N$ is [[nilpotent|0419GJC84P]] with $N^k = 0$.
15. The matrices $t\lambda I$ and $tN$ commute. By the [[exponential of a sum of commuting matrices|04BD23PSK5]], $e^{t J_k(\lambda)} = e^{t \lambda I} e^{tN} = e^{\lambda t} \sum_{j=0}^{k-1} \frac{t^j}{j!} N^j$.
16. So the entry at $(p, p + j)$ of $e^{t J_k(\lambda)}$ is $e^{\lambda t} t^j / j!$ for $0 \le j \le k - 1$, and all other entries are $0$.
17. Let $\mu = \operatorname{Re} \lambda$. By the [[product of exponentials|0WM7DJCM6G]] and [[Euler's formula|F6PH4JEGS5]], $\abs{e^{\lambda t}} = e^{\mu t}$.
18. If $\mu < 0$ and $j \ge 0$, then $t^j e^{\mu t} \to 0$ as $t \to \infty$. Indeed, with $x = -\mu t$ we get $t^j e^{\mu t} = (-\mu)^{-j} x^j e^{-x}$, and $e^x / x^j \to \infty$ because [[exponential growth beats polynomial growth|0CT6CBGTYY]].
19. All entries of $e^{tJ}$ tend to $0$ if and only if every $\lambda_i$ has $\operatorname{Re} \lambda_i < 0$. "If" follows from steps 16 to 18. For "only if", a block with $\mu \ge 0$ has diagonal entries of modulus $e^{\mu t} \ge 1$.
20. All entries of $e^{tJ}$ are bounded on $[0, \infty)$ if and only if each block has $\operatorname{Re} \lambda_i < 0$, or has $\operatorname{Re} \lambda_i = 0$ and size $k_i = 1$.
21. Proof of step 20, "if". Entries of blocks with $\mu < 0$ tend to $0$, so they are bounded as in step 9. A block of size $1$ with $\mu = 0$ is $e^{\lambda t}$, of modulus $1$.
22. Proof of step 20, "only if". If $\mu > 0$, a diagonal entry has modulus $e^{\mu t}$, which is unbounded. If $\mu = 0$ and $k \ge 2$, the entry at $(1, 2)$ has modulus $t$, which is unbounded.

Multiplicities.

23. The eigenvalues and multiplicities are those of $A$ as a complex matrix. By [[invariance of the characteristic polynomial|0TYMASG33Y]], $A$ and $J$ have the same [[characteristic polynomial|039HF58KQ5]].
24. The matrix $xI - J$ is upper triangular. By the [[determinant of a triangular matrix|0K1KKMFHYH]], this polynomial is $\prod_{i=1}^r (x - \lambda_i)^{k_i}$.
25. So the [[eigenvalues|053QVHF6N7]] of $A$ are exactly $\lambda_1, \dots, \lambda_r$. The algebraic multiplicity of an eigenvalue $\lambda$, its [[multiplicity as a root|03XVP8Q4GY]], is the sum of the $k_i$ with $\lambda_i = \lambda$.
26. The map $v \mapsto P^{-1} v$ is a linear bijection from $\ker(A - \lambda I)$ onto $\ker(J - \lambda I)$. So these kernels have the same dimension, the [[geometric multiplicity|06YSJVR356]] of $\lambda$.
27. The kernel of the block diagonal matrix $J - \lambda I$ is the direct sum of the kernels of its blocks $(\lambda_i - \lambda) I + N$.
28. If $c = \lambda_i - \lambda \ne 0$ and $(cI + N) v = 0$, then $c v_k = 0$ and $c v_p + v_{p+1} = 0$ for $p < k$. Going upward from $p = k$ gives $v = 0$.
29. If $\lambda_i = \lambda$, then $N v = (v_2, \dots, v_k, 0)$, so $\ker N$ is spanned by $e_1$ and has dimension $1$.
30. So the geometric multiplicity of $\lambda$ is the number of blocks with $\lambda_i = \lambda$. Each $k_i \ge 1$. By step 25, the two multiplicities agree exactly when all these blocks have size $1$.
31. For a real eigenvalue, the real kernel of $A - \lambda I$ has the same dimension. Row reduction of the real matrix gives the same rank over $\R$ and over $\C$, and the [[rank–nullity theorem|TR48YQGCCA]] applies.

Conclusion.

32. Part (1). By Claim B and steps 12, 19 and 25, $0$ is asymptotically stable exactly when every eigenvalue of $A$ has negative real part.
33. Part (3). By Claim A and steps 12, 20 and 30, $0$ is Lyapunov stable exactly when two conditions hold. Every eigenvalue has $\operatorname{Re} \lambda \le 0$. Each eigenvalue with $\operatorname{Re} \lambda = 0$ has equal algebraic and geometric multiplicities.
34. Part (2): if some eigenvalue has $\operatorname{Re} \lambda > 0$, the condition in step 33 fails. So $0$ is not Lyapunov stable, that is, it is unstable.

## Idea

The solutions of $x' = Ax$ are $e^{tA} x_0$, so stability only asks whether the matrix $e^{tA}$ stays bounded or tends to zero. In Jordan form, each block contributes the terms $e^{\lambda t} t^j$. Exponential decay beats every power of $t$ when $\operatorname{Re} \lambda < 0$. On the imaginary axis the powers $t^j$ with $j \ge 1$ grow, and they are absent exactly when every Jordan block has size one.
