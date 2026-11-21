---
tag: A9XBRF3A7Z
kind: concept
name: Hanf number
aliases: [hanf-number, hanf-number-of-a-logic, hanf-number-for-omitting-types]
msc: ["03C55", "03C75", "03C95"]
topics: [W9CHA4PD9H]
audience: research
uses: [PQG7VAZ1R2, G6X7SZSNC5, 0EBACQFAZW, DKFGQTRYZE, ZC4BHVHWE9, 484M0TZ1S7, NW4DREQ5DQ, 9V71Q3SD1G]
sources:
  - url: https://en.wikipedia.org/wiki/Löwenheim_number
    locator: lead section
  - book: isbn:9780486488219
    locator: Chapter 7
  - book: isbn:9780387987606
---

## Summary

Let $\mathcal{L}$ be a logic, such as first-order logic, the [[infinitary logic|PQG7VAZ1R2]] $L_{\omega_1\omega}$ or [[second-order logic|G6X7SZSNC5]], and fix a set of allowed signatures.
The *Hanf number* $h(\mathcal{L})$ is the least [[cardinal|0EBACQFAZW]] $\kappa$ with the following property.
Every [[sentence|DKFGQTRYZE]] of $\mathcal{L}$ that has a model of size at least $\kappa$ has models of arbitrarily large size.
Hanf showed that $h(\mathcal{L})$ exists whenever the sentences of $\mathcal{L}$, up to renaming of symbols, form a set.
The Hanf number measures how far a logic can pin down the size of its models, and its value ties model theory to cardinal arithmetic and to large cardinals.

## Motivation

The upward [[Löwenheim-Skolem theorem|484M0TZ1S7]] says that a first-order sentence with an infinite model has models of every infinite size.
Stronger logics lose this property: a sentence of $L_{\omega_1\omega}$ can say that every element is one of countably many constants, and then all its models are countable.
One can still ask for a threshold beyond which a sentence cannot stop.
For a logic with a set of sentences, each sentence without arbitrarily large models has a bound on its sizes, and the supremum of these bounds is such a threshold.
Computing it is a problem about the combinatorics of large models.

## Notation

The Hanf number of $\mathcal{L}$ is written $h(\mathcal{L})$ or $\operatorname{hn}(\mathcal{L})$.
Some authors use instead the supremum of the sizes of the models of sentences without arbitrarily large models.
The two values are equal or differ by one successor step.
For first-order theories, the *Hanf number for omitting types* is the least $\kappa$ such that a countable theory with a model of size at least $\kappa$ that omits a countable set of [[types|9V71Q3SD1G]] has arbitrarily large such models.
The [[beth numbers|ZC4BHVHWE9]] $\beth_\alpha$ give the values: $\beth_0 = \aleph_0$, $\beth_{\alpha+1} = 2^{\beth_\alpha}$, and suprema at limits.

## Remarks

### Examples

- First-order logic has Hanf number $\aleph_0$: the sentences "there are exactly $n$ elements" exclude finite values, and upward Löwenheim-Skolem gives the bound; see [[this example|Y1TD2DS14K]].
- The logic $L_{\omega_1\omega}$ with countable signatures has Hanf number $\beth_{\omega_1}$, by Morley's method of indiscernibles and a matching family of sentences; see [[this example|QC25K2Y91B]].
- The Hanf number for omitting types in countable first-order theories is $\beth_{\omega_1}$, by the same method; Chang's reduction turns sentences of $L_{\omega_1\omega}$ into countable theories with countably many types to omit.
- Second-order logic has a Hanf number, since its sentences in a fixed set of symbols form a set. If an [[inaccessible cardinal|NW4DREQ5DQ]] exists, the Hanf number is larger than the least one.

### Non-examples

- For $L_{\omega_1\omega}$ no $\beth_\alpha$ with $\alpha < \omega_1$ is the Hanf number: some sentence has a model of size $\beth_\alpha$ and no larger model; see [[this example|CGEPN90SDZ]].
- The value $\aleph_0$ is not the Hanf number of $L_{\omega_1\omega}$: the sentence $\forall x \bigvee_{n} x = c_n$ has a countably infinite model and no uncountable one.
- The logic $L_{\infty\omega}$ with all set-sized conjunctions has no Hanf number. For each cardinal $\mu$, the sentence $\forall x \bigvee_{\beta < \mu} x = c_\beta$ with distinct constants has models of size exactly $\mu$ only.

