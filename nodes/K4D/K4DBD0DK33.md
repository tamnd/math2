---
tag: K4DBD0DK33
kind: statement
role: theorem
name: Fisher's fundamental theorem of natural selection
msc: [92D15, 92D10]
uses: [0477R9PYAE, 0NT64JV96A, CCN582E2C4]
about: [CCN582E2C4]
sources:
  - url: https://en.wikipedia.org/wiki/Fisher%27s_fundamental_theorem_of_natural_selection
same_as:
  wikidata: Q197869
  wikipedia: Fisher's fundamental theorem of natural selection
---

## Statement

Consider an asexual population in continuous time with $n$ types.
Let $p_i(t) \ge 0$ be the frequency of type $i$ at time $t$, with $p_1 + \cdots + p_n = 1$.
Let $m_i \in \R$ be the constant Malthusian fitness (growth rate) of type $i$, and let $\bar m = \sum_i p_i m_i$ be the mean fitness.
Assume that the frequencies follow the selection equations
$$\frac{dp_i}{dt} = p_i (m_i - \bar m), \quad i = 1, \dots, n.$$
Then the mean fitness grows at a rate equal to the [[variance|0477R9PYAE]] of fitness:
$$\frac{d\bar m}{dt} = \sum_{i=1}^n p_i (m_i - \bar m)^2 \ge 0.$$

## Remarks

The proof is one line.
Since the $m_i$ are constant, $d\bar m/dt = \sum_i m_i \, dp_i/dt = \sum_i p_i m_i^2 - \bar m^2$, and this is the variance of $m$ under the weights $p_i$.
For example, with two types of fitness $m_1 = 1$ and $m_2 = 0$ in equal frequency, the mean fitness $1/2$ increases at rate $1/4$.
In diploid Mendelian populations the total change in mean fitness is not the variance, because dominance, epistasis and changes of the environment also play a part.
Fisher's own claim concerns only the part of the change due to natural selection, which equals the additive genetic variance in fitness.
This reading of the theorem is due to later work of Price and others.

## Explanations

### L1 human

Natural selection makes the average fitness of a population go up.
The theorem says how fast: the speed equals the spread of fitness among the individuals.
If all types are equally fit, selection has nothing to act on and the mean stays put.
If the types differ a lot, the fitter ones take over quickly and the mean rises fast.

### L2 human

The statement is an exact identity for the replicator-type [[ordinary differential equation|0NT64JV96A]] of haploid selection.
It shows that mean fitness is a Lyapunov function for these dynamics, so the population moves to the fittest type present.
In [[population genetics|CCN582E2C4]] the general form needs care.
One splits the change in mean fitness into a part due to selection on additive effects and a part due to the "environment".
The second part includes the change in the genetic background of each allele.
The Price equation gives a convenient frame for this split.
