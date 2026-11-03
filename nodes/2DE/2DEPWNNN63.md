---
tag: 2DEPWNNN63
kind: statement
role: theorem
name: Kimura's diffusion approximation
msc: [92D15, 60J70]
uses: [GVMM9GC7CE, 5APPKBE8Q4, MBW183XCKH]
about: [5APPKBE8Q4]
sources:
  - url: https://en.wikipedia.org/wiki/Fixation_(population_genetics)
---

## Statement

Let $N_e > 0$ be an [[effective population size|MBW183XCKH]] and $s \in \R$ a selection coefficient.
Let $(p_t)_{t \ge 0}$ be the [[diffusion process|GVMM9GC7CE]] on $[0, 1]$ with drift coefficient $s \, p (1 - p)$ and diffusion coefficient $p (1 - p) / (2 N_e)$, started at $p_0 = p \in [0, 1]$.
This is the diffusion approximation of the allele frequency of a diploid population with additive selection.
Then the [[fixation probability|5APPKBE8Q4]], the probability that $p_t$ reaches $1$, is
$$u(p) = \frac{1 - e^{-4 N_e s p}}{1 - e^{-4 N_e s}} \quad (s \ne 0), \qquad u(p) = p \quad (s = 0).$$

## Remarks

Proof idea: the function $u$ solves the backward equation
$$\frac{p (1 - p)}{4 N_e} \, u''(p) + s \, p (1 - p) \, u'(p) = 0, \qquad u(0) = 0, \quad u(1) = 1.$$
Dividing by $p (1 - p)$ gives $u'' + 4 N_e s \, u' = 0$, whose solutions are $A + B e^{-4 N_e s p}$.
The boundary conditions fix $A$ and $B$ and give the formula.

Example: for a single new mutant in a population of $N = N_e$ diploid individuals, $p = 1/(2N)$.
If $s > 0$ is small and $N s$ is large, then $u \approx 1 - e^{-2 s} \approx 2 s$.
This recovers Haldane's result that a new beneficial mutation is fixed with probability about $2s$.
For $s = 0.01$, only about $2\%$ of such mutations are fixed.

As $s \to 0$, the formula tends to $u(p) = p$, the neutral value.
For $s < 0$, the formula still applies and shows that a slightly harmful allele can be fixed by drift when $\abs{N_e s}$ is small.

## Explanations

### L1 human

When a population is large, the random ups and downs of an allele's frequency look like a continuous random motion with a push from selection.
Kimura used this picture to compute the chance that a new variant takes over.
The answer depends on the product of population size and selective advantage.
A variant with a $1\%$ advantage still disappears about $98\%$ of the time when it starts as one copy.

### L2 human

The approximation replaces the [[Wright–Fisher model|SR4F169EKF]] or the [[Moran process|A9M7VKRRV9]] by a diffusion and solves an ordinary differential equation instead of a recursion.
It is accurate when $N_e$ is large and $s$ is of order $1/N_e$.
The key parameter is $4 N_e s$: selection dominates drift when $\abs{4 N_e s} \gg 1$, and drift dominates when $\abs{4 N_e s} \ll 1$.
This dichotomy is the basis of the nearly neutral theory and of the neutral theory of molecular evolution.
The same method gives mean times to fixation and the stationary distributions of allele frequencies.