### Basic properties

- If every sentence of $\mathcal{L}$ is equivalent to a sentence of $\mathcal{L}'$, then $h(\mathcal{L}) \le h(\mathcal{L}')$.
- The Hanf number differs from the Löwenheim number, the least $\kappa$ such that every satisfiable sentence has a model of size at most $\kappa$. For $L_{\omega_1\omega}$ the Löwenheim number is $\aleph_0$ and the Hanf number is $\beth_{\omega_1}$.
- For $L_{\omega_1\omega}$, a sentence with models of size at least $\beth_\alpha$ for all $\alpha < \omega_1$ has models of every infinite size, by [[Ehrenfeucht-Mostowski models|TSGB29FJM0]].
- The upper bound for $L_{\omega_1\omega}$ uses Morley's form of the [[existence of indiscernibles|RG6D2FAS14]].

### History

The Hanf number is named after William Hanf, who proved that it exists for logics whose sentences form a set.
Morley computed the Hanf number of $L_{\omega_1\omega}$ and the Hanf number for omitting types, both equal to $\beth_{\omega_1}$, with his method of indiscernibles.
The Hanf number of second-order logic is larger than many large cardinals when they exist, because second-order sentences can describe initial segments $V_\kappa$ of the set-theoretic universe.

### Common errors

- Arbitrarily large models need not mean models of every large size. In second-order logic a sentence can say that the size of the universe is an infinite successor cardinal.
- The Hanf number is not the least size of a model with special properties; it is a bound for the sizes of models of sentences without arbitrarily large models.

## Explanations

### L1 human

Some descriptions of a structure force it to be small: "there are exactly five elements" is one.
Other descriptions allow structures of every size, however large.
The Hanf number is a size such that any description with a structure at least that big has structures of every larger size as well.
For ordinary first-order logic this size is the first infinite size, because a description with an infinite example has examples of all infinite sizes.
For stronger logics the size is much larger, and it tells how much the logic can control size.

### L2 human

We check that $\aleph_0$ is not the Hanf number of $L_{\omega_1\omega}$, with the sentence $\varphi := \forall x \bigvee_{n \in \N} x = c_n \wedge \bigwedge_{m < n} c_m \ne c_n$.

1. The structure $\N$ with $c_n = n$ is a model, since every element is some $n$ and the constants are distinct.
2. In every model $\mathcal{M}$ of $\varphi$, the map $n \mapsto c_n^{\mathcal{M}}$ is onto $M$, so $M$ is countable.
3. So $\varphi$ has a model of size $\aleph_0$ and no model of size $\aleph_1$, and $\aleph_0$ does not have the property.

The typical use of the Hanf number is as a size threshold: to show that a sentence has arbitrarily large models, it suffices to find one model of size at least $h(\mathcal{L})$.
The trap is to forget that the threshold depends on the logic: for first-order logic the threshold is $\aleph_0$, and the same argument fails for $L_{\omega_1\omega}$.

### L3 human

Hanf numbers are the size side of abstract model theory, as Löwenheim numbers are the small side.
For $L_{\omega_1\omega}$ the value $\beth_{\omega_1}$ is computed by Morley's use of the Erdős-Rado theorem, and it is sharp because $L_{\omega_1\omega}$ can describe the levels $V_{\omega + \alpha}$ for countable $\alpha$.
For second-order logic the Hanf number is beyond the reach of ZFC: it depends on which large cardinals exist, and second-order sentences can describe $V_\kappa$ for many large cardinals $\kappa$.
Hanf numbers also appear as thresholds for abstract elementary classes, for instance in [[Shelah's categoricity conjecture|TSFJ71QC4G]].
The partition methods behind the computation are those of the [[existence of indiscernibles|RG6D2FAS14]], and the models that realize the bound are Ehrenfeucht-Mostowski models.
