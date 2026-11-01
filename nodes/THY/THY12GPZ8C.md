---
tag: THY12GPZ8C
kind: statement
role: theorem
name: Paley–Wiener theorem
msc: ["30D15", "42A38"]
uses: [0419794R0T, 9P8D8YAHQS]
about: [9P8D8YAHQS, 0419794R0T]
sources:
  - url: https://en.wikipedia.org/wiki/Paley%E2%80%93Wiener_theorem
---

## Statement

Let $\sigma > 0$, and let $F$ be an [[entire function|0419794R0T]].
The following two conditions are equivalent.

1. $F$ is of [[exponential type|9P8D8YAHQS]] at most $\sigma$, and its restriction to the real line is square-integrable: $\int_{-\infty}^{\infty} \abs{F(x)}^2 \, dx < \infty$.
2. There is a square-integrable function $\varphi$ on the interval $[-\sigma, \sigma]$ such that
$$F(z) = \int_{-\sigma}^{\sigma} \varphi(t) \, e^{i z t} \, dt \quad \text{for all } z \in \C.$$

## Remarks

The implication from 2 to 1 is direct: $\abs{e^{izt}} = e^{-t \operatorname{Im} z} \le e^{\sigma \abs{z}}$ for $\abs{t} \le \sigma$, and the Plancherel theorem gives the square-integrability on $\R$.
For the converse, $\varphi$ is the Fourier transform of $F$ on $\R$, up to a constant.
It vanishes outside $[-\sigma, \sigma]$; this follows by shifting the line of integration into the upper or lower half-plane.
The growth there is controlled by the [[Phragmén–Lindelöf principle|FYR6V2NH6C]].
For example, with $\varphi = 1/2$ on $[-\sigma, \sigma]$ one gets $F(z) = \sin(\sigma z)/z$, which has exponential type $\sigma$ and is square-integrable on $\R$.
The square-integrability is needed: $\sin(\sigma z)$ has exponential type $\sigma$ but is not of the form 2, since it is not square-integrable on $\R$.

## Explanations

### L1 human

A signal whose frequencies all lie in a bounded band $[-\sigma, \sigma]$ extends from the real line to an entire function of the complex variable.
That entire function grows at most like $e^{\sigma \abs{z}}$.
The theorem says that the converse holds too: such growth, together with finite energy on the real line, forces the frequencies into the band.
So the smallest band $[-\sigma, \sigma]$ that contains the frequencies is given by the exponential type.

### L2 human

The space of functions in the theorem is the Paley–Wiener space, a Hilbert space of entire functions that is the basic example of a [[de Branges space|NYHNTP9AND]].
It is the setting of the sampling theorem of signal processing: such a function is determined by its values at the points $\pi n/\sigma$, $n \in \Z$.
There are related Paley–Wiener theorems for smooth functions and distributions with compact support, where the growth condition also involves $\abs{\operatorname{Im} z}$.
