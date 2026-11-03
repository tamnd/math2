---
tag: 8WT39NFCTP
kind: statement
role: fact
name: Kingman's formula
msc: [60K25, 90B22]
uses: [P64V0HTE78, 0477R9PYAE, 0WQNRCNY3M, 9HTFATQNJ2]
about: [P64V0HTE78]
sources:
  - url: https://en.wikipedia.org/wiki/Kingman%27s_formula
same_as:
  wikidata: Q6412804
  wikipedia: Kingman's formula
---

## Statement

Consider a G/G/1 queue in the sense of [[Kendall's notation|9HTFATQNJ2]], with first-come first-served discipline.
Interarrival times are independent and identically distributed with mean $1/\lambda$ and standard deviation $\sigma_a$.
Service times are independent of them, independent and identically distributed with mean $\tau = 1/\mu$ and standard deviation $\sigma_s$.
Let $\rho = \lambda / \mu$ be the utilisation, assume $\rho < 1$, and let $c_a = \lambda \sigma_a$ and $c_s = \mu \sigma_s$ be the coefficients of variation.
*Kingman's formula* is the approximation
$$\mathbb{E}[W_q] \approx \frac{\rho}{1 - \rho} \cdot \frac{c_a^2 + c_s^2}{2} \cdot \tau$$
for the mean stationary waiting time $W_q$ before service.
The approximation becomes exact in the [[heavy traffic|4XPHS45KSP]] limit $\rho \to 1$.

## Remarks

The formula comes from Kingman's heavy traffic analysis of the [[Lindley equation|GJT4VQ46KH]], where the waiting time behaves like the maximum of a random walk with small negative drift.
A related exact result is Kingman's upper bound $\mathbb{E}[W_q] \le \lambda (\sigma_a^2 + \sigma_s^2) / (2 (1 - \rho))$.
For the [[M/M/1 queue|GTFRPF5J2K]], $c_a = c_s = 1$ and the formula gives $\rho \tau / (1 - \rho) = \rho / (\mu - \lambda)$, which is the exact mean wait.
For the [[M/G/1 queue|Q3VCF5R06B]], $c_a = 1$ and the formula is exactly the Pollaczek–Khinchine mean value formula.
For general arrivals and light traffic, the formula can be far off.

## Explanations

### L1 human

The formula says how long a customer waits on average in a single-server line.
The wait is a product of three factors: one for how busy the server is, one for how irregular arrivals and services are, and the mean service time.
The first factor $\rho / (1 - \rho)$ explodes as the server becomes fully busy.
So a server busy $90\%$ of the time makes customers wait about nine service times when the variability factor is $1$.

### L2 human

The formula is a rule of thumb in operations management, often written as $V \cdot U \cdot T$: variability times utilisation times time.
It shows that cutting variability lowers waiting times as much as cutting load does.
It is exact for Poisson arrivals and is justified in general by the heavy traffic limit theorem of Kingman.
Combined with [[Little's law|JN2YME6F4A]], it also gives an approximation of the mean queue length, $\lambda \, \mathbb{E}[W_q]$.
