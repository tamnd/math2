---
tag: 79DH4GBCZ5
kind: definition
name: Gelfand–Naimark–Segal construction
msc: ["46L30", "46L05", "22D25"]
defines: 9FWZTK819W
uses: [F7MB2WREBJ, HM2HHE3J51]
sources:
  - url: https://en.wikipedia.org/wiki/Gelfand%E2%80%93Naimark%E2%80%93Segal_construction
---

## Definition

Let $A$ be a unital [[C*-algebra|M2WFY1D3SZ]] and let $\rho$ be a [[state|F7MB2WREBJ]] on $A$, a positive linear functional with $\rho(1) = 1$.
The *GNS construction* for $\rho$ is the triple $(H_\rho, \pi_\rho, \xi_\rho)$ defined as follows.

1. The set $N_\rho = \set{a \in A : \rho(a^*a) = 0}$ is a closed left ideal of $A$, and $\ip{a + N_\rho}{b + N_\rho} = \rho(b^*a)$ is an inner product on $A/N_\rho$.
2. $H_\rho$ is the [[Hilbert space|HM2HHE3J51]] completion of $A/N_\rho$ for this inner product.
3. For $a \in A$, $\pi_\rho(a)$ is the bounded operator on $H_\rho$ that extends $b + N_\rho \mapsto ab + N_\rho$.
4. $\xi_\rho = 1 + N_\rho$.

## Remarks

Then $\pi_\rho$ is a $*$-representation of $A$, the vector $\xi_\rho$ is cyclic, that is, $\pi_\rho(A)\xi_\rho$ is dense in $H_\rho$, and $\rho(a) = \ip{\pi_\rho(a)\xi_\rho}{\xi_\rho}$ for all $a \in A$.
Any other cyclic representation with a cyclic vector $\xi$ satisfying $\rho(a) = \ip{\pi(a)\xi}{\xi}$ is unitarily equivalent to $\pi_\rho$ by a unitary sending $\xi$ to $\xi_\rho$.
The boundedness in clause 3 comes from $\rho(b^*a^*ab) \le \norm{a}^2 \rho(b^*b)$.

Example: $A = C[0, 1]$ and $\rho(f) = \int_0^1 f(x) \, dx$.
Then $N_\rho = \set{0}$, since $\int_0^1 \abs{f}^2 \, dx = 0$ forces a continuous $f$ to vanish, and the inner product is $\int_0^1 f \overline{g} \, dx$.
So $H_\rho = L^2[0, 1]$, $\pi_\rho(f)$ is multiplication by $f$ and $\xi_\rho$ is the constant function $1$.

Non-example: the functional $\sigma(f) = -f(0)$ on $C[0, 1]$ is linear but not a state, and the construction fails at clause 1.
The form $\ip{a}{b} = \sigma(b^*a)$ gives $\ip{1}{1} = -1 < 0$, so it is not an inner product.

For a non-unital C\*-algebra the construction works in the same way for positive functionals, with the cyclic vector obtained from an approximate unit.
