---
tag: BT4S0B7BPY
kind: definition
name: Kostant partition function
msc: [17B10, 17B22, "05E10"]
defines: DH720Y9NSD
uses: [AVVV93CASN, CSBM217V1N]
sources:
  - url: https://en.wikipedia.org/wiki/Kostant_partition_function
---

## Definition

Let $\Phi$ be a [[root system|AVVV93CASN]] in a real vector space $E$, with a set of positive roots $\Phi^+$.
The *Kostant partition function* is the function $P \colon E \to \Z_{\ge 0}$ such that $P(\mu)$ is the number of families $(n_\alpha)_{\alpha \in \Phi^+}$ of nonnegative integers with
$$\mu = \sum_{\alpha \in \Phi^+} n_\alpha \alpha.$$

## Remarks

The number is finite, because every positive root is a nonnegative combination of the [[simple roots|CSBM217V1N]] with at least one positive coefficient.
So $P(0) = 1$, and $P(\mu) = 0$ unless $\mu$ is a nonnegative integer combination of simple roots.
In generating form, $\prod_{\alpha \in \Phi^+} (1 - e^{-\alpha})^{-1} = \sum_\mu P(\mu)\, e^{-\mu}$.
Example: for $A_2$ with simple roots $\alpha_1, \alpha_2$, one has $P(m\alpha_1 + n\alpha_2) = \min(m, n) + 1$ for $m, n \ge 0$.
Indeed, the number $k$ of copies of $\alpha_1 + \alpha_2$ can be any integer from $0$ to $\min(m, n)$, and it determines the rest.
Non-example: counting with all roots $\Phi$ instead of $\Phi^+$ gives no function, since $0 = \alpha + (-\alpha)$ can be written in infinitely many ways.
For a complex semisimple Lie algebra, the weight space of weight $\lambda - \mu$ of the Verma module $M(\lambda)$ has dimension $P(\mu)$.
Kostant's multiplicity formula states $\dim L(\lambda)_\mu = \sum_{w \in W} \det(w)\, P\big(w(\lambda + \rho) - (\mu + \rho)\big)$ for dominant integral $\lambda$.
