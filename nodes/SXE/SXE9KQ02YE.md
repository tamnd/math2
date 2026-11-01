---
tag: SXE9KQ02YE
kind: problem
name: Secretary problem
msc: [60G40, 62L15]
uses: [WND87FBAKC, 05RWFKVTJ7]
sources:
  - url: https://en.wikipedia.org/wiki/Secretary_problem
same_as:
  wikidata: Q1372364
  wikipedia: Secretary problem
history:
  posed_by: "Martin Gardner, who popularised it"
  first_stated: "1960"
---

## Problem

Let $n \ge 1$ applicants with distinct qualities be interviewed one at a time, in an order given by a uniformly random [[permutation|05RWFKVTJ7]].
After each interview, the only information is the relative rank of the current applicant among those seen so far.
After each interview the applicant must be accepted or rejected at once, and the decision cannot be changed.
The process ends at the first acceptance.
Find a rule that maximises the probability of accepting the best of the $n$ applicants, and find this maximal probability.
A rule is a [[stopping time|WND87FBAKC]] for the observed relative ranks.

## Remarks

The problem is solved, and it is a standard example of optimal stopping.
An optimal rule has a threshold form: reject the first $r - 1$ applicants, then accept the first applicant who is better than all earlier ones.
For $r \ge 2$ this rule picks the best applicant with probability
$$P_n(r) = \frac{r - 1}{n} \sum_{i=r}^{n} \frac{1}{i - 1},$$
and $P_n(1) = 1/n$.
The optimal $r$ satisfies $r/n \to 1/e$ and the maximal probability tends to $1/e \approx 0.368$ as $n \to \infty$.
For $n = 3$, the rule with $r = 2$ succeeds with probability $\frac{1}{3}(1 + \frac{1}{2}) = \frac{1}{2}$, which is optimal.

## Explanations

### L1 human

You must hire one of $n$ candidates who arrive in random order, and you must say yes or no to each one on the spot.
A good plan is to look at about $37\%$ of the candidates without hiring anyone, to learn the level of the field.
After that, hire the first candidate who beats everyone seen so far.
Surprisingly, this plan finds the very best candidate about $37\%$ of the time, however large $n$ is.
