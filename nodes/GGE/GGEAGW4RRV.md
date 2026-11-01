---
tag: GGEAGW4RRV
kind: statement
role: theorem
name: Talagrand's concentration inequality
msc: ["60E15", 28A35]
uses: [0NFPJVJJHX, 0AW1E6YTJY, 07Q7CNM5WF, 07Y2E7P9NP]
sources:
  - url: https://en.wikipedia.org/wiki/Talagrand%27s_concentration_inequality
same_as:
  wikidata: Q7678798
  wikipedia: Talagrand's concentration inequality
---

## Statement

Let $n \ge 1$, and for $i = 1, \dots, n$ let $(\Omega_i, P_i)$ be a finite [[probability space|0NFPJVJJHX]] in which every subset is an event.
Let $\Omega = \Omega_1 \times \dots \times \Omega_n$ with the product measure $P = P_1 \otimes \dots \otimes P_n$.
For a nonempty set $A \subseteq \Omega$ and a point $x \in \Omega$, define the convex distance
$$d_T(x, A) = \sup_{\alpha} \ \inf_{y \in A} \sum_{i \,:\, x_i \ne y_i} \alpha_i,$$
where the supremum is over all $\alpha \in [0, \infty)^n$ with $\alpha_1^2 + \dots + \alpha_n^2 = 1$.
Then for every nonempty $A \subseteq \Omega$ and every $t \ge 0$,
$$P(A) \cdot P(\set{x \in \Omega : d_T(x, A) \ge t}) \le e^{-t^2/4}.$$

## Remarks

The theorem holds, with the same proof, for products of general probability spaces, provided the sets involved are measurable.
Talagrand proved the stronger bound $\int_\Omega e^{d_T(x, A)^2 / 4} \, P(dx) \le 1 / P(A)$, by induction on $n$; Markov's inequality applied to $e^{d_T^2/4}$ gives the statement.
The convex distance is at least the normalised Hamming distance $\min_{y \in A} \#\set{i : x_i \ne y_i} / \sqrt{n}$, by the choice $\alpha_i = 1/\sqrt{n}$, so the theorem implies Hamming concentration.
A main consequence concerns convex Lipschitz functions.
Let $X_1, \dots, X_n$ be independent with values in $[0, 1]$, and let $F \colon [0, 1]^n \to \R$ be [[convex|07Q7CNM5WF]] and $1$-[[Lipschitz|0AW1E6YTJY]] for the Euclidean norm.
Then $P(\abs{F(X) - m} \ge t) \le C e^{-c t^2}$ for absolute constants $C, c > 0$, where $m$ is a [[median|07Y2E7P9NP]] of $F(X)$.
The bound does not depend on $n$, while bounded-difference methods would give a bound that gets worse with the dimension for this class.
It is used, for example, to show that the length of the longest increasing subsequence of a random permutation is concentrated around its median.

## Explanations

### L1 human

Take a set $A$ in a product of many independent coordinates that has probability at least one half.
Then almost every point is close to $A$, in a strong sense: changing a few well-chosen coordinates brings it into $A$, whatever weights one puts on the coordinates.
The probability of being at distance $t$ from $A$ drops like $e^{-t^2/4}$, independently of the number of coordinates.

### L2 human

Talagrand's inequality is a central result of the concentration of measure phenomenon in product spaces.
It goes beyond [[McDiarmid's inequality|8APFT1RPM4]] because the distance adapts to each point through the weights $\alpha$, which yields dimension-free bounds for convex Lipschitz functions and for functions with small certificates.
Applications include the largest eigenvalue of random matrices with bounded entries, longest increasing subsequences, and combinatorial optimisation problems on random inputs.
