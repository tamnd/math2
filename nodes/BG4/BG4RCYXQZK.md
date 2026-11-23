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

In Kleene's system the ordinal $\omega$ has infinitely many names, one for each program that lists the names of $0, 1, 2, \ldots$ in increasing order.
[[Kleene's O|WHAP0K600D]] is the set $\mathcal{O} \subseteq \mathbb{N}$, with the relation $<_{\mathcal{O}}$ and the map $a \mapsto \lvert a \rvert$, given by three rules.
Here $\varphi_e$ is the $e$-th partial [[computable function|KZSB5E471K]].

- $1 \in \mathcal{O}$, with $\lvert 1 \rvert = 0$.
- If $a \in \mathcal{O}$, then $2^a \in \mathcal{O}$, with $\lvert 2^a \rvert = \lvert a \rvert + 1$ and $a <_{\mathcal{O}} 2^a$.
- If $\varphi_e$ is total, each $\varphi_e(n)$ is in $\mathcal{O}$, and $\varphi_e(n) <_{\mathcal{O}} \varphi_e(n+1)$ for all $n$, then $3 \cdot 5^e \in \mathcal{O}$, with $\lvert 3 \cdot 5^e \rvert = \sup_n \lvert \varphi_e(n) \rvert$ and $\varphi_e(n) <_{\mathcal{O}} 3 \cdot 5^e$ for all $n$.

The relation $<_{\mathcal{O}}$ is the least transitive relation that contains these instances.
We check the conditions of an [[ordinal notation system|3CNSYYX2HF]] one by one.

1. Computability of the set fails.
   The set $\mathcal{O}$ is $\Pi^1_1$-complete in the [[analytical hierarchy|M6JGF4TPM6]], so it is not computable, and not even arithmetical.
2. Totality fails.
   Let $\varphi_e(n)$ be the notation for $n$ and let $\varphi_{e'}(n)$ be the notation for $n + 1$, with $e \ne e'$.
   Both $3 \cdot 5^e$ and $3 \cdot 5^{e'}$ denote $\omega$, and neither is below the other, because the only elements below a limit notation are those below the terms of its own sequence, and these are finite notations.
3. Well-foundedness holds.
   Each $a \in \mathcal{O}$ has an ordinal $\lvert a \rvert$, and $b <_{\mathcal{O}} a$ implies $\lvert b \rvert < \lvert a \rvert$.

Conditions 1 and 2 of the definition fail, so $(\mathcal{O}, <_{\mathcal{O}})$ is not an ordinal notation system.

## Remarks

Some structure survives.
For each $a \in \mathcal{O}$, the set $\{ b : b <_{\mathcal{O}} a \}$ is computably enumerable and is well-ordered by $<_{\mathcal{O}}$ with type $\lvert a \rvert$.
The ordinals $\lvert a \rvert$ for $a \in \mathcal{O}$ are exactly the ordinals below the Church-Kleene ordinal $\omega_1^{\mathrm{CK}}$.
So $\mathcal{O}$ points to all computable ordinals at once, and pays for this with decidability.
A path through $\mathcal{O}$, a downward closed set that $<_{\mathcal{O}}$ orders linearly, is closer to a notation system, but it is still not computable in general.

## Explanations

### L1 human

Kleene's O gives a name to every ordinal that a computer can describe.
But many ordinals get many different names, and two names for the same ordinal are often not compared at all.
Worse, no program can decide whether a given number is a name.
So it is a catalogue of all computable ordinals, not a naming scheme that a program can use.

### L2 human

Follow the first names and see why the system is too large.
The number $1$ names $0$, then $2^1 = 2$ names $1$, $2^2 = 4$ names $2$, and $2^4 = 16$ names $3$.
A program $e$ that lists $1, 2, 4, 16, \ldots$ gives the name $3 \cdot 5^e$ for $\omega$.
To accept $3 \cdot 5^e$ as a name, we must know that program $e$ halts on every input and lists names in increasing order.
That is a question about all inputs, and for higher names a question about all paths, so no program answers it in general.
The typical use of $\mathcal{O}$ is in computability theory, as a complete set at the level $\Pi^1_1$.
Watch out: $\mathcal{O}$ is not the "largest notation system" of proof theory, because it is not a notation system at all.
