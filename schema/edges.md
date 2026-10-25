# Edge types

This file is generated from `node.v1.json` by `.github/scripts/gen_edges.py`. Do not edit it.

A node file stores each edge that touches it in a front matter field. The table gives the field. The `cites` edge has no field, because it exists only between records.

## Logical

Logical edges carry truth. The build uses them for the AND-OR dependency closure.

| Edge | From | To | Field |
|---|---|---|---|
| `proves` | proof | statement | `proves` |
| `uses` | statement, proof, definition | any | `uses` |
| `implies` | statement | statement | `implies` |
| `equivalent` | statement or definition | the same kind | `equivalent` |
| `refutes` | counterexample or statement | statement or conjecture | `refutes` |
| `resolves` | statement | conjecture or problem | `resolves` |
| `generalizes` | statement | statement | `generalizes` |
| `bounds` | statement | problem | `bounds` |

## Conceptual

Conceptual edges carry meaning. They are for navigation and search, and they do not change status.

| Edge | From | To | Field |
|---|---|---|---|
| `defines` | definition | concept | `defines` |
| `instance_of` | example or object | concept | `instance_of` |
| `about` | statement, conjecture or problem | concept | `about` |
| `specializes` | concept | concept | `specializes` |
| `method` | proof | concept in the methods topic | `methods` |
| `analogous_to` | any | any | `analogous_to` |
| `part_of` | any | topic | `topics` |

## Record

Record edges carry provenance and identity.

| Edge | From | To | Field |
|---|---|---|---|
| `formalizes` | formal declaration | node | `formal` |
| `source` | node | record | `sources` |
| `aligned` | paper result | node | `aligned` |
| `same_as` | node | external id | `same_as` |
| `close_to` | node | external id | `close_to` |
| `cites` | record | record | none |
| `resolved_by` | conjecture or problem | statement | `resolved_by` |
| `successor` | retired node | node | `retired.successor` |
