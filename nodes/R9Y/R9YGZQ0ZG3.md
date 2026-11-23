---
tag: R9YGZQ0ZG3
kind: example
name: Small values of the Veblen function and their fundamental sequences
msc: ["03E10", "03F15"]
topics: [XTTKZTYDSD]
audience: grad
instance_of: [JQFAE9S2F4]
uses: [6QFEVWKE25, VB6YXF761M, KT50SMH3EC, PQSHBKCE7V, ERTAM0SFVB]
sources:
  - url: https://en.wikipedia.org/wiki/Veblen_function
    locator: Fundamental sequences for the Veblen hierarchy
  - url: https://en.wikipedia.org/wiki/Veblen_function
    locator: The Γ function
---

## Example

A fundamental sequence for a limit ordinal $\alpha$ is a strictly increasing sequence $\alpha[0] < \alpha[1] < \cdots$ with supremum $\alpha$.
For $\omega^2$ the natural choice is $0, \omega, \omega \cdot 2, \omega \cdot 3, \ldots$.
We compute small values of the [[Veblen function|6QFEVWKE25]] together with [[fundamental sequences|VB6YXF761M]] in the convention of the cited section:

- $\varphi_0(\gamma + 1)[n] = \omega^\gamma \cdot n$;
- $\varphi_{\beta+1}(0)[0] = 0$ and $\varphi_{\beta+1}(0)[n+1] = \varphi_\beta(\varphi_{\beta+1}(0)[n])$;
- $\varphi_{\beta+1}(\gamma+1)[0] = \varphi_{\beta+1}(\gamma) + 1$ and $\varphi_{\beta+1}(\gamma+1)[n+1] = \varphi_\beta(\varphi_{\beta+1}(\gamma+1)[n])$;
- $\varphi_\beta(\gamma)[n] = \varphi_\beta(\gamma[n])$ for a limit $\gamma < \varphi_\beta(\gamma)$, and $\varphi_\beta(0)[n] = \varphi_{\beta[n]}(0)$ for a limit $\beta < \varphi_\beta(0)$.

### Seven values

1. $\varphi_0(2) = \omega^2$, with $\omega^2[n] = \omega \cdot n$.
   The sequence $0, \omega, \omega \cdot 2, \ldots$ has supremum $\omega \cdot \omega = \omega^2$.
2. $\varphi_1(0) = \varepsilon_0$, with the sequence $0$, $\varphi_0(0) = 1$, $\omega^1 = \omega$, $\omega^\omega$, and so on.
   This is the tower of [[epsilon nought|KT50SMH3EC]] after an initial $0$.
3. $\varphi_1(1) = \varepsilon_1$, with the sequence $\varepsilon_0 + 1, \omega^{\varepsilon_0 + 1}, \omega^{\omega^{\varepsilon_0 + 1}}, \ldots$.
4. $\varphi_1(\omega) = \varepsilon_\omega$, with $\varepsilon_\omega[n] = \varphi_1(\omega[n]) = \varepsilon_n$.
   The supremum is $\varepsilon_\omega$, since $\varphi_1$ is continuous.
5. $\varphi_2(0) = \zeta_0$, with the sequence $0$, $\varphi_1(0) = \varepsilon_0$, $\varphi_1(\varepsilon_0) = \varepsilon_{\varepsilon_0}$, $\varepsilon_{\varepsilon_{\varepsilon_0}}$, and so on.
6. $\varphi_\omega(0)$, with $\varphi_\omega(0)[n] = \varphi_n(0)$, so the sequence is $1, \varepsilon_0, \zeta_0, \eta_0, \ldots$.
7. $\Gamma_0$, the [[Feferman-Schütte ordinal|CNN7BK5YAW]], with $\Gamma_0[0] = 0$ and $\Gamma_0[n+1] = \varphi_{\Gamma_0[n]}(0)$.
   The sequence is $0, 1, \varepsilon_0, \varphi_{\varepsilon_0}(0), \ldots$.

### Check of step 6

For each $m$ and each $n > m$, $\varphi_n(0)$ is a fixed point of $\varphi_m$, by clause 2 or 3 of the definition.
Continuity of $\varphi_m$ gives the following equation.
$$\varphi_m\Big(\sup_n \varphi_n(0)\Big) = \sup_{n > m} \varphi_m(\varphi_n(0)) = \sup_n \varphi_n(0)$$
So the supremum is a common fixed point of all $\varphi_m$.
Every common fixed point $\alpha$ is fixed by each $\varphi_n$, so $\alpha = \varphi_n(\alpha) \ge \varphi_n(0)$, and the supremum is the least one, $\varphi_\omega(0)$.

## Remarks

The convention matters.
Other books use $\varepsilon_0[0] = \omega$, or $\omega^{\gamma+1}[n] = \omega^\gamma \cdot (n + 1)$, and then $\alpha[n]$ changes for small $n$.
The limits stay the same, but functions defined from the sequences, such as the [[fast-growing hierarchy|R6ZC4BJGXV]], change their values.

Ordinals with $\alpha = \varphi_\alpha(0)$, such as $\Gamma_0$, get no sequence from the four rules, since the last rule needs $\beta < \varphi_\beta(0)$.
The rule in step 7 is an extra choice, and it follows the iteration that defines $\Gamma_0$.

## Explanations

### L1 human

A fundamental sequence is a list of smaller ordinals that climbs up to a given limit ordinal.
For $\omega^2$ the list is $0, \omega, \omega \cdot 2, \omega \cdot 3, \ldots$.
For $\varepsilon_0$ it is $0, 1, \omega, \omega^\omega, \ldots$, the tower of powers.
For the larger values of the Veblen function, each list is built by applying the previous function again and again.

### L2 human

We compute $\zeta_0[3]$ in the convention above.
Since $\zeta_0 = \varphi_2(0)$, the second rule gives $\zeta_0[0] = 0$ and $\zeta_0[n+1] = \varphi_1(\zeta_0[n])$.
Apply it three times:
$$\zeta_0[1] = \varphi_1(0) = \varepsilon_0, \qquad \zeta_0[2] = \varepsilon_{\varepsilon_0}, \qquad \zeta_0[3] = \varepsilon_{\varepsilon_{\varepsilon_0}}.$$

The typical use is to define the fast-growing hierarchy beyond $\varepsilon_0$, by $f_\lambda(n) = f_{\lambda[n]}(n)$.
Watch out: $\zeta_0[1] = \varepsilon_0$ is already a limit ordinal, so one step of a fundamental sequence can jump very far.
