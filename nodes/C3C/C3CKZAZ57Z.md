---
tag: C3CKZAZ57Z
kind: statement
role: theorem
name: Vitali convergence theorem
msc: [28A25, 28A20]
uses: [VRVVKMXDGV, X7GTF3D98F, RARTMA0ZEC, 63Z1Q4FS23, S95TR54TCG]
about: [VRVVKMXDGV, DWJF7ABPR1]
sources:
  - url: https://en.wikipedia.org/wiki/Vitali_convergence_theorem
same_as:
  wikidata: Q11352023
  wikipedia: Vitali convergence theorem
---

## Statement

Let $(X, \Sigma, \mu)$ be a [[finite measure|63Z1Q4FS23]] space.
Let $f_1, f_2, \dots$ be real or complex [[integrable functions|X7GTF3D98F]] on $X$.
Let $f$ be a measurable function with $f_n \to f$ [[almost everywhere|RARTMA0ZEC]].
Then the following are equivalent.

1. The family $\set{f_n : n \ge 1}$ is [[uniformly integrable|VRVVKMXDGV]].
2. The function $f$ is integrable and $\lim_{n \to \infty} \int_X \abs{f_n - f} \, d\mu = 0$.

## Remarks

Proof idea for 1 implies 2: uniform integrability bounds $\int \abs{f_n}$, so $f$ is integrable by [[Fatou's lemma|S95TR54TCG]].
Split $\int \abs{f_n - f}$ into the part on a set where $f_n \to f$ uniformly, given by Egorov's theorem, and the part on a small set.
Uniform integrability makes the second part small, uniformly in $n$.
For 2 implies 1, a sequence converging in $L^1$ is uniformly integrable, because finitely many integrable functions are, and the tail is close to $f$.

Example: if $\sup_n \int \abs{f_n}^2 \, d\mu < \infty$ and $f_n \to f$ almost everywhere, then the family is uniformly integrable and $f_n \to f$ in $L^1$.

The finiteness of $\mu$ is needed in this form.
On $\R$ with Lebesgue measure, $f_n = \frac{1}{n} \mathbf{1}_{[0, n]}$ satisfies the condition of uniform integrability, since $\abs{f_n} \le 1$, and tends to $0$ everywhere, but $\int \abs{f_n} = 1$ for all $n$.
The theorem also holds with convergence in measure in place of convergence almost everywhere.

## Explanations

### L1 human

Pointwise convergence alone does not make integrals converge, because mass can escape into thin tall spikes.
On a space of finite total measure, uniform integrability is exactly the condition that forbids such spikes.
So it is the precise condition for convergence of the integrals.

### L2 human

The theorem refines the dominated convergence theorem: a dominated sequence is uniformly integrable, but not conversely.
It is the form of the convergence theorem used in probability, where one shows uniform integrability with a moment bound such as $\sup_n \mathbb{E}[\abs{Y_n}^p] < \infty$ for some $p > 1$.
There are versions for $L^p$ and for infinite measure spaces, where a condition of tightness is added.
