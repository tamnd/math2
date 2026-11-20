---
tag: 1JJCGNX240
kind: concept
name: Categorical theory
aliases: [kappa-categorical-theory, categoricity-in-power]
msc: ["03C35"]
topics: [6XEXRME4C1]
audience: grad
uses: [92SWXST1ZM, MVCH6N9SNW, 0EBACQFAZW, PZMGQMDN25, 484M0TZ1S7]
sources:
  - url: https://en.wikipedia.org/wiki/Categorical_theory
    locator: History and motivation
  - book: isbn:9780387987606
  - book: isbn:9780521587136
same_as:
  wikidata: Q15830473
  wikipedia: Categorical theory
---

## Summary

Let $T$ be a [[first-order theory|92SWXST1ZM]] in a signature $L$, and let $\kappa$ be an infinite [[cardinal|0EBACQFAZW]].
The theory $T$ is *$\kappa$-categorical* when $T$ has a [[model|MVCH6N9SNW]] of cardinality $\kappa$, and any two models of $T$ of cardinality $\kappa$ are [[isomorphic|PZMGQMDN25]].
So $T$ is $\kappa$-categorical when it has exactly one model of size $\kappa$ up to isomorphism.
The idea matters because a theory with one model in a size describes that model completely, and the [[Łoś-Vaught test|ZR7Y5C235P]] turns this uniqueness into completeness.

## Motivation

Axioms often aim at one intended structure, such as the rational order or the complex field.
A first-order theory with an infinite model cannot pin down one structure, since the [[Löwenheim-Skolem theorem|484M0TZ1S7]] gives it models of many sizes.
Models of different sizes are never isomorphic.
So the best that first-order logic can give is uniqueness inside one cardinality.
This weaker uniqueness still happens often: the countable dense orders without endpoints are all isomorphic, and so are the algebraically closed fields of characteristic $0$ and size $\aleph_1$.
Categoricity in power asks which theories have this property, and in which cardinals.

## Notation

The phrases "$\kappa$-categorical" and "categorical in power $\kappa$" are synonyms.
For $\kappa = \aleph_0$ one says $\aleph_0$-categorical, $\omega$-categorical or countably categorical; see [[omega-categorical theory|A22K1X8GKD]].
A theory is *uncountably categorical* when it is $\kappa$-categorical for every uncountable $\kappa$, and *totally categorical* when it is $\kappa$-categorical for every infinite $\kappa$.
The number of models of $T$ of size $\kappa$ up to isomorphism is written $I(T, \kappa)$, so $T$ is $\kappa$-categorical exactly when $I(T, \kappa) = 1$.
Some books drop the existence of a model of size $\kappa$ from the definition; for a theory with an infinite model and $\kappa \ge \abs{L}$ the two versions agree, because such a model always exists.
In older texts a theory is *categorical* when all its models are isomorphic; this notion is due to Veblen.

## Remarks

### Examples

- The theory of [[dense linear orders without endpoints|2W4S2H4VYA]] is $\aleph_0$-categorical, by Cantor's back-and-forth argument, and not $\kappa$-categorical for uncountable $\kappa$.
- The theory of infinite sets in the empty signature is totally categorical, because two sets of the same cardinality are in bijection.
- The theory of nonzero [[vector spaces over the rationals|~187e3871]] is uncountably categorical, because a space of uncountable size $\kappa$ has dimension $\kappa$; it is not $\aleph_0$-categorical.
- The theory of algebraically closed fields of a fixed characteristic is uncountably categorical, by Steinitz's classification by transcendence degree.
- More cases, with a table of all four possible behaviors, are in [[the standard examples|~9a561b71]].

### Non-examples

- The complete theory of $(\Z, <)$ is $\kappa$-categorical for no infinite $\kappa$; see [[this non-example|~9769b292]]. The uniqueness condition fails in every infinite size.
- The theory of groups is not $\kappa$-categorical for any infinite $\kappa$: the abelian groups $\bigoplus_{\kappa} \Z/2\Z$ and $\bigoplus_{\kappa} \Z/3\Z$ both have size $\kappa$, and they are not isomorphic, since only the first has an element of order $2$.
- Let $L$ have constants $c_\alpha$ for $\alpha < \omega_1$, and let $T$ say that they are pairwise distinct. Then $T$ has no countable model, so the existence condition fails and $T$ is not $\aleph_0$-categorical.

