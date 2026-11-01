---
tag: 3EH4C3M5GV
kind: concept
name: Finitely presented module
msc: ["13E15", 13C05]
specializes: [05QY1VEBYD]
sources:
  - url: https://en.wikipedia.org/wiki/Finitely_generated_module
---

## Summary

A finitely presented module is a module given by finitely many generators and finitely many relations among them.
It is the cokernel of a linear map between two finitely generated [[free modules|0DZ9DKAKZR]], so it is described by a finite matrix.
Every finitely presented module is [[finitely generated|05QY1VEBYD]], and over a [[Noetherian ring|0670T59HGE]] the two notions agree.
Many statements about modules, such as the behaviour of $\Hom$ under localization, need finite presentation rather than finite generation.

## Explanations

### L1 human

A module is finitely presented when you can describe it completely with a finite list of generators and a finite list of rules.
For example, $\Z/6\Z$ has one generator $e$ and one rule $6e = 0$.
A presentation is like a finite recipe for building the module from a free module.
Over familiar rings, such as $\Z$ or polynomial rings in finitely many variables over a field, every finitely generated module has such a recipe.
