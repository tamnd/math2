---
tag: 3JE85VQR4G
kind: definition
name: Oscillator representation
msc: ["22E46", "22E70", 11F27]
defines: CCR7BAQ5N5
uses: [ZZYCV5EX9J, Z877XDBMQ3, 8B0JM2YDE2, X12FS2JAP0, PQ7JJY0VPH, 74BPYJNZTM, 7KGF78FGEF]
sources:
  - url: https://en.wikipedia.org/wiki/Oscillator_representation
---

## Definition

Let $n \ge 1$ and let $W = \R^{2n}$ with the standard [[symplectic form|PQ7JJY0VPH]] $\omega$.
Let $\mathbb H = W \times \R$ be the [[Heisenberg group|ZZYCV5EX9J]] with product $(w, s)(w', s') = (w + w', s + s' + \tfrac12 \omega(w, w'))$.
Let $\rho$ be the Schrödinger representation of $\mathbb H$ on $L^2(\R^n)$ with central character $(0, s) \mapsto e^{is}$.
Let $\mathrm{Sp}(W) = \mathrm{Sp}_{2n}(\R)$ be the [[symplectic group|X12FS2JAP0]], which acts on $\mathbb H$ by automorphisms $g \cdot (w, s) = (gw, s)$.
Let $p \colon \mathrm{Mp}(W) \to \mathrm{Sp}(W)$ be the [[metaplectic group|8B0JM2YDE2]], the connected double cover.
The *oscillator representation* is the unitary representation $\omega_\psi$ of $\mathrm{Mp}(W)$ on $L^2(\R^n)$ such that
$$\omega_\psi(\tilde g) \, \rho(w, s) \, \omega_\psi(\tilde g)^{-1} = \rho(p(\tilde g) w, s)$$
for all $\tilde g \in \mathrm{Mp}(W)$ and $(w, s) \in \mathbb H$.

## Remarks

Such a representation exists and is unique.
For each $g \in \mathrm{Sp}(W)$, the representation $(w, s) \mapsto \rho(gw, s)$ has the same central character as $\rho$.
So by the [[Stone–von Neumann theorem|Z877XDBMQ3]] there is a unitary $T_g$ with $T_g \rho(w, s) T_g^{-1} = \rho(gw, s)$, unique up to a scalar of modulus $1$.
The map $g \mapsto T_g$ is a projective representation of $\mathrm{Sp}(W)$, and the scalars can be chosen so that it lifts to a genuine representation of $\mathrm{Mp}(W)$.
Two lifts differ by a character of $\mathrm{Mp}(W)$, which is trivial since $\mathrm{Mp}(W)$ is connected with semisimple Lie algebra, hence equal to its commutator subgroup.

Example: for $n = 1$, the dilation $g = \operatorname{diag}(a, a^{-1})$ with $a > 0$ lifts to the operator $\psi(x) \mapsto a^{-1/2} \psi(x / a)$, up to sign.
It is unitary on $L^2(\R)$.
Conjugation by it turns the position operator $x$ into $x / a$ and the momentum operator $-i \, d/dx$ into $a \cdot (-i \, d/dx)$, which is the action of a diagonal symplectic map on position and momentum.

Non-example: the operators $T_g$ cannot be normalised to give a representation of $\mathrm{Sp}(W)$ itself.
Only the double cover carries a genuine representation, so the condition on $\mathrm{Mp}(W)$ in the definition cannot be replaced by one on $\mathrm{Sp}(W)$.

The oscillator representation splits into two irreducible pieces, on the even and on the odd functions.
