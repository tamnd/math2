---
tag: GPA6BJQGZ9
kind: statement
role: theorem
name: Afriat's theorem
msc: [91B42, 91B08, 91B16]
uses: [MZENDW8DKD, GZZS4MTDG9, 0GCM7B6PBK, 0X3WGX95FE]
about: [MZENDW8DKD]
sources:
  - url: https://en.wikipedia.org/wiki/Revealed_preference
---

## Statement

Let $(p^t, x^t)$, $t = 1, \dots, T$, be a data set with prices $p^t \in \R^n$ with all entries positive and bundles $x^t \in \R^n_{\ge 0}$.
A [[utility function|GZZS4MTDG9]] $u \colon \R^n_{\ge 0} \to \R$ rationalizes the data if $u(x^t) \ge u(x)$ for every $t$ and every $x \in \R^n_{\ge 0}$ with $p^t \cdot x \le p^t \cdot x^t$.
It is locally nonsatiated if every neighbourhood of every bundle contains a bundle with a strictly larger utility.
Then the following are equivalent.

1. There is a locally nonsatiated utility function that rationalizes the data.
2. The data satisfy the generalized axiom of [[revealed preference|MZENDW8DKD]] (GARP).
3. There are numbers $U^t$ and $\lambda^t > 0$, for $t = 1, \dots, T$, such that $U^s \le U^t + \lambda^t\, p^t \cdot (x^s - x^t)$ for all $s, t$.
4. There is a [[continuous|0X3WGX95FE]], strictly increasing and [[concave|0GCM7B6PBK]] utility function that rationalizes the data.

## Remarks

The step from 1 to 2 is direct: local nonsatiation makes a strictly cheaper bundle strictly worse, so a cycle of revealed preferences cannot contain a strict step.
The step from 2 to 3 is the combinatorial heart; it solves the linear inequalities in 3, the Afriat inequalities, along the graph of revealed preferences.
For 3 to 4, set $u(x) = \min_t \big( U^t + \lambda^t\, p^t \cdot (x - x^t) \big)$, a minimum of finitely many affine functions with positive gradients, hence continuous, strictly increasing and concave.
The step from 4 to 1 is clear, because a strictly increasing function is locally nonsatiated.
A striking consequence: finite data can never reject concavity of the utility once they are consistent with some nonsatiated utility.
Without local nonsatiation every data set is rationalized by a constant utility, so the condition is needed for the test to say anything.

## Explanations

### L1 human

Given a finite record of what a shopper bought at what prices, one can ask whether some utility function explains all the purchases.
Afriat's theorem says this happens exactly when the record has no inconsistent cycle of choices.
If the record passes, there is even a nicely shaped utility function that explains it.

### L2 human

The theorem gives a finite, checkable test of consumer theory, computed by a transitive closure on $T$ observations.
Condition 3 is a system of linear inequalities, so a rationalizing utility can be built by linear programming.
It is the empirical counterpart of the integrability results of demand theory, which recover preferences from a full demand function.
