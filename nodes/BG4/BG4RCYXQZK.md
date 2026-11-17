---
tag: BG4RCYXQZK
kind: example
name: Kleene's O is not an ordinal notation system
msc: ["03D60", "03F15"]
topics: [XTTKZTYDSD]
audience: research
not_instance_of:
  - target: 7MBX59Y7N9
    note: the set of notations of Kleene's O is not computable (it is Π¹₁-complete), and its order is not total
uses: [3CNSYYX2HF, WHAP0K600D, M6JGF4TPM6, KZSB5E471K]
sources:
  - url: https://en.wikipedia.org/wiki/Kleene%27s_O
    locator: lead section
  - url: https://en.wikipedia.org/wiki/Ordinal_notation
    locator: Kleene's O
---

## Example

[[Kleene's O|WHAP0K600D]] is the set $\mathcal{O} \subseteq \N$ with the relation $<_{\mathcal{O}}$ and the map $a \mapsto \abs{a}$ defined by three rules.
Here $\varphi_e$ is the $e$-th partial [[computable function|KZSB5E471K]].

- $1 \in \mathcal{O}$, with $\abs{1} = 0$.
- If $a \in \mathcal{O}$, then $2^a \in \mathcal{O}$, with $\abs{2^a} = \abs{a} + 1$ and $a <_{\mathcal{O}} 2^a$.
- If $\varphi_e$ is total, each $\varphi_e(n)$ is in $\mathcal{O}$, and $\varphi_e(n) <_{\mathcal{O}} \varphi_e(n+1)$ for all $n$, then $3 \cdot 5^e \in \mathcal{O}$, with $\abs{3 \cdot 5^e} = \sup_n \abs{\varphi_e(n)}$ and $\varphi_e(n) <_{\mathcal{O}} 3 \cdot 5^e$ for all $n$.

The relation $<_{\mathcal{O}}$ is the least transitive relation that contains these instances.
We check the conditions of an [[ordinal notation system|3CNSYYX2HF]] one by one.

1. Computability of the set fails. The set $\mathcal{O}$ is $\Pi^1_1$-complete in the [[analytical hierarchy|M6JGF4TPM6]], so it is not computable, and it is not even arithmetical.
2. Totality fails. Let $e$ and $e'$ be indices of two total functions with $\varphi_e(n) = 2^{2^{\cdots}}$ ($n$ times applied to $1$), the notation for $n$, and with $\varphi_{e'}(n)$ the notation for $n + 1$. Both $3 \cdot 5^e$ and $3 \cdot 5^{e'}$ denote $\omega$ and are different numbers when $e \ne e'$, and neither is below the other in $<_{\mathcal{O}}$, because $<_{\mathcal{O}}$ only adds a limit above the terms of its own sequence.
3. Well-foundedness holds. Each $a \in \mathcal{O}$ has an ordinal $\abs{a}$, and $b <_{\mathcal{O}} a$ implies $\abs{b} < \abs{a}$.

So $(\mathcal{O}, <_{\mathcal{O}})$ is not an ordinal notation system: conditions 1 and 2 of the definition fail.

## Remarks

What survives: for each $a \in \mathcal{O}$, the set $\set{b : b <_{\mathcal{O}} a}$ is computably enumerable and is well-ordered by $<_{\mathcal{O}}$ with type $\abs{a}$.
The ordinals $\abs{a}$ for $a \in \mathcal{O}$ are exactly the ordinals below the Church-Kleene ordinal $\omega_1^{\mathrm{CK}}$.
So $\mathcal{O}$ is a universal pointer to all computable ordinals, at the price of decidability.
A single path through $\mathcal{O}$ is a set that is linearly ordered by $<_{\mathcal{O}}$ and closed downward.
Such a path is closer to a notation system, but it is still not computable in general.

## Explanations

### L1 human

Kleene's O gives a name to every ordinal that a computer can describe.
But many ordinals get many different names, and two names for the same ordinal are often not compared at all.
Worse, no program can decide whether a given number is a name.
So it is a catalogue of all computable ordinals, not a naming scheme that a program can use.

### L2 human

We check one name and see why the system is too large.

1. The number $1$ names $0$, and $2^1 = 2$ names $1$, and $2^2 = 4$ names $2$.
2. A program $e$ that lists $1, 2, 4, 16, \ldots$ gives the name $3 \cdot 5^e$ for $\omega$.
3. To accept $3 \cdot 5^e$ as a name, one must know that the program $e$ halts on every input and lists names in increasing order.
4. This is a question about all inputs, and for higher names a question about all paths, so no program can answer it in general.

The typical use of $\mathcal{O}$ is in computability theory, as a complete set at the level $\Pi^1_1$.
The trap: $\mathcal{O}$ is not the "largest notation system" of proof theory, because it is not a notation system at all.