### Basic properties

- A theory with an infinite model is never categorical in Veblen's sense. The [[Löwenheim-Skolem theorem|484M0TZ1S7]] gives models of every infinite size $\kappa \ge \abs{L}$, and models of different sizes are not isomorphic.
- The [[Łoś-Vaught test|ZR7Y5C235P]]: a $\kappa$-categorical theory with no finite models and $\kappa \ge \abs{L}$ is complete.
- The [[Ryll-Nardzewski theorem|1513J40TKA]] characterizes $\aleph_0$-categoricity of a countable complete theory by counting types.
- [[Morley's categoricity theorem|V7N84P60SJ]]: a countable theory that is $\kappa$-categorical for one uncountable $\kappa$ is $\kappa$-categorical for all uncountable $\kappa$.
- So a countable complete theory with infinite models is in exactly one of four classes: totally categorical, $\aleph_0$-categorical only, uncountably categorical only, or categorical in no infinite cardinal. All four occur.

### History

Oswald Veblen called a theory categorical in 1904 when all its models are isomorphic.
Jerzy Łoś and Robert Vaught introduced categoricity in a cardinal, and in 1954 both proved the completeness test.
Łoś asked whether categoricity in one uncountable cardinal implies categoricity in all uncountable cardinals.
Michael Morley proved in 1965 that categoricity in one uncountable cardinal gives categoricity in all of them, and Saharon Shelah extended this to uncountable languages in 1974.

### Common errors

- To conclude completeness from categoricity alone. The test needs the absence of finite models; the empty theory is totally categorical and not complete.
- To believe the converse of the test. The theory of $(\Z, <)$ is complete and categorical in no infinite cardinal.
- To forget the size of the language. A theory in a language of size $\aleph_1$ can be $\aleph_0$-categorical and incomplete, as the proof of the [[Łoś-Vaught test|ZR7Y5C235P]] shows.

## Explanations

### L1 human

A theory is a list of rules, and a model is a world that obeys the rules.
Usually many different worlds obey the same rules.
A theory is categorical in a size when all its worlds of that size are copies of one another.
For example, think of points on a line where between any two points there is a third, and there is no first or last point.
Any two such lines with countably many points can be matched point by point, keeping the order.
So the rules of dense orders are categorical in the countable size.
For uncountable sizes this fails: the real line and some other dense lines of the same size cannot be matched.

### L2 human

We check that the theory $T$ of infinite sets in the empty signature is $\kappa$-categorical for every infinite $\kappa$.

1. The signature has no symbols, so a model of $T$ is just an infinite set, and an isomorphism is just a bijection.
2. $T$ has a model of size $\kappa$, namely $\kappa$ itself, which is infinite.
3. Let $A$ and $B$ be models of size $\kappa$. By the definition of cardinality there is a bijection $f : A \to B$.
4. A bijection preserves equality, the only relation of the empty signature, so $f$ is an isomorphism.

The typical use is the step before the [[Łoś-Vaught test|ZR7Y5C235P]]: $T$ has no finite models, so $T$ is complete.
A trap is to drop the axioms "there are at least $n$ elements": then the theory has finite models of different sizes, and it is not complete.

### L3 human

Categoricity in power is the start of classification theory.
For a countable theory, Morley's theorem shows that uncountable categoricity is one property, and its proof introduced $\omega$-stability and Morley rank, the subject of [[strongly minimal sets and Morley rank|S4EZ9JZJS6]].
The Baldwin-Lachlan theorem describes uncountably categorical theories by a strongly minimal set and a dimension, as for vector spaces and algebraically closed fields.
Countable categoricity is a different property, and it is about the finiteness of type spaces; see the [[Ryll-Nardzewski theorem|1513J40TKA]] and the sub-area on [[Fraïssé theory|ZS8X8KS54R]].
The function $\kappa \mapsto I(T, \kappa)$ is the spectrum problem; Shelah's main gap theorem describes its possible shapes for uncountable $\kappa$.
