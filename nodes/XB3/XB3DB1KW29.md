---
tag: XB3DB1KW29
kind: example
name: Fields of characteristic zero form an elementary class that is not basic
msc: ["03C52", "12L12"]
topics: [AY09KYSW81]
audience: ug2
instance_of: [MEC3ZMC4F1]
not_instance_of:
  - target: JR6XPJ7X56
    note: every finite part of the axioms has a finite field of large prime characteristic as a model
uses: [MEC3ZMC4F1, JR6XPJ7X56, 1NR3HAWG9D, 1ZB13N78XW, 0ZXZ82FTX2, 04C5ZBG1WT]
sources:
  - url: https://en.wikipedia.org/wiki/Elementary_class
    locator: Examples
  - book: isbn:9780387987606
    locator: Chapter 2
---

## Example

Let $L = \set{+, -, \cdot, 0, 1}$, and for $n \ge 1$ write $n \cdot 1$ for the term $1 + \cdots + 1$ with $n$ ones.
Let $\Phi$ be the conjunction of the [[field|04C5ZBG1WT]] axioms, and let $T_0 = \set{\Phi} \cup \set{\neg(p \cdot 1 = 0) : p \text{ prime}}$.
We check that the fields of [[characteristic|1ZB13N78XW]] $0$ form an [[elementary class|MEC3ZMC4F1]], and that the class is not basic, so that $T_0$ is not [[finitely axiomatizable|JR6XPJ7X56]].

1. The characteristic of a field is $0$ or a prime. So a field has characteristic $0$ exactly when $p \cdot 1 \ne 0$ for every prime $p$, and the models of $T_0$ are exactly the fields of characteristic $0$.
2. Suppose a single sentence $\sigma$ has the same models. Then $T_0 \models \sigma$.
3. By the [[compactness theorem|1NR3HAWG9D]], some finite $T' \subseteq T_0$ has $T' \models \sigma$. Let $N$ be larger than every prime $p$ with $\neg(p \cdot 1 = 0) \in T'$.
4. Let $q > N$ be prime. The [[finite field|0ZXZ82FTX2]] $\mathbb{F}_q$ is a field with $p \cdot 1 \ne 0$ for every prime $p \ne q$, so $\mathbb{F}_q \models T'$.
5. So $\mathbb{F}_q \models \sigma$, and $\mathbb{F}_q$ has characteristic $0$ by the choice of $\sigma$. But $q \cdot 1 = 0$ in $\mathbb{F}_q$, a contradiction.

So the class is elementary, and no single sentence and no finite set of sentences axiomatizes it.

## Remarks

The same argument shows that every sentence true in all fields of characteristic $0$ is true in all fields of characteristic $p$ for all large enough primes $p$.
For a fixed prime $p$, the fields of characteristic $p$ form a basic elementary class, axiomatized by $\Phi \land p \cdot 1 = 0$.
The class of fields of positive characteristic is not elementary at all: it is the complement, among fields, of a class that is not basic; see [[the criterion for finite axiomatizability|9XKWFMVKJD]].

## Explanations

### L1 human

A field has characteristic $0$ when $1 + 1 + \cdots + 1$ is never $0$.
To say this we need one axiom for each prime: $1 + 1 \ne 0$, $1 + 1 + 1 \ne 0$, and so on.
Any finite part of this list is satisfied by a finite field whose size is a large prime.
So no finite list of axioms can describe the fields of characteristic $0$.

### L2 human

We check step 4 for $T' = \set{\Phi, \neg(2 \cdot 1 = 0), \neg(3 \cdot 1 = 0), \neg(5 \cdot 1 = 0)}$.

1. Take $q = 7$, a prime larger than $5$.
2. In $\mathbb{F}_7$, $2 \cdot 1 = 2$, $3 \cdot 1 = 3$ and $5 \cdot 1 = 5$, and none of them is $0$.
3. So $\mathbb{F}_7 \models T'$, although $7 \cdot 1 = 0$ in $\mathbb{F}_7$.

The typical use of the argument is to show that a property needs infinitely many axioms.
A trap is to stop at step 1: the fact that one natural axiomatization is infinite does not show that no finite one exists.
