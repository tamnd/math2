---
tag: N7C06T3KCZ
kind: statement
role: theorem
name: Shadowing lemma
msc: [37C50, 37D05]
uses: [7CBT4SM83Y, 0KZZ70ZHXP, MPFD24TYW2, TAFJV2YWKR]
about: [MPFD24TYW2]
sources:
  - url: https://en.wikipedia.org/wiki/Shadowing_lemma
same_as:
  wikidata: Q7460736
  wikipedia: Shadowing lemma
---

## Statement

Let $M$ be a [[Riemannian manifold|7CBT4SM83Y]] with distance $d$, let $f \colon M \to M$ be a $C^1$ [[diffeomorphism|0KZZ70ZHXP]], and let $\Lambda \subseteq M$ be a compact [[hyperbolic set|MPFD24TYW2]] for $f$.
For $\varepsilon > 0$, an *$\varepsilon$-pseudo-orbit* is a sequence $(x_n)_{n \in \Z}$ in $M$ with $d(f(x_n), x_{n+1}) < \varepsilon$ for all $n \in \Z$.
A point $x \in M$ *$\delta$-shadows* it if $d(f^n(x), x_n) < \delta$ for all $n \in \Z$.
Then there is an open neighbourhood $U$ of $\Lambda$ with the property that follows.
For every $\delta > 0$ there is $\varepsilon > 0$ such that every $\varepsilon$-pseudo-orbit contained in $U$ is $\delta$-shadowed by some $x \in M$.
Moreover, there is $\delta_0 > 0$ such that for $\delta < \delta_0$ the shadowing point $x$ is unique.

## Remarks

The idea of the proof: a pseudo-orbit is a near-solution of the equation $x_{n+1} = f(x_n)$ in a space of sequences.
Hyperbolicity makes the linearised equation invertible with a bounded inverse, contracting forward along stable directions and backward along unstable ones, and a fixed-point argument gives a true solution nearby.
Uniqueness comes from [[expansiveness|TAFJV2YWKR]] near $\Lambda$: two orbits that stay $\delta$-close for all times coincide.
For an Anosov diffeomorphism of a compact manifold, $\Lambda = M$, so every pseudo-orbit with small enough errors is shadowed.
Hyperbolicity is needed: consider the rotation of the circle by an irrational angle $\alpha$.
The pseudo-orbit that rotates by $\alpha + \varepsilon/2$ at each step drifts away from every true orbit at rate $\varepsilon/2$ per step.

## Explanations

### L1 human

When a computer follows an orbit, it makes a small rounding error at each step, so it computes a pseudo-orbit rather than a true one.
For chaotic hyperbolic systems the errors grow fast, so the computed orbit soon differs from the true orbit with the same start.
The shadowing lemma says that it still stays close to some other true orbit for all times.
So the pictures a computer draws of such systems are faithful in this sense: each computed orbit is close to some real orbit.

### L2 human

Shadowing is the main tool for building orbits with prescribed behaviour in hyperbolic dynamics.
One glues pieces of orbits into a pseudo-orbit and shadows it.
This gives the Anosov closing lemma, which finds a periodic orbit near any orbit segment that nearly closes up.
It also gives the Markov partitions used to code the dynamics by subshifts of finite type.
It also gives structural stability of Anosov diffeomorphisms, since a perturbed orbit is a pseudo-orbit of the original map.
