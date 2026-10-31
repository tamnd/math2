---
records:
    - id: E4P6011ED2
      kind: problem-set
      title: Kvant 2017, no. 6
      date: "2017"
      expressions:
        - key: e1
          kind: edition
          date: "2017"
          structure: E4P6011ED2/e1.json
      relations:
        - kind: part_of
          to: W84MAFPC23
          source: cluster/1
      scope:
        value: in
        rule: S4
        by: m2 v0.6.4 scope/1
      catalogue:
        - source: kvant
          snapshot: blake3:9ef7ec326c8e38c2cc1957ddca07480f15b4e9ef49d8059191fc4a1c78c7cd39
          native_id: 2017-6
          level: work
      history:
        - op: add
          at: "2026-10-31"
          by: m2 v0.6.2 cluster/1
        - op: scope
          at: "2026-10-31"
          by: m2 v0.6.2 scope/1
          note: to in
    - id: E4PGMSEQTS
      kind: preprint
      title: Disproof of the dominating Hadwiger conjecture
      creators:
        - name: Freddie Illingworth
          role: author
        - name: Raphael Steiner
          role: author
      date: "2026-09-28"
      subjects:
        - system: arxiv
          code: math.CO
      expressions:
        - key: e1
          kind: version
          label: preprint
          date: "2026-09-28"
          ids:
            arxiv: "2609.35361"
      catalogue:
        - source: arxiv
          snapshot: blake3:e8374453dcab7bada88a6b850ab5bc0a0d87abd798991c12ac2d6c76ecd2c055
          native_id: "2609.35361"
          level: work
      history:
        - op: add
          at: "2026-10-31"
          by: m2 v0.6.7 cluster/1
---
