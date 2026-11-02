---
tag: S1CJV1PA3D
kind: statement
role: theorem
name: Oka principle
msc: [32Q56, 32L05, "32E10"]
uses: [HMCD0JBFST, QAC7BYK9KX, PQ6Q143ARJ, R7VKRV8AGQ]
about: [HMCD0JBFST, QAC7BYK9KX]
sources:
  - url: https://en.wikipedia.org/wiki/Stein_manifold
---

## Statement

Let $X$ be a [[Stein manifold|HMCD0JBFST]].
Then two [[holomorphic line bundles|QAC7BYK9KX]] on $X$ are holomorphically isomorphic if and only if they are isomorphic as topological complex line bundles.
Moreover, every topological complex line bundle on $X$ is isomorphic to a holomorphic one.
Equivalently, the first Chern class map $c_1 \colon H^1(X, \mathcal{O}^*) \to H^2(X, \Z)$ is a group isomorphism.

## Remarks

The proof uses the exponential sequence $0 \to \Z \to \mathcal{O} \to \mathcal{O}^* \to 0$, where the second map is $f \mapsto e^{2\pi i f}$.
Its long exact [[cohomology|PQ6Q143ARJ]] sequence contains $H^1(X, \mathcal{O}) \to H^1(X, \mathcal{O}^*) \to H^2(X, \Z) \to H^2(X, \mathcal{O})$.
By [[Cartan's theorem B|R7VKRV8AGQ]], the two outer groups are zero, so the middle map, which is $c_1$, is an isomorphism.
Topological complex line bundles are classified by $H^2(X, \Z)$ through their Chern class, which gives the first two sentences.
Oka proved this result in 1939, in the language of the second Cousin problem.
In that form it says that on a domain of holomorphy, a second Cousin problem is solvable holomorphically if and only if it is solvable continuously.
The name Oka principle is also used for a general heuristic.
On Stein spaces, holomorphic problems with only topological obstructions should be solvable holomorphically as soon as they are solvable continuously.
The Stein hypothesis is needed.
On a compact complex torus of dimension $1$, the holomorphic line bundles of degree $0$ are all topologically trivial, but they form a family parametrized by the torus itself.

## Explanations

### L1 human

On a Stein manifold, a holomorphic line bundle is determined, up to isomorphism, by its topology alone.
So a question about holomorphic objects, which looks hard, is the same as a question about continuous objects, which is a question of algebraic topology.
This surprising rigidity is the original Oka principle.

### L2 human

The result solves the second Cousin problem on Stein manifolds: it is solvable exactly when the associated line bundle has Chern class zero, in particular always when $H^2(X, \Z) = 0$.
Grauert extended the principle from line bundles to vector bundles and principal bundles with a complex Lie group as structure group.
Gromov and Forstnerič extended it further to sections of holomorphic submersions and to maps into Oka manifolds.
