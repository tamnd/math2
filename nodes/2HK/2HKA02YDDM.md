---
tag: 2HKA02YDDM
kind: definition
name: Nilpotency class
msc: [20F18, 20F14, 20D15]
defines: 4SQYNP0B4Y
uses: [0Q7MMQHC1P, 0K98R7A4VC, 0XW54DH28V]
sources:
  - url: https://en.wikipedia.org/wiki/Nilpotent_group
---

## Definition

Let $G$ be a [[nilpotent group|0Q7MMQHC1P]].
Let $\gamma_1(G) = G$ and $\gamma_{i+1}(G) = [\gamma_i(G), G]$ be its [[lower central series|0K98R7A4VC]].
The *nilpotency class* of $G$ is the least integer $c \ge 0$ such that $\gamma_{c+1}(G) = \{e\}$.

## Remarks

Equivalently, the class is the least $c$ such that the [[upper central series|0XW54DH28V]] satisfies $Z_c(G) = G$.
It is also the least length of a central series of $G$.
The trivial group has class $0$, and a nontrivial [[abelian group|082GHNPJ53]] has class $1$.
Example: the [[quaternion group|0NRJGW864D]] $Q_8$ has class $2$.
Indeed $\gamma_2(Q_8) = [Q_8, Q_8] = \{\pm 1\} \neq \{1\}$, and $\gamma_3(Q_8) = [\{\pm 1\}, Q_8] = \{1\}$ because $-1$ is central.
Non-example: the symmetric group $S_3$ has no class, because it is not nilpotent.
Its lower central series is $\gamma_1 = S_3$ and then $\gamma_i = A_3$ for all $i \ge 2$, so it never reaches $\{e\}$.

## Explanations

### L1 human

The class counts how many times you must take commutators with the whole group before everything becomes trivial.
