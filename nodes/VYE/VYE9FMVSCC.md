---
tag: VYE9FMVSCC
kind: definition
name: Structured singular value
msc: [93B35, 93D09, 15A18]
defines: 2EASHBY4TX
uses: [09VMDSRXWJ, 9V7YQA85PC]
sources:
  - url: https://en.wikipedia.org/wiki/Robust_control
---

## Definition

Let $n \ge 1$, and fix block sizes $r_1, \dots, r_S$ and $m_1, \dots, m_F$ with sum $n$.
Let $\mathbf{\Delta}$ be the set of all matrices $\operatorname{diag}(\delta_1 I_{r_1}, \dots, \delta_S I_{r_S}, \Delta_1, \dots, \Delta_F)$.
Here $\delta_i \in \C$, and each $\Delta_j$ is a complex $m_j \times m_j$ matrix.
Write $\bar\sigma(\Delta)$ for the largest [[singular value|09VMDSRXWJ]] of $\Delta$.
For a complex $n \times n$ matrix $M$, the *structured singular value* of $M$ with respect to $\mathbf{\Delta}$ is
$$\mu_{\mathbf{\Delta}}(M) = \frac{1}{\min\set{\bar\sigma(\Delta) : \Delta \in \mathbf{\Delta},\ \det(I - M \Delta) = 0}},$$
with $\mu_{\mathbf{\Delta}}(M) = 0$ if $\det(I - M \Delta) \ne 0$ for every $\Delta \in \mathbf{\Delta}$.

## Remarks

For the full structure $\mathbf{\Delta} = \C^{n \times n}$, $\mu_{\mathbf{\Delta}}(M) = \bar\sigma(M)$.
For the scalar structure $\mathbf{\Delta} = \set{\delta I_n : \delta \in \C}$, $\mu_{\mathbf{\Delta}}(M) = \rho(M)$, the [[spectral radius|9V7YQA85PC]], because $\det(I - \delta M) = 0$ exactly when $1/\delta$ is an eigenvalue of $M$.
Every structure of the form above contains the scalar one and lies in the full one, so $\rho(M) \le \mu_{\mathbf{\Delta}}(M) \le \bar\sigma(M)$.
Example: let $M = \begin{pmatrix} 0 & a \\ 0 & 0 \end{pmatrix}$ with $a \ne 0$, and let $\mathbf{\Delta}$ be the diagonal matrices $\operatorname{diag}(\delta_1, \delta_2)$.
Then $I - M \Delta = \begin{pmatrix} 1 & -a \delta_2 \\ 0 & 1 \end{pmatrix}$ has determinant $1$, so $\mu_{\mathbf{\Delta}}(M) = 0$, while $\bar\sigma(M) = \abs{a}$.
So the structure can make $\mu$ much smaller than $\bar\sigma$.
The function $\mu_{\mathbf{\Delta}}$ is not a norm in general: in this example it vanishes on a nonzero matrix.
In robust control, let a stable loop $M(s)$ be closed with stable perturbations $\Delta(s)$ of structure $\mathbf{\Delta}$ and $\norm{\Delta}_\infty < 1/\beta$.
The loop is stable for all such $\Delta$ if and only if $\sup_\omega \mu_{\mathbf{\Delta}}(M(i\omega)) \le \beta$.
