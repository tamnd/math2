# Projects

A project is a campaign with people attached (spec 13.6). It has a goal in the graph, a monthly budget for agent runs, the agent roles that work for it and the people who run it. Each project is one file `projects/<id>.yaml`. The id is the name of the file. Use lower-case letters, digits and hyphens.

## The file

```yaml
name: Sylow theory
goal: Bind each member of the topic to Lean and give it E5.
topic: 4F2M9A
level: E5
budget: 25
roles: [formalize, prove]
members:
  - {id: github:your-login, role: owner}
  - {id: orcid:0000-0000-0000-0000, role: member}
```

| Field | Meaning |
|---|---|
| `name` | The name of the project. |
| `goal` | The goal in one or two sentences. |
| `topic` | The tag of a topic node. The members of the topic are the targets of the project. |
| `level` | The evidence level that each member of the topic must reach, from E1 to E5. Leave it out for no level. |
| `budget` | The most US dollars that the agent runs of the project can spend in a month. Use 0 for no agent work. |
| `roles` | The agent roles that work for the project, for example `explore`, `prove` or `formalize`. Leave it out for no agent work. |
| `members` | The people of the project. Each one has an `id`, a GitHub login as `github:login` or an ORCID iD as `orcid:...`, and a `role`, `owner` or `member`. |

The example uses placeholders for the topic, the logins and the iD. Put your own values in the file.

## What the project gives

- The blueprint of the project is the blueprint of the topic: the members of the topic and each node that they need. The graph computes it, and nobody writes it by hand.
- The tasks are the statements with no proof and the open conjectures and problems in the blueprint, and the members of the topic below the level of the goal.
- An agent job works for the project when it runs on behalf of `project:<id>`. Only the roles of the project work for it, and only a member can request a job for it. The orchestrator stops the agent runs of the project when they spent the budget of the month.
- The wiki has a page for each project at `projects/<id>/`, with the blueprint, the tasks, the members, the spend of each month and the run log.

## Start a project

1. Find or add the topic node of the goal in `nodes/`. Its members are the nodes with `part_of` the topic. The tree has no topic nodes yet, thus the first project also adds its topic node.
2. Add the file `projects/<id>.yaml` in a pull request. Give at least one owner.
3. Run `m2 check`. It fails on a project file that is not valid, and on a topic that is not a topic node of the tree.

The owners set the goal and the budget. Ask an owner to review each change to the file, in the same way as a change to a node.
