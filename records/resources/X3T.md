---
records:
    - id: X3TDN77E3C
      kind: problem-set
      title: Kvant 1973, no. 2
      date: "1973"
      expressions:
        - key: e1
          kind: edition
          date: "1973"
          structure: X3TDN77E3C/e1.json
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
          native_id: 1973-2
          level: work
      history:
        - op: add
          at: "2026-10-31"
          by: m2 v0.6.2 cluster/1
        - op: scope
          at: "2026-10-31"
          by: m2 v0.6.2 scope/1
          note: to in
    - id: X3TQDJY7PS
      kind: monograph
      title: General Relativity for Mathematicians
      creators:
        - name: Rainer K. Sachs
          role: author
        - name: Hung-Hsi Wu
          role: author
      date: "1977"
      expressions:
        - key: e1
          kind: edition
          date: "1977"
          ids:
            doi: 10.1007/978-1-4612-9903-5
          manifestations:
            - key: m1
              kind: print
              publisher: Springer New York
              date: "1977"
              ids:
                isbn:
                    - "9781461299059"
                    - "9781461299035"
      relations:
        - kind: part_of
          to: 7ME1ABA6H5
          source: cluster/1
      scope:
        value: in
        rule: S4
        by: m2 v0.6.4 scope/1
      catalogue:
        - source: springer-series
          snapshot: blake3:09492c429ae54789c72bd081d21b950751ebbf0910012c1957fb140a008b7b5e
          native_id: 10.1007/978-1-4612-9903-5
          level: work
      history:
        - op: add
          at: "2026-10-31"
          by: m2 v0.6.2 cluster/1
        - op: scope
          at: "2026-10-31"
          by: m2 v0.6.2 scope/1
          note: to in
    - id: X3TYD6TMCE
      kind: preprint
      title: Discrete Painlev\'e transcendent solutions to the multiplicative type discrete KdV equations
      creators:
        - name: Nobutaka Nakazono
          role: author
      date: "2021-04-23"
      subjects:
        - system: arxiv
          code: nlin.SI
        - system: arxiv
          code: math-ph
        - system: arxiv
          code: math.MP
      expressions:
        - key: e1
          kind: version
          label: preprint
          date: "2021-04-23"
          ids:
            arxiv: "2104.11433"
            doi: 10.1063/5.0054905
      catalogue:
        - source: arxiv
          snapshot: blake3:e8374453dcab7bada88a6b850ab5bc0a0d87abd798991c12ac2d6c76ecd2c055
          native_id: "2104.11433"
          level: work
      history:
        - op: add
          at: "2026-10-31"
          by: m2 v0.6.7 cluster/1
---
