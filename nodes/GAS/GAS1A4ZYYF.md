---
tag: GAS1A4ZYYF
kind: definition
name: Detonation
msc: [76L05, 80A25, 76V05]
defines: FBR0PYYJJ7
uses: [FRVV0NHBXT, SN4J6KP03C, SXSCYXH068]
sources:
  - url: https://en.wikipedia.org/wiki/Detonation
---

## Definition

Consider a combustible gas mixture that can react and release heat, as in [[combustion theory|SXSCYXH068]].
A combustion wave is a front that moves into the unburnt mixture and leaves burnt gas behind it.
Let $D$ be the speed of the front relative to the unburnt gas and let $c_1$ be the [[speed of sound|SN4J6KP03C]] in the unburnt gas.
The wave is a *detonation* if the following hold.

1. It moves supersonically into the unburnt gas: $D > c_1$.
2. It is led by a [[shock wave|FRVV0NHBXT]] that compresses the unburnt gas and starts the reaction.
3. The pressure and density of the burnt gas are higher than those of the unburnt gas.

## Remarks

In the simplest model the whole wave is a discontinuity across which mass, momentum and total energy, including chemical energy, are conserved.
The burnt states then lie on the reactive Hugoniot curve of the unburnt state, which has two branches.
On the detonation branch the pressure rises and the wave is supersonic; on the deflagration branch the pressure falls and the wave is subsonic.

Example: a steady planar Chapman–Jouguet detonation in a hydrogen and oxygen mixture runs at a speed of the order of kilometres per second.
This is far above the sound speed of the unburnt gas.

Non-example: a premixed laminar flame, as on a gas stove, moves into the fresh gas at well below the speed of sound and the pressure drops slightly across it.
It fails clause 1 and is a deflagration.
