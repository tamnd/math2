---
tag: 4STP69KESQ
kind: statement
role: theorem
name: Chang's two-cardinal theorem
aliases: [chang-two-cardinal-theorem, changs-two-cardinal-theorem]
msc: ["03C55", "03C50", "03E45"]
topics: [W9CHA4PD9H]
audience: research
about: [XT227BYP7B]
uses: [XT227BYP7B, 92SWXST1ZM, 13ZV2F8JAR, RMTZ5J64FX, GSQ833HAZT, DZ65A6X12W, 0MN2MER9WN]
history:
  notes: "Chen Chung Chang proved the theorem; Jensen invented morasses for his proof that cardinal transfer theorems hold under the axiom of constructibility."
sources:
  - url: https://en.wikipedia.org/wiki/Morass_(set_theory)
    locator: lead section
  - url: https://en.wikipedia.org/wiki/Chang's_conjecture
    locator: lead section
  - book: isbn:9780486488219
    locator: Chapter 7
  - book: isbn:9780387987606
---

## Statement

Let $L$ be a countable signature with a unary relation symbol $P$, and let $T$ be an $L$-[[theory|92SWXST1ZM]].
A $(\kappa, \lambda)$-model of $T$ is a model $\mathcal{M}$ with $\abs{M} = \kappa$ and $\abs{P^{\mathcal{M}}} = \lambda$, as in [[Vaught's two-cardinal theorem|XT227BYP7B]].
Let $\kappa$ be an infinite cardinal with $\kappa^{<\kappa} = \kappa$.

If $T$ has an $(\aleph_1, \aleph_0)$-model, then $T$ has a $(\kappa^+, \kappa)$-model.

The condition $\kappa^{<\kappa} = \kappa$ implies that $\kappa$ is [[regular|13ZV2F8JAR]].
Under the generalized continuum hypothesis it holds for every regular $\kappa$, so then $(\aleph_1, \aleph_0)$-models give $(\kappa^+, \kappa)$-models for all regular $\kappa$.
An outline of the proof is in [[the outline proof of Chang's two-cardinal theorem|5C2K2REQCC]].

## Remarks

### Why each hypothesis is needed

- The $(\aleph_1, \aleph_0)$-model: the theory $\set{\forall x \, P(x)}$ has no $(\kappa^+, \kappa)$-model, and it has no $(\aleph_1, \aleph_0)$-model.
- The condition $\kappa^{<\kappa} = \kappa$: the proof needs a [[saturated model|RMTZ5J64FX]] of size $\kappa$, and such models need not exist without it. For example, the theory of dense linear orders has a saturated model of size $\aleph_1$ exactly when the [[continuum hypothesis|0MN2MER9WN]] holds.
- Countable $L$: the [[existence of saturated models|GSQ833HAZT]] of size $\kappa$ needs $\abs{L} < \kappa$, and the first step uses the countable case of Vaught's theorem.

### Consequences

- For $\kappa = \aleph_0$ the theorem is the conclusion of Vaught's theorem, with nothing to prove.
- Under the generalized continuum hypothesis, a countable theory with a $(\kappa, \lambda)$-model for some $\kappa > \lambda \ge \aleph_0$ has a $(\mu^+, \mu)$-model for every regular $\mu$. This combines the theorem with Vaught's theorem.
- With the continuum hypothesis, $\kappa = \aleph_1$ satisfies $\kappa^{<\kappa} = 2^{\aleph_0} = \aleph_1$, so an $(\aleph_1, \aleph_0)$-model gives an $(\aleph_2, \aleph_1)$-model.

### Converse

The converse holds in ZFC: a $(\kappa^+, \kappa)$-model with $\kappa \ge \aleph_0$ has $\kappa^+ > \kappa \ge \aleph_0$, so Vaught's theorem gives an $(\aleph_1, \aleph_0)$-model.

### Generalizations

- Gap-$n$ transfers ask whether a $(\kappa^{+n}, \kappa)$-model gives a $(\mu^{+n}, \mu)$-model, for $n \ge 2$. The gap is the number of cardinal steps between $\abs{P}$ and $\abs{M}$.
- Jensen invented morasses for his proof that cardinal transfer theorems hold under the axiom of constructibility, and gap-$n$ morasses serve the larger gaps.
- Shelah and Stanley, and independently Velleman, gave forcing axioms equivalent to the existence of morasses, which make morasses easier to use.
- Downward transfers are also set-theoretic. [[Chang's conjecture|F855E3QA4B]] says that every $(\aleph_2, \aleph_1)$-model of a countable theory has an elementary submodel that is an $(\aleph_1, \aleph_0)$-model.
- Chang's conjecture fails under the axiom of constructibility, and Silver proved its consistency from the consistency of an $\omega_1$-Erdős cardinal. So two-cardinal transfers can be independent of ZFC.

## History

Chen Chung Chang proved the theorem.
Jensen invented morasses for his proof that cardinal transfer theorems hold in the constructible universe.
Silver proved the consistency of Chang's conjecture from the consistency of an $\omega_1$-Erdős cardinal.

## Explanations

### L1 human

Vaught's theorem moves any gap between two sizes down to the smallest gap: countable and the first uncountable size.
Chang's theorem moves this smallest gap up again, to any size $\kappa$ and the next size $\kappa^+$.
For this it needs an assumption about set theory, such as the generalized continuum hypothesis.
For example, under that hypothesis, a theory with a model of size $\aleph_1$ whose small part is countable also has a model of size $\aleph_2$ whose small part has size $\aleph_1$.

### L2 human

We check the hypothesis $\kappa^{<\kappa} = \kappa$ for $\kappa = \aleph_1$ under the continuum hypothesis.

1. A function from a cardinal $\mu < \aleph_1$ to $\aleph_1$ has a countable domain.
2. Its range is countable, so it is bounded below some $\beta < \omega_1$, and it is a function from $\mu$ to $\beta$.
3. For a fixed countable $\beta$ and $\mu$ there are at most $\aleph_0^{\aleph_0} = 2^{\aleph_0}$ such functions.
4. There are countably many choices of $\mu$ and $\aleph_1$ choices of $\beta$, so $\aleph_1^{<\aleph_1} \le \aleph_1 \cdot 2^{\aleph_0}$, which is $\aleph_1$ under the continuum hypothesis.

The typical use is to transfer a two-cardinal property of a countable theory to all regular cardinals in a model of the generalized continuum hypothesis, such as the constructible universe.
The trap is to apply the theorem to singular $\kappa$: then $\kappa^{<\kappa} > \kappa$, and other methods are needed.

### L3 human

Chang's theorem is the first upward transfer theorem for two cardinals, and it shows that upward transfer depends on cardinal arithmetic.
Its proof uses saturated models of size $\kappa$, which exist when $\kappa^{<\kappa} = \kappa$, and the [[uniqueness of saturated models|DZ65A6X12W]] in place of the countable homogeneous models in Vaught's proof.
Larger gaps and singular cardinals lead to combinatorial principles of the constructible universe, such as morasses, and downward transfers such as Chang's conjecture lead to large cardinals.
So the two-cardinal problems form a bridge between model theory and set theory.
