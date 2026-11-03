---
tag: DMT7HP2Q2Y
kind: statement
role: proposition
name: Mutation–selection balance
msc: [92D10, 92D15]
uses: [380DYJJWT0, AFJ02FJ1KR, CCN582E2C4]
about: [CCN582E2C4]
sources:
  - url: https://en.wikipedia.org/wiki/Mutation%E2%80%93selection_balance
same_as:
  wikidata: Q3730906
  wikipedia: Mutation–selection balance
---

## Statement

Consider one locus with a wild-type allele $A$ and a deleterious allele $a$, in a population so large that drift is negligible.
In each generation, selection acts first and then $A$ mutates to $a$ with probability $\mu$; there is no back mutation.
Let $q$ be the frequency of $a$.

1. (Haploid.) Let $A$ have fitness $1$ and $a$ fitness $1 - s$, with $0 < \mu < s \le 1$. Then $q$ has the unique equilibrium $\hat q = \mu / s$ in $[0, 1)$. At this equilibrium the mean fitness is exactly $1 - \mu$.
2. (Diploid, partly dominant.) Let the genotypes $AA$, $Aa$, $aa$ be in [[Hardy–Weinberg proportions|380DYJJWT0]] at birth. Let their fitnesses be $1$, $1 - hs$, $1 - s$, with $0 < h \le 1$ and $0 < s \le 1$ fixed. Then the equilibrium satisfies $\hat q = \mu/(hs) + O(\mu^2)$ as $\mu \to 0$.
3. (Diploid, recessive.) If $h = 0$ in clause 2, then $\hat q = \sqrt{\mu / s} + O(\mu)$ as $\mu \to 0$.

## Remarks

In the haploid case, let $p = 1 - q$.
After selection $p' = p/(1 - sq)$, and after mutation $p'' = (1 - \mu) p/(1 - sq)$.
An equilibrium with $p > 0$ needs $1 - sq = 1 - \mu$, which gives $\hat q = \mu/s$, and the mean fitness $1 - s\hat q$ equals $1 - \mu$.
The diploid cases follow by equating the decrease of $q$ by selection, about $hsq$ or $sq^2$ for small $q$, with the increase $\mu(1 - q)$ by mutation.
For example, a recessive lethal allele ($s = 1$) with $\mu = 10^{-6}$ settles near frequency $10^{-3}$.
The loss of mean fitness at equilibrium, the mutation load, is about $\mu$ for haploids and recessives and about $2\mu$ for partly dominant alleles in diploids, independent of $s$.

## Explanations

### L1 human

Mutation keeps creating harmful alleles, and selection keeps removing them.
At balance, the harmful allele stays at a low frequency set by the ratio of the two rates.
A harmful allele that hides in carriers, because it is recessive, is removed slowly and so stays much more common than one that always shows its effect.

### L2 human

This balance explains why rare genetic diseases persist at roughly constant frequencies.
The striking fact is that the load depends on the mutation rate and not on how harmful each mutation is.
More harmful alleles are rarer, which exactly compensates.
In finite populations [[genetic drift|AFJ02FJ1KR]] adds noise around these equilibria, and when selection is weak relative to drift the deterministic picture fails.
