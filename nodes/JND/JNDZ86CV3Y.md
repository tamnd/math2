---
tag: JNDZ86CV3Y
kind: statement
role: lemma
name: Fundamental lemma of the calculus of variations
msc: [49K05, 49K10, 46F05]
uses: [02BH3MCBQB, X7GTF3D98F, HS65DW0HXH, RARTMA0ZEC, DWJF7ABPR1]
about: [PQ25NHV0KS]
sources:
  - url: https://en.wikipedia.org/wiki/Fundamental_lemma_of_the_calculus_of_variations
same_as:
  wikidata: Q2474925
  wikipedia: Fundamental lemma of the calculus of variations
---

## Statement

Let $\Omega \subseteq \R^n$ be an [[open set|02BH3MCBQB]], and let $C^\infty_c(\Omega)$ be the set of smooth functions $\varphi \colon \Omega \to \R$ whose support is a compact subset of $\Omega$.
Let $f \colon \Omega \to \R$ be locally [[integrable|X7GTF3D98F]], that is, integrable on every compact subset of $\Omega$.
If
$$\int_\Omega f(x) \varphi(x) \, dx = 0 \quad \text{for every } \varphi \in C^\infty_c(\Omega),$$
then $f = 0$ [[almost everywhere|RARTMA0ZEC]] on $\Omega$.
In particular, if $f$ is continuous, then $f(x) = 0$ for every $x \in \Omega$.

## Remarks

For continuous $f$ the proof is short.
If $f(x_0) > 0$, then $f > 0$ on a ball $B$ around $x_0$; a [[bump function|HS65DW0HXH]] $\varphi \ge 0$ supported in $B$ with $\varphi(x_0) > 0$ gives $\int_\Omega f \varphi \, dx > 0$, a contradiction.
For locally integrable $f$, one convolves $f$ with a smooth mollifier: the hypothesis makes every mollified function vanish, and these converge to $f$ in $L^1$ on compact sets.

The lemma is the step that turns the vanishing of the [[first variation|5B8NFYB2XQ]] into the [[Euler–Lagrange equation|PS0VV149ET]].
After an integration by parts, the first variation has the form $\int_\Omega E(x) \varphi(x) \, dx$, where $E$ is the Euler–Lagrange expression; the lemma gives $E = 0$.

The class of test functions must be large enough.
If only $\varphi$ with $\int_\Omega \varphi \, dx = 0$ were allowed, every constant $f$ would satisfy the hypothesis; this case is the [[du Bois-Reymond lemma|AATQKCWAAC]].

## Explanations

### L1 human

If a function gives zero when it is averaged against every smooth bump, then the function is zero.
A bump placed where the function is positive would otherwise give a positive answer.
It is the reason why "zero for all variations" can be turned into an equation that holds at every point.

### L2 human

In a derivation of the Euler–Lagrange equation one first finds $\int_a^b \big(L_z - \frac{d}{dx} L_p\big)\eta \, dx = 0$ for all $\eta$ that vanish at the ends.
The lemma then gives the pointwise equation $L_z - \frac{d}{dx} L_p = 0$.
In distribution theory the lemma says that a locally integrable function is determined by the distribution it defines.
