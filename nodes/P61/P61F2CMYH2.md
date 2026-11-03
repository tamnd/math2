---
tag: P61F2CMYH2
kind: example
name: Random energy model
msc: [82B44, 60G15, 60K35]
illustrates: [EHPA4B5S5W]
uses: [05AQE0QR0D]
sources:
  - url: https://en.wikipedia.org/wiki/Random_energy_model
same_as:
  wikidata: Q2130737
  wikipedia: Random energy model
---

## Example

Let $N \ge 1$ and let $(E_\sigma)_{\sigma \in \set{-1,+1}^N}$ be $2^N$ independent [[Gaussian|05AQE0QR0D]] random variables with mean $0$ and variance $N/2$.
The *random energy model* has the partition function
$$Z_N(\beta) = \sum_{\sigma \in \set{-1,+1}^N} e^{-\beta E_\sigma}, \qquad \beta \ge 0.$$
Let $\beta_c = 2 \sqrt{\log 2}$.
Then, almost surely and in mean,
$$\lim_{N \to \infty} \frac{1}{N} \log Z_N(\beta) = \begin{cases} \log 2 + \beta^2 / 4, & \beta \le \beta_c, \\ \beta \sqrt{\log 2}, & \beta > \beta_c. \end{cases}$$

Check of the formula by counting: for $x \ge 0$, the expected number of $\sigma$ with $E_\sigma \le -N x$ is about $e^{N(\log 2 - x^2)}$.
So typically there are such $\sigma$ only for $x \le \sqrt{\log 2}$, and $\frac{1}{N} \log Z_N$ tends to the maximum of $\log 2 - x^2 + \beta x$ over $0 \le x \le \sqrt{\log 2}$.
The maximum is at $x = \beta / 2$ when $\beta \le \beta_c$, which gives $\log 2 + \beta^2/4$, and at $x = \sqrt{\log 2}$ otherwise, which gives $\beta \sqrt{\log 2}$.
The two values agree at $\beta = \beta_c$, where both equal $2 \log 2$.

## Remarks

Derrida introduced the model in 1980 as the limit of $p$-spin glass models with $p \to \infty$.
It has independent energies, while in the [[Sherrington–Kirkpatrick model|MMSZK6CYRX]] the energies of two configurations are correlated through their overlap.
Below $\beta_c$ the free energy equals the annealed value $\frac{1}{N} \log \mathbb{E} Z_N = \log 2 + \beta^2/4$.
Above $\beta_c$ the entropy per spin vanishes, and the Gibbs measure concentrates on a few configurations of lowest energy; this freezing is a simple picture of a [[spin glass|EHPA4B5S5W]] transition.

## Explanations

### L1 human

Give each of the $2^N$ spin configurations an energy drawn at random, independently of all the others.
At high temperature the system visits a huge number of configurations, and averages behave nicely.
At low temperature it gets stuck in the very few configurations with the lowest energies.
The change happens at a sharp temperature, and the model is simple enough that everything can be computed.
