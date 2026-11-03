---
tag: CJ19SSY2E4
kind: definition
name: Creation and annihilation operators
msc: [81Q12, 81V73, 81V74]
defines: 7N0J4DF8N5
uses: [1TJ8TNH331, Y64G7W4BEC, 6HSJBJ8TTQ, KRJX5RA0PW, 6TW5A09KCB]
sources:
  - url: https://en.wikipedia.org/wiki/Creation_and_annihilation_operators
---

## Definition

Let $\mathfrak{h}$ be a complex Hilbert space, with inner product $\ip{\cdot}{\cdot}$ linear in the second argument.
Let $\mathcal{F}_\pm(\mathfrak{h}) = \widehat{\bigoplus}_{n \ge 0} \mathcal{H}^{(n)}_\pm$ be the bosonic ($+$) or fermionic ($-$) [[Fock space|1TJ8TNH331]].
Here $\mathcal{H}^{(n)}_\pm = P_\pm \mathfrak{h}^{\otimes n}$ is the $n$-particle space of [[identical particles|Y64G7W4BEC]], and $P_\pm$ is the symmetrizing or antisymmetrizing projection.
Let $\mathcal{F}_0$ be the subspace of vectors with only finitely many nonzero components.
For $f \in \mathfrak{h}$, the *creation operator* $a^*(f)$ is the linear operator on $\mathcal{F}_0$ given on $\psi \in \mathcal{H}^{(n)}_\pm$ by
$$a^*(f)\, \psi = \sqrt{n+1}\; P_\pm (f \otimes \psi) \in \mathcal{H}^{(n+1)}_\pm.$$
The *annihilation operator* $a(f)$ is the restriction to $\mathcal{F}_0$ of the [[adjoint|6HSJBJ8TTQ]] of $a^*(f)$.
It maps $\mathcal{H}^{(n+1)}_\pm$ into $\mathcal{H}^{(n)}_\pm$ and sends the vacuum $\Omega = 1 \in \mathcal{H}^{(0)}_\pm = \C$ to $0$.

## Remarks

The map $f \mapsto a^*(f)$ is linear and $f \mapsto a(f)$ is antilinear.
In the bosonic case they satisfy, on $\mathcal{F}_0$,
$$[a(f), a(g)] = 0, \qquad [a(f), a^*(g)] = \ip{f}{g}\, I.$$
In the fermionic case they satisfy the [[canonical anticommutation relations|6TW5A09KCB]]
$$\{a(f), a(g)\} = 0, \qquad \{a(f), a^*(g)\} = \ip{f}{g}\, I,$$
where $\{A, B\} = AB + BA$.
Fermionic operators extend to bounded operators with $\norm{a(f)} = \norm{f}$, while bosonic ones are [[unbounded|KRJX5RA0PW]].

Example: let $\mathfrak{h} = \C$ and $f = 1$, in the bosonic case.
Then $\mathcal{H}^{(n)}_+$ is spanned by the unit vector $e_n = 1^{\otimes n}$, and the definition gives $a^* e_n = \sqrt{n+1}\, e_{n+1}$ and $a\, e_{n+1} = \sqrt{n+1}\, e_n$.
Check: $a a^* e_n = (n+1) e_n$ and $a^* a\, e_n = n\, e_n$, so $[a, a^*] = I$.

Non-example: in the fermionic case with $\mathfrak{h} = \C$, the space $\mathcal{H}^{(2)}_- = \set{0}$, so $a^*(1)^2 = 0$, and a second particle cannot be created in the same state.
Hence the bosonic rule $[a, a^*] = I$ fails there: on $\C^2 = \mathcal{H}^{(0)}_- \oplus \mathcal{H}^{(1)}_-$ the operators satisfy $a a^* + a^* a = I$ instead.
