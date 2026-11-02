---
tag: 8A4GGX1MEY
kind: statement
role: lemma
name: Fekete's lemma
msc: [40A05, 39B62]
uses: [0CTV783HYT, 04KFTA34C5, 05M5SWSZZD]
about: [05M5SWSZZD]
sources:
  - url: https://en.wikipedia.org/wiki/Subadditivity
---

## Statement

Let $(a_n)_{n \ge 1}$ be a [[real sequence|0CTV783HYT]] that is subadditive, that is, $a_{m+n} \le a_m + a_n$ for all integers $m, n \ge 1$.
Then the [[limit|05M5SWSZZD]] of $a_n / n$ as $n \to \infty$ exists in $[-\infty, \infty)$, and
$$\lim_{n \to \infty} \frac{a_n}{n} = \inf_{n \ge 1} \frac{a_n}{n},$$
where $\inf$ is the [[infimum|04KFTA34C5]].

## Remarks

Fix $m \ge 1$ and write each $n$ as $n = qm + r$ with integers $q \ge 0$ and $1 \le r \le m$.
Subadditivity gives $a_n \le q a_m + a_r$, so $a_n / n \le (q m / n)(a_m / m) + a_r / n$.
As $n \to \infty$ the last term tends to $0$ and $qm/n$ tends to $1$, so $\limsup a_n / n \le a_m / m$.
Taking the infimum over $m$ gives $\limsup a_n/n \le \inf_m a_m/m \le \liminf a_n/n$, which proves the claim.
The limit can be $-\infty$: the sequence $a_n = -n^2$ is subadditive, since $-(m+n)^2 \le -m^2 - n^2$, and $a_n / n = -n$.
A typical use: if $c_n > 0$ and $c_{m+n} \le c_m c_n$ for all $m, n$, then $a_n = \log c_n$ is subadditive, so $c_n^{1/n}$ converges to $\inf_n c_n^{1/n}$.
For a bounded linear operator $A$ on a Banach space with no power equal to $0$, this applies to $c_n = \norm{A^n}$.
The same lemma is often called the subadditivity lemma.

## Explanations

### L1 human

A sequence is subadditive when the value at $m + n$ is at most the sum of the values at $m$ and at $n$.
Fekete's lemma says that the average growth $a_n / n$ then settles down.
Its limit is the smallest of all the averages $a_n / n$.

### L2 human

The lemma turns a crude inequality into the existence of a growth rate, without any formula for the terms.
It is used to define constants such as the connective constant of self-avoiding walks, entropies, and the spectral radius $\lim_n \norm{A^n}^{1/n}$.
Kingman's subadditive ergodic theorem is a random version of the same idea.
For a superadditive sequence, with $a_{m+n} \ge a_m + a_n$, apply the lemma to $-a_n$: then $a_n / n$ tends to $\sup_n a_n / n$.
