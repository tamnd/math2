---
tag: F68QFEYFY0
kind: conjecture
name: Pólya's conjecture on Laplacian eigenvalues
msc: [35P15, 49R05, 35P20]
uses: [4VD8XXQ4P3, GS3KT2H645, 0E0B6RA8K0, 2Z2QVWZ262, 2JK9YMZV2B]
about: [4VD8XXQ4P3]
sources:
  - url: https://en.wikipedia.org/wiki/Weyl_law
history:
  posed_by: "George Pólya"
  first_stated: "1954"
---

## Statement

Let $d \ge 1$ and let $\Omega \subseteq \R^d$ be a nonempty bounded open set with [[Lebesgue measure|2Z2QVWZ262]] $\abs{\Omega}$.
Let $\omega_d$ be the volume of the unit ball of $\R^d$.
Let $0 < \lambda_1 \le \lambda_2 \le \cdots$ be the [[Dirichlet eigenvalues|4VD8XXQ4P3]] of $-\Delta$ on $\Omega$, where $\Delta$ is the [[Laplacian|0E0B6RA8K0]].
If $\Omega$ is also connected with Lipschitz boundary, let $0 = \mu_1 < \mu_2 \le \mu_3 \le \cdots$ be its eigenvalues with the [[Neumann boundary condition|GS3KT2H645]].
All are repeated according to multiplicity.
Let $C_d = \dfrac{4 \pi^2}{\omega_d^{2/d}}$.
Then, for every $k \ge 1$,
$$\lambda_k \ge C_d \left( \frac{k}{\abs{\Omega}} \right)^{2/d} \qquad \text{and} \qquad \mu_{k+1} \le C_d \left( \frac{k}{\abs{\Omega}} \right)^{2/d}.$$

## Remarks

The constant is that of [[Weyl's law|2JK9YMZV2B]], $\lambda_k \sim C_d (k / \abs{\Omega})^{2/d}$ as $k \to \infty$, so the conjecture says that the Weyl term is a one-sided bound for every $k$, not only asymptotically.
For $d = 2$ the bounds read $\lambda_k \ge 4 \pi k / \abs{\Omega}$ and $\mu_{k+1} \le 4 \pi k / \abs{\Omega}$.
The conjecture is open in general.
Pólya proved the Dirichlet bound for plane domains that tile the plane.
Li and Yau proved the weaker bound $\lambda_k \ge \frac{d}{d + 2} C_d (k / \abs{\Omega})^{2/d}$ for all bounded domains, now called the Berezin–Li–Yau inequality.
Filonov, Levitin, Polterovich and Sher proved both bounds for the disk.
For $k = 1$ the Dirichlet bound follows from the [[Faber–Krahn inequality|E7TY2TPXX7]].

## Explanations

### L1 human

The eigenvalues of the Laplacian on a region are the squared pitches of a drum of that shape.
Weyl's law says how the $k$-th pitch grows with $k$, on average.
Pólya guessed that, with the Dirichlet condition, every pitch lies above the Weyl prediction, and with the Neumann condition every pitch lies below it.
