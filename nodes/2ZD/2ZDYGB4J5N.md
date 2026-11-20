---
tag: 2ZDYGB4J5N
kind: example
name: Strong Kleene logic is explosive
aliases: [k3-is-explosive]
msc: ["03B50", "03B53"]
topics: [NJB94B39QK]
audience: ug2
instance_of: [TTKZGJEEK7]
not_instance_of:
  - target: C7YWCR87QJ
    note: K3 designates only the value T, so no valuation designates both p and its negation
  - target: BXJZG67PX3
    note: K3 uses the same tables as LP but designates only T, so its consequence relation differs
uses: [TTKZGJEEK7, SZHA10A9X7, 029JBBF693, 1HK0VYWTV7]
sources:
  - url: https://en.wikipedia.org/wiki/Three-valued_logic
    locator: Kleene and Priest logics
  - book: isbn:9780521670265
---

## Example

[[Strong Kleene logic|SZHA10A9X7]] K3 has the values $\mathsf{T}$, $\mathsf{N}$ and $\mathsf{F}$, and only $\mathsf{T}$ is designated.
[[Negation|029JBBF693]] maps $\mathsf{T}$ to $\mathsf{F}$, $\mathsf{F}$ to $\mathsf{T}$, and $\mathsf{N}$ to $\mathsf{N}$.
We show that $\set{\varphi, \neg\varphi} \vDash_{\mathrm{K3}} \psi$ for all formulas $\varphi$ and $\psi$.

1. Let $v$ be a K3 valuation that designates $\varphi$ and $\neg\varphi$.
2. Since only $\mathsf{T}$ is designated, $v(\varphi) = \mathsf{T}$ and $v(\neg\varphi) = \mathsf{T}$.
3. By the table of $\neg$, $v(\varphi) = \mathsf{T}$ gives $v(\neg\varphi) = \mathsf{F}$, which contradicts step 2.
4. So no valuation designates both premises, and the [[consequence|1HK0VYWTV7]] holds vacuously.

Hence K3 is [[explosive|TTKZGJEEK7]].

## Remarks

The logic of paradox LP uses the same three tables and designates $\mathsf{T}$ and the middle value.
Then step 3 fails: the middle value $\mathsf{B}$ has $v(\neg\varphi) = \mathsf{B}$, which is designated.
So the choice of designated values, not the tables, decides explosion here.
K3 is paracomplete instead: $\varphi \lor \neg\varphi$ is not valid, because the valuation $v(\varphi) = \mathsf{N}$ gives it the value $\mathsf{N}$.

## Explanations

### L1 human

K3 adds a third value "neither true nor false" for sentences with a gap.
A sentence counts as accepted only when it is true.
A sentence and its negation can never both be true.
So, as in classical logic, a contradiction proves anything.

### L2 human

Check the three values of $p$ for the premises $p$ and $\neg p$.

- If $v(p) = \mathsf{T}$, then $v(\neg p) = \mathsf{F}$, which is not designated.
- If $v(p) = \mathsf{N}$, then $p$ is not designated.
- If $v(p) = \mathsf{F}$, then $p$ is not designated.

No row designates both premises, so $p, \neg p \vDash_{\mathrm{K3}} q$.
A trap is to think that every three-valued logic is paraconsistent; the designated set decides it.
